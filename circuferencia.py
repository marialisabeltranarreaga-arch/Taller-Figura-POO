import math
from figura_geometrica import FiguraGeometrica


class Circunferencia(FiguraGeometrica):
    """
    Clase que representa una circunferencia.
    Hereda de FiguraGeometrica.
    Recibe solo un parámetro: el radio (que se asigna al ancho).
    """
    
    def __init__(self, radio: float):
        """
        Constructor de la Circunferencia.
        Recibe solo el radio y lo asigna tanto a ancho como alto.
        
        Args:
            radio: Radio de la circunferencia (debe ser mayor que 0)
        """
        super().__init__(radio, radio)
    
    @property
    def radio(self) -> float:
        """Getter para el radio de la circunferencia."""
        return self._ancho
    
    @radio.setter
    def radio(self, valor: float):
        """
        Setter para el radio de la circunferencia.
        Actualiza tanto ancho como alto.
        
        Args:
            valor: Nuevo valor del radio
        """
        self.ancho = valor
        self.alto = valor
    
    def area(self) -> float:
        """
        Calcula el área de la circunferencia.
        
        Returns:
            float: Área de la circunferencia (π * radio²)
        """
        return math.pi * (self._ancho ** 2)
    
    def perimetro(self) -> float:
        """
        Calcula el perímetro de la circunferencia.
        
        Returns:
            float: Perímetro de la circunferencia (2 * π * radio)
        """
        return 2 * math.pi * self._ancho
    
    def __str__(self) -> str:
        """
        Representación en string de la circunferencia.
        
        Returns:
            str: Información de la circunferencia con su radio
        """
        return f"Circunferencia: radio={self._ancho}"