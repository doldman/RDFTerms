/* function getTerms($scope, $http, templateCache ) {

$scope.method = 'POST';
$scope.url = 'getPrefTerm.py';

     $http({
     method: $scope.method,
     url: $scope.url,
     cache: $templateCache
     data: selected }).
       success(function(data, status) {
          $scope.status = status;
          $scope.data = data;
        }).
        error(function(data, status) {
          $scope.data = data || "Request failed";
          $scope.status = status;
      });
    };

*/

function getTerms ($scope) {
    $scope.termModel = null;
    $scope.myModelId = null;
    $scope.isDisabled = true;
}


directives.directive('autocomplete', ['$http', function($http) {
    return function (scope, element, attrs) {
        element.autocomplete({
            minLength:3,
            source:function (request, response) {
                var url = "http://localhost/getPrefTerm.py?keyword=" + request.term;
                $http.get(url).success( function(data) {
                    response(data.results);
                });
            },
            focus:function (event, ui) {
                element.val(ui.item.label);
                return false;
            },
            select:function (event, ui) {
                scope.myModelId.selected = ui.item.value;
                scope.$apply;
                return false;
            },
            change:function (event, ui) {
                if (ui.item === null) {
                    scope.myModelId.selected = null;
                }
            }
        }).data("autocomplete")._renderItem = function (ul, item) {
            return $("<li></li>")
                .data("item.autocomplete", item)
                .append("<a>" + item.label + "</a>")
                .appendTo(ul);
        };
    }
}]);




