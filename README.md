# djangocms-bootstrap3

Some templates and templatetags to be used with django-CMS and Bootstrap3.

Django-CMS is frontend agnostic, which is a good thing. However, in combination with Bootstrap3
the menu structure does not quite fit. This is because Bootstrap3 only allows one nested menu level.

Therefore **djangocms-bootstrap3** adds a few modified templatetags, which render the existing
page tree into a menu structure suitable for the navbar in Bootstrap3.


## CHANGELOG
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
