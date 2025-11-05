# =========== Proyecto Manejo de Archivo y Recursividad =========== #

# ---Gestor de Base de Datos de Alimentos--- #
Este proyecto es una aplicación de consola desarrollada en Python para administrar una base de datos de alimentos. Su principal característica es el uso de una estructura de directorios (categoria/tipo/procesamiento) como sistema de base de datos, lo que permite una organización jerárquica y flexible de la información.

El programa es robusto y generalizado: se adapta dinámicamente a nuevas categorías, tipos o archivos de datos que se añadan a la estructura de carpetas, sin necesidad de modificar el código fuente.


# ---Funcionalidades Clave--- #
El programa ofrece un menú interactivo con las siguientes opciones:

Alta de Nuevo Ítem:

Permite registrar un nuevo alimento guiando al usuario para ingresar su jerarquía (categoría, tipo, procesamiento), nombre y calorías.
Normaliza automáticamente los nombres de la jerarquía para crear rutas de carpetas válidas (ej: "Cítricos" se convierte en "citricos").
Crea la estructura de directorios y el archivo items.csv si no existen.
Mostrar y Filtrar Alimentos:

Mostrar Todo: Presenta una tabla con todos los alimentos de la base de datos.
Filtrado Jerárquico: Permite navegar por la base de datos de forma intuitiva, eligiendo primero una categoría y luego un tipo, ambos menús generados dinámicamente.
Filtrado por Calorías: Muestra alimentos que se encuentren dentro de un rango de calorías (mínimo y máximo) especificado por el usuario.
Top por Calorías: Permite ver los "N" alimentos más calóricos de toda la base de datos.
Modificación de un Ítem:

Busca un alimento por su nombre.
Si existen múltiples coincidencias (ítems con el mismo nombre en diferentes categorías), presenta un menú interactivo para que el usuario elija cuál modificar.
Permite actualizar el nombre y/o las calorías del ítem seleccionado.
Eliminación de un Ítem:

Busca un alimento por su nombre para eliminarlo.
Maneja de forma segura las coincidencias múltiples, pidiendo al usuario que especifique el ítem a borrar.
Pide confirmación antes de realizar la eliminación definitiva.
Estadísticas y Ordenamiento:

Ofrece un submenú con análisis detallados de los datos:
Resumen General: Cantidad total de alimentos, promedio de calorías global, y los ítems con más y menos calorías.
Cantidad por Categoría: Un recuento de cuántos alimentos hay en cada categoría principal.
Análisis por Categoría: Estadísticas detalladas (promedio, máx, mín) para una categoría específica elegida por el usuario.
Ranking de Calorías: Ordena las categorías de la más a la menos calórica en promedio.
Top 3 por Categoría: Muestra los 3 alimentos más y menos calóricos para una categoría seleccionada.


# ---Estructura del Proyecto--- #
El código está organizado en módulos para una mejor legibilidad y mantenimiento:

Integrador_recursividad.py: El punto de entrada principal. Contiene el bucle del menú principal que gestiona la navegación del usuario.
Sub_Menus.py: Contiene la lógica detallada para cada una de las opciones del menú principal (alta, filtrado, estadísticas, etc.).
Manejo_archivo.py: Encapsula toda la interacción con el sistema de archivos. Es responsable de leer y escribir los archivos .csv, así como de crear y recorrer la estructura de directorios.
Utilidades.py: Proporciona funciones de ayuda complejas y reutilizables, como la búsqueda y selección de ítems para modificar/eliminar y la visualización de datos en tablas.
Estructura de la Base de Datos
La base de datos reside en una carpeta principal (por defecto database). Dentro de ella, cada alimento se organiza según su jerarquía:

plaintext
database/
└── categoria/
    └── tipo/
        └── procesamiento/
            └── items.csv
Ejemplo:

plaintext
database/
└── carnes/
    └── vacuna/
        └── parrilla/
            └── items.csv

# ---Instrucciones de Uso--- #
Requisitos
Python 3.10 o superior (para el uso de match-case).
Ejecución
Asegúrate de que todos los archivos .py estén en el mismo directorio.

Abre una terminal en ese directorio.

Ejecuta el programa con el siguiente comando:

bash
python Integrador_recursividad.py
El programa mostrará el menú principal. Ingresa el número de la opción que desees y presiona Enter para continuar.

