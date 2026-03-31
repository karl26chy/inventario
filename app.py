inventario =[]

while True:
    print("1) agregar producto")
    print("2) mostrar inventario")
    print("3) buscar producto")
    print("4) actualizar producto")
    print("5) eliminar producto")
    print("6) calcular estadistica")
    print("7) salir")

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

        
        
        

    elif eleccionMenu =="2":
        
    elif eleccionMenu=="7":
        print("saliendo..")
        break
