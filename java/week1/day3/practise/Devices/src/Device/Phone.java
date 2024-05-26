package Device;

public class Phone extends Device { 

	public Phone(int battery) {
		super(battery);
		
	}
	 //methods 
	
	public void MakeCall( ) {
		
		this.setBattery(getBattery()-5);
		System.out.printf("you made a call now , and your battery is %d ! \n",this.getBattery());
	}
    public void PlayingGame( ) {
		
		this.setBattery(getBattery()-20);
		System.out.printf("you're playing now ,	 your battery is %d ! \n",this.getBattery());
	}
	
    
    public void Charging( ) {
		
		this.setBattery(getBattery()+50);
		System.out.printf("you're phone is charging now , your battery is %d ! \n",this.getBattery());
	}
}
