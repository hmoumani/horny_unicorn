class Recipe:
    def __init__(self, name: str, cooking_lvl: int, cooking_time:int,
                ingredients: list, description: str, recipe_type: str) -> None:
        if not isinstance(name, str) or len(name) == 0:
            print("name is not valide!")
            exit(1)
        if not isinstance(cooking_lvl, int) or cooking_lvl < 1 or cooking_lvl > 5:
            print("cooking_lvl is not valide!")
            exit(1)
        if not isinstance(cooking_time, int) or cooking_time < 0:
            print("cooking_time is not valide!")
            exit(1)
        if not isinstance(ingredients, list) or len(ingredients) == 0 or\
            not all([isinstance(elem, str) and len(elem) != 0 for elem in ingredients]):
            print("ingredients are not valide!")
            exit(1)
        if not isinstance(description, str):
            print("description is not valide!")
            exit(1)
        if not isinstance(recipe_type, str) or recipe_type not in ["starter", "lunch", "dessert"]:
            print("recipe_type is not valide!")
            exit(1)
        self.name = name
        self.cooking_lvl = cooking_lvl
        self.cooking_time = cooking_time
        self.ingredients = ingredients
        self.description = description
        self.recipe_type = recipe_type

    def __str__(self):
        """Return the string to print with the recipe info"""
        txt = ""
        """Your code here"""
        txt += (f"recipe name: {self.name}, "
        f"cooking level: {self.cooking_lvl}, "
        f"cooking time: {self.cooking_time}, "
        f"ingredients: {', '.join(self.ingredients)}, "
        f"description: {self.description}, "
        f"recipe type: {self.recipe_type}")
        return txt

if __name__ == '__main__':
    Reciption = Recipe('cake', 2, 30, ['hello', 'world'], 'description', 'dessert')

    print(type(Reciption.name))

    print(str(Reciption))