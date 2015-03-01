(function(){
    var app = angular.module('login', []);

    app.directive('loginForm', function(){
        return {
            restrict: 'E',
            templateUrl: 'templates/homepage/loginform.html',
            controller: 'loginController',
            controllerAs: 'loginCtrl',
        };
    });

    app.controller('loginController', ['loginService', function(loginService){
        var ctrl = this;

        this.username = '';
        this.password = '';
        this.loginFailed = false;

        this.submit = function(){
            loginService.login(ctrl.username, ctrl.password).
                success(function(data){
                    window.location.href = '/menu';
                }).
                error(function(data){
                    alert('Could not login!');
                });
        };
    }]);

    app.factory('loginService', ['$http', function($http){
        this.login = function(username, password){
            postData = {
                'username': username,
                'password': password,
            };

            headers = {'Content-Type': 'application/json'};

            return $http({url: 'api/session_auth', method: 'POST', data: postData, headers: headers});
        };

        return {
            login: this.login,
        };
    }]);
})();