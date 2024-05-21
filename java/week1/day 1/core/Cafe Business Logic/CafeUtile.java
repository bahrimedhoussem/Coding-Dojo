import java.util.ArrayList;



public class CafeUtile {

    public int getStreakGoal() {
        int numWeeks = 10;
        int sum = 0;
        for (int i = 1; i <= numWeeks ; i++ ) {

            sum += i ;

        }
        
        return sum ;
    }


    public double getOrderTotal(double[] prices) {

        double sum = 0;

        for (int i = 0 ; i <= prices.length-1; i++) {
            sum += prices[i];
        }
        return sum; 
    }
    public void displayMenu(ArrayList<String> menuItems){
        for (int i=0; i<menuItems.size();i++){
            System.out.println(menuItems.get(i));
        }
        }


}
