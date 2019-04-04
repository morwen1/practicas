from stda.rsi_pila import Pila


def convertir_base (numeroDecimal,base):
    digitos = "0123456789ABCDEF"

    pilaResiduo = Pila()

    while numeroDecimal > 0 : 
        residuo = numeroDecimal % base 
        pilaResiduo.incluir(residuo)
        numeroDecimal = numeroDecimal // base 
    
    nuevacadena = '' 
    while not pilaResiduo.estaVacia() :
        nuevacadena += digitos[pilaResiduo.extraer()]
    
    return nuevacadena


print(convertir_base(26,26))