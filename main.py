from funciones import agregar_tarea, eliminar_tarea, mostrar_tareas, salir

tareas = [
    ("Estudiar para el examen", "Revisar capítulos 1 a 5", "en progreso"),
    ("Hacer ejercicio", "Ir al gimnasio por 1 hora", "completada"),
    ("Llamar al médico", "Solicitar una cita para chequeo", "pendiente"),
    ("Enviar el informe", "Enviar el informe a mi jefe por correo", "en progreso")
]

def mostrar_menu():
    print("Menú de tareas:")
    print("1. Agregar tarea")
    print("2. Eliminar tarea")
    print("3. Mostrar tareas")
    print("4. Salir")

while True:
    mostrar_menu()
    opcion = input("Ingrese el número de la función a ejecutar: ")

    if opcion == '1':
        agregar_tarea(tareas)
    elif opcion == '2':
        eliminar_tarea(tareas)
    elif opcion == '3':
        mostrar_tareas(tareas)
    elif opcion == '4':
        salir()
        break
    else:
        print("Opción no válida. Intente de nuevo.")

def agregar_tarea(tareas):
      print("Estamos programando...")

def eliminar_tarea(tareas):
    print("Estamos programando...")

def mostrar_tareas(tareas):
    print("Estamos programando...")

def salir():
    print("Saliendo del programa...")

        