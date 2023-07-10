from src.models.restaurant import Restaurant


class TestRestaurant:


    #### describe_restaurant ####
    def test_describe_restaurant(self):
        # setup
        name = 'Restaurante da Bia'
        type = 'Comida mexicana'

        resultado_esperado = 'Esse restaturante chama Restaurante da Bia and serve Comida mexicana.\nEsse restaturante está servindo 0 consumidores desde que está aberto.'

        rest = Restaurant(restaurant_name=name, cuisine_type=type)

        # Chamada
        resultado = rest.describe_restaurant()

        # Avaliacao
        assert resultado_esperado == resultado

    #### open_restaurant ####
    def test_open_restaurant(self):
        # setup
        name = 'Restaurante da Bia'
        type = 'Comida mexicana'

        resultado_esperado = f"{name} agora está aberto!"
        rest = Restaurant(restaurant_name=name, cuisine_type=type)

        # Chamada
        resultado = rest.open_restaurant()

        # Avaliacao
        assert resultado_esperado == resultado
    def test_open_restaurant_ja_aberto(self):
        # setup
        name = 'Restaurante da Bia'
        type = 'Comida mexicana'

        resultado_esperado = f"{name} já está aberto!"
        rest = Restaurant(restaurant_name=name, cuisine_type=type)
        rest.open_restaurant()
        # Chamada
        resultado = rest.open_restaurant()

        # Avaliacao
        assert resultado_esperado == resultado

    #### close_restaurant ####
    def test_close_restaurant_ja_fechado(self):
        # setup
        name = 'Restaurante da Bia'
        type = 'Comida mexicana'

        resultado_esperado = f"{name} já está fechado!"
        rest = Restaurant(restaurant_name=name, cuisine_type=type)

        # Chamada
        resultado = rest.close_restaurant()

        # Avaliacao
        assert resultado_esperado == resultado
    def test_close_restaurant_aberto(self):
        # setup
        name = 'Restaurante da Bia'
        type = 'Comida mexicana'

        resultado_esperado = f"{name} agora está fechado!"
        rest = Restaurant(restaurant_name=name, cuisine_type=type)
        rest.open_restaurant()

        # Chamada
        resultado = rest.close_restaurant()

        # Avaliacao
        assert resultado_esperado == resultado

    #### set_number_served ####
    def test_set_number_served_restaurante_fechado(self):
        # setup
        name = 'Restaurante da Bia'
        type = 'Comida mexicana'

        resultado_esperado = "Restaurante da Bia está fechado!"

        rest = Restaurant(restaurant_name=name, cuisine_type=type)

        # Chamada
        resultado = rest.set_number_served(10)

        # Avaliacao
        assert resultado_esperado == resultado
    def test_set_number_served(self):
        # setup
        name = 'Restaurante da Bia'
        type = 'Comida mexicana'

        resultado_esperado = 10

        rest = Restaurant(restaurant_name=name, cuisine_type=type)
        rest.open_restaurant()

        # Chamada
        resultado = rest.set_number_served(10)

        # Avaliacao
        assert resultado_esperado == resultado

    #### increment_number_served ####
    def test_increment_number_served_restaurante_fechado(self):
        # setup
        name = 'Restaurante da Bia'
        type = 'Comida mexicana'

        resultado_esperado = "Restaurante da Bia está fechado!"

        rest = Restaurant(restaurant_name=name, cuisine_type=type)

        # Chamada
        resultado = rest.increment_number_served(5)

        # Avaliacao
        assert resultado_esperado == resultado
    def test_increment_number_served(self):
        # setup
        name = 'Restaurante da Bia'
        type = 'Comida mexicana'

        resultado_esperado = 10
        rest = Restaurant(restaurant_name=name, cuisine_type=type)
        rest.open_restaurant()
        rest.increment_number_served(5)
        # Chamada
        resultado = rest.increment_number_served(5)

        # Avaliacao
        assert resultado_esperado == resultado