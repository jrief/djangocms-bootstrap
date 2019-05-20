# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django import template
from django.utils.text import mark_safe
from cms.models.pagemodel import Page
from menus.menu_pool import menu_pool
from classytags.arguments import IntegerArgument, StringArgument, Argument, Flag
from classytags.helpers import InclusionTag
from classytags.core import Options
from menus.templatetags.menu_tags import flatten, remove

register = template.Library()

if 'cmsplugin_cascade.bootstrap3' in settings.CMSPLUGIN_CASCADE_PLUGINS:
    BOOTSTRAP="3"
else:
    BOOTSTRAP="4"

def cut_levels(nodes, start_level):
    """
    cutting nodes away from menus
    """
    final = []
    removed = []
    for node in nodes:
        if not hasattr(node, 'level'):
            # remove and ignore nodes that don't have level information
            remove(node, removed)
            continue
        if node.attr.get('soft_root', False):
            # remove and ignore nodes that are behind a node marked as 'soft_root'
            remove(node, removed)
            continue
        if node.level == start_level:
            # turn nodes that are on from_level into root nodes
            final.append(node)
            node.parent = None
            if not node.visible and not node.children:
                remove(node, removed)
        elif node.level == start_level + 1:
            # remove nodes that are deeper than one level
            node.children = []
        else:
            remove(node, removed)
        if not node.visible:
            keep_node = False
            for child in node.children:
                keep_node = keep_node or child.visible
            if not keep_node:
                remove(node, removed)
    for node in removed:
        if node in final:
            final.remove(node)
    return final


class MainMenu(InclusionTag):
    name = 'main_menu'
    template = 'menu/dummy.html'

    options = Options(
        StringArgument('template', default='bootstrap{}/menu/navbar.html'.format(BOOTSTRAP), required=False),
        StringArgument('namespace', default=None, required=False),
        StringArgument('root_id', default=None, required=False),
        IntegerArgument('offset', default=0, required=False),
        IntegerArgument('limit', default=100, required=False),
        Flag('embody_root', default=False, true_values=['embody_root']),
        Argument('next_page', default=None, required=False),
    )

    def get_context(self, context, template, namespace, root_id, offset, limit, embody_root, next_page):
        try:
            # If there's an exception (500), default context_processors may not be called.
            request = context['request']
        except KeyError:
            return {'template': 'menu/empty.html'}

        start_level = 0
        
        if next_page:
            children = next_page.children
        else:
            menu_renderer = context.get('cms_menu_renderer')
        
            if not menu_renderer:
                menu_renderer = menu_pool.get_renderer(request)
        
            nodes = menu_renderer.get_nodes(namespace, root_id)
            if root_id:
                # find the root id and cut the nodes
                id_nodes = menu_pool.get_nodes_by_attribute(nodes, "reverse_id", root_id)
                if id_nodes:
                    node = id_nodes[0]
                    nodes = node.children
                    for remove_parent in nodes:
                        remove_parent.parent = None
                    start_level = node.level + 1
                    nodes = flatten(nodes)
                    if embody_root:
                        node.level = start_level
                        nodes.insert(0, node)
                else:
                    nodes = []
            children = cut_levels(nodes, start_level)
            children = menu_renderer.apply_modifiers(children, namespace, root_id, post_cut=True)
            children = children[offset:offset + limit]
        context.update({'children': children, 'template': template})
        return context

register.tag(MainMenu)


class MainMenuBelowId(MainMenu):
    name = 'main_menu_below_id'
    options = Options(
        Argument('root_id', default=None, required=False),
        StringArgument('template', default='bootstrap{}/menu/navbar.html'.format(BOOTSTRAP), required=False),
        IntegerArgument('offset', default=0, required=False),
        IntegerArgument('limit', default=100, required=False),
        StringArgument('namespace', default=None, required=False),
        Flag('embody_root', default=False, true_values=['embody_root']),
        Argument('next_page', default=None, required=False),
    )

register.tag(MainMenuBelowId)


class MainMenuEmbodyId(MainMenu):
    name = 'main_menu_embody_id'
    options = Options(
        Argument('root_id', default=None, required=False),
        StringArgument('template', default='bootstrap{}/menu/navbar.html'.format(BOOTSTRAP), required=False),
        IntegerArgument('offset', default=0, required=False),
        IntegerArgument('limit', default=100, required=False),
        StringArgument('namespace', default=None, required=False),
        Flag('embody_root', default=True, false_values=['skip_root']),
        Argument('next_page', default=None, required=False),
    )

register.tag(MainMenuEmbodyId)


class MenuIcon(InclusionTag):
    name = 'menu_icon'
    template = 'bootstrap{}/components/menu-icon.html'.format(BOOTSTRAP)

    options = Options(
        Argument('child_id'),
        StringArgument('template', default=None, required=False),
    )

    def get_template(self, context, template=None, **kwargs):
        return template if template else self.template

    def get_context(self, context, child_id, template):
        try:
            cascadepage = Page.objects.get(id=child_id).cascadepage
        except (Page.DoesNotExist, AttributeError):
            pass
        else:
            icon_font, symbol = cascadepage.icon_font, cascadepage.menu_symbol
            if icon_font and symbol:
                prefix = icon_font.config_data.get('css_prefix_text', 'icon-')
                font_attr = 'class="{}{}"'.format(prefix, symbol)
                context.update({
                    'stylesheet_url': icon_font.get_stylesheet_url(),
                    'icon_font_attrs': mark_safe(font_attr),
                })
        return context

    def render_tag(self, context, **kwargs):
        context.push()
        output = super(MenuIcon, self).render_tag(context, **kwargs)
        context.pop()
        return output

register.tag(MenuIcon)


class Paginator(InclusionTag):
    name = 'paginator'
    template = 'bootstrap{}/components/paginator.html'.format(BOOTSTRAP)

    options = Options(
        IntegerArgument('page_range', default=10, required=False),
        StringArgument('template', default=None, required=False),
    )

    def get_context(self, context, page_range, template):
        try:
            current_page = int(context['request'].GET['page'])
        except (KeyError, ValueError):
            current_page = 1
        page_range -= 1
        template = template or self.template
        context.update({'template': template})
        context.setdefault('paginator_classes', 'pagination')
        paginator = context.get('paginator') or getattr(context.get('request'), 'paginator', None)
        if paginator:
            first_page = max(1, min(int(current_page - page_range / 2), paginator.num_pages - page_range))
            last_page = min(first_page + page_range, paginator.num_pages)
            context.update({
                'show_paginator': paginator.num_pages > 1,
                'show_aquos': paginator.num_pages > page_range + 1,
                'pages': [{'num': p, 'active': p == current_page} for p in range(first_page, last_page + 1)],
                'laquo': {'num': first_page - 1, 'paginate': first_page > 1},
                'raquo': {'num': last_page + 1, 'paginate': last_page < paginator.num_pages},
            })
        return context

register.tag(Paginator)
