"""
COMP 163 - Project 3: Quest Chronicles
Inventory System Module - Starter Code

Name: [Your Name Here]

AI Usage: [Document any AI assistance used]

This module handles inventory management, item usage, and equipment.
"""

from custom_exceptions import (
    InventoryFullError,
    ItemNotFoundError,
    InsufficientResourcesError,
    InvalidItemTypeError
)

# Maximum inventory size
MAX_INVENTORY_SIZE = 20

# ============================================================================
# INVENTORY MANAGEMENT
# ============================================================================

def add_item_to_inventory(character, item_id):
    """
    Add an item to character's inventory
    
    Args:
        character: Character dictionary
        item_id: Unique item identifier
    
    Returns: True if added successfully
    Raises: InventoryFullError if inventory is at max capacity
    """
    # TODO: Implement adding items
    # Check if inventory is full (>= MAX_INVENTORY_SIZE)
    # Add item_id to character['inventory'] list
     # Validate inventory field exists
    
    if "inventory" not in character:
        raise KeyError("Character dictionary must contain an 'inventory' field.")

    inventory = character["inventory"]

    # Check inventory capacity
    if len(inventory) >= MAX_INVENTORY_SIZE:
        raise InventoryFullError(
            f"Cannot add item '{item_id}' — inventory is full "
            f"({MAX_INVENTORY_SIZE} items max)."
        )

    # Add the item
    inventory.append(item_id)
    return True
    pass

def remove_item_from_inventory(character, item_id):
    """
    Remove an item from character's inventory
    
    Args:
        character: Character dictionary
        item_id: Item to remove
    
    Returns: True if removed successfully
    Raises: ItemNotFoundError if item not in inventory
    """
    # TODO: Implement item removal
    # Check if item exists in inventory
    # Remove item from list
     # Ensure inventory exists
    
    if "inventory" not in character:
        raise KeyError("Character dictionary must contain an 'inventory' field.")

    inventory = character["inventory"]

    # Check for item
    if item_id not in inventory:
        raise ItemNotFoundError(f"Item '{item_id}' not found in inventory.")

    # Remove the item
    inventory.remove(item_id)
    return True
    pass

def has_item(character, item_id):
    """
    Check if character has a specific item
    
    Returns: True if item in inventory, False otherwise
    """
    # TODO: Implement item check
    
    if "inventory" not in character:
        raise KeyError("Character dictionary must contain an 'inventory' field.")

    return item_id in character["inventory"]
    pass

def count_item(character, item_id):
    """
    Count how many of a specific item the character has
    
    Returns: Integer count of item
    """
    # TODO: Implement item counting
    # Use list.count() method
     
    if "inventory" not in character:
        raise KeyError("Character dictionary must contain an 'inventory' field.")
    return character["inventory"].count(item_id)
    pass

def get_inventory_space_remaining(character):
    """
    Calculate how many more items can fit in inventory
    
    Returns: Integer representing available slots
    """
    # TODO: Implement space calculation
    if "inventory" not in character:
        raise KeyError("Character dictionary must contain an 'inventory' field.")

    return MAX_INVENTORY_SIZE - len(character["inventory"])
    pass

def clear_inventory(character):
    """
    Remove all items from inventory
    
    Returns: List of removed items
    """
    # TODO: Implement inventory clearing
    # Save current inventory before clearing
    # Clear character's inventory list
    # Save current inventory before clearing
    removed_items = character.get("inventory", []).copy()
    
    # Clear character's inventory list
    character["inventory"] = []
    
    return removed_items
    pass

# ============================================================================
# ITEM USAGE
# ============================================================================

def use_item(character, item_id, item_data):
    """
    Use a consumable item from inventory
    
    Args:
        character: Character dictionary
        item_id: Item to use
        item_data: Item information dictionary from game_data
    
    Item types and effects:
    - consumable: Apply effect and remove from inventory
    - weapon/armor: Cannot be "used", only equipped
    
    Returns: String describing what happened
    Raises: 
        ItemNotFoundError if item not in inventory
        InvalidItemTypeError if item type is not 'consumable'
    """
    # TODO: Implement item usage
    # Check if character has the item
    # Check if item type is 'consumable'
    # Parse effect (format: "stat_name:value" e.g., "health:20")
    # Apply effect to character
    # Remove item from inventory
    
    # Check if character has the item
    if item_id not in character.get("inventory", []):
        raise ItemNotFoundError(f"Item '{item_id}' not found in inventory.")

    # Check if item type is 'consumable'
    item_type = item_data.get("type")
    if item_type != "consumable":
        raise InvalidItemTypeError(f"Item '{item_id}' is not a consumable item.")

    # Parse effect string (format: "stat:value")
    effect_str = item_data.get("effect", "")
    if ":" not in effect_str:
        raise InvalidItemTypeError(f"Invalid effect format for item '{item_id}'.")

    stat_name, value_str = effect_str.split(":")
    value = int(value_str)

    # Apply effect to character
    # Assumes character[stat_name] exists
    character[stat_name] = character.get(stat_name, 0) + value

    # Remove item from inventory
    character["inventory"].remove(item_id)

    return (f"{character.get('name', 'Character')} used {item_id} and gained {value} {stat_name}.")
    pass

def equip_weapon(character, item_id, item_data):
    """
    Equip a weapon
    
    Args:
        character: Character dictionary
        item_id: Weapon to equip
        item_data: Item information dictionary
    
    Weapon effect format: "strength:5" (adds 5 to strength)
    
    If character already has weapon equipped:
    - Unequip current weapon (remove bonus)
    - Add old weapon back to inventory
    
    Returns: String describing equipment change
    Raises:
        ItemNotFoundError if item not in inventory
        InvalidItemTypeError if item type is not 'weapon'
    """
    # TODO: Implement weapon equipping
    # Check item exists and is type 'weapon'
    # Handle unequipping current weapon if exists
    # Parse effect and apply to character stats
    # Store equipped_weapon in character dictionary
    # Remove item from inventory
    
    # Check item exists in inventory
    if item_id not in character.get("inventory", []):
        raise ItemNotFoundError(f"Weapon '{item_id}' not found in inventory.")

    # Check correct item type
    item_type = item_data[item_id].get("type")
    if item_type != "weapon":
        raise InvalidItemTypeError(f"Item '{item_id}' is not a weapon.")

    # Handle unequipping current weapon
    old_weapon = character.get("equipped_weapon")
    message_parts = []

    if old_weapon:
        # Parse old weapon effect and remove it
        old_effect = item_data[old_weapon].get("effect", "")
        if ":" in old_effect:
            stat, value_str = old_effect.split(":")
            character[stat] -= int(value_str)

        # Add old weapon back to inventory
        character["inventory"].append(old_weapon)
        message_parts.append(f"Unequipped {old_weapon}")

    # Parse new weapon effect
    effect = item_data.get("effect", "")
    if ":" not in effect:
        raise InvalidItemTypeError(f"Invalid effect format for weapon '{item_id}'.")

    stat, value_str = effect.split(":")
    value = int(value_str)

    # Apply new weapon stat bonus
    character[stat] = character.get(stat, 0) + value

    # Equip weapon
    character["equipped_weapon"] = item_id

    # Remove weapon from inventory
    character["inventory"].remove(item_id)

    message_parts.append(f"Equipped {item_id} (+{value} {stat})")

    return "; ".join(message_parts) + "."
    pass

def equip_armor(character, item_id, item_data):
    """
    Equip armor
    
    Args:
        character: Character dictionary
        item_id: Armor to equip
        item_data: Item information dictionary
    
    Armor effect format: "max_health:10" (adds 10 to max_health)
    
    If character already has armor equipped:
    - Unequip current armor (remove bonus)
    - Add old armor back to inventory
    
    Returns: String describing equipment change
    Raises:
        ItemNotFoundError if item not in inventory
        InvalidItemTypeError if item type is not 'armor'
    """
    # TODO: Implement armor equipping
    # Similar to equip_weapon but for armor
    
    # Check item exists in inventory
    if item_id not in character.get("inventory", []):
        raise ItemNotFoundError(f"Weapon '{item_id}' not found in inventory.")

    # Check correct item type
    item_type = item_data[item_id].get("type")
    if item_type != "armor":
        raise InvalidItemTypeError(f"Item '{item_id}' is not armor.")

    # Handle unequipping current weapon
    old_weapon = character.get("equipped_armor")
    message_parts = []

    if old_weapon:
        # Parse old weapon effect and remove it
        old_effect = item_data[old_weapon].get("effect", "")
        if ":" in old_effect:
            stat, value_str = old_effect.split(":")
            character[stat] -= int(value_str)

        # Add old weapon back to inventory
        character["inventory"].append(old_weapon)
        message_parts.append(f"Unequipped {old_weapon}")

    # Parse new weapon effect
    effect = item_data.get("effect", "")
    if ":" not in effect:
        raise InvalidItemTypeError(f"Invalid effect format for weapon '{item_id}'.")

    stat, value_str = effect.split(":")
    value = int(value_str)

    # Apply new weapon stat bonus
    character[stat] = character.get(stat, 0) + value

    # Equip weapon
    character["equipped_weapon"] = item_id

    # Remove weapon from inventory
    character["inventory"].remove(item_id)

    message_parts.append(f"Equipped {item_id} (+{value} {stat})")

    return "; ".join(message_parts) + "."
    pass

def unequip_weapon(character):
    """
    Remove equipped weapon and return it to inventory
    
    Returns: Item ID that was unequipped, or None if no weapon equipped
    Raises: InventoryFullError if inventory is full
    """
    # TODO: Implement weapon unequipping
    # Check if weapon is equipped
    # Remove stat bonuses
    # Add weapon back to inventory
    # Clear equipped_weapon from character
    
    equipped = character.get("equipped_weapon")

    # No weapon equipped
    if not equipped:
        return None

    # Check inventory capacity
    if len(character["inventory"]) >= MAX_INVENTORY_SIZE:
        raise InventoryFullError("Inventory is full, cannot unequip weapon.")

    # Remove stat bonuses
    effect = character["item_data"][equipped].get("effect", "")
    if ":" in effect:
        stat, value_str = effect.split(":")
        character[stat] -= int(value_str)

    # Return weapon to inventory
    character["inventory"].append(equipped)

    # Clear equipped weapon
    character["equipped_weapon"] = None

    return equipped
    pass

def unequip_armor(character):
    """
    Remove equipped armor and return it to inventory
    
    Returns: Item ID that was unequipped, or None if no armor equipped
    Raises: InventoryFullError if inventory is full
    """
    # TODO: Implement armor unequipping
    equipped = character.get("equipped_armor")

    # No armor equipped
    if not equipped:
        return None

    # Check inventory capacity
    if len(character["inventory"]) >= MAX_INVENTORY_SIZE:
        raise InventoryFullError("Inventory is full, cannot unequip armor.")

    # Remove stat bonuses
    effect = character["item_data"][equipped].get("effect", "")
    if ":" in effect:
        stat, value_str = effect.split(":")
        character[stat] -= int(value_str)

    # Return armor to inventory
    character["inventory"].append(equipped)

    # Clear equipped armor
    character["equipped_armor"] = None

    return equipped
    pass

# ============================================================================
# SHOP SYSTEM
# ============================================================================

def purchase_item(character, item_id, item_data):
    """
    Purchase an item from a shop
    
    Args:
        character: Character dictionary
        item_id: Item to purchase
        item_data: Item information with 'cost' field
    
    Returns: True if purchased successfully
    Raises:
        InsufficientResourcesError if not enough gold
        InventoryFullError if inventory is full
    """
    # TODO: Implement purchasing
    # Check if character has enough gold
    # Check if inventory has space
    # Subtract gold from character
    # Add item to inventory
    cost = item_data.get("cost")

    # Check for enough gold
    if character["gold"] < cost:
        raise InsufficientResourcesError(
            f"Not enough gold to purchase {item_id} (cost: {cost})"
        )

    # Check inventory space
    if len(character["inventory"]) >= MAX_INVENTORY_SIZE:
        raise InventoryFullError("Inventory is full, cannot purchase item.")

    # Subtract gold
    character["gold"] -= cost

    # Add item to inventory
    character["inventory"].append(item_id)

    return True
    pass

def sell_item(character, item_id, item_data):
    """
    Sell an item for half its purchase cost
    
    Args:
        character: Character dictionary
        item_id: Item to sell
        item_data: Item information with 'cost' field
    
    Returns: Amount of gold received
    Raises: ItemNotFoundError if item not in inventory
    """
    # TODO: Implement selling
    # Check if character has item
    # Calculate sell price (cost // 2)
    # Remove item from inventory
    # Add gold to character
    # Check if character has the item
    if item_id not in character.get("inventory", []):
        raise ItemNotFoundError(f"Item '{item_id}' not found in inventory.")

    # Calculate sell price (half of original cost)
    cost = item_data.get(item_id, {}).get("cost", 0)
    sell_price = cost // 2

    # Remove item from inventory
    character["inventory"].remove(item_id)

    # Add gold to character
    character["gold"] += sell_price

    return sell_price
    pass

# ============================================================================
# HELPER FUNCTIONS
# ============================================================================

def parse_item_effect(effect_string):
    """
    Parse item effect string into stat name and value
    
    Args:
        effect_string: String in format "stat_name:value"
    
    Returns: Tuple of (stat_name, value)
    Example: "health:20" → ("health", 20)
    """
    # TODO: Implement effect parsing
    # Split on ":"
    # Convert value to integer
    if ":" not in effect_string:
        raise ValueError(f"Invalid effect format: '{effect_string}' (missing ':')")

    stat_name, value_str = effect_string.split(":", 1)

    try:
        value = int(value_str)
    except ValueError:
        raise ValueError(f"Invalid effect value: '{value_str}' is not an integer")

    return stat_name, value
    pass

def apply_stat_effect(character, stat_name, value):
    """
    Apply a stat modification to character
    
    Valid stats: health, max_health, strength, magic
    
    Note: health cannot exceed max_health
    """
    # TODO: Implement stat application
    # Add value to character[stat_name]
    # If stat is health, ensure it doesn't exceed max_health
    valid_stats = {"health", "max_health", "strength", "magic"}

    if stat_name not in valid_stats:
        raise ValueError(f"Invalid stat: '{stat_name}'")

    # Initialize stat if missing
    character[stat_name] = character.get(stat_name, 0) + value

    # Ensure health does not exceed max_health
    if stat_name == "health":
        max_hp = character.get("max_health", character["health"])
        if character["health"] > max_hp:
            character["health"] = max_hp
    pass

def display_inventory(character, item_data_dict):
    """
    Display character's inventory in formatted way
    
    Args:
        character: Character dictionary
        item_data_dict: Dictionary of all item data
    
    Shows item names, types, and quantities
    """
    # TODO: Implement inventory display
    # Count items (some may appear multiple times)
    # Display with item names from item_data_dict
    from collections import Counter

    inventory = character.get("inventory", [])

    if not inventory:
        print(f"{character['name']}'s inventory is empty.")
        return

    # Count each item
    item_counts = Counter(inventory)

    print(f"\n{character['name']}'s Inventory:")
    print("-" * 40)
    print(f"{'Item':<20} {'Type':<12} {'Qty':<4}")
    print("-" * 40)

    for item_id, qty in item_counts.items():
        item_info = item_data_dict.get(item_id, {})
        item_type = item_info.get("type", "Unknown")
        item_name = item_info.get("name", item_id)
        print(f"{item_name:<20} {item_type:<12} {qty:<4}")

    print("-" * 40)
    pass

# ============================================================================
# TESTING
# ============================================================================

if __name__ == "__main__":
    print("=== INVENTORY SYSTEM TEST ===")
    
    # Test adding items
    # test_char = {'inventory': [], 'gold': 100, 'health': 80, 'max_health': 80}
    # 
    # try:
    #     add_item_to_inventory(test_char, "health_potion")
    #     print(f"Inventory: {test_char['inventory']}")
    # except InventoryFullError:
    #     print("Inventory is full!")
    
    # Test using items
    # test_item = {
    #     'item_id': 'health_potion',
    #     'type': 'consumable',
    #     'effect': 'health:20'
    # }
    # 
    # try:
    #     result = use_item(test_char, "health_potion", test_item)
    #     print(result)
    # except ItemNotFoundError:
    #     print("Item not found")

