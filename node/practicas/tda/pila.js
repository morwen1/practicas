'use strict'
class Pila {
    constructor (items = []){
        this.items = items

    }
  

    size() {
        return this.items.length
    }

    extraer(){
        return this.items.pop
    }
    insertar(item){
        this.items.push(item)
    }
    estavacia(){
        return this.items == []
    }
    inspeccionar(){
        return this.items[this.items.length-1]
    }
}
//module.export.pila =  Pila