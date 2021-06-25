################
# MARTIN DARRICADES Sebastián - @sebasamd
# BOCCHIGLIERE Andrés - @AndresBochi - elmaildeandresbochi@gmail.com
# CHECCARELLI Sergio -@checas
# UNRN Andina - Introducción a la Ingenieria en Computación
################

# Crear un programa que solicite al usuario un archivo de entrada y
# uno de salida para copiar el contenido de un archivo en el otro.

def copiadora(archivo_entrada, archivo_salida):
    """
    Esta función sobreescribe el contenido de un archivo .txt de entrada (1er argumento)
        en otro .txt de salida (2do argumento)
    
    """
    with open(archivo_entrada, "r", encoding="UTF-8") as entrada:
        with open(archivo_salida, "w", encoding="UTF-8") as salida:
            for linea in entrada:
                salida.write(linea)
                
def principal():
    
    print("Programa Copiadora:")
    print("Este programa copia el contenido del primer archivo de texto solicitado en el segundo")
    
    # Probar con entrada: Archivo1.txt y salida: Archivo2.txt (subidos al repositorio)
    
    print("\nIndique el nombre del primer archivo: (Formato de ingreso: Nombre.txt)")
    archivo1 = str(input())
    print("\nAhora indique el nombre del archivo de destino: (Formato de ingreso: Nombre.txt)")
    archivo2 = str(input())
    
    print("\nRealizando copia")
    copiadora(archivo1, archivo2)
    print("\n¡Copia finalizada!")

if __name__ == "__main__":
    principal()
