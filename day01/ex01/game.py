class GotCharacter:
    def __init__(self, first_name, is_alive=True):
        self.first_name = first_name
        self.is_alive = is_alive

class Stark(GotCharacter):
    """A class representing the Stark family. Or when bad things happen to good people."""
    def __init__(self, first_name, is_alive=True):
        super().__init__(first_name, is_alive)
        self.family_name = "Stark"
        self.house_words = "Winter is Coming"
    def print_house_words(self):
        print(self.house_words)
    def die(self):
        self.is_alive = False

class Targaryan(GotCharacter):
    """A class representing the Targaryan family. Or a Barbecue restaurant :v."""
    def __init__(self, first_name, is_alive=True):
        super().__init__(first_name, is_alive)
        self.family_name = "Targaryan"
        self.house_words = "Fire and Blood"
    def print_house_words(self):
        print(self.house_words)
    def die(self):
        self.is_alive = False