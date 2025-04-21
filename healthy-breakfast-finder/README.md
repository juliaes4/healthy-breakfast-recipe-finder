# BCOG-200
# Healthy Breakfast Recipe Finder 

## Required Installs: Flask (that's it!)
## Project Description
This project is a simple **Flask web application** that helps users find **healthy breakfast recipes** based on ingredients or dietary preferences. Users can enter an ingredient (e.g., "banana" or "oats"), and the app will suggest matching recipes with their nutritional information (calories, protein, etc.). The goal is to make **meal planning easier** for those looking for healthy food options. This project uses **Flask** for the backend and **HTML/CSS** for the frontend.

---

## Why Use This?

- You’re in a rush and want a high-protein breakfast idea with what’s already in your fridge.
- You want to explore breakfast ideas that fit your dietary style (vegan, vegetarian, gluten-free).
- You’re meal-prepping for the week and want recipes with consistent nutrition data.
- You want to sort by flavor: sweet, savory, or spicy breakfasts!

---

## Functions Overview

### `home()`
- **Purpose**: Handles the homepage and form submission.
- **Route**: `/`
- **Methods**: GET and POST
- **Action**: On POST, reads user input, filters recipes, and displays matches in `index.html`.

How Healthy_Recipes Uses GET and POST:
This app uses standard web communication methods to control how users interact with the form.

GET method: Loads the homepage (index.html) when the user first visits the site. No search has been submitted yet, so the page displays a search bar and no results.
POST method: Activated when the user submits the search form. The app grabs the input (like "banana" or "vegan"), passes it into the search function, and returns matching recipes on the same page.

---

### `search_recipe(query, recipes)`
- **Parameters**:
  - `query` (str): The user’s search term
  - `recipes` (dict): Full dictionary of recipes from the CSV
- **Returns**: A filtered dictionary of recipes matching the query by name, ingredients, flavor, or diet tag.

---

### `load_recipes(filepath)`
- **Parameters**:
  - `filepath` (str): Path to the CSV file
- **Returns**: A dictionary of recipe objects, each containing name, ingredients, calories, protein, diet, flavor, servings, and instructions.

---

## Input File Format (`recipes.csv`)

This file contains all breakfast recipes the app uses for searching. It must:

- Be in `.csv` format
- Include a header row with the following exact column names:
name, servings, ingredients & quantities, calories, protein, diet, flavor, instructions
- Each row should represent one recipe
- Values should be formatted as:
  - `name` = string  
  - `servings` = integer  
  - `ingredients & quantities` = string  
  - `calories`, `protein` = integers  
  - `diet` = one of: vegetarian, vegan, meat  
  - `flavor` = one of: sweet, savory, spicy  
  - `instructions` = string

---

## Example Use Cases

- A user searches for **"banana"**: the app returns banana-related breakfast recipes.
- A user enters **"vegan"**: they see only recipes tagged as vegan.
- A user types **"spicy"**: spicy breakfast bowls, wraps, or scrambles appear.
- A user on a high-protein diet wants a **protein > 10g** filter (coming soon).

---

## Group Members

Julia Smith (me)

---

## Next Steps

- Add a rating system for each recipe - would show up in a .csv file (using stars?)

---

## Languages & Tools Used

- Python (Flask)
- HTML / CSS
- CSV (for recipe storage)


