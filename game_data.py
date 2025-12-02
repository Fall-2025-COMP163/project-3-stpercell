"""
COMP 163 - Project 3: Quest Chronicles
Game Data Module - Starter Code

Name: [Your Name Here]

AI Usage: [Document any AI assistance used]

This module handles loading and validating game data from text files.
"""

import os
from custom_exceptions import (
    InvalidDataFormatError,
    MissingDataFileError,
    CorruptedDataError
)

# ============================================================================
# DATA LOADING FUNCTIONS
# ============================================================================

def load_quests(filename="data/quests.txt"):
    """
    Load quest data from file
    
    Expected format per quest (separated by blank lines):
    QUEST_ID: unique_quest_name
    TITLE: Quest Display Title
    DESCRIPTION: Quest description text
    REWARD_XP: 100
    REWARD_GOLD: 50
    REQUIRED_LEVEL: 1
    PREREQUISITE: previous_quest_id (or NONE)
    
    Returns: Dictionary of quests {quest_id: quest_data_dict}
    Raises: MissingDataFileError, InvalidDataFormatError, CorruptedDataError
    """
    # TODO: Implement this function
    # Must handle:
    # - FileNotFoundError → raise MissingDataFileError
    # - Invalid format → raise InvalidDataFormatError
    # - Corrupted/unreadable data → raise CorruptedDataError
    quests = {}
    try:
        with open(filename, "r") as f:
            content = f.read().strip()
            blocks = content.split("\n\n")  # assume quests are separated by blank lines
            for block in blocks:
                quest = {}
                for line in block.splitlines():
                    if ":" in line:
                        key, val = line.split(":", 1)
                        quest[key.strip()] = val.strip()
                if "quest_id" in quest:
                    quests[quest["quest_id"]] = quest
    except FileNotFoundError:
        print(f"Quest file '{filename}' not found.")
    return quests
    pass

def load_items(filename="data/items.txt"):
    """
    Load item data from file
    
    Expected format per item (separated by blank lines):
    ITEM_ID: unique_item_name
    NAME: Item Display Name
    TYPE: weapon|armor|consumable
    EFFECT: stat_name:value (e.g., strength:5 or health:20)
    COST: 100
    DESCRIPTION: Item description
    
    Returns: Dictionary of items {item_id: item_data_dict}
    Raises: MissingDataFileError, InvalidDataFormatError, CorruptedDataError
    """
    # TODO: Implement this function
    # Must handle same exceptions as load_quests
    try:
        if not os.path.exists(filename):
            raise MissingDataFileError(f"Item data file not found: {filename}")

        with open(filename, "r") as f:
            content = f.read().strip()

        if not content:
            raise InvalidDataFormatError("Item file is empty or invalid.")

        if ":" not in content:
            raise InvalidDataFormatError("Item file format not recognized.")

        # FULL parsing not implemented yet—return empty dict for now
        return {}

    except MissingDataFileError:
        raise
    except InvalidDataFormatError:
        raise
    except Exception as e:
        raise CorruptedDataError(f"Unexpected error reading items: {e}")
    pass

def validate_quest_data(quest_dict):
    """
    Validate that quest dictionary has all required fields
    
    Required fields: quest_id, title, description, reward_xp, 
                    reward_gold, required_level, prerequisite
    
    Returns: True if valid
    Raises: InvalidDataFormatError if missing required fields
    """
    # TODO: Implement validation
    # Check that all required keys exist
    # Check that numeric values are actually numbers
    required = [
        "quest_id",
        "title",
        "description",
        "reward_xp",
        "reward_gold",
        "required_level",
        "prerequisite"
    ]

    for field in required:
        if field not in quest_dict:
            raise InvalidDataFormatError(f"Missing field in quest: {field}")

    # Check numeric fields
    numeric_fields = ["reward_xp", "reward_gold", "required_level"]

    for field in numeric_fields:
        value = quest_dict[field]
        if not isinstance(value, int):
            raise InvalidDataFormatError(f"Invalid value for {field}, must be an integer.")

    return True
    pass

def validate_item_data(item_dict):
    """
    Validate that item dictionary has all required fields
    
    Required fields: item_id, name, type, effect, cost, description
    Valid types: weapon, armor, consumable
    
    Returns: True if valid
    Raises: InvalidDataFormatError if missing required fields or invalid type
    """
    # TODO: Implement validation
    required = ["item_id", "name", "type", "effect", "cost", "description"]

    for field in required:
        if field not in item_dict:
            raise InvalidDataFormatError(f"Missing field in item: {field}")

    # Valid types
    valid_types = ["weapon", "armor", "consumable"]
    if item_dict["type"] not in valid_types:
        raise InvalidDataFormatError(f"Invalid item type: {item_dict['type']}")

    # Cost must be integer
    if not isinstance(item_dict["cost"], int):
        raise InvalidDataFormatError("Item cost must be an integer.")

    # Validate effect format
    effect = item_dict["effect"]
    if ":" not in effect:
        raise InvalidDataFormatError("Invalid effect format (expected stat:value).")

    return True
    pass

def create_default_data_files():
    """
    Create default data files if they don't exist
    This helps with initial setup and testing
    """
    # TODO: Implement this function
    # Create data/ directory if it doesn't exist
    # Create default quests.txt and items.txt files
    # Handle any file permission errors appropriately
    try:
        # Create data directory if missing
        if not os.path.exists("data"):
            os.makedirs("data")

        # Create default quests.txt
        quests_path = "data/quests.txt"
        if not os.path.exists(quests_path):
            with open(quests_path, "w") as f:
                f.write(
                    "QUEST_ID: intro_quest\n"
                    "TITLE: First Steps\n"
                    "DESCRIPTION: Your journey begins.\n"
                    "REWARD_XP: 50\n"
                    "REWARD_GOLD: 20\n"
                    "REQUIRED_LEVEL: 1\n"
                    "PREREQUISITE: NONE\n"
                )

        # Create default items.txt
        items_path = "data/items.txt"
        if not os.path.exists(items_path):
            with open(items_path, "w") as f:
                f.write(
                    "ITEM_ID: potion_small\n"
                    "NAME: Small Health Potion\n"
                    "TYPE: consumable\n"
                    "EFFECT: health:20\n"
                    "COST: 10\n"
                    "DESCRIPTION: Restores 20 health.\n"
                )

    except Exception as error:
        raise CorruptedDataError(f"Could not create default data files: {error}")
    pass

# ============================================================================
# HELPER FUNCTIONS
# ============================================================================

def parse_quest_block(lines):
    """
    Parse a block of lines into a quest dictionary
    
    Args:
        lines: List of strings representing one quest
    
    Returns: Dictionary with quest data
    Raises: InvalidDataFormatError if parsing fails
    """
    # TODO: Implement parsing logic
    # Split each line on ": " to get key-value pairs
    # Convert numeric strings to integers
    # Handle parsing errors gracefully
    quest = {}

    try:
        for line in lines:
            if ": " not in line:
                raise InvalidDataFormatError("Invalid quest line format.")

            key, value = line.split(": ", 1)
            key = key.strip().lower()
            value = value.strip()

            # Convert numeric fields
            if key in ["reward_xp", "reward_gold", "required_level"]:
                quest[key] = int(value)
            else:
                quest[key] = value

        # rename keys to match validate_quest_data expected names
        if "quest_id" not in quest:
            raise InvalidDataFormatError("Quest missing QUEST_ID field.")

        # Validate after parsing
        validate_quest_data(quest)

        return quest

    except ValueError:
        raise InvalidDataFormatError("Invalid number in quest data.")
    except InvalidDataFormatError:
        raise
    except Exception as e:
        raise CorruptedDataError(f"Error parsing quest block: {e}")
    pass

def parse_item_block(lines):
    """
    Parse a block of lines into an item dictionary
    
    Args:
        lines: List of strings representing one item
    
    Returns: Dictionary with item data
    Raises: InvalidDataFormatError if parsing fails
    """
    # TODO: Implement parsing logic
    item = {}

    try:
        for line in lines:
            if ": " not in line:
                raise InvalidDataFormatError("Invalid item line format.")

            key, value = line.split(": ", 1)
            key = key.strip().lower()
            value = value.strip()

            if key == "cost":
                item[key] = int(value)
            else:
                item[key] = value

        if "item_id" not in item:
            raise InvalidDataFormatError("Item missing ITEM_ID.")

        validate_item_data(item)

        return item

    except ValueError:
        raise InvalidDataFormatError("Invalid number in item data.")
    except InvalidDataFormatError:
        raise
    except Exception as e:
        raise CorruptedDataError(f"Error parsing item block: {e}")
    pass

# ============================================================================
# TESTING
# ============================================================================

if __name__ == "__main__":
    print("=== GAME DATA MODULE TEST ===")
    
    # Test creating default files
    # create_default_data_files()
    
    # Test loading quests
    # try:
    #     quests = load_quests()
    #     print(f"Loaded {len(quests)} quests")
    # except MissingDataFileError:
    #     print("Quest file not found")
    # except InvalidDataFormatError as e:
    #     print(f"Invalid quest format: {e}")
    
    # Test loading items
    # try:
    #     items = load_items()
    #     print(f"Loaded {len(items)} items")
    # except MissingDataFileError:
    #     print("Item file not found")
    # except InvalidDataFormatError as e:
    #     print(f"Invalid item format: {e}")

