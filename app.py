from servicios import *
from archivos import *

inventario =[]

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

    eleccionMenu = input("ingrese una opcion = ")

    if eleccionMenu =="1":
        nombre = input("ingresa el nombre = ")
        while True:

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
        agregar_productos(inventario,nombre,precio,cantidad)
        

    elif eleccionMenu =="2":
        mostrar_productos(inventario)
    
    elif eleccionMenu =="3":
        nombre = input("buscar producto = ")
        print(buscar_producto(inventario,nombre))
    
    elif eleccionMenu =="4":
        nombre= input("producto = ")
        if buscar_producto(inventario,nombre):
            precio = float(input("nuevo precio = "))
            cantidad =int(input("nueva cantidad = "))
            actualizar_producto(inventario,nombre,precio,cantidad)
    
    elif eleccionMenu =="5":
        nombre=input("producto que desea eliminar = ")
        eliminar_producto(inventario,nombre)
    
    elif eleccionMenu =="6":
        
        stats= calcular_estadistcicas(inventario)
        if stats is None:
            print("no hay productos")
        else:
            print("----estadisticas-----")
            print(f"valor total es: {stats['valor_total']}")
            print(f"la cantidad total es: {stats['cantidad_total']}")
            print(f"el producto mas caro: {stats['producto_mas_caro']}")
            print(f"producto con mayor stock: {stats['producto_mayor_stock']}")
    
    elif eleccionMenu =="7":
        guardar_csv(inventario,"inventario.csv")
    
    elif eleccionMenu =="8":
        inventario= cargar_csv("inventario.csv")
            
    elif eleccionMenu=="9":
        print("saliendo..")
        break
    else:
        print("elige una opcion valida")
