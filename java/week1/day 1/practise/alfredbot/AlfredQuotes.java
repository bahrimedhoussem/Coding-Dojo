import java.text.SimpleDateFormat;
import java.util.Date;
public class AlfredQuotes {
    

    public String guestGreeting(String name) {
        // YOUR CODE HERE
        return String.format("Hello %s, lovely to see you. How are you?", name);
    }
    
    public String dateAnnouncement() {
        Date currentDate = new Date ();
        SimpleDateFormat formatter = new SimpleDateFormat("EEEE MMMM dd HH:mm:ss zzz yyyy");
        return String.format ("It is currently"+ formatter.format(currentDate) );
    }
    


    public String respondBeforeAlexis(String conversation) {
        if (conversation.contains("Alexis")) {
        return "Right away, sir. She certainly isn't sophisticated enough for that.";
        } else if (conversation.contains("Alfred")) {
        return "At your service. As you wish, naturally.";
        } else {
        return "Right. And with that I shall retire.";
        }
    }
      
    
	// NINJA BONUS
	// See the specs to overload the guestGreeting method
        // SENSEI BONUS
        // Write your own AlfredQuote method using any of the String methods you have learned!
}

