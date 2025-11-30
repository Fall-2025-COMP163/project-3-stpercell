"""
COMP 163 - Project 3: Quest Chronicles
Quest Handler Module - Starter Code

Name: [Shikel Percell]

AI Usage: [Document any AI assistance used]

This module handles quest management, dependencies, and completion.
"""

from custom_exceptions import (
    QuestNotFoundError,
    QuestRequirementsNotMetError,
    QuestAlreadyCompletedError,
    QuestNotActiveError,
    InsufficientLevelError
)

# ============================================================================
# QUEST MANAGEMENT
# ============================================================================

def accept_quest(character, quest_id, quest_data_dict):
    """
    Accept a new quest
    
    Args:
        character: Character dictionary
        quest_id: Quest to accept
        quest_data_dict: Dictionary of all quest data
    
    Requirements to accept quest:
    - Character level >= quest required_level
    - Prerequisite quest completed (if any)
    - Quest not already completed
    - Quest not already active
    
    Returns: True if quest accepted
    Raises:
        QuestNotFoundError if quest_id not in quest_data_dict
        InsufficientLevelError if character level too low
        QuestRequirementsNotMetError if prerequisite not completed
        QuestAlreadyCompletedError if quest already done
    """
    # TODO: Implement quest acceptance
    # Check quest exists
    # Check level requirement
    # Check prerequisite (if not "NONE")
    # Check not alr
    if quest_id not in quest_data_dict:
        raise QuestNotFoundError(f"Quest '{quest_id}' does not exist.")
    
    quest_info = quest_data_dict[quest_id]

    # Ensure character lists exist
    if "active_quests" not in character:
        character["active_quests"] = []
    if "completed_quests" not in character:
        character["completed_quests"] = []

    if character.get("level", 0) < quest_info.get("required_level", 1):
        raise InsufficientLevelError(f"Level {quest_info.get('required_level')} required.")
    
    prereq = quest_info.get("prerequisite", "NONE")
    if prereq != "NONE" and prereq not in character["completed_quests"]:
        raise QuestRequirementsNotMetError(f"Prerequisite '{prereq}' not completed.")
    
    if quest_id in character["completed_quests"]:
        raise QuestAlreadyCompletedError(f"Quest '{quest_id}' already completed.")
    
    if quest_id in character["active_quests"]:
        raise QuestNotActiveError(f"Quest '{quest_id}' is already active.")
    
    character["active_quests"].append(quest_id)
    return True 
    # Check not already active
    # Add to character['active_quests']
    pass

def complete_quest(character, quest_id, quest_data_dict):
    """
    Complete an active quest and grant rewards
    
    Args:
        character: Character dictionary
        quest_id: Quest to complete
        quest_data_dict: Dictionary of all quest data
    
    Rewards:
    - Experience points (reward_xp)
    - Gold (reward_gold)
    
    Returns: Dictionary with reward information
    Raises:
        QuestNotFoundError if quest_id not in quest_data_dict
        QuestNotActiveError if quest not in active_quests
    """
    # TODO: Implement quest completion
    # Check quest exists
    # Check quest is active
    # Remove from active_quests
    # Add to completed_quests
    # Grant rewards (use character_manager.gain_experience and add_gold)
    # Return reward summary
    if quest_id not in quest_data_dict:
        raise QuestNotFoundError(f"Quest '{quest_id}' does not exist.")
    
    quest_info = quest_data_dict[quest_id]

    if "active_quests" not in character:
        character["active_quests"] = []
    if "completed_quests" not in character:
        character["completed_quests"] = []
    if "xp" not in character:
        character["xp"] = 0
    if "gold" not in character:
        character["gold"] = 0

    if quest_id not in character["active_quests"]:
        raise QuestNotActiveError(f"Quest '{quest_id}' is not active.")
    
    character["active_quests"].remove(quest_id)
    character["completed_quests"].append(quest_id)
    
    xp_reward = quest_info.get("reward_xp", 0)
    gold_reward = quest_info.get("reward_gold", 0)
    character["xp"] += xp_reward
    character["gold"] += gold_reward
    
    return {
        "quest_id": quest_id,
        "reward_xp": xp_reward,
        "reward_gold": gold_reward
    }

    pass

def abandon_quest(character, quest_id):
    """
    Remove a quest from active quests without completing it
    
    Returns: True if abandoned
    Raises: QuestNotActiveError if quest not active
    """
    # TODO: Implement quest abandonment
    if "active_quests" not in character:
        character["active_quests"] = []
    
    if quest_id not in character["active_quests"]:
        raise QuestNotActiveError(f"Quest '{quest_id}' is not active.")
    
    character["active_quests"].remove(quest_id)
    return True
    pass

def get_active_quests(character, quest_data_dict):
    """
    Get full data for all active quests
    
    Returns: List of quest dictionaries for active quests
    """
    # TODO: Implement active quest retrieval
    # Look up each quest_id in character['active_quests']
    # Return list of full quest data dictionaries
    if "active_quests" not in character:
        character["active_quests"] = []

    active = []
    for qid in character["active_quests"]:
        if qid in quest_data_dict:
            active.append(quest_data_dict[qid])
    return active
    pass

def get_completed_quests(character, quest_data_dict):
    """
    Get full data for all completed quests
    
    Returns: List of quest dictionaries for completed quests
    """
    # TODO: Implement completed quest retrieval
    if "completed_quests" not in character:
        character["completed_quests"] = []

    completed = []
    for qid in character["completed_quests"]:
        if qid in quest_data_dict:
            completed.append(quest_data_dict[qid])
    return completed
    pass

def get_available_quests(character, quest_data_dict):
    """
    Get quests that character can currently accept
    
    Available = meets level req + prerequisite done + not completed + not active
    
    Returns: List of quest dictionaries
    """
    # TODO: Implement available quest search
    # Filter all quests by requirements
    available = []
    for quest_id, quest_info in quest_data_dict.items():
        # -------------------------------------------------
        # Must NOT be already completed
        # -------------------------------------------------
        if quest_id in character["completed_quests"]:
            continue
        # -------------------------------------------------
        # Must NOT be active
        # -------------------------------------------------
        if quest_id in character["active_quests"]:
            continue
        # -------------------------------------------------
        # Check level requirement
        # -------------------------------------------------
        required_level = quest_info.get("required_level", 1)
        if character["level"] < required_level:
            continue 
        # -------------------------------------------------
        # Check prerequisite
        # -------------------------------------------------
        prereq = quest_info.get("prerequisite", "NONE")
        if prereq != "NONE" and prereq not in character["completed_quests"]:
            continue
        # -------------------------------------------------
        # If all checks passed, quest is available
        # -------------------------------------------------
        available.append(quest_info)
    return available
    pass

# ============================================================================
# QUEST TRACKING
# ============================================================================

def is_quest_completed(character, quest_id):
    """
    Check if a specific quest has been completed
    
    Returns: True if completed, False otherwise
    """
    # TODO: Implement completion check
    return quest_id in character["completed_quests"]
    pass

def is_quest_active(character, quest_id):
    """
    Check if a specific quest is currently active
    
    Returns: True if active, False otherwise
    """
    # TODO: Implement active check
    return quest_id in character["active_quests"]
    pass

def can_accept_quest(character, quest_id, quest_data_dict):
    """
    Check if character meets all requirements to accept quest
    
    Returns: True if can accept, False otherwise
    Does NOT raise exceptions - just returns boolean
    """
    # TODO: Implement requirement checking
    # Check all requirements without raising exceptions
    
    # Check quest exists
    # ----------------------------
    if quest_id not in quest_data_dict:
        return False
    quest_info = quest_data_dict[quest_id]
    # ----------------------------
    # Check level requirement
    # ----------------------------
    required_level = quest_info.get("required_level", 1)
    if character["level"] < required_level:
        return False
    # ----------------------------
    # Check prerequisite
    # ----------------------------
    prereq = quest_info.get("prerequisite", "NONE")
    if prereq != "NONE" and prereq not in character["completed_quests"]:
        return False
    # ----------------------------
    # Not already completed
    # ----------------------------
    if quest_id in character["completed_quests"]:
        return False
    # ----------------------------
    # Not already active
    # ----------------------------
    if quest_id in character["active_quests"]:
        return False

    return True
    pass

def get_quest_prerequisite_chain(quest_id, quest_data_dict):
    """
    Get the full chain of prerequisites for a quest
    
    Returns: List of quest IDs in order [earliest_prereq, ..., quest_id]
    Example: If Quest C requires Quest B, which requires Quest A:
             Returns ["quest_a", "quest_b", "quest_c"]
    
    Raises: QuestNotFoundError if quest doesn't exist
    """
    # TODO: Implement prerequisite chain tracing
    # Follow prerequisite links backwards
    # Build list in reverse order

    # Check initial quest exists
    # ----------------------------
    if quest_id not in quest_data_dict:
        raise QuestNotFoundError(f"Quest '{quest_id}' does not exist.")

    chain = []
    current = quest_id
    visited = set()  # For safety, prevents infinite loops

    # ----------------------------
    # Trace backwards through prerequisites
    # ----------------------------
    while True:
        if current in visited:
            # Circular dependency protection
            raise ValueError(f"Circular prerequisite detected involving '{current}'.")
        visited.add(current)

        # Add current quest to chain
        chain.append(current)

        # Get its prerequisite
        quest_info = quest_data_dict[current]
        prereq = quest_info.get("prerequisite", "NONE")

        # No more prerequisites → stop
        if prereq == "NONE":
            break

        # Check prerequisite exists
        if prereq not in quest_data_dict:
            raise QuestNotFoundError(f"Prerequisite quest '{prereq}' does not exist.")

        # Move to the prerequisite and continue tracing
        current = prereq

    # Chain built backwards; reverse it
    chain.reverse()

    return chain
    pass

# ============================================================================
# QUEST STATISTICS
# ============================================================================

def get_quest_completion_percentage(character, quest_data_dict):
    """
    Calculate what percentage of all quests have been completed
    
    Returns: Float between 0 and 100
    """
    # TODO: Implement percentage calculation
    # total_quests = len(quest_data_dict)
    # completed_quests = len(character['completed_quests'])
    # percentage = (completed / total) * 100
    
    total_quests = len(quest_data_dict)
    if total_quests == 0:
        return 0.0  # Avoid division by zero

    completed_quests = len(character["completed_quests"])

    percentage = (completed_quests / total_quests) * 100

    return percentage
    pass

def get_total_quest_rewards_earned(character, quest_data_dict):
    """
    Calculate total XP and gold earned from completed quests
    
    Returns: Dictionary with 'total_xp' and 'total_gold'
    """
    # TODO: Implement reward calculation
    # Sum up reward_xp and reward_gold for all completed quests
    
    total_xp = 0
    total_gold = 0

    # ----------------------------
    # Sum rewards for each completed quest
    # ----------------------------
    for quest_id in character["completed_quests"]:
        if quest_id in quest_data_dict:
            quest_info = quest_data_dict[quest_id]
            total_xp += quest_info.get("reward_xp", 0)
            total_gold += quest_info.get("reward_gold", 0)

    return {
        "total_xp": total_xp,
        "total_gold": total_gold
    }
    pass

def get_quests_by_level(quest_data_dict, min_level, max_level):
    """
    Get all quests within a level range
    
    Returns: List of quest dictionaries
    """
    # TODO: Implement level filtering
    
    filtered_quests = []

    for quest_id, quest_info in quest_data_dict.items():
        level_req = quest_info.get("required_level", 1)
        if min_level <= level_req <= max_level:
            filtered_quests.append(quest_info)

    return filtered_quests
    pass

# ============================================================================
# DISPLAY FUNCTIONS
# ============================================================================

def display_quest_info(quest_data):
    """
    Display formatted quest information
    
    Shows: Title, Description, Rewards, Requirements
    """
    # TODO: Implement quest display
    print(f"\n=== {quest_data['title']} ===")
    print(f"Description: {quest_data['description']}")
    # ... etc
    pass

def display_quest_list(quest_list):
    """
    Display a list of quests in summary format
    
    Shows: Title, Required Level, Rewards
    """
    # TODO: Implement quest list display
    
    if not quest_list:
        print("No quests to display.")
        return

    print(f"{'Title':<30} {'Level':<6} {'XP Reward':<10} {'Gold Reward':<10}")
    print("-" * 60)

    for quest in quest_list:
        title = quest.get("title", "Unknown Quest")
        level = quest.get("required_level", 1)
        xp = quest.get("reward_xp", 0)
        gold = quest.get("reward_gold", 0)

        print(f"{title:<30} {level:<6} {xp:<10} {gold:<10}")
    pass

def display_character_quest_progress(character, quest_data_dict):
    """
    Display character's quest statistics and progress
    
    Shows:
    - Active quests count
    - Completed quests count
    - Completion percentage
    - Total rewards earned
    """
    # TODO: Implement progress display
    
    active_count = len(character.get("active_quests", []))
    completed_count = len(character.get("completed_quests", []))
    completion_percentage = get_quest_completion_percentage(character, quest_data_dict)
    total_rewards = get_total_quest_rewards_earned(character, quest_data_dict)

    print("=== Character Quest Progress ===")
    print(f"Active Quests    : {active_count}")
    print(f"Completed Quests : {completed_count}")
    print(f"Completion       : {completion_percentage:.2f}%")
    print(f"Total XP Earned  : {total_rewards['total_xp']}")
    print(f"Total Gold Earned: {total_rewards['total_gold']}")
    pass

# ============================================================================
# VALIDATION
# ============================================================================

def validate_quest_prerequisites(quest_data_dict):
    """
    Validate that all quest prerequisites exist
    
    Checks that every prerequisite (that's not "NONE") refers to a real quest
    
    Returns: True if all valid
    Raises: QuestNotFoundError if invalid prerequisite found
    """
    # TODO: Implement prerequisite validation
    # Check each quest's prerequisite
    # Ensure prerequisite exists in quest_data_dict

    for quest_id, quest_info in quest_data_dict.items():
        prereq = quest_info.get("prerequisite", "NONE")
        if prereq != "NONE" and prereq not in quest_data_dict:
            raise QuestNotFoundError(
                f"Quest '{quest_id}' has an invalid prerequisite '{prereq}'."
            )
    return True
    pass


# ============================================================================
# TESTING
# ============================================================================

if __name__ == "__main__":
    print("=== QUEST HANDLER TEST ===")
    
    # Test data
    # test_char = {
    #     'level': 1,
    #     'active_quests': [],
    #     'completed_quests': [],
    #     'experience': 0,
    #     'gold': 100
    # }
    #
    # test_quests = {
    #     'first_quest': {
    #         'quest_id': 'first_quest',
    #         'title': 'First Steps',
    #         'description': 'Complete your first quest',
    #         'reward_xp': 50,
    #         'reward_gold': 25,
    #         'required_level': 1,
    #         'prerequisite': 'NONE'
    #     }
    # }
    #
    # try:
    #     accept_quest(test_char, 'first_quest', test_quests)
    #     print("Quest accepted!")
    # except QuestRequirementsNotMetError as e:
    #     print(f"Cannot accept: {e}")

