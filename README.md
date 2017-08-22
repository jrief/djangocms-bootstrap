# djangocms-bootstrap3

Some templates and templatetags to be used with django-CMS and Bootstrap3

Django-CMS is frontend agnostic, which is a good thing. However, in combination with Bootstrap3
the menu structure does not quite fit. This is because Bootstrap3 only allows one nested menu level.

Therefore **djangocms-bootstrap3** adds a few modified templatetag, which render the existing
page tree into a menu structure suitable for the navbar in Bootstrap3.


## CHANGELOG
- 0.3.0
  * The templatetags ``main_menu``, ``main_menu_below_id`` and ``main_menu_embody_id`` now accept
    two optional values: ``offset`` (default 0) and ``limit`` (default 100). With these it is
    possible, to render only a subset of the menu list.

- 0.2.1
  * Add setup.py to MANIFEST.in
  
- 0.2.0
  * Adopted to Angular-UI-bootstrap version 0.14 and later.
  * Fixed division issue in paginator for Python3.

- 0.1.0
  * Added templatetag ``main_menu_embody_id``.
  * Fixed various Django templates to render the menu.

- 0.0.2 Initial release.
