#importamos los modulos servicios y archivos.
from servicios import *
from archivos import *
#creamos el inventario
inventario =[]

#creamos el while con el menu para que este se repita.
while True:
    print("1) agregar producto")
    print("2) mostrar inventario")
    print("3) buscar producto")
    print("4) actualizar producto")
    print("5) eliminar producto")
    print("6) calcular estadistica")
    print("7) guardar csv")
    print("8) cargar csv")
    print("9) salir")
#input para elegir la opcion
    eleccionMenu = input("ingrese una opcion = ")
#condicional para condicionar la accion
    if eleccionMenu =="1":
        nombre = input("ingresa el nombre = ")
        while True:
#usamos try except para evitar que se error con el programa si se ingresa un carácter no valido.
            try:
                precio = float(input("ingresa el precio = ")) 
                break
            except ValueError:
                print("ingrese un valor correcto")

        while True:
            try:
                cantidad = int(input("ingrese una cantidad = "))
                break
            except ValueError:
                print("ingrese un valor correcto")
#ingresamos la funcion para agregar los productos.
        agregar_productos(inventario,nombre,precio,cantidad)
        

    elif eleccionMenu =="2":
        #ingresamos la funcion de mostrar productos.
        mostrar_productos(inventario)
    
    elif eleccionMenu =="3":
        nombre = input("buscar producto = ")
        #imprimimos la funcion buscar producto.
        print(buscar_producto(inventario,nombre))
    
    elif eleccionMenu =="4":
        nombre= input("producto = ")
        if buscar_producto(inventario,nombre):
#añadimos un condicional en la funcion buscar producto donde si se cumple pasa al siguiente proceso con la funcion actualizar producto.
            precio = float(input("nuevo precio = "))
            cantidad =int(input("nueva cantidad = "))
            actualizar_producto(inventario,nombre,precio,cantidad)
    
    elif eleccionMenu =="5":
        nombre=input("producto que desea eliminar = ")
        #añadimos la funcion eliminar producto.
        eliminar_producto(inventario,nombre)
    
    elif eleccionMenu =="6":
        
        stats= calcular_estadistcicas(inventario)
        #creamos una variable para la funcion calcular estadisticas.

        if stats is None:
            print("no hay productos")
#le colocamos una condicional esto con el fin de que si la lista esta vacia nos tire el NONE.
        else:
#imprimimos todos los resultados pedidos de calcular estadisticas.
            print("----estadisticas-----")
            print(f"valor total es: {stats['valor_total']}")
            print(f"la cantidad total es: {stats['cantidad_total']}")
            print(f"el producto mas caro: {stats['producto_mas_caro']}")
            print(f"producto con mayor stock: {stats['producto_mayor_stock']}")
    
    elif eleccionMenu =="7":
        guardar_csv(inventario,"inventario.csv")
        #imprimimos la funcion guardar csv.
    elif eleccionMenu =="8":
        inventario= cargar_csv("inventario.csv")
         #imprimimos la funcion cargar csv.
            
    elif eleccionMenu=="9":
        print("saliendo..")
        break
    #añadimos un break para cuando se elija la opción 9 se cierre el sistema.
    else:
        print("elige una opcion valida")
