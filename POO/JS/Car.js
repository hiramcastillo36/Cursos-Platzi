class Car{
    constructor(license, driver){
        this.id;
        this.license = license;
        this.driver = driver;
        this.passenger;
    }

    printDataCar = function(){
        console.log(this.license)
        console.log(this.driver)
    }
}