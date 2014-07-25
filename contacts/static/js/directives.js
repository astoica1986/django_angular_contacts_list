'use strict';

/* Directives */


angular.module('ngdemo.directives', []).
  directive('appVersion', ['version', function(version) {
    return function(scope, elm, attrs) {
      elm.text(version);
    };
  }]);

angular.module('ngdemo.directives', []).
  directive('serverError',  function() {
    return {
      restrict: 'A',
      require: '?ngModel',
      link: function(scope, element, attrs, ctrl) {
          element.on('change',function(){
              scope.$apply(function(){
                  ctrl.$setValidity('server', true);
              })
          })
      }
    };
  });