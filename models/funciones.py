# Punto 1 ¿Esto es sano?

def ingrediente_es_sano(calorias:int, es_vegetariano:bool) -> bool:
    
    if calorias < 100 or es_vegetariano:
        return True
    return False



# Punto 2 Contar Calorias

def contar_calorias(ingredientes:list) -> float:
    
    total_calorias = 0
    
    for ingrediente in ingredientes:
        total_calorias += ingrediente.obtener_calorias()
        
    return round((total_calorias*0.95), 2)

# Punto 3
def calcular_costo_producto(ingredientes:list) -> int:
    
    total_costo_producto = 0
    
    for ingrediente in ingredientes:
        total_costo_producto += ingrediente.obtener_precio()
        
    return total_costo_producto

# Punto 4

def calcular_rentabilidad_producto(precio_producto:int,ingredientes:list) -> int:
    
    total_costo_producto = calcular_costo_producto(ingredientes)
    
    return precio_producto - total_costo_producto
    

# Punto 5

def producto_mas_rentable(productos:list) -> str:
    
    mas_rentable_producto = ''
    mas_rentable = 0
    
    for producto in productos:
        if producto.calcular_rentabilidad() > mas_rentable:
            mas_rentable_producto = producto
            mas_rentable = producto.calcular_rentabilidad()
            
    return mas_rentable_producto.obtener_nombre()
    
