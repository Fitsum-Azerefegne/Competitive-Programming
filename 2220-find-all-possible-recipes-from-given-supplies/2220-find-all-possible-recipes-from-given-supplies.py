class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        available_supplies = set(supplies)
        recipe_map = {recipe: ingredient for recipe, ingredient in zip(recipes, ingredients)}

        queue = deque()  
        can_make = set()

        for recipe, ingredients_list in recipe_map.items():
            if all(ingredient in available_supplies for ingredient in ingredients_list):
                queue.append(recipe)
                can_make.add(recipe)
        while queue:
            current_recipe = queue.popleft()  
            for recipe, ingredient_list in recipe_map.items():
                if recipe not in can_make: 
                    if all(ingredient in available_supplies or ingredient in can_make for ingredient in ingredient_list):
                        queue.append(recipe) 
                        can_make.add(recipe) 
        return list(can_make)