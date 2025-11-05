from Manejo_archivo import *
from Sub_Menus import *
from Utilidades import *

def main():
    salir = False
    while not salir:
        opciones_principales = [
            "Alta de Nuevo Ítem",
            "Mostrar y Filtrar Alimentos",
            "Modificación de un Ítem",
            "Eliminación de un Ítem",
            "Estadísticas y Ordenamiento"
        ]
        print("\n=========================================")
        imprimir_menu("GESTOR DE BASE DE DATOS DE ALIMENTOS", opciones_principales, "Salir")
        opc = input("Elija una opción: ").strip()
        match opc:
            case "1":
                #1) Alta de nuevo item
                opcion_1_alta()
            case "2":
                #2) Mostrar lista global y filtrado
                opcion_2_mostrar_y_filtrar()
            case "3":
                #3) Modificacion de un item
                nombre = input("Ingrese el nombre exacto del ítem que desea modificar: ")
                if nombre:
                    modificar_item_por_nombre(nombre) # Llamada a la nueva función
                else:
                    print("No ingresó un nombre. Volviendo al menú.")
            case "4":
                #4) Eliminacion de un item/Busqueda multiples coincidencias
                nombre = input("Ingrese el nombre exacto del ítem que desea eliminar: ")
                if nombre:
                    eliminar_item_por_nombre(nombre) # Llamada a la nueva función
                else:
                    print("No ingresó un nombre. Volviendo al menú.")
            case "5":
                #5) Estadisticas y ordenamiento
                opcion_5_estadisticas()
            case "0":
                print("¡Gracias, vuelva pronto!")
                salir = True
            case _:
                print("Opción no válida. Por favor, intente de nuevo.")

if __name__ == "__main__":
    main()
