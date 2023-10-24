/*
 * White Belt - Option C
 * Your Name: ___bahri med houssem________________
 */

* Question 1
* Predict the result of the following code.

var answer = 6 - 3 / 2;
console.log(answer);

/*
 * Your answer: ______1.5_________
 */

* Question 2
* Predict the result of the following code.

var answer = (6 - 3) / 2;
console.log(answer);

/*
 * Your answer: _______1.5__________
 */

* Question 3
* Predict the result of the following code.

for(var i=1; i<17; i++) {
    console.log(i);
    i += 3;
}

/*
 * Your answer: _  1,4,7,10,13,16________________
 */

* Question 4
* Predict the result of the following code.

for(var i=22; i>15; i--) {
    console.log(i);
    i -= 2;
}

/*
 * Your answer: ________22,20,18,16_________
 */

* Question 5
* Predict the result of the following code.

var i = 12;
if(i % 2 == 0) {
    console.log("even");
} else {
    console.log(i);
}

/*
 * Your answer: ________even,12_________
 */

* Question 6
* Predict the result of the following code.

for(var i=7; i<12; i++) {
    if(i % 2 == 0) {
        console.log("even");
    } else {
        console.log(i);
    }
}

/*
 * Your answer: ___7,even,9,even,11______________
 */

* Question 7
* Predict the result of the following code.

var arr = [1, 4, 7, 6, 2, 1];
var count = 0;
for(var i=0; i<arr.length; i++) {
    if(arr[i] < 4) {
        count++;
    }
}
console.log(count);

/*
 * Your answer: ___    1,2,1______________
 */

* Question 8
* Complete the function in the code below to console log all numbers from 7 to 38.

function print7to38() {
 for (var i=7 ; i<=38 ; i++); 
   console.log(i);
    i=i+1
}


}

print7to38();

* Question 9
* Complete the function in the code below to return the sum of all of the values of an array.
* Given: [3, 6, 4, 9, 2]
* Return: 24

function findSum(arr) = [3 ,6,  4, 9, 2] { 
    var currentSum = 0;
    * for (arr i=0 ; i <= x.length-1 ;i++)
    
   
    return currentSum;
}


findSum([12, 21, 3.6, 9, 12, 8]);

* Question 10
* Complete the function in the code below to return a count of all of the positive values in the array.
* Given: [-3, 6, -4, 9, 2]
* Return: 3

function countPositives(arr) [-3,6,4,9,2] {
    var count = 0;
for (arr i=0 ; i <= x.length-1 ; i ++) 
if ( i >=1 )

 
    return count;
}

countPositives([12, -21, 3.6, 9, 12, -8]);