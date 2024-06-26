from os import system

# FUNCIÓN PARA EL MENÚ DE OPCIONES
def menu():
    
    print("******** Programa de descuento ********")
    print("Menú de Opciones:")
    print("1. Ingreso de articulos")
    print("2. Salir del programa")

# FUNCIÓN PARA CALCULAR DESCUENTO
def calcular_descuento(precio):
    
    if precio >= 200:
        return precio * 0.15
    
    elif 100 <= precio < 200:
        return precio * 0.12
    
    else:
        return precio * 0.10
    
# FUNCIÓN PARA INGRESAR PRODUCTOS
def articulos():

  system("cls")
  num_articulos = int(input("Ingrese el número de artículos: "))
  total = 0

  for i in range(num_articulos):

    precio = float(input(f"Ingrese el precio del artículo {i + 1}: "))
    descuento = calcular_descuento(precio)
    precio_final = precio - descuento
    total += precio_final
# IMPRIME LA INFORMACION
    system("cls")
    print("*************** Precio ***************")
    print(f"Artículo {i + 1}:")
    print(f"Precio original: ${precio: .2f}")
    print(f"Descuento: ${descuento: .2f}")
    print(f"Precio final: ${precio_final: .2f}")
# IMPRIME EL TOTAL 
  print(f"Total a pagar por todos los artículos: ${total: .2f}")

# FUNCIÓN MAIN 
def main():
  
    while True:
        menu()
        opcion = int(input("Seleccione una opción: "))
        if opcion == 1:
            articulos()
        elif opcion == 2:
            system("cls")
            print("******** Programa de descuento ********")
            print("Muchas gracias por utilizar nuestro sistema")
            break
        else:
            print("Opcion no valida")

# EJECUCIÓN DE FUNCIÓN MAIN
main()

