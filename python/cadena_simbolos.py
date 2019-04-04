from stda.rsi_pila import Pila


def verifcarParentesis(cadenas):
    """
    ['(']
    ['(', '(']
    ['(', '(', '(']
    ['(', '(', '(', '(']
    el algoritmo agrega todos los parentesis de apertura 
    """
    p = Pila()
    balanceados = True
    indice = 0 
    while indice < len(cadenas) and balanceados == True:
        simbolo = cadenas[indice]
        if simbolo == '(':
            p.incluir(simbolo) 
            p.imprimir()

        else : 
            if p.estaVacia() :
                balanceados = False
            elif simbolo == ')' : #esto funciona solo con else pero esta asi para entender mejor el algoritmo por que soy bruto
                #print(simbolo) elimina un simbolo de la pila, el valor devuelto no se utiliza
                p.extraer()
        indice += 1 
    if balanceados == True and p.estaVacia():
        return True
    else: 
        return False
    




print(verifcarParentesis('(((())))'))
#print(verifcarParentesis('(()'))
