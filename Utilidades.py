from Manejo_archivo import *
def eliminar_item_por_nombre(nombre_item_a_eliminar: str) -> bool:
    """
    Busca un ítem por su nombre y lo elimina del archivo CSV correspondiente.
    """
    print(f"Iniciando búsqueda para eliminar '{nombre_item_a_eliminar}'...")
    
    lista_completa = crear_lista_desde_csv(RUTA_BASE_DATOS)
    if not lista_completa:
        print("La base de datos está vacía. No hay nada que eliminar.")
        return False

    item_a_eliminar = next((item for item in lista_completa if item.get('nombre', '').strip().lower() == nombre_item_a_eliminar.strip().lower()), None)
    
    if not item_a_eliminar:
        print(f"No se encontró ningún ítem con el nombre '{nombre_item_a_eliminar}'.")
        return False

    try:
        ruta_archivo_especifico = os.path.join(
            RUTA_BASE_DATOS,
            item_a_eliminar['categoria'],
            item_a_eliminar['tipo'],
            item_a_eliminar['procesamiento'],
            "items.csv"
        )
        print(f"Ítem encontrado en: {ruta_archivo_especifico}")
    except KeyError:
        print("ERROR: El ítem encontrado no tiene la información de ruta completa (categoría/tipo/procesamiento).")
        return False

    filas_a_mantener = []
    encabezados = []
    try:
        with open(ruta_archivo_especifico, 'r', encoding='utf-8', newline='') as f:
            lector = csv.DictReader(f)
            encabezados = lector.fieldnames
            for fila in lector:
                if fila.get('nombre', '').strip().lower() != nombre_item_a_eliminar.strip().lower():
                    filas_a_mantener.append(fila)
        
        if _sobrescribir_csv(ruta_archivo_especifico, encabezados, filas_a_mantener):
            print(f"¡Éxito! Ítem '{nombre_item_a_eliminar}' eliminado.")
            return True
        else:
            print(f"Fallo al sobrescribir el archivo para eliminar el ítem.")
            return False

    except (IOError, FileNotFoundError) as e:
        print(f"ERROR CRÍTICO al intentar leer el archivo para eliminar: {e}")
        return False