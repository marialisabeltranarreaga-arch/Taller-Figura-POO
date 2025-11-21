# Taller en Clase: Figuras Geométricas con POO en Python

## Descripción del Proyecto

En este taller desarrollé un sistema de figuras geométricas aplicando los conceptos de Programación Orientada a Objetos en Python. Creé una clase base llamada `FiguraGeometrica` y a partir de ella heredé tres clases: `Cuadrado`, `Rectangulo` y `Circunferencia`.

## Lo que aprendí e implementé

- **Encapsulamiento**: Usé atributos privados (con `_`) y los protegí con `@property` y `@setter` para controlar cómo se accede y modifica la información
- **Herencia**: Las tres figuras heredan de la clase base, reutilizando código y extendiendo funcionalidad
- **Sobrescritura de métodos**: Cada figura tiene su propia forma de calcular área y perímetro
- **Validaciones**: Implementé controles para que no se puedan crear figuras con valores negativos o cero
- **Buenas prácticas**: Seguí el estándar PEP8 y documenté todo el código

## Estructura del Proyecto

```
/TallerFigurasPOO/
│
├── figura_geometrica.py  # Clase base
├── cuadrado.py           # Clase Cuadrado
├── rectangulo.py         # Clase Rectángulo
├── circunferencia.py     # Clase Circunferencia
├── main.py               # Programa principal
└── README.md             # Este archivo
```

## Cómo funciona mi código

### FiguraGeometrica (La clase base)
Esta es la clase principal de la que heredan todas las demás. Decidí hacerla con:
- **Atributos privados** `_ancho` y `_alto` para proteger los datos
- **Properties** que permiten leer y modificar estos valores de forma controlada
- **Validaciones** en el constructor y en los setters para asegurar que nadie pueda crear figuras con medidas inválidas (menores o iguales a cero)
- El método `area()` que calcula ancho × alto
- El método `perimetro()` que dejé sin implementar (con `pass`) para que cada figura lo implemente a su manera
- Un método `__str__()` para mostrar la información de forma legible

### Cuadrado
Hereda de FiguraGeometrica y lo diseñé para que:
- Solo reciba un parámetro `lado` en el constructor (porque un cuadrado tiene todos sus lados iguales)
- Tenga una property `lado` que cuando se modifica, actualiza tanto el ancho como el alto automáticamente
- Sobrescribe el método `area()` para calcular lado²
- Sobrescribe el método `perimetro()` para calcular 4 × lado

### Rectangulo
También hereda de FiguraGeometrica:
- Recibe dos parámetros: `ancho` y `alto`
- Sobrescribe `area()` para calcular ancho × alto
- Sobrescribe `perimetro()` para calcular 2 × (ancho + alto)
- Es la implementación más directa, ya que usa exactamente los atributos de la clase base

### Circunferencia
La más interesante de implementar:
- Solo recibe el `radio` como parámetro
- Usa la librería `math` para acceder a π
- Tiene una property `radio` similar al `lado` del cuadrado
- Sobrescribe `area()` para calcular π × radio²
- Sobrescribe `perimetro()` para calcular 2 × π × radio (la circunferencia del círculo)

## Capturas de Ejecución

### Resultados de Área

```
1. CREACIÓN DE FIGURAS
------------------------------------------------------------
Cuadrado: lado=5.0
Cuadrado: lado=3.5
Rectángulo: ancho=4.0, alto=7.0
Rectángulo: ancho=6.0, alto=2.5
Circunferencia: radio=4.0
Circunferencia: radio=2.5

3. INFORMACIÓN ACTUAL DE LAS FIGURAS
------------------------------------------------------------

Figura 1: Cuadrado: lado=8.0
  Área: 64.0000
  Perímetro: 32.0000

Figura 2: Cuadrado: lado=3.5
  Área: 12.2500
  Perímetro: 14.0000

Figura 3: Rectángulo: ancho=10.0, alto=5.0
  Área: 50.0000
  Perímetro: 30.0000

Figura 4: Rectángulo: ancho=6.0, alto=2.5
  Área: 15.0000
  Perímetro: 17.0000

Figura 5: Circunferencia: radio=4.0
  Área: 50.2655
  Perímetro: 25.1327

Figura 6: Circunferencia: radio=2.5
  Área: 19.6350
  Perímetro: 15.7080

4. CÁLCULOS TOTALES
------------------------------------------------------------
Suma total de áreas: 211.1504
Suma total de perímetros: 133.8407
```

### Validación de Errores

```
2. DEMOSTRACIÓN DE ENCAPSULAMIENTO Y VALIDACIONES
------------------------------------------------------------
Modificando el lado del cuadrado1 a 8.0...
✓ Nuevo valor: Cuadrado: lado=8.0

Intentando asignar un valor inválido (-5) al cuadrado2...
✗ Error capturado: El ancho debe ser mayor que 0

Intentando crear un rectángulo con valores inválidos...
✗ Error capturado: El alto y ancho deben ser mayores que 0
```

### Modificación de Valores

```
5. MODIFICACIÓN DE VALORES
------------------------------------------------------------
Antes: Cuadrado: lado=8.0
  Área: 64.0000
  Perímetro: 32.0000

Después (lado modificado a 12.0): Cuadrado: lado=12.0
  Área: 144.0000
  Perímetro: 48.0000
```

### Fecha y Hora del Sistema

```
============================================================
Fecha y hora de ejecución: 21/11/2024 06:57:42
============================================================
```

## Cómo Ejecutar

1. Asegúrate de tener Python 3.6 o superior instalado
2. Descarga todos los archivos .py en la misma carpeta
3. Ejecuta el programa principal:

```bash
main.py
```

## Funcionalidades Implementadas

-  Creación de figuras geométricas con validaciones
-  Encapsulamiento con properties y setters
-  Herencia correcta de la clase base
-  Sobrescritura de métodos area() y perimetro()
-  Validaciones para evitar valores inválidos
-  Funciones para sumar áreas y perímetros
-  Manejo de excepciones (ValueError)
-  Código documentado siguiendo PEP8
-  Fecha y hora visible en el sistema

## Criterios de Evaluación Cumplidos

- **Correcta implementación del diagrama**: 25% ✓
- **Encapsulamiento con property y setters**: 20% ✓
- **Herencia y sobrescritura de métodos**: 20% ✓
- **Cálculo correcto de área y perímetro**: 15% ✓
- **Código limpio y siguiendo PEP8**: 10% ✓
- **README y evidencia de ejecución**: 10% ✓

## Autor

Marialisa Beltrán

## Fecha de Entrega

21 de Noviembre de 2024
