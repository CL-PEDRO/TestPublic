def baseCase(ArrayLetrasOperandos):
    
    
    
    ArrayLetrasOperandosModificados = [] * (len(ArrayLetrasOperandos) + 1 )
    
    for i,signo in enumerate(ArrayLetrasOperandos):
        if signo.isalpha():
            ArrayLetrasOperandosModificados[i] = f"se creo caso base f{signo}"
        else:
            ArrayLetrasOperandosModificados[i] = ArrayLetrasOperandos[i]
            
            
testArray = ["A","B","|","+"]



            
