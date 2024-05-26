package com.houssem.zookeeper;

public class Mamal {

	private int energy ;
	
	// constructor 
	
	public Mamal() {
		
		this.energy = 100 ;
	}
	
	public Mamal(int energy) {
		this.energy = energy ;
	}
	
	// Methods 
	
	public void displayingEnergy() {
		
		System.out.printf("The mamal has %d of energy" , this.getEnergy());
	}
	
	// getters and setters 
	
	public int getEnergy() {
		return this.energy ;
	}
	public void setEnergy(int energy) {
		this.energy=energy ;
	}
	
	
}
