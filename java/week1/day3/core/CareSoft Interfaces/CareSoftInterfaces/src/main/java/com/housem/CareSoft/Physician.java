package com.housem.CareSoft;

import java.sql.Date;
import java.util.ArrayList;

import org.apache.catalina.realm.JNDIRealm.User;

public class Physician extends User implements HIPAACompliantUser  {
    
    private ArrayList<String> patientNotes;
	
    public Physician() {
    }
    public Physician(Integer newid) {
    	id = newid;
    	
    }
    
    public boolean assignPin(int newPin) {
    	if ( newPin <= 1000 || newPin >= 9999) {
    		return false;
    	}
    	pin = newPin;
    	return true;
    }
    
    public boolean accessAuthorized(Integer idNum) {
    	if (idNum == id) {
    		return true;
    	}
    	return false;
    	
    }
	
    public void newPatientNotes(String notes, String patientName, Date date) {
        String report = String.format(
            "Datetime Submitted: %s \n", date);
        report += String.format("Reported By ID: %s\n", this.id);
        report += String.format("Patient Name: %s\n", patientName);
        report += String.format("Notes: %s \n", notes);
        this.patientNotes.add(report);
    }
    
	public ArrayList<String> getPatientNotes() {
		return patientNotes;
	}
	public void setPatientNotes(ArrayList<String> patientNotes) {
		this.patientNotes = patientNotes;
	}
	

}