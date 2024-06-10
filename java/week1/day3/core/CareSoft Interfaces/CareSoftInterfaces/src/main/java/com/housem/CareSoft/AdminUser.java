package com.housem.CareSoft;



import java.sql.Date;
import java.util.ArrayList;

public class AdminUser extends User implements HIPAACompliantAdmin, HIPAACompliantUser {
    // Inside class:
    private String role;
    private ArrayList<String> securityIncidents;
    
    AdminUser(){
    }
    
    AdminUser(int newId, String role){
    	id = newId;
    	this.role = role;
    	this.securityIncidents = new ArrayList<String>();
    }
    
    public boolean assignPin(int newPin) {
    	if ( newPin <= 100000 || newPin >= 999999) {
    		return false;
    	}
    	pin = newPin;
    	return true;
    }
    
    public boolean accessAuthorized(Integer idNum) {
    	if (idNum == id) {
    		return true;
    	}
    	this.authIncident();
    	return false;
    	
    }
	
    // Apparently i cant print anything with this because its an array list
    public ArrayList<String> reportSecurityIncidents(){
    	return this.securityIncidents;
    }
    
    //had to reformat the date because it threw an constructor is undefined error, its handy that this has a spell check feature.
    public void newIncident(String notes) {
        String report = String.format(
            "Datetime Submitted: %s \n,  Reported By ID: %s\n Notes: %s \n", 
            new Date(id, id, id), this.id, notes
        );
        securityIncidents.add(report);
    }
    
    public void authIncident() {
        String report = String.format(
            "Datetime Submitted: %s \n,  ID: %s\n Notes: %s \n", 
            new Date(id, id, id), this.id, "AUTHORIZATION ATTEMPT FAILED FOR THIS USER"
        );
        securityIncidents.add(report);
    }

	public String getRole() {
		return role;
	}

	public void setRole(String role) {
		this.role = role;
	}

	public ArrayList<String> getSecurityIncidents() {
		return securityIncidents;
	}

	public void setSecurityIncidents(ArrayList<String> securityIncidents) {
		this.securityIncidents = securityIncidents;
	}
    
}