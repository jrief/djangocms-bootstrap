(function(angular, undefined) {
'use strict';

// This AngularJS module is only required after including `ng-nav-navbar.html`.
// Usage:
// On initializing your AngularJS app, use
// angular.module('myApp', [..., 'django.cms.bootstrap', ...]);

angular.module('django.cms.bootstrap', []).directive('nav', function() {
	return {
		restrict: 'E',
		link: function(scope) {
			scope.toggleNavCollapse = function () {
				scope.isNavCollapsed = !scope.isNavCollapsed;
			};
			scope.isNavCollapsed = true;
		}
	};
});


})(window.angular);
