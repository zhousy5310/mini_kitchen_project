import json

class KitchenDataManager:
    def __init__(self, file='kitchen_data.json'):
        self.file = file

    def save(self, kitchen):
        data = {
            "ingredients": kitchen.ingredients,
            "dishes": kitchen.dishes
        }
        with open(self.file, 'w') as f:
            json.dump(data, f)
        print("Data saved!")

    def load(self, kitchen):
        try:
            with open(self.file, 'r') as f:
                data = json.load(f)
                kitchen.ingredients = data.get("ingredients", {})
                kitchen.dishes = data.get("dishes", {})
                print("Data loaded!")
        except FileNotFoundError:
            print("No save file found. Starting fresh.")
