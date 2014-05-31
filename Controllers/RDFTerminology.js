var myApp = angular.module('RDFTerminology',[]);

myApp.service('DataService', function($http)
    {this.postData = function(data,callback)
        {$http({
            method: 'POST',
            url: 'http://localhost/rdfterms/cgi/getPrefTerm.py',
            data: data,
            headers: {
                   'Content-type': 'application/json'
                // 'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'
            }
        }).success(function(resp){callback(resp);
        }).error(function(){callback(undefined);
        });
    };
});

/*myApp.controller('GetTermsController', function($scope, DataService){
    $scope.names = {};
    $scope.GetTerms = function(){
        DataService.postData($scope.selected, function(data){
        $scope.names = data.name;
        });
     };
});*/

myApp.function GetTermsController($scope) {
    $scope.names = ["john", "bill", "charlie", "robert", "alban", "oscar", "marie", "celine", "brad", "drew", "rebecca", "michel", "francis", "jean", "paul", "pierre", "nicolas", "alfred", "gerard", "louis", "albert", "edouard", "benoit", "guillaume", "nicolas", "joseph"];
}


myApp.directive('autoComplete', function($timeout) {
    return function(scope, iElement, iAttrs) {
            iElement.autocomplete({
                source: scope[iAttrs.uiItems],          //the Attribute uiItems - this refers to the model names. Basically autocomplete is triggered by input and has a source names
                select: function() {
                    $timeout(function() {
                      iElement.trigger('input');   //the triiger is something typed into input
                    }, 0);
                }
            });

    };
 });

 //Problem is that names does not exist because something is wrong with populating that model. Perhaps trigger is before names can be populated

