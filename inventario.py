inventario =[]
print("1) agregar producto")
print("2) mostrar inventario")
print("3) calcular estadistica")
print("4) salir")

while True:
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

        productos={"nombre":nombre,
                   "precio":precio,
                   "cantidad":cantidad
                  }
        inventario.append(productos)
        print("se agrego correctamente el producto")
        costoTotal = cantidad*precio 

    elif eleccionMenu =="2":
        if len(inventario)==0:
             print("no hay productos")
        else:
            for i in inventario:
                print(f"producto: {i["nombre"]}, precio: {i["precio"]}, cantidad {i["cantidad"]}")

    elif eleccionMenu=="4":
        print("saliendo..")
        break

print(f"producto {nombre}, precio {precio}, cantidad {cantidad}, total {costoTotal}")