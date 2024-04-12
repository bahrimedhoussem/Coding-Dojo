class Ninja {
    constructor(name) {
        this.name = name;
        this.health = 90;
        this.speed = 3;
        this.strength = 3;
    }
    sayName() {
        console.log (`the ninja is ${ this.name }.`);
    }
    showStats() {
        console.log (`the ninja is ${ this.name }`);
        console.log (`health ${ this.health }`);
        console.log (`speed is ${ this.speed }`);
        console.log (`strength ${ this.strength }`);
    }
    drinkSake() {
        this.health += 10
    }
}

class Sensei extends Ninja {
    constructor(name) {
        super(name);
        this.health = 90;
        this.speed = 3;
        this.strength = 3;
        this.wisdom = wisdom || 10;
    }
    speakWisdom() {
        super.drinkSake(); 
        console.log("What one programmer can do in one month, two programmers can do in two months.");
    } 
}
const ninja1 = new Ninja("Hyabusa");
const superSensei = new Sensei("Master Splinter", 15); 
ninja1.sayName();
ninja1.drinkSake();
ninja1.showStats();