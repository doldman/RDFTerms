function getTerms($scope, $http, templateCache ) {

$scope.method = 'POST';
$scope.url = 'getPrefTerm.py';

     $http({
     method: $scope.method,
     url: $scope.url,
     cache: $templateCache
     data: termModel }).
       success(function(data, status) {
          $scope.status = status;
          $scope.data = data;
        }).
        error(function(data, status) {
          $scope.data = data || "Request failed";
          $scope.status = status;
      });
    };






