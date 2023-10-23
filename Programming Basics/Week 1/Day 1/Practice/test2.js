function findSum(arr) { 
    var currentSum = 0;
    for (var i=0 ; i < arr.length ;i++){
        currentSum+=arr[i];
    }
    return currentSum;
}

console.log(findSum([12, 21, 3.6, 9, 12, 8]));
console.log(findSum([5,9,11]));