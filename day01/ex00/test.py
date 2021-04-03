from book import Book
from recipe import Recipe
from datetime import datetime

bk = Book('bk', datetime.now(), datetime.now(), {"starter":[], "lunch":[], "dessert":[]})

rp1 = Recipe('11', 5, 2,['salt'], "", 'lunch')
rp2 = Recipe('22', 5, 2,['lemons'], "squiiiizzzzzz", 'starter')
rp3 = Recipe('33', 5, 2,['salt'], "", 'none')
rp4 = Recipe('44', 5, 2,['salt'], "", 'dessert')
#               THE ERROR
# rp5 = Recipe('55', 5, 2,['salt'], "", '')

pr = str(rp1)

print(pr)

bk.add_recipe(rp1)
bk.add_recipe(rp2)
#           THE ERROR
# bk.add_recipe(rp3)
bk.add_recipe(rp4)


bk.get_recipe_by_name('11')
print(bk.get_recipes_by_types('starter'))