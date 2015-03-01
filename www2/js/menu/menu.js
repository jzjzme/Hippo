(function(){
    var app = angular.module('menu', ['menulist']);

    app.config(['$httpProvider', '$interpolateProvider', function($httpProvider, $interpolateProvider) {
        $httpProvider.defaults.xsrfCookieName = 'csrftoken';
        $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
        $interpolateProvider.startSymbol('{$');
        $interpolateProvider.endSymbol('$}');
    }]);
    
})();