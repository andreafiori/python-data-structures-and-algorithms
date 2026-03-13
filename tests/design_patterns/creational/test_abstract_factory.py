from python_design_patterns.design_patterns.creational.abstract_factory import DellFactory, DellLaptop, SamsungFactory, SamsungFactory, SamsungSmartphone

class TestAbstractFactory:

    def test_dell_factory(self):
        factory1 = DellFactory()
        laptop = factory1.create_laptop()
        smartphone = factory1.create_smartphone()

        assert isinstance(laptop, DellLaptop) == True
        assert smartphone is None

    def test_samsung_factory(self):
        factory2 = SamsungFactory()
        laptop = factory2.create_laptop()
        smartphone = factory2.create_smartphone()

        assert laptop is None
        assert isinstance(smartphone, SamsungSmartphone) == True
