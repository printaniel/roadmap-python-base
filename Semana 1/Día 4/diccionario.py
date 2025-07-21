""" Diccionarios
Crear un diccionario con información de un contacto (nombre, teléfono, email)

Modificar el teléfono.

Agregar una nueva clave: direccion.

Iterar e imprimir clave y valor."""

contacto = {"Nombre": "Aniel Varela", "Teléfono": "53344256", "Email":"anielvarela64@gmail.com"}

contacto["Teléfono"] = "55518924"
contacto["Dirección"] = "Ave. este entre 3ra y 5ta"

print("\nInformación del estudiante \n")
for clave,valor in contacto.items():
    print(f"{clave}: {valor}")
    
print("\n")