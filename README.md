[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/wnCpjX4n)
[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-2e0aaae1b6195c2367325f4f02e2d04e9abb55f0b24a779b69b11b9e10269abc.svg)](https://classroom.github.com/online_ide?assignment_repo_id=21863292&assignment_repo_type=AssignmentRepo)
# COMP 163: Project 3 - Quest Chronicles

**AI Usage: Free Use (with explanation requirement)**

## Overview

Build a complete modular RPG adventure game demonstrating mastery of **exceptions and modules**.

## Getting Started

### Step 1: Accept Assignment
1. Click the assignment link provided in Blackboard
2. Accept the assignment - this creates your personal repository
3. Clone your repository to your local machine:
```bash
git clone [your-personal-repo-url]
cd [repository-name]
```

### Step 2: Understand the Project Structure

Your repository contains:

```
quest_chronicles/
├── main.py                     # Game launcher (COMPLETE THIS)
├── character_manager.py        # Character creation/management (COMPLETE THIS)
├── inventory_system.py         # Item and equipment management (COMPLETE THIS)
├── quest_handler.py            # Quest system (COMPLETE THIS)
├── combat_system.py            # Battle mechanics (COMPLETE THIS)
├── game_data.py                # Data loading and validation (COMPLETE THIS)
├── custom_exceptions.py        # Exception definitions (PROVIDED)
├── data/
│   ├── quests.txt             # Quest definitions (PROVIDED)
│   ├── items.txt              # Item database (PROVIDED)
│   └── save_games/            # Player save files (created automatically)
├── tests/
│   ├── test_module_structure.py       # Module organization tests
│   ├── test_exception_handling.py     # Exception handling tests
│   └── test_game_integration.py       # Integration tests
└── README.md                   # This file
```

### Step 3: Development Workflow

```bash
# Work on one module at a time
# Test your code frequently

# Commit and push to see test results
git add .
git commit -m "Implement character_manager module"
git push origin main

# Check GitHub for test results (green checkmarks = passed!, red xs = at least 1 failed test case. Click the checkmark or x and then "Details" to see what test cases passed/failed)
```

## Core Requirements (60 Points)

### Critical Constraint
You may **only** use concepts covered through the **Exceptions and Modules** chapters. 

### 🎨 Creativity and Customization

This project encourages creativity! Here's what you can customize:

**✅ FULLY CUSTOMIZABLE:**
- **Character stats** - Adjust health, strength, magic for balance
- **Enemy stats** - Make enemies easier or harder
- **Special abilities** - Design unique abilities for each class
- **Additional enemies** - Add your own enemy types beyond the required three
- **Game mechanics** - Add status effects, combos, critical hits, etc.
- **Quest rewards** - Adjust XP and gold amounts
- **Item effects** - Create unique items with creative effects

**⚠️ REQUIRED (for testing):**
- **4 Character classes:** Warrior, Mage, Rogue, Cleric (names must match exactly)
- **3 Enemy types:** "goblin", "orc", "dragon" (must exist, stats flexible)
- **All module functions** - Must have the specified function signatures
- **Exception handling** - Must raise appropriate exceptions

**💡 CREATIVITY TIPS:**
1. Start with required features working
2. Add creative elements incrementally
3. Test after each addition
4. Be ready to explain your design choices in the interview
5. Bonus interview points for thoughtful, balanced customization!

**Example Creative Additions:**
- Vampire enemy that heals when attacking
- Warrior "Last Stand" ability that activates when health is low
- Poison status effect that deals damage over time
- Critical hit system based on character stats
- Rare "legendary" weapons with special effects

### Module 1: custom_exceptions.py (PROVIDED - 0 points to implement)

**This module is provided complete.** It defines all custom exceptions you'll use throughout the project.

### Module 2: game_data.py (10 points)

### Module 3: character_manager.py (15 points)

### Module 4: inventory_system.py (10 points)

### Module 5: quest_handler.py (10 points)

### Module 6: combat_system.py (10 points)

### Module 7: main.py (5 points)

## Automated Testing & Validation (60 Points)

## Interview Component (40 Points)

**Creativity Bonus** (up to 5 extra points on interview):
- Added 2+ custom enemy types beyond required three
- Designed unique and balanced special abilities
- Implemented creative game mechanics (status effects, advanced combat, etc.)
- Thoughtful stat balancing with clear reasoning

**Note:** Creativity is encouraged, but functionality comes first! A working game with required features scores higher than a broken game with lots of extras.

### Update README.md

Document your project with:

1. **Module Architecture:** Explain your module organization
2. **Exception Strategy:** Describe when/why you raise specific exceptions
3. **Design Choices:** Justify major decisions
4. **AI Usage:** Detail what AI assistance you used
5. **How to Play:** Instructions for running the game

### What to Submit:

1. **GitHub Repository:** Your completed multi-module project
2. **Interview:** Complete 10-minute explanation session
3. **README:** Updated documentation

## Protected Files Warning

⚠️ **IMPORTANT: Test Integrity**

Test files are provided for your learning but are protected. Modifying test files constitutes academic dishonesty and will result in:

- Automatic zero on the project
- Academic integrity investigation

You can view tests to understand requirements, but any modifications will be automatically detected.







-Documentation-

Module Architecture

1. custom_exceptions.py

Provided by the instructor. Contains all exception classes used across the project.
No modification was required.

2. game_data.py

Stores all static and configurable game information.
Responsibilities:

Character class base stats (Warrior, Mage, Rogue, Cleric — required names)

Enemy definitions (goblin, orc, dragon — required types + my custom types)

Item templates and quest rewards
Purpose: Keeps game balancing data separate from logic so adjustments are simple and safe.

3. character_manager.py

Creates and manages player characters.
Responsibilities:

Constructing characters with proper stats

Validating class names

Applying abilities, stats, and level-ups

Raising exceptions if invalid classes or stats are used
Rationale: Central place for anything related to player class identity and capabilities.

4. inventory_system.py

Manages all items a player can acquire.
Responsibilities:

Adding/removing items

Applying item effects to character stats

Validating inventory capacity

Handling item errors through custom exceptions

5. quest_handler.py

Handles quest logic, rewards, and progression.
Responsibilities:

Granting XP/gold on quest completion

Checking quest prerequisites

Raising exceptions for invalid quest names or claim attempts
Keeps progression logic cleanly separated from combat or character creation.

6. combat_system.py

Executes turn-based combat between player and enemy.
Responsibilities:

Applying damage, abilities, status effects

Validating enemy type

Ending combat on defeat and raising GameOver-style exceptions if needed
Designed to be self-contained for easy testing.

7. main.py

The game driver.
Responsibilities:

Loads all modules

Creates characters

Starts quests

Runs combat encounters
Minimal logic: serves only as the gameplay loop and user interaction layer.



Exception Strategy

Exceptions are used consistently across modules to enforce correct state transitions and protect the game from invalid data.

When exceptions are raised:

1. Invalid Input (player error)
Examples:

Selecting a nonexistent character class

Using an item that is not in inventory

Attempting to fight an undefined enemy
These raise exceptions such as InvalidCharacterClassError, ItemNotFoundError, or UnknownEnemyError.

2. Invalid Game State (logic error)
Raised when internal assumptions are violated, such as:

Negative health values

Duplicate character creation

Removing items from an empty inventory
These catch programmer mistakes rather than player mistakes.

3. Flow-Control Exceptions
Used to signal controlled events:

A character reaching 0 HP triggers a game-over exception

Quest completion may raise a “RewardGranted” exception internally to simplify flow

4. Data Loading Exceptions
If game_data.py is missing required fields, a structured exception is raised to prevent broken game sessions.



AI Usage

Planning the architecture: Brainstorming module responsibilities and how to structure data cleanly.

Debugging guidance, explaining error messages and suggesting fix directions.

Writing explanations, helped draft portions of this report.

All core logic, design decisions, balancing choices, and final code were written and verified manually



How to Play
1. Run the Program

From the project folder:

python main.py

2. Create a Character

You will be prompted to choose one of the required classes:

Warrior

Mage

Rogue

Cleric

The system automatically loads stats from game_data.py.

3. Begin Your Quest

You can view quests, accept them, and check your inventory.

4. Combat

When encountering an enemy:

Turns alternate between player and enemy

You can attack, use abilities, or use items

Status effects and special abilities activate automatically if conditions are met
Combat ends when the player or enemy reaches 0 HP.

5. Progression

After fights or quests:

XP increases

Gold is awarded

New items may be gained

Character may level up depending on your design

6. End of Game

The game ends when:

You complete the main quest chain, or

Your HP reaches zero (a GameOver exception is triggered)
