# -*- coding: utf-8 -*-
"""Copia de PC_1_Quimica_UNMSM.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/16ejpUJ8wff6GRmV6qD7WyW3MVDhZbVuz

$$\Large \textit{UNMSM | Química}$$
$$\large \textbf{PC Nº1 | Materia y clasificación}$$

_Profesor: Jesus Alvarado Huayhuaz_

Todas las indicaciones para la presentación de la práctica son explicadas en clase y brindadas en el material de enunciado de preguntas en formato PDF.

## Pregunta 1: Sobre el ABC de python (4 puntos)

Durante la semana de revisión del material "ABC de python", reflexiona sobre qué conceptos aprendiste con claridad y cuáles consideras los más desafiantes. A continuación resuelve los siguiente ejercicios, puedes ayudarte del material en http://bit.ly/3YKICSZ.
"""

import sys
print("Versión de Python:", sys.version)

# Crear una matriz de 3x3
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Inicializar la suma de la traza
suma_traza = 0

# Calcular la suma de la traza
for i in range(len(matriz)):
    suma_traza += matriz[i][i]

# Imprimir la matriz
print("Matriz:")
for fila in matriz:
    print(fila)

# Imprimir la suma de la traza
print("Suma de la traza:", suma_traza)

# Definir las masas atómicas
masa_atomica_C = 12.01  # masa atómica del Carbono en uma
masa_atomica_H = 1.01   # masa atómica del Hidrógeno en uma
masa_atomica_O = 16.00   # masa atómica del Oxígeno en uma

# Calcular la masa molecular del etanol (C2H5OH)
masa_molecular_etanol = (2 * masa_atomica_C) + (6 * masa_atomica_H) + (1 * masa_atomica_O)

# Imprimir la masa molecular del etanol
print("Masa Molecular del Etanol (C2H5OH):", masa_molecular_etanol, "uma")

# Crear una lista de metales y sus temperaturas de fusión en grados Celsius
metales = {
    "Aluminio": 660.32,
    "Cobre": 1084.62,
    "Hierro": 1538.0,
    "Plata": 961.78,
    "Zinc": 419.53
}

# Inicializar una lista para las temperaturas en Kelvin
temperaturas_kelvin = []

# Convertir las temperaturas de Celsius a Kelvin y almacenarlas en la lista
for metal, temperatura_celsius in metales.items():
    temperatura_kelvin = temperatura_celsius + 273.15
    temperaturas_kelvin.append((metal, temperatura_kelvin))

# Imprimir las temperaturas en Kelvin
for metal, temperatura_kelvin in temperaturas_kelvin:
    print(f"{metal}: {temperatura_kelvin} K")

"""## Pregunta 2: Operaciones (4 puntos)

Escribe un programa que lea repetidamente elementos químicos en español hasta que el usuario introduzca “fin”. Una vez se haya introducido “fin”, muestra por pantalla (o sea imprime) el total de elementos ingresados. Si el usuario introduce cualquier otra cosa que no sea un elemento químico, detecta su fallo usando try y except, muestra un mensaje de error y pasa al siguiente elemento.
"""

# Diccionario de elementos químicos en español
elementos_quimicos = {
    "hidrogeno": 1,
    "helio": 2,
    "litio": 3,
    # Agrega más elementos aquí
}

# Inicializamos el contador
total_elementos = 0

while True:
    entrada = input("Introduce un elemento químico en español (o 'fin' para terminar): ").lower()

    if entrada == "fin":
        break

    try:
        numero_atomico = elementos_quimicos[entrada]
        total_elementos += 1
        print(f"Elemento {entrada} encontrado. Número atómico: {numero_atomico}")
    except KeyError:
        print(f"'{entrada}' no es un elemento químico válido.")

print(f"Total de elementos ingresados: {total_elementos}")

"""# Pregunta 3: Conservación de la masa (4 puntos)

### Código necesario para generar la imagen
"""

!pip install faerun-notebook==0.1.5b0

import ipywidgets as widgets
from faerun_notebook import SmilesDrawer
from google.colab import output
output.enable_custom_widget_manager()

"""### Reacción química

Demuestra cómo se cumple la conservación de la masa en la siguiente reacción química. Sugerencia: hacer un balance estequiométrico y luego emplear la masa molecular de reactivos y productos.
"""

SmilesDrawer(value=[("Rxn", "C(C1C(C(C(C(O1)O)O)O)O)O.O=O>>C(=O)=O.O")], theme='dark', background="#1e1e1e", options={'scale': 1.25})

# Definir las masas molares de los reactivos y productos (en g/mol)
masa_molar_glucosa = 180.18
masa_molar_O2 = 32.00
masa_molar_CO2 = 44.01
masa_molar_H2O = 18.02

# Definir las cantidades estequiométricas de reactivos (en moles)
moles_glucosa = 1.0
moles_O2 = 6.0

# Calcular las masas de los reactivos (en gramos)
masa_glucosa = moles_glucosa * masa_molar_glucosa
masa_O2 = moles_O2 * masa_molar_O2

# Calcular las masas de los productos (en gramos) utilizando las relaciones estequiométricas
moles_CO2 = moles_glucosa
moles_H2O = moles_glucosa
masa_CO2 = moles_CO2 * masa_molar_CO2
masa_H2O = moles_H2O * masa_molar_H2O

# Verificar la conservación de la masa
masa_total_reactivos = masa_glucosa + masa_O2
masa_total_productos = masa_CO2 + masa_H2O

# Imprimir resultados
print("Masa total de reactivos:", masa_total_reactivos, "gramos")
print("Masa total de productos:", masa_total_productos, "gramos")

if abs(masa_total_reactivos - masa_total_productos) < 1e-6:
    print("La conservación de la masa se cumple en esta reacción.")
else:
    print("La conservación de la masa no se cumple en esta reacción.")

"""## Pregunta 4: Notación científica (4 puntos)

Imprime las siguientes operaciones según la notación científica:

(1) $1.321 \times 10^{-4} + 8.5 \times 10^{-2}$

(2) $1.71 \times 10^{3} - 2.01 \times 10^{2}\$

(3) $(7.4 \times 10^5)(7.2 \times 10^4)$

(4) $(7.4 \times 10^5)/(7.2 \times 10^4)$
"""

# Definir las cantidades en notación científica
numero1 = 1.321e-4
numero2 = 8.5e-2
numero3 = 7.4e5
numero4 = 7.2e4

# Realizar las operaciones
resultado1 = numero1 + numero2
resultado2 = numero3 - numero4
resultado3 = numero3 * numero4
resultado4 = numero3 / numero4

# Imprimir los resultados en notación científica
print("(1) Resultado:", format(resultado1, ".2e"))
print("(2) Resultado:", format(resultado2, ".2e"))
print("(3) Resultado:", format(resultado3, ".2e"))
print("(4) Resultado:", format(resultado4, ".2e"))

"""## Pregunta 5: Método científico (4 puntos)

Artículo: https://bit.ly/3surZ1W
Leer el siguiente artículo y explica cómo es aplicado el método científico. Emplea como máximo 300 palabras.

Observación: La investigación comienza con la observación de un fenómeno o un problema. Los científicos observan cuidadosamente para identificar patrones o comportamientos inusuales.

Pregunta: Basándose en la observación, se formula una pregunta específica que se desea responder. Esta pregunta debe ser clara y precisa.

Hipótesis: Se propone una hipótesis como una posible respuesta a la pregunta formulada. La hipótesis es una suposición basada en el conocimiento previo y debe ser comprobable mediante experimentos o investigación adicional.

Experimentación: Se diseñan experimentos o se recopila información de manera controlada y sistemática para probar la hipótesis. Los datos se registran con precisión.

Análisis de datos: Se analizan los datos recopilados para identificar patrones, relaciones y conclusiones. Los resultados se comparan con la hipótesis.

Conclusiones: Basándose en el análisis de datos, se llega a una conclusión sobre si la hipótesis es compatible con los resultados o si necesita ser ajustada o rechazada.

Comunicación: Los resultados y conclusiones se comunican a la comunidad científica y al público en general a través de publicaciones científicas, conferencias u otros medios. La revisión por pares es común en este proceso.

Repetición: Otros científicos repiten el experimento y analizan los resultados para validar las conclusiones. Si se confirma, el conocimiento se convierte en parte del cuerpo de la ciencia.

El método científico es un proceso cíclico y autoajustable. Si las conclusiones no son consistentes con la evidencia, se ajustan las hipótesis y se realizan más investigaciones. Este proceso riguroso es fundamental para el avance del conocimiento y la comprensión de nuestro mundo.
"""