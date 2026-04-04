from tools.toolbox import input

DAYS_PER_YEAR = 365

age_in_years = int(input("Wie alt bist Du? "))  # Reads input, converts to integer
age_in_days = age_in_years * DAYS_PER_YEAR

print(f"Dann bist Du mindestens {age_in_days:n} Tage alt.")
