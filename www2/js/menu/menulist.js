(function(){
    var app = angular.module('menulist', []);

    app.directive('menuList', function() {
        return {
            restrict: 'E',
            templateUrl: 'templates/menu/menulist.html',
            controller: 'menulistController',
            controllerAs: 'menulistCtrl',
        };
    });

    app.directive('itemOrderCounter', function() {
        return {
            restrict: 'E',
            templateUrl: 'templates/menu/ordercounter.html',
            controller: 'itemOrderCounterController',
            controllerAs: 'itemOrderCounterCtrl',
        };
    });

    app.directive('orderCart', function() {
        return {
            restrict: 'E',
            templateUrl: 'templates/menu/ordercart.html',
            controller: 'ordercartController',
            controllerAs: 'ordercartCtrl',
        };
    });

    app.controller('itemOrderCounterController', ['menulistService', function(menulistService){
        var ctrl = this;

        this.item = undefined;

        this.increment = function() {
            ++ctrl.item.orderCounter;
        };

        this.decrement = function() {
            if (ctrl.item.orderCounter > 0) {
                --ctrl.item.orderCounter;
            }
        };

        this.init = function(item) {
            ctrl.item = item;
            ctrl.item.orderCounter = 0;
            menulistService.order.push(item);
        };
    }]);

    app.controller('menulistController', ['menulistService', function(menulistService){
        var ctrl = this;

        this.menuItems = menulistService.order;
        this.foodTags = [];

        this.loadMenuItems = function(){
            menulistService.getMenuItems().
                success(function(data){
                    ctrl.menuItems = data.items;
                    ctrl.loadUserFoodTags();
                }).
                error(function(data){
                    alert('Could not fetch menu!');
                });
        };

        this.loadUserFoodTags = function(){
            menulistService.getUserFoodTags().
                success(function(data){
                    ctrl.foodTags = data.user.food_tags;

                    for (var i = ctrl.menuItems.length - 1; i >= 0; i--) {
                        ctrl.checkMissingTags(ctrl.foodTags, ctrl.menuItems[i]);
                    };
                }).
                error(function(data){
                    alert('Could not fetch menu!');
                });
        };

        this.checkMissingTags = function(usertags, item){
            for (var i = usertags.length - 1; i >= 0; i--) {
                if (item.tags.indexOf(usertags[i]) == -1) return item.inactive = true;
            };

            return item.inactive = false;
        }

        this.init = function(){
            ctrl.loadMenuItems();
        };
    }]);

    app.controller('ordercartController', ['ordercartService', function(ordercartService){
        var ctrl = this;

        this.order = [];

        this.total = 0;

        this.visible = false;

        this.quantityFilter = function(item) {
            return item.orderCounter > 0;
        };

        this.show = function() {
            ctrl.visible = true;

            ordercartService.updateCart();
            ctrl.order = ordercartService.servData.order;
            ctrl.total = ordercartService.servData.total;
        };

        this.hide = function() {
            ctrl.visible = false;
        };

    }]);

    app.factory('menulistService', ['$http', function($http){
        this.order = [];

        this.getMenuItems = function(){
            return $http({url: 'api/menu', method: 'GET'});
        };

        this.getUserFoodTags = function(){
            return $http({url: 'api/user', method: 'GET'});
        };

        return {
            getMenuItems: this.getMenuItems,
            getUserFoodTags: this.getUserFoodTags,
            order: this.order,
        };
    }]);

    app.factory('ordercartService', ['$http', 'menulistService', function($http, menulistService){
        var serv = this;

        this.servData = {order: [], total: 0};

        this.updateCart = function(){
            serv.servData.order = menulistService.order;
            serv.servData.total = serv.calculate_total();
        };

        this.calculate_total = function() {
            sum = 0;

            for (var i = serv.servData.order.length - 1; i >= 0; i--) {
                order = serv.servData.order[i];
                sum += order.orderCounter * order.price;
            };

            return sum;
        };

        return {
            updateCart: this.updateCart,
            servData: serv.servData,
        };
    }]);

})();