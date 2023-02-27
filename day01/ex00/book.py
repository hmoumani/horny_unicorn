import datetime
from recipe import Recipe

class Book:
    def __init__(self, name: str) -> None:
        if not isinstance(name, str) or len(name) == 0:
            print("name is not valide!")
            exit(1)
        self.name = name
        self.last_update = datetime.datetime.now()
        self.creation_date = self.last_update
        self.recipes_list = {
            "starter": [],
            "lunch": [],
            "dessert": []
        }

    def get_recipe_by_name(self, name):
        """Prints a recipe with the name \texttt{name} and returns the instance"""
        results = map(lambda recipes: filter(lambda x: x.name == name, recipes),
                    self.recipes_list.values())
        recipes = [recipe for meal_type in results for recipe in meal_type]
        if not recipes:
            print("recipe not found!")
            return None
        print(recipes[0])
        return recipes[0]
    
    def get_recipes_by_types(self, recipe_type):
        """Get all recipe names for a given recipe_type """ 
        if recipe_type not in self.recipes_list:
            print("recipe type not found!")
            return None
        return [item.name for item in self.recipes_list[recipe_type]]
    
    def add_recipe(self, recipe):
        """Add a recipe to the book and update last_update"""
        if not isinstance(recipe, Recipe):
            print("recipe is not valide!")
            return None
        if not recipe.recipe_type in self.recipes_list:
            print("recipe type not found!")
            return None
        self.recipes_list[recipe.recipe_type].append(recipe)
        self.last_update = datetime.datetime.now()

if __name__ == '__main__':
    book = Book('book')

    book.get_recipe_by_name('cake')
    
    print(book.get_recipes_by_types('lunfwefwech'))