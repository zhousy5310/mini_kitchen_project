from Kitchen import Kitchen 
from KitchenDataManager import KitchenDataManager 

def main():
    kitchen = Kitchen()
    manager = KitchenDataManager()
    manager.load(kitchen)

    while True:
        print("\n=== Kitchen Menu ===")
        print("1. Add Ingredient")
        print("2. Add Dish")
        print("3. Show Ingredients")
        print("4. Show Available Dishes")
        print("5. Pick Dish for Today")
        print("6. Save & Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            name = input("Ingredient name: ").strip().lower()
            amt = int(input("Amount: "))
            kitchen.add_ingredient(name, amt)

        elif choice == "2":
            name = input("Dish name: ").strip().lower()
            recipe = {}
            print("Enter ingredients for the dish (enter 'done' to finish):")
            while True:
                ing = input("Ingredient name: ").strip().lower()
                if ing == "done":
                    break
                amount = int(input(f"Amount of {ing}: "))
                recipe[ing] = amount
            kitchen.add_dish(name, recipe)

        elif choice == "3":
            kitchen.show_ingredients()

        elif choice == "4":
            kitchen.show_available_dishes()

        elif choice == "5":
            dish = input("Dish to prepare: ").strip().lower()
            num = int(input("How many to prepare? "))
            kitchen.pick_dish_for_today(dish, num)

        elif choice == "6":
            manager.save(kitchen)
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()