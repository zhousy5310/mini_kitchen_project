# Mini Kitchen Project

A simple command-line kitchen manager to track ingredients, add dishes with recipes, and pick dishes to prepare based on available ingredients. Data is saved between sessions.

## Features

- **Add Ingredients:** Add and update ingredient quantities.
- **Add Dishes:** Define dishes with their required ingredients and amounts.
- **Show Ingredients:** View all current ingredients and their quantities.
- **Show Available Dishes:** See which dishes can be made and how many times, based on current ingredients.
- **Pick Dish for Today:** Prepare a dish, automatically deducting used ingredients.
- **Save & Load:** All data is saved to `kitchen_data.json` and loaded on startup.

## How to Use

1. **Run the program:**
   ```bash
   python main.py
   ```

2. **Menu Options:**
   - `1. Add Ingredient`  
     Enter the name and amount to add or update an ingredient.
   - `2. Add Dish`  
     Enter the dish name and its recipe (ingredient names and required amounts).
   - `3. Show Ingredients`  
     Lists all ingredients and their current amounts.
   - `4. Show Available Dishes`  
     Shows each dish and how many times it can be made with current ingredients.
   - `5. Pick Dish for Today`  
     Choose a dish and quantity to prepare; ingredients are deducted.
   - `6. Save & Exit`  
     Saves all data and exits the program.

## File Structure

- `main.py` — Main program loop and user interface.
- `Kitchen.py` — `Kitchen` class: manages ingredients, dishes, and kitchen logic.
- `KitchenDataManager.py` — Handles saving/loading kitchen data to/from `kitchen_data.json`.

## Example
=== Kitchen Menu ===
Add Ingredient
Add Dish
Show Ingredients
Show Available Dishes
Pick Dish for Today
Save & Exit
Choose an option: 1
Ingredient name: tomato
Amount: 5


## Requirements

- Python 3.x

No external dependencies required.

## Notes

- Data is saved automatically when you choose "Save & Exit".
- If `kitchen_data.json` does not exist, a new one will be created.

---

Enjoy managing your kitchen!