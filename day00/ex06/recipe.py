cookbook= {
    'sandwich' : {
        'ingredients' : ['ham', 'bread', 'cheese', 'tomatoes'],
        'meal' : 'lunch',
        'prep_time' : 10
    },
    'cake' : {
        'ingredients' : ['flour', 'sugar', 'eggs'],
        'meal' : 'dessert',
        'prep_time' : 60
    },
    'salad' : {
        'ingredients' : ['avocado', 'arugula', 'tomatoes', 'spinach'],
        'meal' : 'lunch',
        'prep_time' : 15
    }

}

def print_recipe(name):
    if name not in cookbook:
        print("recipe does not exist")
        return None
    print("Recipe for " + name)
    print('Ingredients list: ', cookbook[name]['ingredients'])
    print('To be eaten for', cookbook[name]['meal']+ ".")
    print('Takes {} minutes of cooking.'.format(cookbook[name]['prep_time']))

def delete_recipe(name):
    if name not in cookbook:
        print("recipe does not exist")
        return None
    del cookbook[name]
    print("successfully deleted")

def add_recipe(name="name", ingredients=[], meal='lunch', prep_time=20):
    cookbook[name] = {
        'ingredients' : ingredients,
        'meal' : meal,
        'prep_time' : prep_time
    }

def print_all_recipe():
    for key in cookbook.keys():
        print("*" * 40)
        print_recipe(key)
        print("*" * 40)


def show_promp():
    print("""Please select an option by typing the corresponding number:
1: Add a recipe
2: Delete a recipe
3: Print a recipe
4: Print the cookbook
5: Quit""")

while True:
    show_promp()
    inp = input(">>")
    if (not inp.isdigit() or int(inp) < 1 or int(inp) > 5):
        print("""This option does not exist, please type the corresponding number.
To exit, enter 5.""")
        continue
    if int(inp) == 1:
        name = input("name: ")
        ll=[]
        while True:
            ingr = input('enter ingredients, [tupe 0 in the end of the list]')
            if ingr == '0':
                break
            ll.append(ingr)
        meal = input("meal :")
        prepa_time = int(input("preparation time: "))
        add_recipe(name, ll, meal, prepa_time)
    elif int(inp) == 2:
        delete_recipe(input('name of recipe to delete : '))
    elif int(inp) == 3:
        print_recipe(input('name of recipe to print : '))
    elif int(inp) == 4:
        print_all_recipe()
    elif int(inp) == 5:
        print('Cookbook closed.')
        exit()
    