"""🎯 Objetivo:
Crear una función llamada escribir_log que:

Reciba un mensaje y un nivel de log (DEBUG, INFO, WARNING, ERROR o CRITICAL).

Escriba ese mensaje en un archivo log.txt, con la fecha y hora actual.

Cada línea debe verse así:

txt
Copiar
Editar
[2025-07-21 11:40:12] [INFO] Inicio del programa
🔧 Requisitos técnicos:
El archivo se llama log.txt (se abre en modo append).

Usá datetime.now() para registrar la fecha y hora.

El texto debe estar codificado en UTF-8."""

from datetime import datetime
def escribir_log(info, nivel):
    
    niveles_validos = ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]
    nivel = nivel.upper()

    if nivel not in niveles_validos:
        raise ValueError(f"Nivel de log invalido: {nivel}. Debe ser uno de: {', '.join(niveles_validos)}")  
      
    fecha_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    linea = f"[{fecha_hora}] [{nivel.upper()}] {info}\n"
    
    # Se agrega informacion al log (se crea si no existe)
    with open(r"log.txt","a",encoding="utf-8") as archivo:
        archivo.write(linea)
    
def abrir_archivo(archivo):
    try:
        with open(f"{archivo}","r", encoding = "utf-8") as arch:
            print(arch.read())       
    except:
        escribir_log(f" No se pudo leer el archivo {archivo}","ERROR")
    
abrir_archivo("agenda.txt")





