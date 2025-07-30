class ErrorDeNegocio(Exception):
        """Base para errores de logica de negocio"""
        pass

class ProductoNoEncontrado(ErrorDeNegocio):   
        def __init__(self,nombre):
            super().__init__(f"No se ha encontrado un producto con el nombre: {nombre}")
class InventarioVacioError(ErrorDeNegocio):
        
        def __init__(self):
                super().__init__(f"El inventario esta vacío")
class InventarioNoEncontradoError(ErrorDeNegocio):
        
        def __init__(self):
                super().__init__("No existe ningun inventario de productos")
            
class NombreVacio(ValueError):    
        def __init__(self):
            super().__init__(f"El nombre del producto no puede estar vacío")
            
class NombreAlfabeticoInvalido(ValueError):
        def __init__(self,nombre):
            super().__init__(f"El nombre ({nombre}) no es válido para un producto")
            
class NombreDuplicado(ValueError):
        def __init__(self, nombre):
            super().__init__(f"Ya existe un producto con el nombre: {nombre}")
            
class ValorNoNumerico(ValueError):
        
        def __init__(self):
                super().__init__("Solo se aceptan valores numéricos")

class NumeroNoPositivo(ValueError):
        
        def __init__(self):
                super().__init__("Solo se aceptan numeros positivos ")

class NumeroNoEntero(ValueError):
        
        def __init__(self):
                super().__init__("Solo se aceptan numeros enteros")

class PermisoEdicionDenegado(PermissionError):
        
        def __init__(self):
                super().__init__("El archivo está en uso o sin permisos.")