from Feactures import AFND, Estado

def kleen( afn1):
    
    afn3 =AFND(Estado(),Estado())
    
    afn3.inicial.agregar_transicion("e",afn1.inicial)
    afn3.inicial.agregar_transicion("e",afn3.final)
    
    afn1.final.agregar_transicion("e",afn3.final)
    afn1.final.agregar_transicion("e",afn1.inicial)
    
    
    return afn3
    
    
    
def opcional( afn1):
    
    afn3 =AFND(Estado(),Estado())
    
    afn3.inicial.agregar_transicion("e",afn1.inicial)
    afn3.inicial.agregar_transicion("e",afn3.final)
    afn1.final.agregar_transicion("e",afn3.final)
     
    return afn3    

def positiva( afn1):
    
    afn3 =AFND(Estado(),Estado())
    
    afn3.inicial.agregar_transicion("e",afn1.inicial)
    
    afn1.final.agregar_transicion("e",afn3.final)
    afn1.final.agregar_transicion("e",afn1.inicial)
     
    return afn3    
     
    
def concatenacion(A1,A2):
    
    A1.final.transiciones.update(A2.inicial.transiciones)
    A1.final = A2.final
    
        
    return A1

def union(A1,A2):
    
    A3 = AFND(Estado(),Estado())
    
    if A3:
        A3.inicial.transiciones.append["e"] = A1.inicial
        A3.inicial.transiciones.append["e"] = A2.inicial

        A1.final.transiciones.append["e"] = A3.final
        A2.final.transiciones.append["e"] = A3.final

    return A3