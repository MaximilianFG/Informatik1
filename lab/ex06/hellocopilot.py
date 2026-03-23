from datetime import datetime

# Get current hour
current_hour = datetime.now().hour

# Determine greeting based on time of day
if current_hour < 12:
    time_greeting = "Good morning"
elif current_hour < 18:
    time_greeting = "Good afternoon"
else:
    time_greeting = "Good evening"

# Prompt the user to enter their name
name = input("What is your name? ")

# Display a greeting message with the user's name and time-based greeting
print(f"{time_greeting}, {name}!")
