import tkinter as tk  # Importa tkinter para construir interfaces gráficas
from tkinter import messagebox  # Importa módulo para mostrar cuadros de mensaje

# Clase que representa a un usuario del sistema.
class Usuario:
    # Diccionario con usuarios válidos usuario: contraseña
    usuarios = {
        "boni": "abcd",
        "ricky": "1234"
    }

    # El metodo constructor que guarda los datos del usuario
    def __init__(self, nombre_usuario, contraseña):
        self.__nombre_usuario = nombre_usuario  # Atributo privado para el nombre
        self.__contraseña = contraseña  # Atributo privado para la contraseña

    # El metodo que valida si el usuario existe con la contraseña correcta
    def validar_acceso(self):
        return Usuario.usuarios.get(self.__nombre_usuario) == self.__contraseña

# Función que se ejecuta al presionar el botón "Ingresar"
def iniciar_sesion():
    nombre = entry_usuario.get()  # Obtiene el nombre del campo de entrada
    clave = entry_contraseña.get()  # Obtiene la contraseña del campo de entrada
    usuario = Usuario(nombre, clave)  # Crea un objeto Usuario con los datos

    # Verifica si el usuario es válido y muestra el mensaje correspondiente
    if usuario.validar_acceso():
        messagebox.showinfo("Acceso", "Acceso exitoso.")  # Mensaje de éxito
        ventana.destroy()  # Cierra la ventana principal
    else:
        messagebox.showerror("Acceso denegado", "Usuario o contraseña incorrectos.")  # Mensaje de error

# Creación de la ventana principal
ventana = tk.Tk()
ventana.title("Inicio de Sesión - POO")  # Título de la ventana
ventana.geometry("640x480")  # Dimensiones de la ventana

# Etiqueta y campo de entrada para el usuario
tk.Label(ventana, text="Usuario:", font=("Arial", 16)).place(x=140, y=150)
entry_usuario = tk.Entry(ventana, font=("Arial", 16), width=20)
entry_usuario.place(x=270, y=150)

# Etiqueta y campo de entrada para la contraseña
tk.Label(ventana, text="Contraseña:", font=("Arial", 16)).place(x=140, y=210)
entry_contraseña = tk.Entry(ventana, show="*", font=("Arial", 16), width=20)
entry_contraseña.place(x=270, y=210)

# Botón para iniciar sesión, asociado a la función iniciar_sesion
btn_ingresar = tk.Button(ventana, text="Ingresar", font=("Arial", 16), command=iniciar_sesion, width=12)
btn_ingresar.place(x=260, y=280)

# Inicia el ciclo principal de ejecución de la ventana
ventana.mainloop()
