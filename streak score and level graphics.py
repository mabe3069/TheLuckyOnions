
import random
import time

def display_level(level):
    print(f"===== Level {level} =====")
    # Insert graphics or any visual representation for the level here
    print()

def typing_game():
    streak = 0
    level = 1
    target_words = ['apple', 'banana', 'cherry', 'grape', 'orange']
    
    while True:
        display_level(level)
        target_word = random.choice(target_words)
        
        print(f"Type the word: {target_word}")
        user_input = input()
        
        if user_input == target_word:
            streak += 1
            print(f"Correct! Streak: {streak}")
            
            if streak % 5 == 0:
                level += 1
                print("Congratulations! You've advanced to the next level.")
            
        else:
            print(f"Wrong! Streak reset. Try again.")
            streak = 0
            
        time.sleep(1)  # Brief pause between rounds

typing_game()
