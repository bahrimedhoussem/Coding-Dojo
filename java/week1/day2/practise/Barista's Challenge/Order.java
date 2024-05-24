import java.util.ArrayList;

public class Order {
    // Member variables 
    private String name;
    private Boolean ready;
    private ArrayList<Item> items ;

     // constructor 
    public Order() {
        this.name = "Guest";
        this.items = new ArrayList<>()
    }
    // overloaded constructor
    public Order(String name ) {
        this.name = name;
        this.items = new ArrayList<>()
    }

    //Order constructor 

    public void addItem(Item item){
        items.add(item);
    }

    //Order constructor

    public String getStatusMessage(){
        if   ( ready == true) {
            return "Your order is ready";
        }else {
            return "Thank you for waiting . Your order will be ready soon.";
        }
    }

    public double getOrderTotal() {
        double total = 0.0;
        for (int i=0 ; i<this.items.size() ; i++ ) {
        total += this.items.get(i).getPrice();
        }
        return total;
    }

}