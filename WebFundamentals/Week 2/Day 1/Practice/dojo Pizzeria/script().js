var sandwich = {
    bread:    "sourdough",
    protein:  "london broil",
    cheese:   "lacey swiss cheese",
    toppings: ["romaine lettuce", "heirloom tomatoes", "horseradish sauce"]
};



console.log(sandwich);


function sandwichFactory(bread, protein, cheese, toppings) {
    var sandwich = {};
    sandwich.bread = bread;
    sandwich.protein = protein;
    sandwich.cheese = cheese;
    sandwich.toppings = toppings;
    return sandwich;
}

var s1 = sandwichFactory("wheat", "turkey", "provolone", ["mustard", "fried onions", "arugula"]);
console.log(s1);


function pizzaOven(crustType,sauceType,cheeses,toppings){
    var pizza ={};
    pizza.crustType=crustType;
    pizza.sauceType=sauceType;
    pizza.cheeses=cheeses;
    pizza.toppings=toppings;
    return pizzaOven;
}

var p1=pizzaOven("deep dish","traditional",["mozzarella","pepperoni", "sausage"]);
console.log(p1);

var p2=pizzaOven("hand tossed", "marinara", ["mozzarella", "feta"], ["mushrooms", "olives", "onions"]);
console.log(p2);


var p3=pizzaOven("hand tossed", "Ton", ["mozzarella"], ["olives", "onions"]);
console.log(p3);

var p4=pizzaOven("hand tossed", "Traditional", ["mozzarella"], ["Tomato", "Nuts"]);
console.log(p3);
