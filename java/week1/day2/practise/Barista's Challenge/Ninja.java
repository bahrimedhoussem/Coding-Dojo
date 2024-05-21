public class Ninja {
    // Member variables 
    private String name;
    private Integer health; 
    private Weapon weapon;
    private Integer power;


    // constructor 

    public Ninja(String name , Weapon weaponName , Integer power ) {
        this.name = name;
        this.health = 100;
        this.weapon = weaponName;
        this.power = power;
    }

}