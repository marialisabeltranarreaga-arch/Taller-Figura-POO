from figura_geometrica import FiguraGeometrica
from cuadrado import Cuadrado
from rectangulo import Rectangulo
from circunferencia import Circunferencia
from datetime import datetime


def sumar_areas(figuras: list) -> float:
    """
    Suma las áreas de todas las figuras en la lista.
    
    Args:
        figuras: Lista de objetos que heredan de FiguraGeometrica
    
    Returns:
        float: Suma total de las áreas
    """
    total = 0
    for figura in figuras:
        total += figura.area()
    return total


def sumar_perimetros(figuras: list) -> float:
    """
    Suma los perímetros de todas las figuras en la lista.
    
    Args:
        figuras: Lista de objetos que heredan de FiguraGeometrica
    
    Returns:
        float: Suma total de los perímetros
    """
    total = 0
    for figura in figuras:
        total += figura.perimetro()
    return total


def main():
    """
    Programa principal que demuestra el uso de las clases.
    Crea figuras, demuestra encapsulamiento y calcula áreas y perímetros.
    """
    print("=" * 60)
    print("TALLER EN CLASE: FIGURAS GEOMÉTRICAS CON POO EN PYTHON")
    print("=" * 60)
    print()
    
    # 1. Crear dos cuadrados y dos rectángulos
    print("1. CREACIÓN DE FIGURAS")
    print("-" * 60)
    
    cuadrado1 = Cuadrado(5.0)
    cuadrado2 = Cuadrado(3.5)
    rectangulo1 = Rectangulo(4.0, 7.0)
    rectangulo2 = Rectangulo(6.0, 2.5)
    circunferencia1 = Circunferencia(4.0)
    circunferencia2 = Circunferencia(2.5)
    
    print(f"✓ {cuadrado1}")
    print(f"✓ {cuadrado2}")
    print(f"✓ {rectangulo1}")
    print(f"✓ {rectangulo2}")
    print(f"✓ {circunferencia1}")
    print(f"✓ {circunferencia2}")
    print()
    
    # 2. Asignar valores válidos e inválidos (demostrar encapsulamiento)
    print("2. DEMOSTRACIÓN DE ENCAPSULAMIENTO Y VALIDACIONES")
    print("-" * 60)
    
    print("Modificando el lado del cuadrado1 a 8.0...")
    cuadrado1.lado = 8.0
    print(f"✓ Nuevo valor: {cuadrado1}")
    print()
    
    print("Intentando asignar un valor inválido (-5) al cuadrado2...")
    try:
        cuadrado2.lado = -5
    except ValueError as e:
        print(f"✗ Error capturado: {e}")
    print()
    
    print("Modificando dimensiones del rectangulo1...")
    rectangulo1.ancho = 10.0
    rectangulo1.alto = 5.0
    print(f"✓ Nuevo valor: {rectangulo1}")
    print()
    
    print("Intentando crear un rectángulo con valores inválidos...")
    try:
        rectangulo_invalido = Rectangulo(-2, 5)
    except ValueError as e:
        print(f"✗ Error capturado: {e}")
    print()
    
    # 3. Mostrar información de las figuras
    print("3. INFORMACIÓN ACTUAL DE LAS FIGURAS")
    print("-" * 60)
    
    figuras = [cuadrado1, cuadrado2, rectangulo1, rectangulo2, 
               circunferencia1, circunferencia2]
    
    for i, figura in enumerate(figuras, 1):
        print(f"\nFigura {i}: {figura}")
        print(f"  • Área: {figura.area():.4f}")
        print(f"  • Perímetro: {figura.perimetro():.4f}")
    
    print()
    print("=" * 60)
    
    # 4. Calcular sumas totales
    print("\n4. CÁLCULOS TOTALES")
    print("-" * 60)
    
    area_total = sumar_areas(figuras)
    perimetro_total = sumar_perimetros(figuras)
    
    print(f"Suma total de áreas: {area_total:.4f}")
    print(f"Suma total de perímetros: {perimetro_total:.4f}")
    print()
    
    # 5. Modificación de valores
    print("5. MODIFICACIÓN DE VALORES")
    print("-" * 60)
    
    print(f"Antes: {cuadrado1}")
    print(f"  Área: {cuadrado1.area():.4f}")
    print(f"  Perímetro: {cuadrado1.perimetro():.4f}")
    print()
    
    cuadrado1.lado = 12.0
    
    print(f"Después (lado modificado a 12.0): {cuadrado1}")
    print(f"  Área: {cuadrado1.area():.4f}")
    print(f"  Perímetro: {cuadrado1.perimetro():.4f}")
    print()
    
    # 6. Mostrar fecha y hora del sistema
    print("=" * 60)
    fecha_hora = datetime.now()
    print(f"Fecha y hora de ejecución: {fecha_hora.strftime('%d/%m/%Y %H:%M:%S')}")
    print("=" * 60)


if __name__ == "__main__":
    main()
