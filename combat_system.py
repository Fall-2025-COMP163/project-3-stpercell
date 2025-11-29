"""
COMP 163 - Project 3: Quest Chronicles
Combat System Module - Starter Code

Name: [Your Name Here]

AI Usage: [Document any AI assistance used]

Handles combat mechanics
"""

from custom_exceptions import (
    InvalidTargetError,
    CombatNotActiveError,
    CharacterDeadError,
    AbilityOnCooldownError
)

# ============================================================================
# ENEMY DEFINITIONS
# ============================================================================

def create_enemy(enemy_type):
    """
    Create an enemy based on type
    
    Example enemy types and stats:
    - goblin: health=50, strength=8, magic=2, xp_reward=25, gold_reward=10
    - orc: health=80, strength=12, magic=5, xp_reward=50, gold_reward=25
    - dragon: health=200, strength=25, magic=15, xp_reward=200, gold_reward=100
    
    Returns: Enemy dictionary
    Raises: InvalidTargetError if enemy_type not recognized
    """
    # TODO: Implement enemy creation
    # Return dictionary with: name, health, max_health, strength, magic, xp_reward, gold_reward
    enemies = {
        "goblin": {
            "name": "Goblin",
            "health": 50,
            "max_health": 50,
            "strength": 8,
            "magic": 2,
            "xp_reward": 25,
            "gold_reward": 10
        },
        "orc": {
            "name": "Orc",
            "health": 80,
            "max_health": 80,
            "strength": 12,
            "magic": 5,
            "xp_reward": 50,
            "gold_reward": 25
        },
        "dragon": {
            "name": "Dragon",
            "health": 200,
            "max_health": 200,
            "strength": 25,
            "magic": 15,
            "xp_reward": 200,
            "gold_reward": 100
        }
    }

    if enemy_type.lower() not in enemies:
        raise InvalidTargetError(f"Enemy type '{enemy_type}' is not valid.")

    return enemies[enemy_type.lower()]
    pass

def get_random_enemy_for_level(character_level):
    """
    Get an appropriate enemy for character's level
    
    Level 1-2: Goblins
    Level 3-5: Orcs
    Level 6+: Dragons
    
    Returns: Enemy dictionary
    """
    # TODO: Implement level-appropriate enemy selection
    # Use if/elif/else to select enemy type
    # Call create_enemy with appropriate type
    if character_level <= 0:
        raise ValueError("Character level must be 1 or higher.")

    if 1 <= character_level <= 2:
        enemy_type = "goblin"
    elif 3 <= character_level <= 5:
        enemy_type = "orc"
    else:  # level 6+
        enemy_type = "dragon"

    return create_enemy(enemy_type)
    pass

# ============================================================================
# COMBAT SYSTEM
# ============================================================================

class SimpleBattle:
    """
    Simple turn-based combat system
    
    Manages combat between character and enemy
    """
    def __init__(self, character, enemy):
        """Initialize battle with character and enemy"""
        # TODO: Implement initialization
        # Store character and enemy
        # Set combat_active flag
        # Initialize turn counter
    
        # Store references to character and enemy
        self.character = character
        self.enemy = enemy

        # Flag to track whether combat is currently active
        self.combat_active = True

        # Turn counter (1 = character's turn, 2 = enemy's turn, etc.)
        self.turn_counter = 1

        # Optionally, store initial health for reference
        self.initial_character_health = character.get("health", 0)
        self.initial_enemy_health = enemy.get("health", 0)
        pass
    
    def start_battle(self):
        """
        Start the combat loop
        
        Returns: Dictionary with battle results:
                {'winner': 'player'|'enemy', 'xp_gained': int, 'gold_gained': int}
        
        Raises: CharacterDeadError if character is already dead
        """
        # TODO: Implement battle loop
        # Check character isn't dead
        # Loop until someone dies
        # Award XP and gold if player wins
        if self.character.get("health", 0) <= 0:
            raise CharacterDeadError(f"{self.character.get('name', 'Character')} is dead and cannot fight.")

    self.combat_active = True

    # Simple turn-based combat loop
    while self.character.get("health", 0) > 0 and self.enemy.get("health", 0) > 0:
        # Player's turn: simple attack
        damage_to_enemy = self.character.get("strength", 0)
        self.enemy["health"] -= damage_to_enemy
        # Ensure enemy health doesn't drop below 0
        self.enemy["health"] = max(self.enemy["health"], 0)

        if self.enemy["health"] <= 0:
            # Player wins
            self.combat_active = False
            xp = self.enemy.get("xp_reward", 0)
            gold = self.enemy.get("gold_reward", 0)
            return {"winner": "player", "xp_gained": xp, "gold_gained": gold}

        # Enemy's turn: simple attack
        damage_to_player = self.enemy.get("strength", 0)
        self.character["health"] -= damage_to_player
        self.character["health"] = max(self.character["health"], 0)

        if self.character["health"] <= 0:
            # Enemy wins
            self.combat_active = False
            return {"winner": "enemy", "xp_gained": 0, "gold_gained": 0}

        # Increment turn counter
        self.turn_counter += 1
        pass
    
    def player_turn(self):
        """
        Handle player's turn
        
        Displays options:
        1. Basic Attack
        2. Special Ability (if available)
        3. Try to Run
        
        Raises: CombatNotActiveError if called outside of battle
        """
        # TODO: Implement player turn
        # Check combat is active
        # Display options
        # Get player choice
        # Execute chosen action
        if not self.combat_active:
            raise CombatNotActiveError("Cannot take a turn because combat is not active.")

    # Display player options
    print("\nYour turn! Choose an action:")
    print("1. Basic Attack")
    print("2. Special Ability (if available)")
    print("3. Try to Run")

    # Get player input
    choice = input("Enter the number of your action: ").strip()

    if choice == "1":
        # Basic attack
        damage = self.character.get("strength", 0)
        self.enemy["health"] -= damage
        self.enemy["health"] = max(self.enemy["health"], 0)
        print(f"You attack the {self.enemy.get('name', 'enemy')} for {damage} damage!")

    elif choice == "2":
        # Special ability (check cooldown or availability)
        ability = self.character.get("special_ability")
        if not ability:
            print("You have no special ability available. Using basic attack instead.")
            damage = self.character.get("strength", 0)
            self.enemy["health"] -= damage
            self.enemy["health"] = max(self.enemy["health"], 0)
            print(f"You attack the {self.enemy.get('name', 'enemy')} for {damage} damage!")
        else:
            # Example: deal double strength damage
            damage = self.character.get("strength", 0) * 2
            self.enemy["health"] -= damage
            self.enemy["health"] = max(self.enemy["health"], 0)
            print(f"You use {ability} and deal {damage} damage!")

    elif choice == "3":
        # Try to run (simple 50% chance)
        import random
        if random.random() < 0.5:
            print("You successfully escaped the battle!")
            self.combat_active = False
        else:
            print("You failed to escape!")

    else:
        print("Invalid choice. Turn skipped.")
        pass
    
    def enemy_turn(self):
        """
        Handle enemy's turn - simple AI
        
        Enemy always attacks
        
        Raises: CombatNotActiveError if called outside of battle
        """
        # TODO: Implement enemy turn
        # Check combat is active
        # Calculate damage
        # Apply to character
        if not self.combat_active:
            raise CombatNotActiveError("Cannot take enemy turn because combat is not active.")

        # Calculate damage using the battle's damage formula
        damage = self.calculate_damage(self.enemy, self.character)

        # Apply damage to character's health
        self.character["health"] = max(self.character.get("health", 0) - damage, 0)

        print(f"The {self.enemy.get('name', 'enemy')} attacks you for {damage} damage!")

        # Check if character died
        if self.character.get("health", 0) <= 0:
            print(f"{self.character.get('name', 'You')} have been defeated!")
            self.combat_active = False
            from custom_exceptions import CharacterDeadError
            raise CharacterDeadError(f"{self.character.get('name', 'Character')} has died in battle.")
        pass
    
    def calculate_damage(self, attacker, defender):
        """
        Calculate damage from attack
        
        Damage formula: attacker['strength'] - (defender['strength'] // 4)
        Minimum damage: 1
        
        Returns: Integer damage amount
        """
        # TODO: Implement damage calculation
        attacker_str = attacker.get("strength", 0)
        defender_str = defender.get("strength", 0)

        damage = attacker_str - (defender_str // 4)

        # Ensure minimum damage is 1
        if damage < 1:
                damage = 1

        return damage
        pass
    
    def apply_damage(self, target, damage):
        """
        Apply damage to a character or enemy
        
        Reduces health, prevents negative health
        """
        # TODO: Implement damage application
        if not isinstance(damage, int) or damage < 0:
            raise ValueError("Damage must be a non-negative integer.")

        # Ensure target has health
        target["health"] = max(target.get("health", 0) - damage, 0)
        pass
    
    
    def attempt_escape(self):
        """
        Try to escape from battle
        
        50% success chance
        
        Returns: True if escaped, False if failed
        """
        # TODO: Implement escape attempt
        # Use random number or simple calculation
        # If successful, set combat_active to False
        if not self.combat_active:
            from custom_exceptions import CombatNotActiveError
            raise CombatNotActiveError("Cannot attempt escape because combat is not active.")

        # 50% chance
        success = random.random() < 0.5

        if success:
            self.combat_active = False
            print(f"{self.character.get('name', 'You')} successfully escaped from battle!")
        else:
            print(f"{self.character.get('name', 'You')} failed to escape!")

        return success
        pass

# ============================================================================
# SPECIAL ABILITIES
# ============================================================================

def use_special_ability(character, enemy):
    """
    Use character's class-specific special ability
    
    Example abilities by class:
    - Warrior: Power Strike (2x strength damage)
    - Mage: Fireball (2x magic damage)
    - Rogue: Critical Strike (3x strength damage, 50% chance)
    - Cleric: Heal (restore 30 health)
    
    Returns: String describing what happened
    Raises: AbilityOnCooldownError if ability was used recently
    """
    # TODO: Implement special abilities
    # Check character class
    # Execute appropriate ability
    # Track cooldowns (optional advanced feature)
    def use_special_ability(character, enemy):
    """
    Use character's class-specific special ability
    
    Example abilities by class:
    - Warrior: Power Strike (2x strength damage)
    - Mage: Fireball (2x magic damage)
    - Rogue: Critical Strike (3x strength damage, 50% chance)
    - Cleric: Heal (restore 30 health)
    
    Returns: String describing what happened
    Raises: AbilityOnCooldownError if ability was used recently
    """
    # TODO: Implement special abilities
    # Check character class
    # Execute appropriate ability
    # Track cooldowns (optional advanced feature)
    if character.get("ability_on_cooldown", False):
        raise AbilityOnCooldownError(f"{character.get('name', 'Character')}'s ability is on cooldown.")

    char_class = character.get("class", "").lower()

    if char_class == "warrior":
        return warrior_power_strike(character, enemy)
    elif char_class == "mage":
        return mage_fireball(character, enemy)
    elif char_class == "rogue":
        return rogue_critical_strike(character, enemy)
    elif char_class == "cleric":
        return cleric_heal(character)
    else:
        return f"{character.get('name', 'Character')} has no special ability."
    pass

def warrior_power_strike(character, enemy):
    """Warrior special ability"""
    damage = max(character.get("strength", 0) * 2 - (enemy.get("strength", 0) // 4), 1)
    enemy["health"] = max(enemy.get("health", 0) - damage, 0)
    return f"{character.get('name', 'Warrior')} used Power Strike on {enemy.get('name', 'enemy')} for {damage} damage!"
    # TODO: Implement power strike
    # Double strength damage
    pass

def mage_fireball(character, enemy):
    """Mage special ability"""
    damage = max(character.get("magic", 0) * 2 - (enemy.get("magic", 0) // 4), 1)
    enemy["health"] = max(enemy.get("health", 0) - damage, 0)
    return f"{character.get('name', 'Mage')} cast Fireball on {enemy.get('name', 'enemy')} for {damage} damage!"
    # TODO: Implement fireball
    # Double magic damage
    pass

def rogue_critical_strike(character, enemy):
    """Rogue special ability"""
    base_damage = character.get("strength", 0)
    if random.random() < 0.5:  # Critical hit
        damage = max(base_damage * 3 - (enemy.get("strength", 0) // 4), 1)
        critical = True
    else:  # Normal hit
        damage = max(base_damage - (enemy.get("strength", 0) // 4), 1)
        critical = False

    enemy["health"] = max(enemy.get("health", 0) - damage, 0)

    if critical:
        return f"{character.get('name', 'Rogue')} landed a CRITICAL STRIKE on {enemy.get('name', 'enemy')} for {damage} damage!"
    else:
        return f"{character.get('name', 'Rogue')} attacked {enemy.get('name', 'enemy')} for {damage} damage."
    # TODO: Implement critical strike
    # 50% chance for triple damage
    pass

def cleric_heal(character):
    """Cleric special ability"""
    max_hp = character.get("max_health", 0)
    current_hp = character.get("health", 0)
    heal_amount = min(30, max_hp - current_hp)
    character["health"] = current_hp + heal_amount
    return f"{character.get('name', 'Cleric')} healed for {heal_amount} health!"
    # TODO: Implement healing
    # Restore 30 HP (not exceeding max_health)
    pass
    pass
# ============================================================================
# COMBAT UTILITIES
# ============================================================================

def can_character_fight(character):
    """
    Check if character is in condition to fight
    
    Returns: True if health > 0 and not in battle
    """
    # TODO: Implement fight check
    if character.get("health", 0) <= 0:
        return False
    
    # Character should not already be in combat
    if character.get("in_combat", False):
        return False
    
    return True
    pass

def get_victory_rewards(enemy):
    """
    Calculate rewards for defeating enemy
    
    Returns: Dictionary with 'xp' and 'gold'
    """
    # TODO: Implement reward calculation
    if not enemy:
        return {"xp": 0, "gold": 0}

    xp = enemy.get("xp_reward", 0)
    gold = enemy.get("gold_reward", 0)

    return {"xp": xp, "gold": gold}
    pass

def display_combat_stats(character, enemy):
    """
    Display current combat status
    
    Shows both character and enemy health/stats
    """
    # TODO: Implement status display
    print(f"\n{character['name']}: HP={character['health']}/{character['max_health']}")
    print(f"{enemy['name']}: HP={enemy['health']}/{enemy['max_health']}")
    pass

def display_battle_log(message):
    """
    Display a formatted battle message
    """
    # TODO: Implement battle log display
    print(f">>> {message}")
    pass

# ============================================================================
# TESTING
# ============================================================================

if __name__ == "__main__":
    print("=== COMBAT SYSTEM TEST ===")
    
    # Test enemy creation
    # try:
    #     goblin = create_enemy("goblin")
    #     print(f"Created {goblin['name']}")
    # except InvalidTargetError as e:
    #     print(f"Invalid enemy: {e}")
    
    # Test battle
    # test_char = {
    #     'name': 'Hero',
    #     'class': 'Warrior',
    #     'health': 120,
    #     'max_health': 120,
    #     'strength': 15,
    #     'magic': 5
    # }
    #
    # battle = SimpleBattle(test_char, goblin)
    # try:
    #     result = battle.start_battle()
    #     print(f"Battle result: {result}")
    # except CharacterDeadError:
    #     print("Character is dead!")

