from book import Book
from recipe import Recipe


# testing recipe

r1 = Recipe('cake', 2, 30, ['hello', 'world'], 'description', 'dessert')

r2 = Recipe('salade', 1, 20, ['khoss', 'maticha',
            'khyar'], '3choub', 'starter')

# r3 = Recipe('invalid', 10, 20, ['khoss', 'maticha', 'khyar'], 'description',
# 'starter') # cooking_lvl is not valide!

# r4 = Recipe('invalid', 1, -20, ['khoss', 'maticha', 'khyar'], 'description',
# 'starter') # cooking_time is not valide!

# r5 = Recipe('invalid', 1, 20, ['khoss', 'maticha', 'khyar'], 'description',
# 'invalid') # recipe_type is not valide!

# r6 = Recipe('invalid', 1, 20, ['khoss', 'maticha', 'khyar'], 'description',
# 1) # recipe_type is not valide!

# r7 = Recipe('invalid', 1, 20, ['khoss', 'maticha', ''], 'description',
# 'starter') # ingredients are not valide!

# r8 = Recipe('invalid', 1, 20, [], 'description', 'starter')
# # ingredients are not valide!

r9 = Recipe('tajin', 5, 60, ['bassla', 'lham',
            'bar9ou9', 'mchmach'], 'art', 'lunch')

# valid recipes : r1, r2, r9

# testing book

book = Book('book')

print(book.get_recipe_by_name('cake'))  # recipe not found! && None

print(book.creation_date)  # date

print(book.last_update)  # the same date as creation_date

book.add_recipe(r1)
book.add_recipe(r2)
book.add_recipe(r9)

print(book.creation_date)  # date
print(book.last_update)  # date

book.get_recipe_by_name("salade")

book.get_recipe_by_name("doesnt exist")  # recipe not found!

print(book.get_recipes_by_types('starter'))  # [r2]

book.add_recipe(Recipe('ka3b ghzal', 5, 120, [
                'louz', 'l3ssl', 'idk'], 'tasty', 'starter'))

print(book.get_recipes_by_types('starter'))  # [r2, 'ka3b ghzal']

book.get_recipes_by_types("invalid type")  # invalid type!
