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
    $scope.GetTerms = function(){
        DataService.postData("term:" + $scope.selected, function(data){
        $scope.results = data;
        });
    };
});




