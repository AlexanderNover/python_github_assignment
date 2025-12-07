print("Welcome to my workout tracker!")

# Ask the user for input
minutes = input("How many minutes did you work out today? ")

# Error handling
try:
    minutes = float(minutes)
except ValueError:
    print("Please enter a valid number.")
    exit()

# Calculation
weekly_minutes = minutes * 7

# Output the result
print(f"You are on track to work out for {weekly_minutes} minutes this week.")