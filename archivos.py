import csv     #importamos el modulo csv que sirve para leer y escribir archivos csv.

def guardar_csv(inventario,ruta,incluir_header=True):         #definimos la funcion para guardar el inventario en un archivo csv.
    
    if not inventario:
        print("inventario vacio, no se puede guardar.")
        return
    try:                                                    #usamos try except para manejo de errores.
        with open(ruta,"w",newline="", encoding="utf-8") as archivo:
            writer= csv.writer(archivo)  #crea un objeto para escribir en formato csv.
            if incluir_header:
                writer.writerow(["nombre","precio","cantidad"])
            for i in inventario:
                writer.writerow([i["nombre"],i["precio"],i["cantidad"]])

        print(f"inventario guardado en: {ruta}")  #se imprime si se guarda correctamente.

    except Exception as e:
        print("error al guardar:", e)

def cargar_csv(ruta):   #creamos la funcion para leer archivo csv y convertirlo en lista de diccionarios
    
    inventario=[]
    errores=0

    try:
        with open(ruta,"r",encoding="utf-8") as archivo:
            reader = csv.reader(archivo)

            encabezado = next(reader)
            if encabezado != ["nombre","precio","cantidad"]:
                print("encabezado invalido")
                return[]
            for fila in reader:
                try:
                    if len(fila)!=3:
                        raise ValueError
                    nombre = fila[0]
                    precio= float(fila[1])
                    cantidad=int(fila[2])

                    if precio< 0 or cantidad < 0:
                        raise ValueError
                    
                    inventario.append({"nombre":nombre,
                                       "precio":precio,
                                       "cantidad":cantidad})
                except:
                    errores+=1
        print(f"{errores} filas invalidas omitidas")
        return inventario
    except FileNotFoundError:
        print("archivo no encontrado")
        return[]
