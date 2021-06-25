################
# MARTIN DARRICADES Sebastián - @sebasamd
# BOCCHIGLIERE Andrés - @AndresBochi - elmaildeandresbochi@gmail.com
# CHECCARELLI Sergio -@checas
# UNRN Andina - Introducción a la Ingenieria en Computación
################

# Crear un programa que solicite al usuario un archivo de entrada y
# uno de salida para copiar el contenido de un archivo en el otro.


class ArchivoNoEncontrado(Exception):
    pass

def abrir_archivo(archivo, modo):
    try:
        archivo_abierto = open(archivo, modo, encoding="UTF-8")
        
    except FileNotFoundError as err:
        raise ArchivoNoEncontrado("No se encontró el archivo") from err
    
    return archivo_abierto
    
def copiadora(archivo_entrada, archivo_salida):
    """
    Esta función sobreescribe el contenido de un archivo .txt de entrada (1er argumento)
        en otro .txt de salida (2do argumento)
    
    """
    entrada = abrir_archivo(archivo_entrada, "r")
    salida = abrir_archivo(archivo_salida, "w")
    
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
    
    try:
        print("\nRealizando copia")
        copiadora(archivo1, archivo2)
        print("\n¡Copia finalizada!")
    except ArchivoNoEncontrado:
        print("\n¡No se encontró el archivo!")
    
    

if __name__ == "__main__":
    principal()
