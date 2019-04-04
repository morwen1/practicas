from stda.cola import Cola
import random as rd


def papaCaliente(items=[]):
    vueltas = rd.randint(0,len(items)*2)
    colasimulacion = Cola()
    for item in items:
        colasimulacion.agregar(item)
    while colasimulacion.tamano() > 1 :
        for i in range(vueltas):
            colasimulacion.agregar(colasimulacion.avanzar())
        colasimulacion.avanzar()
        print(colasimulacion.items)
    return colasimulacion.avanzar()

print(papaCaliente(["Bill","David","Susan","Jane","Kent","Brad"]))
