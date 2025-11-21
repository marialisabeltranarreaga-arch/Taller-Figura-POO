class FiguraGeometrica:
    """
    Clase base para figuras geométricas.
    Implementa encapsulamiento con atributos privados y properties.
    """
    
    def __init__(self, ancho: float, alto: float):
        """
        Constructor de la clase FiguraGeometrica.
        
        Args:
            ancho: Ancho de la figura (debe ser mayor que 0)
            alto: Alto de la figura (debe ser mayor que 0)
        
        Raises:
            ValueError: Si ancho o alto no son mayores que 0
        """
        if ancho <= 0 or alto <= 0:
            raise ValueError("El alto y ancho deben ser mayores que 0")
        
        self._ancho = ancho
        self._alto = alto
    
    @property
    def ancho(self) -> float:
        """Getter para el ancho de la figura."""
        return self._ancho
    
    @ancho.setter
    def ancho(self, valor: float):
        """
        Setter para el ancho de la figura.
        
        Args:
            valor: Nuevo valor del ancho
        
        Raises:
            ValueError: Si el valor no es mayor que 0
        """
        if valor <= 0:
            raise ValueError("El ancho debe ser mayor que 0")
        self._ancho = valor
    
    @property
    def alto(self) -> float:
        """Getter para el alto de la figura."""
        return self._alto
    
    @alto.setter
    def alto(self, valor: float):
        """
        Setter para el alto de la figura.
        
        Args:
            valor: Nuevo valor del alto
        
        Raises:
            ValueError: Si el valor no es mayor que 0
        """
        if valor <= 0:
            raise ValueError("El alto debe ser mayor que 0")
        self._alto = valor
    
    def area(self) -> float:
        """
        Calcula el área de la figura.
        Implementación base: ancho * alto.
        
        Returns:
            float: Área de la figura
        """
        return self._ancho * self._alto
    
    def perimetro(self):
        """
        Método abstracto para calcular el perímetro.
        Debe ser implementado por las subclases.
        """
        pass
    
    def __str__(self) -> str:
        """
        Representación en string de la figura.
        
        Returns:
            str: Información de la figura con sus dimensiones
        """
        return f"{self.__class__.__name__}: ancho={self._ancho}, alto={self._alto}"