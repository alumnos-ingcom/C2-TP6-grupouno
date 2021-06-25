################
# MARTIN DARRICADES Sebastián - @sebasamd
# BOCCHIGLIERE Andrés - @AndresBochi - elmaildeandresbochi@gmail.com
# CHECCARELLI Sergio -@checas
# UNRN Andina - Introducción a la Ingenieria en Computación
################

# Implementar una función que determine si dos cadenas son anagramas entre si,
# ignorando espacios y diferencias entre mayusculas y minusculas

def levantar_datos():
    archivo = open('anagramas.txt', 'r', encoding='UTF-8')
    lista = []
    for linea in archivo.readlines():
        linea_sin_espacios = linea.replace(" ", "")
        linea_sin_comas = linea_sin_espacios.replace(",", "")
        linea_sin_guion = linea_sin_comas.replace('–', ',')
        linea_sin_salto = linea_sin_guion.replace('\n', '')
        final = linea_sin_salto.split(",")
        for i in final:
            lista.append(i)
    print(lista)
    archivo.close
    return lista

def niidea(lista):
    """Esta funcion toma de a dos elementos de una lista y revisa si son anagramas llamando a la otra funcion"""
    indice_movil = 0
    indice_movil2 = 1
    #Los indices sirve, para tomar de a dos items.
    largo_lista = len(lista)
    elementos_pares = 0
    for elemento in lista:
        while elementos_pares < largo_lista:
            cadena1 = lista[indice_movil]
            cadena2 = lista[indice_movil2]
            if es_anagrama(cadena1, cadena2):
                print(f"\n'{cadena1}' es anagrama de '{cadena2}'")
            else:
                print(f"\n'{cadena1}' NO es anagrama de '{cadena2}'")
            elementos_pares += 2
            indice_movil += 2
            indice_movil2 += 2
    pass


def dividir_cadena_en_lista(cadena):
    """
    Esta función toma como argumento una cadena y devuelve una lista con los caracteres de la cadena
    
    """
    return [caracter for caracter in cadena]

def es_anagrama(cadena1, cadena2):
    """
    Esta función devuelve True si las cadenas pasadas como argumentos son anagramas
    
    """
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
    datos = levantar_datos()
    prueba = niidea(datos)
                                        
if __name__ == "__main__":
    principal()

