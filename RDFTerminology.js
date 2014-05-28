var myApp = angular.module('RDFTerminology',[]);

myApp.service('DataService', function($http)
    {this.postData = function(data,callback)
        {$http({
            method: 'POST',
            url: 'getPrefTerm.py',
            data: data,
            headers: {
                //'Content-type': 'application/json'
                  'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'
            }
        }). success( function(resp){callback(resp);
        }). error( function(){callback(undefined);
        });
    };
});

myApp.controller('GetTermsController', function($scope, DataService){
    /* $scope.GetTerms = function($event){ */

        DataService.postData($scope.selected, function(data){
        $scope.names = data;
        });
    // };
});


myApp.directive('autoComplete', function($timeout) {
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