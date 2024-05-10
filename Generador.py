import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import random
import music21

# Diccionario de información sobre las escalas
info_escalas = {
    "mayor": {
        "nombre": "Escala Mayor",
        "info": "La escala mayor es una de las escalas más comunes en la música occidental. Está formada por una secuencia de tonos y semitonos que sigue el patrón: Tono-Tono-Semitono-Tono-Tono-Tono-Semitono.",
    },
    "menor": {
        "nombre": "Escala Menor",
        "info": "La escala menor es otra escala fundamental en la música occidental. Tiene un sonido más oscuro que la escala mayor y sigue el patrón: Tono-Semitono-Tono-Tono-Semitono-Tono-Tono.",
    },
    "armonica menor": {
        "nombre": "Escala Armónica Menor",
        "info": "La escala armónica menor es una variante de la escala menor que presenta un séptimo grado elevado, proporcionando un sonido más exótico. Su patrón es: Tono-Semitono-Tono-Tono-Semitono-Tono y medio-Semitono.",
    }
}

# Función para generar melodías según la escala seleccionada
def generar_melodia(escala):
    if escala == "mayor":
        scale = music21.scale.MajorScale('C')
    elif escala == "menor":
        scale = music21.scale.MinorScale('C')
    elif escala == "armonica menor":
        scale = music21.scale.HarmonicMinorScale('C')
    else:
        raise ValueError("Escala no válida")

    # Escoge una nota central aleatoria de la escala
    nota_central = random.choice(scale.pitches)
    
    # Genera una secuencia de notas aleatorias dentro de la escala musical
    num_notas = random.randint(12, 20)
    
    # Asegura que la nota central esté en la melodía al menos una vez
    melody = [nota_central]
    for _ in range(num_notas - 1):
        melody.append(random.choice(scale.pitches))

    # Mezcla las notas para que la nota central no siempre sea la primera
    random.shuffle(melody)

    # Dividir la melodía en tres partes iguales
    num_segmentos = 3
    segment_length = len(melody) // num_segmentos
    segmentos = [melody[i:i + segment_length] for i in range(0, len(melody), segment_length)]
    
    # Concatenar los dos últimos segmentos después del primero
    melody_final = segmentos[0] + segmentos[1] * (num_segmentos - 1)

    # Crea un objeto Stream de Music21 para la melodía
    melody_stream = music21.stream.Stream()
    for pitch in melody_final:
        note = music21.note.Note(pitch)
        melody_stream.append(note)
    
    return melody_stream

# Función para mostrar las notas de la melodía en una ventana emergente
def mostrar_notas(melodia_stream):
    ventana = tk.Toplevel(root)
    ventana.title("Notas de la Melodía")
    ventana.geometry("200x450")  # Mantener la geometría original

    # Crear un marco para las notas
    frame_notas = tk.Frame(ventana, bg="#F0F0F0")
    frame_notas.pack(expand=True, fill="both")

    # Etiqueta de título
    label_titulo = tk.Label(frame_notas, text="Notas de la Melodía", font=("Helvetica", 12, "bold"), bg="#F0F0F0")
    label_titulo.pack(pady=(10, 5))

    # Mostrar las notas de la melodía
    for nota in melodia_stream:
        label_nota = tk.Label(frame_notas, text=str(nota).replace("music21.note.Note ", ""), font=('Helvetica', 10), bg="#F0F0F0")
        label_nota.pack()

# Función para mostrar información sobre las escalas en una ventana emergente
def mostrar_info_escalas():
    ventana_info = tk.Toplevel(root)
    ventana_info.title("Información de Escalas")
    ventana_info.geometry("1920x1080")
    
    # Establecer posición relativa a la ventana principal
    x = root.winfo_x()
    y = root.winfo_y()
    ventana_info.geometry("1680x920")
    
    # Crear un marco para la información
    frame_info = tk.Frame(ventana_info, bg="#E6E6FA")  # Cambiar color de fondo
    frame_info.pack(expand=True, fill="both")
    
    # Etiqueta de título
    label_titulo = tk.Label(frame_info, text="Información de Escalas", font=("Helvetica", 20, "bold"), bg="#E6E6FA")  # Cambiar color de fondo
    label_titulo.pack(pady=(10, 5))
    
    # Mostrar información sobre cada escala
    for escala, info in info_escalas.items():
        label_escala = tk.Label(frame_info, text=info["nombre"], font=("Helvetica", 14, "bold"), bg="#E6E6FA")  # Cambiar color de fondo
        label_escala.pack(pady=(5, 2))
        label_info = tk.Label(frame_info, text=info["info"], font=("Helvetica", 12), bg="#E6E6FA")  # Cambiar color de fondo
        label_info.pack(pady=(2, 10))

# Función para mostrar la melodía en una ventana emergente y reproducirla
def mostrar_melodia(escala):
    melodia_stream = generar_melodia(escala)
    mostrar_notas(melodia_stream)  # Mostrar notas en una ventana emergente
    melodia_stream.show('midi')  # Reproducir la melodía

# Función para manejar el clic en los botones de la interfaz
def manejar_clic(escala):
    mostrar_melodia(escala)

# Creación de la ventana principal
root = tk.Tk()
root.title("Generador de melodías con IA")

# Colores
fondo = '#D2E7FA'  # Azul claro
color_botones = '#FFD966'  # Amarillo suave
color_titulo = '#003366'  # Azul oscuro

# Marco principal
main_frame = ttk.Frame(root, padding=20)
main_frame.grid(row=0, column=0, sticky="nsew")

# Cargar imagen
imagen = Image.open("sol.gif")
imagen = imagen.resize((400, 200), Image.BICUBIC)
imagen = ImageTk.PhotoImage(imagen)
imagen_label = ttk.Label(main_frame, image=imagen)
imagen_label.grid(row=0, column=0, columnspan=3, pady=20)

# Etiqueta de título
title_label = ttk.Label(main_frame, text="Generador de melodías con IA", font=('Helvetica', 24, 'bold'))
title_label.grid(row=1, column=0, columnspan=3, pady=20)

# Botones de escalas
mayor_button = ttk.Button(main_frame, text="Escala mayor", command=lambda: manejar_clic("mayor"), style='my.TButton')
mayor_button.grid(row=2, column=0, padx=10, pady=10)

menor_button = ttk.Button(main_frame, text="Escala menor", command=lambda: manejar_clic("menor"), style='my.TButton')
menor_button.grid(row=2, column=1, padx=10, pady=10)

armonica_menor_button = ttk.Button(main_frame, text="Escala armónica menor", command=lambda: manejar_clic("armonica menor"), style='my.TButton')
armonica_menor_button.grid(row=2, column=2, padx=10, pady=10)

# Botón de información de escalas
info_button = ttk.Button(main_frame, text="Información de escalas", command=mostrar_info_escalas, style='my.TButton')
info_button.grid(row=3, column=0, columnspan=3, pady=10)

# Estilo para los botones
style = ttk.Style()
style.configure('my.TButton', font=('Helvetica', 14), padding=10, background=color_botones)

# Ajustar la geometría de la ventana
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

root.mainloop()
