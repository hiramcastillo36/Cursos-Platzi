class Uberpool extends Car {
    String brand;
    String model;
    
    public Uberpool(String license, Integer passegenger, Account driver, String brand, String model){
        super(license, passegenger, driver);
        this.brand = brand;
        this.model=model;
    }
}