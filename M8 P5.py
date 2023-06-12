#Greg Brewer
#6/4/23
#Problem Game character picked up the items

def check_character_status(items, debuffs):
    task1_items = {'rope', 'coat', 'first aid kit'}
    task2_items = {'pan', 'groceries'}
    task3_items = {'pen', 'paper', 'idea'}

    task1_debuff = 'slow'
    task2_debuff = 'small'
    task3_debuff = 'confusion'

    if set(task1_items).issubset(items) and task1_debuff not in debuffs:
        print("Task 1: Climb a mountain - All items acquired, no status debuffs.")
    else:
        print("Task 1: Climb a mountain - Incomplete items or status debuff.")

    if set(task2_items).issubset(items) and task2_debuff not in debuffs:
        print("Task 2: Cook a meal - All items acquired, no status debuffs.")
    else:
        print("Task 2: Cook a meal - Incomplete items or status debuff.")

    if set(task3_items).issubset(items) and task3_debuff not in debuffs:
        print("Task 3: Write a book - All items acquired, no status debuffs.")
    else:
        print("Task 3: Write a book - Incomplete items or status debuff.")


# Example usage:
character_items = ['pan', 'paper', 'idea', 'rope', 'groceries']
character_debuffs = ['slow']
check_character_status(character_items, character_debuffs)
