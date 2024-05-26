package com.houssem.zookeeper;

public class Bat extends Mamal {
	
	public Bat (int energy) {
		super(energy);
	}
	
	public Bat () {
		
		super(300);
	}
	
	public void fly() {
		setEnergy(getEnergy() -50);
		System.out.println("the bat is airborne");
	}
	
	public void eatHumans() {
		setEnergy(getEnergy() +10);
		System.out.println(" the bat's satisfaction");
	}
	
	public void attackTown() {
		
		setEnergy(getEnergy()-100);
		
		System.out.printf("the bat's attack");
	}
	
	
}
