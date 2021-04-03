import datetime
from recipe import Recipe
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
        if type(recipes_list) != dict or len(recipes_list) != 3 or not all([elem in ["starter", "lunch", "dessert"] for elem in recipes_list.keys()]):
            print("recipes_list is not valide!")
            exit(1)
        self.name = name
        self.last_update = last_update
        self.creation_date = creation_date
        self.recipes_list = recipes_list
    def get_recipe_by_name(self, name):
        """Print a recipe with the name `name` and return the instance"""
        # if not any(name == nname for elem in self.recipes_list for nname in elem.name )
        #     print("undefined name")
        #     return None
        for key in self.recipes_list.keys():
            for elem in self.recipes_list[key]:
                if name == elem.name:
                    self.recipes_list[key].__str__()

    def get_recipes_by_types(self, recipe_type):
        """Get all recipe names for a given recipe_type """
        ret = []
        for key in self.recipes_list.keys():
            for elem in self.recipes_list[key]:
                if elem.recipe_type == recipe_type:
                    ret.append(elem.name)
        return ret

    def add_recipe(self, recipe):
        """Add a recipe to the book and update last_update"""
        if (Recipe != type(recipe) or recipe.recipe_type not in self.recipes_list.keys()):
            print("invalide recipe type")
            exit(1)
        self.recipes_list[recipe.recipe_type].append(recipe)
        print(self.recipes_list[recipe.recipe_type][0].__str__())