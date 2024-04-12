// parent Vehicle class
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



const ninja1 = new Ninja("Hyabusa");
ninja1.sayName();
ninja1.drinkSake();
ninja1.showStats();
