from stda.rsi_pila import Pila


def dividepor2 (numeroDecimal):
    pilaResiduo = Pila()

    while numeroDecimal > 0 :
        residuo = numeroDecimal % 2 
        pilaResiduo.incluir(residuo)
        numeroDecimal = numeroDecimal // 2
    #pilaResiduo.imprimir()
    cadenaBinaria = '' 

    while not pilaResiduo.estaVacia():
        cadenaBinaria += str(pilaResiduo.extraer())

    return cadenaBinaria





print(dividepor2(500))