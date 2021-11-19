# ingredients = {'eggs': '2 pcs', 'milk': '60 g', 'salt':'20g'}
# print(ingredients['eggs'])

class Recipe:

   number_of_cooking_stages = 3

   def __init__(self,name,ingredients,annotation,cooking_time,cooking_device ):
      self.name = name
      self.ingredients = ingredients
      self.annotation = annotation
      self.cooking_time = cooking_time
      self.cooking_device = cooking_device


recipe_1 = Recipe(name='Chicken soup', ingredients='potato,chiken breast,salt,carrot,onion', annotation = 'vegetable soup with chicken breast',cooking_time = '40',cooking_device =
'RMC-M903S')

print(recipe_1.name)
print(recipe_1.ingredients)
print(recipe_1.annotation)
print(recipe_1.cooking_time)
print(recipe_1.cooking_device)



recipe_2 = Recipe(name='hot dog', ingredients='sausage,bun,ketchup,mayonnaise', annotation = 'wheat bun with sausage seasoned with ketchup, mayonnaise, mustard',cooking_time = '10',cooking_device =
'none')

print(recipe_2.name)
print(recipe_2.ingredients)
print(recipe_2.annotation)
print(recipe_2.cooking_time)
print(recipe_2.cooking_device)



recipe_3 = Recipe(name='омлет', ingredients='milk,eggs,milk', annotation = 'нежный омлет с молоком',cooking_time = '20',cooking_device = 'SkyBaker')

print(recipe_3.name)
print(recipe_3.ingredients)
print(recipe_3.annotation)
print(recipe_3.cooking_time)
print(recipe_3.cooking_device)

recipe_1 = {
   'name': 'chicken soup',
   'annotation': 'vegetable soup with chicken breast',
   'cooking time':40,
   'number of cooking stages': 3,
   'ingredients':['potato', 'chiken breast', 'salt','carrot','onion'],
   'stages of preparation': {'broth':'pour a saucepan with clean water, put chicken breast in it', 'vegetables':'cut into small pieces'}

}
print(("\033[35m {}" .format(recipe_1)))

recipe_2 = {
   'name': 'hot dog',
   'annotation': 'wheat bun with sausage seasoned with ketchup, mayonnaise, mustard',
   'cooking time':10,
   'number of cooking stages': 3,
   'ingredients':['sausage', 'bun', 'ketchup','mayonnaise'],
   'stages of preparation': {'bun':'Ножом сделать надрез вдоль булочек до половины глубины','sausage': 'Сосиски отварить или поджарить', 'компоновка':'положить сосиски на булочку и залить кетчупов и майонезом по вкусу'}

}
print(("\033[34m {}" .format(recipe_2)))

recipe_3 = {
   'name': 'омлет',
   'annotation': 'нежный омлет с молоком',
   'cooking time':20,
   'number of cooking stages': 3,
   'ingredients':['milk','eggs','milk'],
   'stages of preparation': {'eggs':'разбить яйца в миску', 'milk': 'залить яйца молоком', 'запекание':'взболтать и выложить в форму'}

}
print(("\033[31m {}" .format(recipe_3)))
