import pytest

from python_design_patterns.design_patterns.structural.bridge import Circle, RasterRenderer, Square, VectorRenderer

class TestBridgePattern:

    @pytest.fixture
    def vector_renderer(self):
        return VectorRenderer()

    @pytest.fixture
    def raster_renderer(self):
        return RasterRenderer()

    def test_circle_with_vector_renderer(self, vector_renderer):
        circle = Circle(vector_renderer, 5)
        assert circle.draw() == "Drawing a circle of radius 5 using vector graphics."

    def test_circle_with_raster_renderer(self, raster_renderer):
        circle = Circle(raster_renderer, 5)
        assert circle.draw() == "Drawing a circle of radius 5 using raster graphics."

    def test_square_with_vector_renderer(self, vector_renderer):
        square = Square(vector_renderer, 4)
        assert square.draw() == "Drawing a square of side 4 using vector graphics."

    def test_square_with_raster_renderer(self, raster_renderer):
        square = Square(raster_renderer, 4)
        assert square.draw() == "Drawing a square of side 4 using raster graphics."
