package com.houssem.zookeeper;

public class Gorilla extends Mamal {
	
	public Gorilla(int energy) {
		super(energy);
	}
	
	public Gorilla() {
		
	}
	// methods 
	
	public void throwSomething() {
		this.setEnergy(getEnergy() -5);
		System.out.println(" the gorilla has thrown something");
	}
	
	public void eatBananas() {
		this.setEnergy(getEnergy() +10);
		System.out.println("the gorilla's satisfaction");
	}
	
	public void climb() {
		this.setEnergy(getEnergy()-10);
		System.out.println("gorilla has climbed a tree");
	}
	
	
}
