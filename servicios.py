def agregar_productos(inventario,nombre,precio,cantidad):
    
    
    productos={"nombre":nombre,
            "precio":precio,
            "cantidad":cantidad
}
    inventario.append(productos)
    print("se agrego correctamente el producto")
    



def mostrar_productos(inventario):
    if len(inventario)==0:
            print("no hay productos")
    else:
        for i in inventario:
            print(f"producto: {i["nombre"]}, precio: {i["precio"]}, cantidad {i["cantidad"]}")
    

def buscar_producto(inventario,nombre):
    for i in inventario:
         if i["nombre"].lower() == nombre.lower():
            return i
    return print("no se encuentra ese producto")

def actualizar_producto(inventario,nombre,nuevo_precio=None,nueva_cantidad=None):
    producto = buscar_producto(inventario,nombre)
    if producto:
        if nuevo_precio is not None:
            producto["precio"]= nuevo_precio
        if nueva_cantidad is not None:
            producto["cantidad"]= nueva_cantidad
        return print("se actualizo con exito")
    return False
     
def eliminar_producto(inventario,nombre):
    producto = buscar_producto(inventario,nombre)
    if producto:
        inventario.remove(producto)
        return print("se elimino con exito")
    return False



def calcular_estadistcicas(inventario):
    if not inventario:
        return None
    
    valorTotal = 0
    cantidadTotal = 0
    for i in inventario:
        valorTotal += i["cantidad"]*i["precio"]
        cantidadTotal+= i["cantidad"]
        
    producto_mas_caro = inventario[0]
    for i in inventario:
        if i["precio"]> producto_mas_caro["precio"]:
            producto_mas_caro=i
        
    producto_mayor_stock = inventario[0]
    for i in inventario:
        if i["cantidad"]> producto_mayor_stock["cantidad"]:
            producto_mayor_stock=i
        
    return{"valor_total":valorTotal,
        "cantidad_total":cantidadTotal,
        "producto_mas_caro":producto_mas_caro,
        "producto_mayor_stock":producto_mayor_stock
        }