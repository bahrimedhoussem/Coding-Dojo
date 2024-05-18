public class CafeJava {
    public static void main(String[] args) {
        // APP VARIABLES
        // Lines of text that will appear in the app. 
        String generalGreeting = "Welcome to Cafe Java, ";
        String pendingMessage = ", your order will be ready shortly";
        String readyMessage = ", your order is ready";
        String displayTotalMessage = "Your total is $";
        
        // Menu variables (add yours below)
        double mochaPrice = 3;
        double dripCoffee = 4;
        double latte = 5;
        double cappuccino = 4.7;
    
        // Customer name variables (add yours below)
        String customer1 = "Cindhuri";
        String customer2 = "Sam";
        String customer3 = "Jimmy";
        String customer4 = "Noah";

    
        // Order completions (add yours below)
        boolean isReadyOrder1 = false;
        boolean isReadyOrder2 = true;
        boolean isReadyOrder3 = true;
        boolean isReadyOrder4 = true;
        

        // APP INTERACTION SIMULATION (Add your code for the challenges below)
        // Example:

        System.out.println(generalGreeting + customer1);
        if (isReadyOrder1) {
            System.out.println(customer1 + displayTotalMessage);
        }else {System.out.println( customer1 + pendingMessage );
        
        }
        


        System.out.println(generalGreeting + customer4);
        if (isReadyOrder4) {
            System.out.println( customer4 + displayTotalMessage + cappuccino);

        } else {
            System.out.println( customer4 + pendingMessage);
        }  
        
        System.out.println(generalGreeting + customer2);
        if (isReadyOrder2) {
            System.out.println( customer2 + readyMessage);
            

        System.out.println( customer2 + displayTotalMessage + (latte*2) );

        } else {
            System.out.println( customer2 + pendingMessage);
        }  
        
        
        
        
        System.out.println( generalGreeting  + customer3);

        double priceDifference = latte - dripCoffee;
        
        if (isReadyOrder3) {
            System.out.println(customer2 + displayTotalMessage + priceDifference );
        } else {
            System.out.println(customer3 + pendingMessage );
        }
        
        
    }
}
