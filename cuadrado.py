from figura_geometrica import FiguraGeometrica


class Cuadrado(FiguraGeometrica):
    """
    Clase que representa un cuadrado.
    Hereda de FiguraGeometrica.
    El cuadrado tiene ambos lados iguales.
    """
    
    def __init__(self, lado: float):
        """
        Constructor del Cuadrado.
        Recibe solo un valor (lado) y lo asigna tanto a ancho como alto.
        
        Args:
            lado: Longitud del lado del cuadrado (debe ser mayor que 0)
        """
        super().__init__(lado, lado)
    
    @property
    def lado(self) -> float:
        """Getter para el lado del cuadrado."""
        return self._ancho
    
    @lado.setter
    def lado(self, valor: float):
        """
        Setter para el lado del cuadrado.
        Actualiza tanto ancho como alto para mantener la forma cuadrada.
        
        Args:
            valor: Nuevo valor del lado
        """
        self.ancho = valor
        self.alto = valor
    
    def area(self) -> float:
        """
        Calcula el área del cuadrado.
        
        Returns:
            float: Área del cuadrado (lado²)
        """
        return self._ancho ** 2
    
    def perimetro(self) -> float:
        """
        Calcula el perímetro del cuadrado.
        
        Returns:
            float: Perímetro del cuadrado (4 * lado)
        """
        return 4 * self._ancho
    
    def __str__(self) -> str:
        """
        Representación en string del cuadrado.
        
        Returns:
            str: Información del cuadrado con su lado
        """
        return f"Cuadrado: lado={self._ancho}"