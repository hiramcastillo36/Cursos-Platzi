class Car {
    Account driver;
    Integer passegenger;
    String license;
    public Car(String license, Integer passegenger, Account driver){
        this.license=license;
        this.passegenger = passegenger;
        this.driver=driver;   
    }

    void printdata(){
        System.out.println("ID: " + driver.id + " License: " + license + " Driver: " + driver.name + " Passengenger: " + passegenger);
    }
}