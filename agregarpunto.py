def agregaPunto(expresionR): 
    resultado = ""
    j = 0
    i = 0
    tam = len(expresionR)
    
    expre = [' '] * (tam +1) 
    
    while j < len(expresionR):
    
        expre[j] = expresionR[j]
        j = j+1
   
    while i < len(expresionR):
        expresion = expresionR[i]
             
        # Salta los caracteres especiales
        if expresion in ('(', '|'):
            resultado += expresion
            i += 1
            continue  
        # Si encuentra 'L' o 'l' al inicio de 'Letra'
        if expresion in ('L', 'l'):
            if comprobarLetra(expresionR[i:]):  # Verificar si comienza con "letra"
                if expre[i+5] in ( ')', '+', '*', '|', '?',' '):
                    resultado += "Letra"
                    i += 5
                    continue 
                else:
                    resultado += "Letra"  # Agregar "Letra" completo
                    resultado += '.'  # Insertar un punto después
                    i += 5  # Saltar el resto de "Letra"
                    continue
        # Si encuentra 'D' o 'd' al inicio de 'Digito'
        elif (expresion == 'D' or expresion == 'd'):
            if comprobarDigito(expresionR[i:]):  # Verificar si comienza con "digito"
                if expre[i+6] in ('(', ')', '+', '*', '|', '?'):
                    resultado += "Digito" 
                    i += 6
                    continue 
                else:
                    resultado += "Digito"  # Agregar "Digito" completo
                    resultado += '.'  # Insertar un punto después
                    i += 6  # Saltar el resto de "Digito"
                    continue
        
        # Si es una letra o digito no verificado, agregar el caracter actual
        if expre[i+1] in (')', '+', '*', '|', '?'):
            resultado += expresion
        else:
            resultado += expresion
            resultado += '.'  # Insertar un punto después de cada letra
        i += 1  # Avanza al siguiente caracter
    
    return resultado.rstrip('.')  # Eliminar el último punto si existe

def comprobarLetra(ExpresionR):
    if ExpresionR[0]== 'l':
        return ExpresionR.startswith("letra") 
    else:
        return ExpresionR.startswith("Letra")
    
def comprobarDigito(ExpresionR):
    
    if ExpresionR[0]== 'd':
        return ExpresionR.startswith("digito") 
    else:
        return ExpresionR.startswith("Digito")
