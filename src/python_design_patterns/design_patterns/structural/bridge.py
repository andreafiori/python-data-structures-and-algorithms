"""
Bridge pattern | https://wikipedia.org/wiki/Bridge_pattern

The Bridge pattern decouples abstraction and implementation.
Abstraction (Shape) defines the high-level interface.
Implementor (Renderer) defines the interface for implementation classes.
Concrete Implementors (VectorRenderer, RasterRenderer) provide platform-specific implementations.
Concrete Abstractions (Circle, Square) use the implementor's methods.
"""

from abc import ABC, abstractmethod

class Renderer(ABC):
    @abstractmethod
    def render_circle(self, radius: float) -> str:
        pass

    @abstractmethod
    def render_square(self, side: float) -> str:
        pass

class VectorRenderer(Renderer):
    def render_circle(self, radius: float) -> str:
        return f"Drawing a circle of radius {radius} using vector graphics."

    def render_square(self, side: float) -> str:
        return f"Drawing a square of side {side} using vector graphics."

class RasterRenderer(Renderer):
    def render_circle(self, radius: float) -> str:
        return f"Drawing a circle of radius {radius} using raster graphics."

    def render_square(self, side: float) -> str:
        return f"Drawing a square of side {side} using raster graphics."

class Shape:
    def __init__(self, renderer: Renderer):
        self.renderer = renderer

    def draw(self) -> str:
        raise NotImplementedError

class Circle(Shape):
    def __init__(self, renderer: Renderer, radius: float):
        super().__init__(renderer)
        self.radius = radius

    def draw(self) -> str:
        return self.renderer.render_circle(self.radius)

class Square(Shape):
    def __init__(self, renderer: Renderer, side: float):
        super().__init__(renderer)
        self.side = side

    def draw(self) -> str:
        return self.renderer.render_square(self.side)
