![image](https://github.com/DrPepperFan/GeneradorIAmusic21/assets/158233792/706604fd-d405-4d59-96ee-52b081bb69d1)

# Generador de Melodías con IA

## Descripción

El Generador de Melodías con IA es un proyecto de software desarrollado en Python que utiliza principios de programación musical y de interfaz gráfica de usuario (GUI) para crear y reproducir melodías musicales en diferentes escalas. Aunque el término "Inteligencia Artificial" puede no aplicarse directamente a este proyecto, podemos considerar que la aplicación involucra elementos de inteligencia computacional en la generación y manipulación de secuencias musicales.

![image](https://github.com/DrPepperFan/GeneradorIAmusic21/assets/158233792/279e9d7d-0523-4215-bd42-7a767f0237a5)


## Características Principales

- **Generación Aleatoria de Melodías**: La aplicación utiliza algoritmos de generación de melodías basados en escalas musicales predefinidas para crear secuencias musicales aleatorias. Estos algoritmos pueden considerarse como un enfoque computacional para la composición musical, donde la aplicación utiliza reglas y patrones predefinidos para generar nuevas melodías de manera autónoma, lo que refleja un aspecto de "inteligencia" en la toma de decisiones musicales.
  
- **Interfaz Gráfica de Usuario Intuitiva**: La aplicación cuenta con una interfaz gráfica de usuario diseñada con Tkinter, lo que facilita la interacción del usuario con el programa. Aunque la interfaz en sí misma no implica directamente inteligencia artificial, la forma en que el programa maneja y procesa los datos de entrada del usuario puede considerarse como un aspecto de la inteligencia computacional.

- **Visualización de Notas en Ventana Emergente**: Después de generar una melodía, el usuario puede ver las notas musicales correspondientes en una ventana emergente, lo que permite una experiencia más inmersiva. Esta capacidad de visualización en tiempo real de las notas generadas puede considerarse como una aplicación de técnicas de inteligencia computacional para presentar información musical de manera comprensible y atractiva para el usuario.

- **Información Detallada sobre Escalas Musicales**: La aplicación proporciona información detallada sobre cada escala musical disponible, lo que permite al usuario comprender mejor las características y diferencias entre las escalas. Si bien la presentación de esta información no implica directamente inteligencia artificial, el proceso de recopilación y organización de datos puede beneficiarse de técnicas de procesamiento de datos inteligentes para ofrecer una experiencia de usuario más informativa y personalizada.

![image](https://github.com/DrPepperFan/GeneradorIAmusic21/assets/158233792/a8606a07-c9be-4bf9-8cdb-a35330a110f6)


## Instalación

Para instalar y ejecutar el Generador de Melodías con IA, sigue estos pasos:

1. **Clona el Repositorio**: Utiliza el siguiente comando para clonar el repositorio en tu máquina local:

   ```bash
   git clone https://github.com/tu_usuario/generador-melodias-ia.git
   ```

2. **Instala las Dependencias**: Asegúrate de tener Python 3.x instalado en tu sistema. Luego, instala las bibliotecas necesarias ejecutando el siguiente comando:

   ```bash
   pip install music21 pillow
   ```

## Uso

1. **Ejecución del Programa**: Navega hasta el directorio donde clonaste el repositorio y ejecuta el archivo `generador_melodias.py` utilizando Python:

   ```bash
   python generador_melodias.py
   ```

2. **Interfaz Gráfica de Usuario**: Una vez que el programa esté en funcionamiento, verás una interfaz gráfica con botones para seleccionar las escalas musicales y otras opciones.

3. **Generación de Melodías**: Haz clic en uno de los botones de escala musical para generar una melodía aleatoria en esa escala.

4. **Visualización de Notas**: Después de generar una melodía, haz clic en el botón "Notas de la Melodía" para ver las notas musicales correspondientes en una ventana emergente.

5. **Información de Escalas**: Para obtener información detallada sobre las escalas musicales disponibles, haz clic en el botón "Información de Escalas".

## Patrones de Diseño

### 1. Modelo-Vista-Controlador (MVC)

El Generador de Melodías con IA sigue el patrón Modelo-Vista-Controlador (MVC), donde:
- **Modelo**: Las funciones de generación de melodías y la estructura de datos de información de escalas actúan como el modelo del programa.
- **Vista**: La interfaz gráfica de usuario proporciona una vista interactiva para el usuario.
- **Controlador**: Las funciones controladoras manejan los eventos del usuario y coordinan las operaciones entre el modelo y la vista.

### 2. Patrón Singleton
El patrón Singleton se utiliza en la creación de ventanas emergentes para mostrar las notas de la melodía. Dado que solo se necesita una instancia de la ventana emergente en toda la aplicación para mostrar las notas, el patrón Singleton garantiza que solo se cree una instancia de la clase de ventana emergente y se reutilice cada vez que sea necesario. Esto mejora la eficiencia y evita la creación innecesaria de múltiples ventanas emergentes.

# Conclusión
El Generador de Melodías con IA representa un proyecto de software versátil y educativo que combina principios de programación musical, interfaces gráficas de usuario y aspectos de inteligencia computacional para ofrecer una experiencia interactiva y enriquecedora para los usuarios interesados en la creación y exploración de melodías musicales.

A lo largo de este proyecto, hemos explorado diferentes facetas de la programación en Python, desde el uso de bibliotecas especializadas como music21 para manipular y generar secuencias musicales, hasta la creación de interfaces de usuario intuitivas utilizando Tkinter. Además, hemos aplicado conceptos de diseño de software como el patrón Modelo-Vista-Controlador (MVC) para estructurar nuestro código de manera organizada y mantenible.

Una de las características destacadas de este programa es su capacidad para generar melodías de manera aleatoria en diferentes escalas musicales, lo que brinda a los usuarios la oportunidad de experimentar con diferentes patrones y estilos musicales de forma interactiva. La inclusión de información detallada sobre las escalas musicales disponibles también enriquece la experiencia del usuario al proporcionar un contexto educativo sobre las características y diferencias entre cada escala.

Si bien el término "Inteligencia Artificial" puede no aplicarse directamente a este proyecto en el sentido tradicional, podemos considerar que la aplicación involucra elementos de inteligencia computacional en la generación y manipulación de secuencias musicales. La capacidad del programa para generar melodías de forma autónoma, basándose en reglas y patrones predefinidos, refleja un aspecto de "inteligencia" en la toma de decisiones musicales.


