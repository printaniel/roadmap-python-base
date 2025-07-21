import matematicas
import utilidades
from rich import print
from rich.table import Table
from rich.console import Console
from rich.text import Text
import inspect
import time

consola = Console()
table = Table(title = "[bold green]Calculadora Inteligente[/bold green]")

table.add_column("Aritmética", style="bold cyan")
table.add_column("Geometría", justify="right", style="green")

table.add_row("1. suma","5. Perimetro del Triangulo")
table.add_row("2. resta","6. Area del Trianagulo")
table.add_row("3. multiplicación", "7. Perimetro del Cuadrado")
table.add_row("4. división","8. Area del Cuadrado")
table.add_row("           ","9. Perimetro del Rectangulo")
table.add_row("           ","10. Area del Rectangulo")

texto = Text("0. Salir del programa", style = "bold red",justify = "center")
table.add_row(texto, "")

consola.print(table)
opcion = None

opciones_diccionario = {
    "1": matematicas.aritmetica.suma,
    "2": matematicas.aritmetica.resta,
    "3": matematicas.aritmetica.multplicacion,
    "4": matematicas.aritmetica.division,
    "5": matematicas.geometria.perimetro_triangulo,
    "6": matematicas.geometria.area_triangulo,
    "7": matematicas.geometria.perimetro_cuadrado,
    "8": matematicas.geometria.area_cuadrado,
    "9": matematicas.geometria.perimetro_rectangulo,
    "10": matematicas.geometria.area_rectangulo
}
contador_tabla = 0
contador_tabla_anterior = 0
while opcion != "0":
     opcion = input( "Elija una opcion: ")
     
  
     
     if opcion != "0":
        opcion_elegida = opciones_diccionario.get(opcion)
        
        if opcion_elegida:
            # Obtener la cantidad de parametros que pide la funcion
            parametros = inspect.signature(opcion_elegida).parameters
            numeros = []
            # Pedir cada parametro por consola
            for i in parametros:
                numeros.append(input("Escriba un numero: "))
            try:           
                print(f"Resultado: {opcion_elegida(*numeros)}")
                contador_tabla += 1
                
                if(contador_tabla == contador_tabla_anterior + 3):
                    contador_tabla_anterior +=3
                    time.sleep(0.5)
                    consola.print(table)
                
                
            except Exception as e:
                print("[bold red]Error[/bold red]:",e)
            
        else:
            print("[bold red]Opción inválida, intenta de nuevo.[/bold red]")
     else:
         print("[red]Has salido del programa[/red]")
         
     


if __name__=="__main__":
    print("Prueba del modulo main terminada")