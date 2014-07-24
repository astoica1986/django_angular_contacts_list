'use strict';

// Declare app level module which depends on filters, and services
angular.module('ngdemo', ['ngdemo.filters', 'ngdemo.services', 'ngdemo.directives', 'ngdemo.controllers']).
    config(['$routeProvider', function ($routeProvider) {

        $routeProvider.when('/', {templateUrl: 'user-list.html', controller: 'UserListCtrl'});
        $routeProvider.when('/user-detail/:id', {templateUrl: 'user-detail.html', controller: 'UserDetailCtrl'});
        $routeProvider.when('/user-creation', {templateUrl: 'user-creation.html', controller: 'UserCreationCtrl'});
        $routeProvider.otherwise({redirectTo: ''});
    }]);
