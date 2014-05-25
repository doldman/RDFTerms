function getTerms($scope, $http, $templateCache ) {


   // $scope.names = ["john", "bill", "charlie", "robert", "alban", "oscar", "marie", "celine", "brad", "drew", "rebecca", "michel", "francis", "jean", "paul", "pierre", "nicolas", "alfred", "gerard", "louis", "albert", "edouard", "benoit", "guillaume", "nicolas", "joseph"];
   $scope.method = 'POST';
   $scope.url = 'getPrefTerm.py';
   $scope.parameter = {keyword: $scope.selected} ;

     $http({
         method: $scope.method,
         url: $scope.url,
         cache: $templateCache,
         headers: {'Content-Type': 'application/x-www-form-urlencoded'},
         data: $scope.selected }).
           success(function(data, status) {
              $scope.status = status;
              $scope.data = data;
            }).
            error(function(data, status) {
              $scope.data = data || "Request failed";
              $scope.status = status;
          });
        };



angular.module('MyModule', []).directive('autoComplete', function($timeout) {
    return function(scope, iElement, iAttrs) {
            iElement.autocomplete({
                source: scope[iAttrs.uiItems],
                select: function() {
                    $timeout(function() {
                      iElement.trigger('input');
                    }, 0);
                }
            });
    };
});