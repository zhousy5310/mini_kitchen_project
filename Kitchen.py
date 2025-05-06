class Kitchen:
    def __init__(self):
        self.ingredients = {}
        self.dishes = {}

    def add_ingredient(self, name, amount):
        self.ingredients[name] = self.ingredients.get(name, 0) + amount

    def add_dish(self, dish_name, recipe):
        self.dishes[dish_name] = recipe

    def max_dishes_possible(self, dish_name):
        if dish_name not in self.dishes:
            return 0
        recipe = self.dishes[dish_name]
        return min(self.ingredients.get(ing, 0) // amount for ing, amount in recipe.items())

    def show_available_dishes(self):
        print("\n--- Available Dishes ---")
        for dish in self.dishes:
            count = self.max_dishes_possible(dish)
            print(f"{dish}: {count} can be made")

    def pick_dish_for_today(self, dish_name, count):
        if self.max_dishes_possible(dish_name) < count:
            print(f"Not enough ingredients for {count} {dish_name}(s)")
            return
        for ing, amt in self.dishes[dish_name].items():
            self.ingredients[ing] -= amt * count
        print(f"{count} {dish_name}(s) made!")

    def show_ingredients(self):
        print("\n--- Ingredients ---")
        for ing, amt in self.ingredients.items():
            print(f"{ing}: {amt}")
