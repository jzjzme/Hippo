angular.module('starter.controllers', [])
.run(function($rootScope) {
  $rootScope.totalQuantity = 0;
})

.controller('quantityCtrl', function($scope, $rootScope) {
  $scope.quantity = 0;
  $scope.increment = function(num) {
    // deal with quantity of individual card 
    if ($scope.quantity == 0 && num == -1) {
      return;
    }
    else {
      $scope.quantity += num;
      $rootScope.totalQuantity += num;
    }

    // deal with displaying checkout if any card has quantity >= 1
    if ($rootScope.totalQuantity == 0) {
      
    }
    else if ($rootScope.totalQuantity == 1) {

    }
    else if ($rootScope.totalQuantity == 2) {

    }
    else if ($rootScope.totalQuantity == 3) {

    }
  }
})

.controller('DashCtrl', function($scope) {})

.controller('ChatsCtrl', function($scope, Chats) {
  $scope.chats = Chats.all();
  $scope.remove = function(chat) {
    Chats.remove(chat);
  }
})

.controller('ChatDetailCtrl', function($scope, $stateParams, Chats) {
  $scope.chat = Chats.get($stateParams.chatId);
})

.controller('FriendsCtrl', function($scope, Friends) {
  $scope.friends = Friends.all();
})

.controller('FriendDetailCtrl', function($scope, $stateParams, Friends) {
  $scope.friend = Friends.get($stateParams.friendId);
})

.controller('AccountCtrl', function($scope) {
  $scope.settings = {
    enableFriends: true
  };
});