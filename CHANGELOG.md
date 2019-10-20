# CHANGELOG
  
- 1.1.2
  * Fix external dependencies to latest available versions.

- 1.1.1
  * Replace `mark_safe` modules path by `from django.utils.safestring` for compatibility in Django 2.0.
 
- 1.1
  * Adopt to django-cms version 3.6.
  * Do no render menu item pointing onto current page in bold.
  * Add templatetag `menu_icon`, which in combination with **djangocms-cascade** version 0.19+, renders an icon
    in front of the menu title.
  * Add Bootstrap-4 template for templatetag `language_chooser`, which renders a drop-down menu to choose one of
    the languages configured for **django-CMS**
  * Add Bootstrap-4 template for templatetag `paginator`, which renders a paginator according to the best given
    practices.

- 1.0.2
  * Add AngularJS directive for toggling navbar in responsive mode.

- 1.0.1
  * Fix navbar and menu templates if used in combination with **Bootstrap-4** and jQuery.

- 1.0
  * In addition to **Bootstrap-3** add support for **Bootstrap-4**. This requires to be more generic, therefore also
  * rename project from `djangocms-bootstrap3` to `djangocms-bootstrap` in your requirements.
  * rename Django app from `cms_bootstrap3` to `cms_bootstrap` in your `INSTALLED_APPS`.
  * rename in existing templates `bootstrap/…` to `bootstrap3/…`.

- 0.4.2
  * adopted navbar to work with `angular-ui-bootstrap` version 2.5 and later.

- 0.4.1
  * Fix versions in `install_requires` of `setup.py`.

- 0.4
  * Add support for django-CMS version 3.5
  * Replace `dropdown`, `dropdown-toggle` by `uib-dropdown`, `uib-dropdown-toggle` to be compatible
    with **angular-ui-bootstrap** version 0.14 and later.
  * In hamburger menu, replace `<button>`- by `<a>`-tag, because `ng-click` didn't fire properly.
  * Make use of `uib-collapse` for mobile menus. This adds an animation.

- 0.3.2
  * In Navbar, render `get_menu_title` as safe string in order to allow HTML tags in
    Mune Title.

- 0.3.1
  * Fix: Use `uib-dropdown` rather than `dropdown` to be compatible with
    **angular-ui-bootstrap** version 0.14 and later.

- 0.3.0
  * The templatetags `main_menu`, `main_menu_below_id` and `main_menu_embody_id` now accept
    two optional values: `offset` (default 0) and `limit` (default 100). With these it is
    possible, to render only a subset of the menu list.

- 0.2.1
  * Add setup.py to MANIFEST.in
  
- 0.2.0
  * Adopted to Angular-UI-bootstrap version 0.14 and later.
  * Fixed division issue in paginator for Python3.

- 0.1.0
  * Added templatetag `main_menu_embody_id`.
  * Fixed various Django templates to render the menu.

- 0.0.2 Initial release.
