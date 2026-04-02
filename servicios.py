def agregar_productos(inventario,nombre,precio,cantidad):
#creamos la funcion de agregar productos.
    
    productos={"nombre":nombre,
            "precio":precio,
            "cantidad":cantidad
}  #creamos el diccionario y añadiendo el metodo de append para que pueda el usuario añadir producto.
    inventario.append(productos)
    print("se agrego correctamente el producto")
    



def mostrar_productos(inventario):
    #utilizamos len para que recorra inventario y asi decidir si esta vacio o no.
    if len(inventario)==0:
            print("no hay productos")
    #si no se usara un for para que con iterador recorra la lista de inventario y muestre su contenido.
    else:
        for i in inventario:
            print(f"producto: {i["nombre"]}, precio: {i["precio"]}, cantidad {i["cantidad"]}")
    

def buscar_producto(inventario,nombre):
    #usamos for para recorrer lista y .lower para no tener conflictos de mayus con minusculas en la busqueda del producto.
    for i in inventario:
         if i["nombre"].lower() == nombre.lower():
            return i
    return print("no se encuentra ese producto")

def actualizar_producto(inventario,nombre,nuevo_precio=None,nueva_cantidad=None): #añadimos nuevos parametros para actualizar solo (precio) y (cantidad).
    producto = buscar_producto(inventario,nombre)
    if producto:
        if nuevo_precio is not None: #se verifica si hubo cambios.
            producto["precio"]= nuevo_precio #se actualiza.
        if nueva_cantidad is not None:
            producto["cantidad"]= nueva_cantidad #se actualiza.
        return print("se actualizo con exito")
    return False
     
def eliminar_producto(inventario,nombre):
    producto = buscar_producto(inventario,nombre)
    if producto:                                    #si el producto es encontrado se elimina con .remove.
        inventario.remove(producto)           
        return print("se elimino con exito")
    return False



def calcular_estadistcicas(inventario):
    if not inventario:                 #si la lista esta vacia retornara en NONE.
        return None
    
    valorTotal = 0                      #creamos acomuladores para que guarden los ciclos.
    cantidadTotal = 0
    for i in inventario:
        valorTotal += i["cantidad"]*i["precio"]    #definimos las operaciones a realizar.
        cantidadTotal+= i["cantidad"]
        
    producto_mas_caro = inventario[0]             #definimos la variable 
    for i in inventario:
        if i["precio"]> producto_mas_caro["precio"]:
            producto_mas_caro=i                        #el producto mas caro reemplazara al iterador.
        
    producto_mayor_stock = inventario[0]
    for i in inventario:
        if i["cantidad"]> producto_mayor_stock["cantidad"]:
            producto_mayor_stock=i
        
    return{"valor_total":valorTotal,
        "cantidad_total":cantidadTotal,               #retorna el diccionario con las estadisticas.
        "producto_mas_caro":producto_mas_caro,
        "producto_mayor_stock":producto_mayor_stock
        }