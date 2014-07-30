'use strict';

/* Controllers */

var app = angular.module('ngdemo.controllers', []);





app.controller('UserListCtrl', ['$scope', 'UsersFactory', 'UserFactory', '$location',
    function ($scope, UsersFactory, UserFactory, $location) {

        // callback for ng-click 'editUser':
        $scope.editUser = function (userId) {
            $location.path('/user-detail/' + userId);

        };

        // callback for ng-click 'deleteUser':
        $scope.deleteUser = function (userId) {
           UserFactory.delete({ id: userId });
           $(".user"+userId).hide();

        };

        // callback for ng-click 'createUser':
        $scope.createNewUser = function () {
            $location.path('/user-creation');
        };

        $scope.triggerUpload = function () {
             $('#fileUpload').click();
        };

        UsersFactory.query(function(data) {
            $scope.users = data.objects;
        });

    }]);

app.controller('UserDetailCtrl', ['$scope', '$routeParams', 'UserFactory', '$location',
    function ($scope, $routeParams, UserFactory, $location) {

        // callback for ng-click 'updateUser':
        $scope.updateUser = function () {
            UserFactory.update(
                $scope.user,
                function(){
                    $location.path('');
                },
                function(error){
                    angular.forEach(error.data.contacts,function(error,field){

                        $scope.form[field].$setValidity('server', false);
                        $scope.errors[field] = error.join(', ');
                    });

                }
            );
         };

        // callback for ng-click 'cancel':
        $scope.cancel = function () {
            $location.path('');
        };

        $scope.user = UserFactory.show({id: $routeParams.id});
    }]);

app.controller('UserCreationCtrl', ['$scope', 'UsersFactory', '$location',
    function ($scope, UsersFactory, $location) {

        // callback for ng-click 'createNewUser':
        $scope.createNewUser = function () {

            $scope.errors = {};
            UsersFactory.create(
                $scope.user,
                function(){
                    $location.path('');
                },
                function(error){
                    angular.forEach(error.data.contacts,function(error,field){

                        $scope.form[field].$setValidity('server', false);
                        $scope.errors[field] = error.join(', ');
                    });

                }
            );

        }
    }]);
