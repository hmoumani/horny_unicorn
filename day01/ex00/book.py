import datetime
class Book:
    def __init__(self, name, last_update, creation_date, recipes_list):
        if type(name) != str:
            print("name is not valide!")
            exit(1)
        if type(last_update) != datetime.datetime:
            print("last_update is not valide!")
            exit(1)
        if type(creation_date) != datetime.datetime:
            print("creation_date is not valide!")
            exit(1)
        if type(recipes_list) != dict or len(recipes_list) != 3 all([elem in ["starter", "lunch", "dessert"] for elem in recipes_list.keys()]):
            print("creation_date is not valide!")
            exit(1)
    def get_recipe_by_name(self, name):
        """Print a recipe with the name `name` and return the instance"""
        # if not any(name == nname for elem in self.recipes_list for nname in elem.name )
        #     print("undefined name")
        #     return None
        for key in self.recipes_list.keys():
            if name == recipes_list[key].name:
                save = key
                break

        print(recipes_list[key].name +", "+ l +", "+ )
        pass

    def get_recipes_by_types(self, recipe_type):
        """Get all recipe names for a given recipe_type """
        pass

    def add_recipe(self, recipe):
        """Add a recipe to the book and update last_update"""
        pass