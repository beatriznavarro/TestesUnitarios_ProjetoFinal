from src.models.ice_cream_stand import IceCreamStand
from unittest import TestCase


class TestIceCreamStand(TestCase):


    #### flavors_available ####
    def test_flavors_available(self):
        # setup
        name = 'Sorveteria da Bia'
        type = 'Sorveteria'
        list = ["Morango"]
        resultado_esperado = ["Morango"]

        icecreamstand = IceCreamStand(restaurant_name=name, cuisine_type=type, flavors_list=list)

        # Chamada
        resultado = icecreamstand.flavors_available()

        # Avaliacao
        self.assertListEqual(resultado, resultado_esperado)
    def test_flavors_available_sem_estoque(self):
        # Setup
        name = 'Sorveteria da Bia'
        type = 'Sorveteria'
        list = []
        resultado_esperado = "Estamos sem estoque atualmente!"

        icecreamstand = IceCreamStand(restaurant_name=name, cuisine_type=type, flavors_list=list)

        # Chamada
        resultado = icecreamstand.flavors_available()

        # Avaliacao
        assert resultado_esperado == resultado

    #### find_flavor ####
    def test_find_flavor_sem_estoque(self):
        # Setup
        name = 'Sorveteria da Bia'
        type = 'Sorveteria'
        list = []
        resultado_esperado = "Estamos sem estoque atualmente!"

        icecream = IceCreamStand(restaurant_name=name, cuisine_type=type, flavors_list=list)

        # Chamada
        resultado = icecream.find_flavor('Morango')

        # Avaliacao
        assert resultado_esperado == resultado


    def test_find_flavor_indiponivel(self):
        # Setup
        name = 'Sorveteria da Bia'
        type = 'Sorveteria'
        list = ['Flocos','Chocolate']
        resultado_esperado = f"Não temos no momento ['Flocos', 'Chocolate']!"

        icecream = IceCreamStand(restaurant_name=name, cuisine_type=type, flavors_list=list)

        # Chamada
        resultado = icecream.find_flavor('Morango')

        # Avaliacao
        assert resultado_esperado == resultado

    def test_find_flavor(self):
        # Setup
        name = 'Sorveteria da Bia'
        type = 'Sorveteria'
        list = ['Flocos','Chocolate']
        resultado_esperado = f"Temos no momento ['Flocos', 'Chocolate']!"

        icecream = IceCreamStand(restaurant_name=name, cuisine_type=type, flavors_list=list)

        # Chamada
        resultado = icecream.find_flavor('Flocos')

        # Avaliacao
        assert resultado_esperado == resultado

    #### add_flavor ####
    def test_add_flavor_ja_disponivel(self):
        # setup
        name = 'Sorveteria da Bia'
        type = 'Sorveteria'
        list = ['Morango','Chocolate']
        resultado_esperado = "\nSabor já disponivel!"

        icecreamstand = IceCreamStand(restaurant_name=name, cuisine_type=type, flavors_list=list)

        # Chamada
        resultado = icecreamstand.add_flavor('Morango')

        # Avaliacao
        assert resultado_esperado == resultado
    def test_add_flavor_sem_estoque(self):
        # setup
        name = 'Sorveteria da Bia'
        type = 'Sorveteria'
        list = []
        resultado_esperado = "Estamos sem estoque atualmente!"

        icecreamstand = IceCreamStand(restaurant_name=name, cuisine_type=type, flavors_list=list)

        # Chamada
        resultado = icecreamstand.add_flavor('Morango')

        # Avaliacao
        assert resultado_esperado == resultado
    def test_add_flavor(self):
        # setup
        name = 'Sorveteria da Bia'
        type = 'Sorveteria'
        list = ['Flocos']
        resultado_esperado = f"{'Morango'} adicionado ao estoque!"

        icecreamstand = IceCreamStand(restaurant_name=name, cuisine_type=type, flavors_list=list)

        # Chamada
        resultado = icecreamstand.add_flavor('Morango')

        # Avaliacao
        assert resultado_esperado == resultado
