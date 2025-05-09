from flask import Flask, render_template, request
import csv

print("app.py is running...")

app = Flask(__name__)

def load_recipes():
    recipes = {}
    try:
        with open("recipes.csv", newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                recipes[row["name"]] = {
                    "ingredients": row["ingredients & quantities"],
                    "calories": int(row["calories"]),
                    "protein": int(row["protein"]),
                    "diet": row["diet"],
                    "flavor": row["flavor"],
                    "servings": row["servings"],
                    "instructions": row["instructions"]
                }

    except Exception as e:
        print(f"Error loading CSV: {e}")
    return recipes

recipes = load_recipes()

@app.route("/", methods=["GET", "POST"])
def home():
    results = {}
    if request.method == "POST":
        query = request.form["query"].lower()
        results = search_recipe(query)

        # Add average ratings
        for name in results:
            ratings = []
            try:
                with open("ratings.csv", newline='', encoding="utf-8") as file:
                    reader = csv.reader(file)
                    next(reader, None)
                    for row in reader:
                        if row[0] == name:
                            ratings.append(int(row[1]))
            except:
                pass
            avg = round(sum(ratings) / len(ratings), 2) if ratings else None
            results[name]["average_rating"] = avg

    return render_template("index.html", recipes=results)

def search_recipe(query):
    matches = {}
    for name, data in recipes.items():
        if (
            query in name.lower()
            or query in data["ingredients"].lower()
            or query in data["diet"].lower()
        ):
            matches[name] = data
    return matches

@app.route("/recipe/<recipe_name>", methods=["GET", "POST"])
def recipe_detail(recipe_name):
    recipe_name = recipe_name.replace("%20", " ")

    if recipe_name not in recipes:
        return "Recipe not found", 404

    # Handle new rating submission
    if request.method == "POST":
        rating = request.form.get("rating")
        if rating:
            try:
                with open("ratings.csv", mode="a", newline="", encoding="utf-8") as file:
                    writer = csv.writer(file)
                    writer.writerow([recipe_name, rating])
            except Exception as e:
                print(f"Error saving rating: {e}")

    # Calculate average rating
    ratings = []
    try:
        with open("ratings.csv", newline='', encoding="utf-8") as file:
            reader = csv.reader(file)
            next(reader, None)  # skip header if present
            for row in reader:
                if row[0] == recipe_name:
                    ratings.append(int(row[1]))
    except FileNotFoundError:
        pass
    except Exception as e:
        print(f"Error loading ratings: {e}")

    average_rating = round(sum(ratings) / len(ratings), 2) if ratings else None

    recipe = recipes[recipe_name]
    return render_template("detail.html", name=recipe_name, recipe=recipe, average_rating=average_rating)

@app.route("/suggest", methods=["GET", "POST"])
def suggest_recipe():
    if request.method == "POST":
        name = request.form["name"]
        suggestion = request.form["suggestion"]
        with open("suggestions.csv", mode="a", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow([name, suggestion])
        return render_template("thankyou.html", name=name)
    return render_template("suggest.html")

@app.route("/submissions")
def view_suggestions():
    suggestions = []
    try:
        with open("suggestions.csv", newline='', encoding="utf-8") as file:
            reader = csv.reader(file)
            for row in reader:
                if len(row) == 2:
                    suggestions.append({"name": row[0], "suggestion": row[1]})
    except FileNotFoundError:
        suggestions = []

    return render_template("submissions.html", suggestions=suggestions)

if __name__ == "__main__":
    print("Flask is launching...")
    app.run(debug=True, port=5001)
