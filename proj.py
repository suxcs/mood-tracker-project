import datetime
import random

# Predefined list of moods to choose from, including "Neutral"
moods_list = ["Happy", "Sad", "Angry", "Relaxed", "Excited", "Motivated", "Tired", "Stressed", "Neutral"]

# Suggestions and Quotes for each mood
mood_suggestions = {
    "Happy": [
        "That's awesome! Keep spreading the joy!",
        "Love your energy today!^^",
        "You're a ray of sunshine! Keep shining bright!",
        "Your happiness is contagious, keep it up!"
    ],
    "Sad": [
        "It's okay to feel sad. Maybe take a deep breath or talk to a friend.",
        "You're doing your best. Take it one step at a time.",
        "Cry if you need to; it's part of healing.",
        "Sending you a virtual hug. You got this!"
    ],
    "Angry": [
        "Take a moment to cool down. A quick walk could help clear your mind.",
        "Deep breaths... count to ten and let it out.",
        "Channel your anger into something productive.",
        "It's okay to feel angry. Find a healthy way to express it."
    ],
    "Relaxed": [
        "Great to hear you're relaxed! Keep enjoying the peace and calm.",
        "Life's good! Soak in this moment of serenity.",
        "Let this calm carry you through the day.",
        "Enjoy the stillness. You've earned it."
    ],
    "Excited": [
        "Your energy is contagious! Channel that excitement into something creative.><",
        "What an amazing day to be excited!",
        "Use this energy to do something you've been dreaming of!",
        "Excitement looks good on you! Keep going!"
    ],
    "Motivated": [
        "You're on fire! Keep pushing forward and make your dreams happen.",
        "Every small step counts. You're making progress!",
        "Stay focused—success is just around the corner.",
        "Motivation like yours changes the world. Keep it up!"
    ],
    "Tired": [
        "It's okay to take a break. Rest up and recharge your energy.",
        "You've done enough today. Rest is productive too!",
        "Be kind to yourself—get some sleep.",
        "Relax your body and let yourself recover."
    ],
    "Stressed": [
        "Take a deep breath and try some relaxation exercises. You've got this!",
        "You're stronger than you think. Keep moving forward.",
        "Why not take a walk outside and clear your head?",
        "Tackle one thing at a time. You can do this!"
    ],
    "Neutral": [
        "Hey there! Why not try something new today?",
        "Take this moment to pause and reflect on what you're grateful for.",
        "Sometimes being neutral is a chance to reset. Keep going!",
        "You're doing great! Keep being your awesome self."
    ]
}

mood_quotes = {
    "Happy": "Happiness depends upon ourselves. – Aristotle",
    "Sad": "Tears are words that need to be written. – Paulo Coelho",
    "Angry": "For every minute you are angry, you lose sixty seconds of happiness. – Ralph Waldo Emerson",
    "Relaxed": "Take time to do what makes your soul happy.",
    "Excited": "Success is not the key to happiness. Happiness is the key to success.",
    "Motivated": "The future belongs to those who believe in the beauty of their dreams. – Eleanor Roosevelt",
    "Tired": "Sleep is the best meditation. – Dalai Lama",
    "Stressed": "In the middle of difficulty lies opportunity. – Albert Einstein",
    "Neutral": "Life is 10% what happens to us and 90% how we react to it. – Charles R. Swindoll"
}

# Function to log a mood and corresponding reflection
def log_mood():
    """
    Log a mood and user reflection with a timestamp.
    The function:
    1. Displays a list of moods for the user to choose from.
    2. Collects user input for mood and reflection.
    3. Writes the data into 'mood_tracker.txt' with a timestamp.
    4. Provides a motivational suggestion and quote based on the selected mood.
    """
    print("\n--- Log Your Mood ---")
    print("Choose a mood from the list below:")

    # Display mood options
    for i, mood in enumerate(moods_list, 1):
        print(f"{i}. {mood}")

    # Allow user to select a mood
    try:
        mood_choice = int(input("Enter the number of your mood: "))
        if 1 <= mood_choice <= len(moods_list):
            mood = moods_list[mood_choice -1 ]  # Get the corresponding mood
        else:
            print("Invalid choice. Defaulting to 'Neutral'.")
            mood = "Neutral"
    except ValueError:
        # Handle invalid input
        print("Invalid input. Defaulting to 'Neutral'.")
        mood = "Neutral"

    # Collect user reflection input
    reflection = input("What’s on your mind? (Reflection): ")

    # Get current timestamp
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Write the mood, reflection, and timestamp to the file
    with open("mood_tracker.txt", "a") as file:
        file.write(f"Timestamp: {timestamp}\nMood: {mood}\nReflection: {reflection}\n\n")

    print(f"\nYour mood and reflection have been logged!\n")

    # Share suggestion and quote based on the user's mood
    if mood in mood_suggestions:
        suggestion = random.choice(mood_suggestions[mood])
        print(f"\n{suggestion}")
        print(f"Quote for the moment: {mood_quotes[mood]}")
    else:
        print("\nStay strong and keep going! You're amazing.")


# Function to view past mood entries
def view_entries():
    """
    View previously logged mood entries from the file.
    Reads and displays the content of 'mood_tracker.txt'.
    If the file does not exist or is empty, a relevant message is shown.
    """
    print("\n--- Your Mood Entries ---")
    try:
        with open("mood_tracker.txt", "r") as file:
            content = file.read()
            if content.strip():
                print(content)
            else:
                print("No entries yet. Start by logging your mood!")
    except FileNotFoundError:
        print("No entries found. Start by logging your mood!")


# Main function to run the mood tracker
def main():
    """
    Main menu for the mood tracker application.
    Allows users to:
    1. Log their mood and reflection.
    2. View past entries.
    3. Exit the program.
    """
    print("Welcome to the Simple Mood Tracker!")

    while True:
        print("\nWhat would you like to do?")
        print("1. Log your mood and reflection")
        print("2. View past entries")
        print("3. Exit")
        choice = input("Enter your choice (1/2/3): ")

        if choice == "1":
            log_mood()
        elif choice == "2":
            view_entries()
        elif choice == "3":
            print("Goodbye! Keep tracking your moods and reflections!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")


if __name__ == "__main__":
    main()
