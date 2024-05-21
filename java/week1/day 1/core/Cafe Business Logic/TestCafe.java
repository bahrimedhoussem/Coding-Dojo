import java.util.ArrayList;
import java.util.Arrays;




public class TestCafe {
    public static void main(String[] args) {
        
        CafeUtile appTest = new CafeUtile();

        int streakGoal = appTest.getStreakGoal();

        System.out.println("Total drinks needed for 10 week streak: " + streakGoal);

            }
        


            ArrayList<double> menu = new ArrayList<double>();
            menu.add(3.22);
            menu.add(4.23);
            menu.add(5.23);
            System.out.println(menu); 
            
            
            ArrayList<string> menu = new ArrayList<string>();
            menu.add("drip coffee");
            menu.add("cappuccino");
            menu.add("latte");
            appTest.displayMenu(menu);
            
        }


