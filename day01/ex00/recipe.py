class Recipe:
    def __init__(self, name, cooking_lvl, cooking_time, ingredients, description, recipe_type):
        if type(name) != str or len(nam) == 0:
            print("name is not string")
            exit(1)
        if type(cooking_lvl) != int or cooking_lvl not in range(1, 6):
            print("cooking_lvl is not valid")
            exit(1)
        if type(cooking_time) != int or cooking_time < 0:
            print("cooking_time is not valid")
            exit(1)
        if type(ingredients) != list or any(type(elem) != str for elem in ingredients) or len(ingredients) == 0:
            print("ingredients list is not valid")
            exit(1)
        if type(description) != str :
            print("description is not valid")
            exit(1)
        if type(recipe_type) != str and recipe_type not in ["starter", "lunch", "dessert"] or len(recipe_type) == 0:
            print("recipe_type is not valid")
            exit(1)
        self.name = name
        self.cooking_lvl = cooking_lvl
        self.cooking_time = cooking_time
        self.ingredients = ingredients
        self.description = description
        self.recipe_type = recipe_type
    def __str__(self):
        """Return the string to print with the recipe info"""
        txt = "name " + self.name + " cooking_lvl" + self.cooking_lvl + " cooking_time" + self.cooking_time + " ingredients" + self.ingredients + " description" + self.description + " recipe_type" + self.recipe_type
        """Your code goes here"""
        return txt