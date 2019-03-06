# djangocms-bootstrap

Some templates and templatetags to be used with django-CMS and Bootstrap3/Bootstrap4.

Django-CMS is frontend agnostic, which is a good thing. However, in combination with Bootstrap3/4
the menu structure does not quite fit. This is because Bootstrap3/4 only allows one nested menu level.

Therefore **djangocms-bootstrap** adds a few modified templatetags, which render the existing
page tree into a menu structure suitable for the navbar in Bootstrap3/4.

[![PyPI](https://img.shields.io/pypi/pyversions/djangocms-bootstrap.svg)]()
[![PyPI version](https://img.shields.io/pypi/v/djangocms-bootstrap.svg)](https://https://pypi.python.org/pypi/djangocms-bootstrap)
[![PyPI](https://img.shields.io/pypi/l/djangocms-bootstrap.svg)]()
[![Twitter Follow](https://img.shields.io/twitter/follow/shields_io.svg?style=social&label=Follow&maxAge=2592000)](https://twitter.com/jacobrief)

## CHANGELOG
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
