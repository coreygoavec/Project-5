import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('FridayProj5.db')

# Create a cursor object to execute SQL queries
cursor = conn.cursor()

# Query to retrieve table names from sqlite_master
#cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")

import random

# Function to retrieve questions and answers from the database
def get_questions_answers():
    # Connect to the SQLite database
    conn = sqlite3.connect('FridayProj5.db')

    # Create a cursor object to execute SQL queries
    cursor = conn.cursor()

    # Execute a SELECT query to retrieve questions and answers from the QuestAns table
    cursor.execute('SELECT question, answer FROM QuestAns')

    # Fetch all rows from the result set
    rows = cursor.fetchall()

    # Close the cursor and the database connection
    cursor.close()
    conn.close()

    # Return the fetched rows
    return rows

# Function to ask quiz questions
def ask_questions():
    # Retrieve questions and answers from the database
    questions_answers = get_questions_answers()

    # Shuffle the questions and answers
    random.shuffle(questions_answers)

    # Ask each question in the shuffled list
    for question, answer in questions_answers:
        print("Question:", question)
        user_answer = input("Your answer: ").strip().lower()

        # Check if the user's answer is correct
        if user_answer == answer.lower():
            print("Correct!")
        else:
            print(f"Sorry, the correct answer is: {answer}")

# User input function
def play_quiz_bowl():
    while True:
        choice = input("Would you like to play Quiz Bowl? (Yes/No): ").strip().lower()
        
        if choice == 'yes':
            ask_questions()
            break
        elif choice == 'no':
            print("Goodbye!")
            break
        else:
            print("Invalid input. Please enter 'Yes' or 'No'.")

# Calling the function to start the quiz bowl game
play_quiz_bowl()