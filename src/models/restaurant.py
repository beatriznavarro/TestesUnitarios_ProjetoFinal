class Restaurant:
    """Model de restaurante simples."""

    # Melhoria: Alteração dos prints necessário para Return seguindo as boas práticas
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name #bug:removendo o .title() e considerando o nome como foi definifo pelo usuário
        self.cuisine_type = cuisine_type
        self.number_served = 0
        self.open = False

    def describe_restaurant(self):
        """Imprima uma descrição simples da instância do restaurante."""
        # bug: alterando o self.cuisine_type para self.cuisine_name no primeiro parâmetro

        return (f"Esse restaturante chama {self.restaurant_name} and serve {self.cuisine_type}.\nEsse restaturante está servindo {self.number_served} consumidores desde que está aberto.")

    def open_restaurant(self):
        """Imprima uma mensagem indicando que o restaurante está aberto para negócios."""
        if not self.open:
            self.open = True #bug: alterando False para True, pois aqui o restaurante está aberto
            self.number_served = 0 #bug: alterando number_served para 0, pois o restaurante acabou de abrir
            return f"{self.restaurant_name} agora está aberto!"
        else:
            return f"{self.restaurant_name} já está aberto!"

    def close_restaurant(self):
        """Imprima uma mensagem indicando que o restaurante está fechado para negócios."""
        # Melhoria: Fazendo a lógica ao contrário para economizar um else
        if not self.open:
            return f"{self.restaurant_name} já está fechado!"


        self.open = False
        self.number_served = 0
        return f"{self.restaurant_name} agora está fechado!"

    def set_number_served(self, total_customers):
        """Defina o número total de pessoas atendidas por este restaurante até o momento."""
        # Melhoria: Fazendo a lógica ao contrário para economizar um else
        if not self.open:
            return f"{self.restaurant_name} está fechado!"

        self.number_served = total_customers
        return self.number_served

    def increment_number_served(self, more_customers):
        """Aumenta número total de clientes atendidos por este restaurante."""
        #Melhoria: Fazendo a lógica ao contrário para economizar um else
        if not self.open:
            return f"{self.restaurant_name} está fechado!"

        self.number_served += more_customers #bug: necessário incrementar o número de clientes e não substituir pelos novos, add += ao invés de =
        return self.number_served