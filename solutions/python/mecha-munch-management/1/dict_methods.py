def add_item(current_cart, items_to_add):
    """Add items to shopping cart."""
    for item in items_to_add:
        current_cart[item] = current_cart.get(item, 0) + 1

    return current_cart


def read_notes(notes):
    """Create user cart from an iterable notes entry."""
    return {item: 1 for item in notes}


def update_recipes(ideas, recipe_updates):
    """Update the recipe ideas dictionary."""
    for recipe, ingredients in recipe_updates:
        ideas[recipe] = ingredients

    return ideas


def sort_entries(cart):
    """Sort a user's shopping cart in alphabetical order."""
    return dict(sorted(cart.items()))


def send_to_store(cart, aisle_mapping):
    """Combine user's order to aisle and refrigeration information."""
    fulfillment_cart = {}

    for item in sorted(cart, reverse=True):
        quantity = cart[item]
        aisle, refrigerated = aisle_mapping[item]
        fulfillment_cart[item] = [quantity, aisle, refrigerated]

    return fulfillment_cart


def update_store_inventory(fulfillment_cart, store_inventory):
    """Update store inventory levels with user order."""
    for item, details in fulfillment_cart.items():
        quantity = details[0]

        store_inventory[item][0] -= quantity

        if store_inventory[item][0] == 0:
            store_inventory[item][0] = "Out of Stock"

    return store_inventory