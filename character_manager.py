"""
COMP 163 - Project 3: Quest Chronicles
Character Manager Module - Starter Code

Name: [Shikel Percell]

AI Usage: [Used AI for formatting, debugging, and understanding the code itself]

This module handles character creation, loading, and saving.
"""

import os
from custom_exceptions import (
    InvalidCharacterClassError,
    CharacterNotFoundError,
    SaveFileCorruptedError,
    InvalidSaveDataError,
    CharacterDeadError
)

# ============================================================================
# CHARACTER MANAGEMENT FUNCTIONS
# ============================================================================

def create_character(name, character_class):
    """
    Create a new character with stats based on class
    
    Valid classes: Warrior, Mage, Rogue, Cleric
    
    Returns: Dictionary with character data including:
            - name, class, level, health, max_health, strength, magic
            - experience, gold, inventory, active_quests, completed_quests
    
    Raises: InvalidCharacterClassError if class is not valid
    """
    # TODO: Implement character creation
    # Validate character_class first
    # Example base stats:
    # Warrior: health=120, strength=15, magic=5
    # Mage: health=80, strength=8, magic=20
    # Rogue: health=90, strength=12, magic=10
    # Cleric: health=100, strength=10, magic=15
    
    # All characters start with:
    # - level=1, experience=0, gold=100
    # - inventory=[], active_quests=[], completed_quests=[]
    
    # Raise InvalidCharacterClassError if class not in valid list
    # Valid class list
    valid_classes = ["Warrior", "Mage", "Rogue", "Cleric"]
    
    # Validate class
    if character_class not in valid_classes:
        raise InvalidCharacterClassError(f"Invalid class: {character_class}")
    
    # Base stats per class
    class_stats = {
        "Warrior": {"health": 120, "strength": 15, "magic": 5},
        "Mage":    {"health": 80,  "strength": 8,  "magic": 20},
        "Rogue":   {"health": 90,  "strength": 12, "magic": 10},
        "Cleric":  {"health": 100, "strength": 10, "magic": 15}
    }
    
    stats = class_stats[character_class]

    # Create character dictionary
    character = {
        "name": name,
        "class": character_class,
        "level": 1,
        "experience": 0,
        "gold": 100,
        
        # Stats
        "health": stats["health"],
        "max_health": stats["health"],
        "strength": stats["strength"],
        "magic": stats["magic"],
        
        # Collections
        "inventory": [],
        "active_quests": [],
        "completed_quests": []
    }
    
    return character
    
    pass

def save_character(character, save_directory="data/save_games"):
    """
    Save character to file
    
    Filename format: {character_name}_save.txt
    
    File format:
    NAME: character_name
    CLASS: class_name
    LEVEL: 1
    HEALTH: 120
    MAX_HEALTH: 120
    STRENGTH: 15
    MAGIC: 5
    EXPERIENCE: 0
    GOLD: 100
    INVENTORY: item1,item2,item3
    ACTIVE_QUESTS: quest1,quest2
    COMPLETED_QUESTS: quest1,quest2
    
    Returns: True if successful
    Raises: PermissionError, IOError (let them propagate or handle)
    """
    # TODO: Implement save functionality
    # Create save_directory if it doesn't exist
    # Handle any file I/O errors appropriately
    # Lists should be saved as comma-separated values
    # Ensure directory exists
     # Build file path
    # Ensure directory exists
    os.makedirs(save_directory, exist_ok=True)
    filename = f"{character['name']}_save.txt"
    filepath = os.path.join(save_directory, filename)
    
    # Convert lists → comma-separated strings
    inventory_str = ",".join(character.get("inventory", []))
    active_q_str = ",".join(character.get("active_quests", []))
    completed_q_str = ",".join(character.get("completed_quests", []))
    
    # Build text content
    save_text = (
        f"NAME: {character['name']}\n"
        f"CLASS: {character['class']}\n"
        f"LEVEL: {character['level']}\n"
        f"HEALTH: {character['health']}\n"
        f"MAX_HEALTH: {character['max_health']}\n"
        f"STRENGTH: {character['strength']}\n"
        f"MAGIC: {character['magic']}\n"
        f"EXPERIENCE: {character['experience']}\n"
        f"GOLD: {character['gold']}\n"
        f"INVENTORY: {inventory_str}\n"
        f"ACTIVE_QUESTS: {active_q_str}\n"
        f"COMPLETED_QUESTS: {completed_q_str}\n"
    )
    
    # Write to file
    with open(filepath, "w", encoding="utf-8") as save_file:
        save_file.write(save_text)
    
    return True
    pass

def load_character(character_name, save_directory="data/save_games"):
    """
    Load character from save file
    Args:
        character_name: Name of character to load # Build file path
        save_directory: Directory containing save files
    
    Returns: Character dictionary
    Raises: 
        CharacterNotFoundError if save file doesn't exist
        SaveFileCorruptedError if file exists but can't be read
        InvalidSaveDataError if data format is wrong
    """
    # TODO: Implement load functionality
    # Check if file exists → CharacterNotFoundError
    # Try to read file → SaveFileCorruptedError
    # Validate data format → InvalidSaveDataError
    # Parse comma-separated lists back into Python lists
    
    filepath = os.path.join(save_directory, f"{character_name}_save.txt")

    # --- Check if save file exists ---
    if not os.path.isfile(filepath):
        raise CharacterNotFoundError(f"No save file found for '{character_name}'.")

    try:
        with open(filepath, "r", encoding="utf-8") as f:
            lines = f.readlines()
    except Exception as e:
        raise SaveFileCorruptedError(f"Could not read save file: {e}")

    # --- Parse file ---
    character = {}

    expected_fields = {
        "NAME", "CLASS", "LEVEL", "HEALTH", "MAX_HEALTH",
        "STRENGTH", "MAGIC", "EXPERIENCE", "GOLD",
        "INVENTORY", "ACTIVE_QUESTS", "COMPLETED_QUESTS"
    }

    for line in lines:
        if ":" not in line:
            raise InvalidSaveDataError("Malformed line in save file.")

        key, value = line.strip().split(":", 1)
        key = key.strip().upper()
        value = value.strip()

        # Validate field name
        if key not in expected_fields:
            raise InvalidSaveDataError(f"Unexpected field: {key}")

        # Convert numerical fields
        if key in {"LEVEL", "HEALTH", "MAX_HEALTH", "STRENGTH", "MAGIC", "EXPERIENCE", "GOLD"}:
            if not value.isdigit():
                raise InvalidSaveDataError(f"Invalid value for {key}: {value}")
            character[key.lower()] = int(value)

        # Convert list fields
        elif key in {"INVENTORY", "ACTIVE_QUESTS", "COMPLETED_QUESTS"}:
            if value == "":
                character[key.lower()] = []
            else:
                character[key.lower()] = value.split(",")

        # Normal string fields
        else:
            character[key.lower()] = value

    # --- Final validation ---
    missing = expected_fields - {k.upper() for k in character.keys()}
    if missing:
        raise InvalidSaveDataError(f"Missing fields: {missing}")
    return character
    pass

def list_saved_characters(save_directory="data/save_games"):
    """
    Get list of all saved character names
    
    Returns: List of character names (without _save.txt extension)
    """
    # TODO: Implement this function
    # Return empty list if directory doesn't exist
    # Extract character names from filenames
    
    if not os.path.isdir(save_directory):
        return []

    characters = []

    for filename in os.listdir(save_directory):
        if filename.endswith("_save.txt"):
            characters.append(filename.replace("_save.txt", ""))

    return characters
    pass

def delete_character(character_name, save_directory="data/save_games"):
    """
    Delete a character's save file
    
    Returns: True if deleted successfully
    Raises: CharacterNotFoundError if character doesn't exist
    """
    # TODO: Implement character deletion
    # Verify file exists before attempting deletion
    filepath = os.path.join(save_directory, f"{character_name}_save.txt")

    # Check if save exists
    if not os.path.isfile(filepath):
        raise CharacterNotFoundError(f"No save file found for '{character_name}'.")

    # Delete file
    os.remove(filepath)
    return True
    pass

# ============================================================================
# CHARACTER OPERATIONS
# ============================================================================

def gain_experience(character, xp_amount):
    """
    Add experience to character and handle level ups
    
    Level up formula: level_up_xp = current_level * 100
    Example when leveling up:
    - Increase level by 1
    - Increase max_health by 10
    - Increase strength by 2
    - Increase magic by 2
    - Restore health to max_health
    
    Raises: CharacterDeadError if character health is 0
    """
    # TODO: Implement experience gain and leveling
    # Check if character is dead first
    # Add experience
    # Check for level up (can level up multiple times)
    # Update stats on level up
     # Cannot gain XP if dead
    
    if character["health"] <= 0:
        raise CharacterDeadError("Character is dead and cannot gain experience.")

    # Add XP
    character["experience"] += xp_amount
    print(f"\n+{xp_amount} XP gained!")

    # Check for level-ups (may happen multiple times)
    leveled_up = False

    while character["experience"] >= character["level"] * 100:
        character["experience"] -= character["level"] * 100
        character["level"] += 1
        leveled_up = True

        # Stat increases
        character["max_health"] += 10
        character["strength"] += 2
        character["magic"] += 2

        # Heal to full on level up
        character["health"] = character["max_health"]

        print(f"\n🎉 LEVEL UP! You are now level {character['level']}!")
        print(f"+10 Max Health, +2 Strength, +2 Magic")

    return leveled_up
    pass

def add_gold(character, amount):
    """
    Add gold to character's inventory
    
    Args:
        character: Character dictionary
        amount: Amount of gold to add (can be negative for spending)
    
    Returns: New gold total
    Raises: ValueError if result would be negative
    """
    # TODO: Implement gold management
    # Check that result won't be negative
    # Update character's gold
      # Ensure character has a gold field
    
    if "gold" not in character:
        raise KeyError("Character dictionary must contain a 'gold' field.")

    new_gold = character["gold"] + amount

    # Prevent negative gold
    if new_gold < 0:
        raise ValueError(
            f"Cannot remove {abs(amount)} gold — result would be negative."
        )

    # Update gold
    character["gold"] = new_gold
    return new_gold
    pass

def heal_character(character, amount):
    """
    Heal character by specified amount
    
    Health cannot exceed max_health
    
    Returns: Actual amount healed
    """
    # TODO: Implement healing
    # Calculate actual healing (don't exceed max_health)
    # Update character health
    
    if amount < 0:
        raise ValueError("Healing amount cannot be negative.")

    current_hp = character.get("health")
    max_hp = character.get("max_health")

    if current_hp is None or max_hp is None:
        raise KeyError("Character must have 'health' and 'max_health' fields.")

    # Calculate heal without exceeding max health
    heal_amount = min(amount, max_hp - current_hp)

    # Apply healing
    character["health"] = current_hp + heal_amount

    return heal_amount
    pass

def is_character_dead(character):
    """
    Check if character's health is 0 or below
    
    Returns: True if dead, False if alive
    """
    # TODO: Implement death check
    
    if "health" not in character:
        raise KeyError("Character dictionary must contain a 'health' field.")
    
    return character["health"] <= 0
    pass

def revive_character(character):
    """
    Revive a dead character with 50% health
    
    Returns: True if revived
    """
    # TODO: Implement revival
    # Restore health to half of max_health
    
    if "health" not in character or "max_health" not in character:
        raise KeyError("Character must have 'health' and 'max_health' fields.")

    # Only revive if dead
    if character["health"] > 0:
        return False  # Already alive

    # Restore to 50% of max health (rounded down)
    character["health"] = max(1, character["max_health"] // 2)

    return True
    pass

# ============================================================================
# VALIDATION
# ============================================================================

def validate_character_data(character):
    """
    Validate that character dictionary has all required fields
    
    Required fields: name, class, level, health, max_health, 
                    strength, magic, experience, gold, inventory,
                    active_quests, completed_quests
    
    Returns: True if valid
    Raises: InvalidSaveDataError if missing fields or invalid types
    """
    # TODO: Implement validation
    # Check all required keys exist
    # Check that numeric values are numbers
    # Check that lists are actually lists
    
    required_fields = {
        "name": str,
        "class": str,
        "level": int,
        "health": int,
        "max_health": int,
        "strength": int,
        "magic": int,
        "experience": int,
        "gold": int,
        "inventory": list,
        "active_quests": list,
        "completed_quests": list,
    }
    # --- Check required fields exist ---
    for field, expected_type in required_fields.items():
        if field not in character:
            raise InvalidSaveDataError(f"Missing required field: {field}")

        value = character[field]

        # --- Type validation ---
        if not isinstance(value, expected_type):
            raise InvalidSaveDataError(
                f"Invalid type for '{field}': expected {expected_type.__name__}, "
                f"got {type(value).__name__}"
            )

    return True
    pass

# ============================================================================
# TESTING
# ============================================================================

if __name__ == "__main__":
    print("=== CHARACTER MANAGER TEST ===")
    
    # Test character creation
    # try:
    #     char = create_character("TestHero", "Warrior")
    #     print(f"Created: {char['name']} the {char['class']}")
    #     print(f"Stats: HP={char['health']}, STR={char['strength']}, MAG={char['magic']}")
    # except InvalidCharacterClassError as e:
    #     print(f"Invalid class: {e}")
    
    # Test saving
    # try:
    #     save_character(char)
    #     print("Character saved successfully")
    # except Exception as e:
    #     print(f"Save error: {e}")
    
    # Test loading
    # try:
    #     loaded = load_character("TestHero")
    #     print(f"Loaded: {loaded['name']}")
    # except CharacterNotFoundError:
    #     print("Character not found")
    # except SaveFileCorruptedError:
    #     print("Save file corrupted")
if __name__ == "__main__":
    print("=== CHARACTER MANAGER TEST ===")
    print("\n[TEST] Creating character...")
    try:
        char = create_character("LeGoat", "Warrior")
        print(f"Created: {char['name']} the {char['class']}")
        print(f"Stats: HP={char['health']}, STR={char['strength']}, MAG={char['magic']}")
    except InvalidCharacterClassError as e:
        print(f"Character creation failed: {e}")
        char = None

    # If creation failed, do not proceed
    if char is not None:

        # Test saving the character
        print("\n[TEST] Saving character...")
        try:
            save_character(char)
            print("Character saved successfully.")
        except Exception as e:
            print(f"Save error: {e}")

        # Test loading the character
        print("\n[TEST] Loading character...")
        try:
            loaded = load_character("TestHero")
            print(f"Loaded: {loaded['name']} the {loaded['class']}")
            print(f"Loaded Stats: HP={loaded['health']}, STR={loaded['strength']}, MAG={loaded['magic']}")
        except CharacterNotFoundError:
            print("Character not found.")
        except SaveFileCorruptedError:
            print("Save file corrupted.")
        except InvalidSaveDataError as e:
            print(f"Invalid save data: {e}")

    print("\n=== TEST COMPLETE, Phenomenal ===")

