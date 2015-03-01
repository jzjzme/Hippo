(function(){
    var app = angular.module('register', []);

    app.directive('registerForm', function() {
        return {
            restrict: 'E',
            templateUrl: 'templates/homepage/registerform.html',
            controller: 'registerController',
            controllerAs: 'registerCtrl',
        };
    });

    app.controller('registerController', ['registerService', function(registerService){
        var ctrl = this;

        this.username = '';
        this.email = '';
        this.password = '';

        this.foodtags = {'Vegetarian': false, 'Vegan': false, 'Gluten-free': false, 'Nut-free': false, 'Dairy-free': false, 'Paleo': false, 'Halal': false, 'Kosher': false};

        this.submit = function(){
            registerService.register(ctrl.username, ctrl.email, ctrl.password, ctrl.foodtags).
                success(function(data){
                    window.location.href = '/menu';
                }).
                error(function(data){
                    alert('Could not register!');
                });
        };
    }]);

    app.factory('registerService', ['$http', function($http){
        this.register = function(username, email, password, foodtags){
            postData = {
                'username': username,
                'email': email,
                'password': password,
                'foodtags': foodtags,
            };

            headers = {'Content-Type': 'application/json'};

            return $http({url: 'api/users/register', method: 'POST', data: postData, headers: headers});
        };

        return {
            register: this.register,
        };
    }]);

})();