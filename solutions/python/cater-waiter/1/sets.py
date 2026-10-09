"""Functions for compiling dishes and ingredients for a catering company."""


from sets_categories_data import (VEGAN,
                                  VEGETARIAN,
                                  KETO,
                                  PALEO,
                                  OMNIVORE,
                                  ALCOHOLS,
                                  SPECIAL_INGREDIENTS)


def clean_ingredients(dish_name, dish_ingredients):
    """Remove duplicates from dish_ingredients."""
    return dish_name, set(dish_ingredients)


def check_drinks(drink_name, drink_ingredients):
    """Append Mocktail or Cocktail to drink_name."""
    if set(drink_ingredients) & ALCOHOLS:
        return f"{drink_name} Cocktail"

    return f"{drink_name} Mocktail"


def categorize_dish(dish_name, dish_ingredients):
    """Categorize dish based on its ingredients."""
    if dish_ingredients <= VEGAN:
        category = "VEGAN"
    elif dish_ingredients <= VEGETARIAN:
        category = "VEGETARIAN"
    elif dish_ingredients <= PALEO:
        category = "PALEO"
    elif dish_ingredients <= KETO:
        category = "KETO"
    else:
        category = "OMNIVORE"

    return f"{dish_name}: {category}"


def tag_special_ingredients(dish):
    """Return dish name and its special ingredients."""
    dish_name, ingredients = dish

    special = set(ingredients) & SPECIAL_INGREDIENTS

    return dish_name, special


def compile_ingredients(dishes):
    """Create a master set of all ingredients."""
    ingredients = set()

    for dish in dishes:
        ingredients.update(dish)

    return ingredients


def separate_appetizers(dishes, appetizers):
    """Remove appetizer names from dishes."""
    return list(set(dishes) - set(appetizers))


def singleton_ingredients(dishes, intersection):
    """Find ingredients that appear in only one dish."""
    all_ingredients = set.union(*dishes)

    for ingredient in intersection:
        all_ingredients.discard(ingredient)

    return all_ingredients