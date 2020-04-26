import java.util.Map;
import java.util.ArrayList;

class Ubervan extends Car {
    Map<String, Map<String, Integer>> typeCarAccepted;
    ArrayList <String> seatsMaterial;
    public Ubervan(String license, Integer passegenger, Account driver, String brand, String model,Map <String, Map<String, Integer>> typeCarAccepted, ArrayList <String> seatsMaterial){
        super(license, passegenger, driver);
        this.typeCarAccepted = typeCarAccepted;
        this.seatsMaterial=seatsMaterial;
    }
}