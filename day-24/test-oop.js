class Car{

    constructor(brand){
        this.brand = brand;
    }

    details(){
        return "I have a " + this.brand
    }


}

class Model extends Car{

    constructor(brand, model){
        super(brand)
        this.model = model
    }

    details(){
        return super.details() + ', it is a ' + this.model

    }
}

mycar = new Car("Mercedes")
console.log(mycar.details())

myOtherCar = new Model("Ford", "Mustang")
console.log(myOtherCar.details())