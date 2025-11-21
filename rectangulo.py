from figura_geometrica import FiguraGeometrica


class Rectangulo(FiguraGeometrica):
    """
    Clase que representa un rectángulo.
    Hereda de FiguraGeometrica.
    """
    
    def __init__(self, ancho: float, alto: float):
        """
        Constructor del Rectángulo.
        
        Args:
            ancho: Ancho del rectángulo (debe ser mayor que 0)
            alto: Alto del rectángulo (debe ser mayor que 0)
        """
        super().__init__(ancho, alto)
    
    def area(self) -> float:
        """
        Calcula el área del rectángulo.
        
        Returns:
            float: Área del rectángulo (ancho * alto)
        """
        return self._ancho * self._alto
    
    def perimetro(self) -> float:
        """
        Calcula el perímetro del rectángulo.
        
        Returns:
            float: Perímetro del rectángulo (2 * ancho + 2 * alto)
        """
        return 2 * (self._ancho + self._alto)
    
    def __str__(self) -> str:
        """
        Representación en string del rectángulo.
        
        Returns:
            str: Información del rectángulo con sus dimensiones
        """
        return f"Rectángulo: ancho={self._ancho}, alto={self._alto}"