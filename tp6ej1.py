################
# MARTIN DARRICADES Sebastián - @sebasamd
# BOCCHIGLIERE Andrés - @AndresBochi - elmaildeandresbochi@gmail.com
# CHECCARELLI Sergio -@checas
# UNRN Andina - Introducción a la Ingenieria en Computación
################

# Implementar una función que determine si dos cadenas son anagramas entre si,
# ignorando espacios y diferencias entre mayusculas y minusculas.

def dividir_cadena_en_lista(cadena):
    """
    Esta función toma como argumento una cadena y devuelve una lista con los caracteres de la cadena
    
    """
    return [caracter for caracter in cadena]

def es_anagrama(cadena1, cadena2):
    """
    Esta función devuelve True si las cadenas pasadas como argumentos son anagramas
    
    """
    
    cadena1 = cadena1.replace(" ", "")
    cadena2 = cadena2.replace(" ", "")
    cadena1 = cadena1.lower()
    cadena2 = cadena2.lower()
    cadena1 = dividir_cadena_en_lista(cadena1)
    cadena2 = dividir_cadena_en_lista(cadena2)

    anagrama = False
    
    if len(cadena1) != len(cadena2):
        anagrama = False
        return anagrama
    else:
        for caracter in cadena1:
            if caracter in cadena2:
                anagrama = True
                cadena2.remove(caracter)     
            else:
                anagrama = False
                break
        return anagrama      
    

def principal():
    print("¿Es Anagrama?")
    print("\nIntroduzca una palabra o frase: ")
    frase1 = input()
    print("Introduzca una segunda palabra o frase para verificar si es anagrama de la primera: ")
    frase2 = input()
    
    if es_anagrama(frase1, frase2):
        print(f"\n'{frase1}' es anagrama de '{frase2}'")
    else:
        print(f"\n'{frase1}' NO es anagrama de '{frase2}'")
                                        
if __name__ == "__main__":
    principal()

