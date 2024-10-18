from Feactures import *
from Funtions import *



def Creacion(expresionParser):
    
    #MasterAFND = AFND()
    testArray = 'a|b'
    
    checkedText = agregaPunto(testArray)

    print("Cheking",agregaPunto(testArray))

    parserText = parser(checkedText)

    print("Parser",parserText)

    finalText = baseCase(parserText)

    #print(finalText[0].inicial.transiciones)    
    pila = []
    PoppedElements = []
    
    print(finalText)
    
    for i,valor in enumerate(finalText,start=0):
        
        if isinstance(valor,AFND): 
            pila.append(valor)
        elif valor == "*":
        
            pila.append(kleen(pila.pop()))
                      
        elif valor == "+":
            pila.append(positiva(pila.pop()))
        elif valor == "?":
            pila.append(opcional(pila.pop()))
        elif valor == ".":
            PoppedElements.append(pila.pop())
            PoppedElements.append(pila.pop())
         
            print("Elemetnos para verificar")
            print(type(PoppedElements[0]))
            print(type(PoppedElements[1]))
            pila.append(concatenacion(PoppedElements[1],PoppedElements[0]))
            PoppedElements.clear()
        elif valor == "|":
            PoppedElements.append(pila.pop())
            PoppedElements.append(pila.pop())
            print("Elemetnos para verificar",PoppedElements)
            pila.append(union(PoppedElements[1],PoppedElements[0]))
            PoppedElements.clear()
                        
    return pila       


#Prueba = AFND(Estado(),Estado())
#Prueba2 = AFND(Estado(),Estado())

#Prueba.inicial.agregar_transicion("e",Prueba2.final)
#Prueba.inicial.agregar_transicion("e",Prueba2.inicial)


#print(9)

            
MainNode = Creacion('ab')  
MainNode[0].final.isStateFinal = True
MainNode[0].final.number = contador
enumerateOfNodos(MainNode[0].inicial)

print("Hol")
