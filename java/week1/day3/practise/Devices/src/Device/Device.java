package Device;

public class Device {
	 
	private Integer battery ; 
		
		
		public Device() {
			this.battery = 100;
		}
		public Device(int battery) {
			this.battery = battery;
		}
		// Getters and Setters
		public Integer getBattery() {
			return battery;
		}
		public void setBattery(Integer battery) {
			this.battery = battery;
		}
		
		// methods 
		public void displayStats() {
			System.out.println("battery's life is" + this.getBattery());
		}
}
