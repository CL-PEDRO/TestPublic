class Estado:
    def __init__(self):
        self.transiciones = {}  
        self.epsilon = []  
    
    def agregar_transicion(self, simbolo, estado):
        if simbolo not in self.transiciones:
            self.transiciones[simbolo] = []
        self.transiciones[simbolo].append(estado)

class AFND:
    def __init__(self, inicial, final):
        self.inicial = inicial
        self.final = final


def makeCaseBase(LetterToTransition):
    
    NewCaseBase = AFND(Estado(),Estado())
    
    if NewCaseBase:
        
        NewCaseBase.inicial.transiciones[f'{LetterToTransition}'] = NewCaseBase.final
        print(f"base case made con {LetterToTransition}")
        return NewCaseBase
    
    return None

def baseCase(ArrayLetrasOperandos):
    
    
    tam = (len(ArrayLetrasOperandos) + 1 )
    ArrayLetrasOperandosModificados = []
    
    for i,signo in enumerate(ArrayLetrasOperandos, start=0):
        if signo.isalpha():
            ArrayLetrasOperandosModificados.append(makeCaseBase(signo))
        else:
            ArrayLetrasOperandosModificados.append(ArrayLetrasOperandos[i])

    return ArrayLetrasOperandosModificados 

