function countPositives(arr){
    var count = 0;
for (var i=0 ; i < arr.length ; i ++) {
    if ( arr[i] >0 ){
        count++;
    }
}
    return count;
}
console.log(countPositives([12, -21, 3.6, 9, 12, -8]));