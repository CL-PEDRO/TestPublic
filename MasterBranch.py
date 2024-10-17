from Feactures import *
from Funtions import *



def Creacion(expresionParser):
    
    MasterAFND = AFND()
    testArray = 'a|c'
    
    checkedText = agregaPunto(testArray)

    print("Cheking",agregaPunto(testArray))

    parserText = parser(checkedText)

    print("Parser",parserText)

    finalText = baseCase(parserText)

    print(finalText[0].inicial.transiciones)
    
        
    pila = []
    
    for i,valor in enumerate(finalText,start=0):
        if isinstance(expresionParser[i],AFND):  # Si es un operando (carácter del alfabeto) :d
            pila.append(valor)
        elif valor == "*":
            MasterAFND = kleen(pila.pop())
        elif valor == "+":
            pass
        elif valor == "?":
            pass
        elif valor == ".":
            pass
        elif valor == "|":
            union()
            
            
                    

    