
import pandas as pd

# from ..api import app
# import os
# print("Current Working Directory:", os.getcwd())

# Load the Excel file with double backslashes
file_path ='menu.xlsx'




df = pd.read_excel(file_path)


# so when you write the .\, it takes the current working directory, the directory in which you are in 
# in terms of terminal 
# Map days to their respective column indices (0-indexed)
day_column_map = {
    'monday': 2,   # 2nd column in the Excel sheet
    'tuesday': 3,
    'wednesday': 4,
    'thursday': 5,
    'friday': 6,
    'saturday': 7,
    'sunday': 8
}

# Map meal types to row ranges (0-indexed)
meal_row_map = {
    'breakfast': range(3, 11),   # Row 5 to Row 11 (0-indexed)
    'lunch': range(12, 22),      # Row 13 to Row 22 (0-indexed)
    'snacks': range(22, 26),     # Row 24 to Row 26 (0-indexed)
    'dinner': range(27, 38)      # Row 28 to Row 39 (0-indexed)
}

def get_menu(day, meal):
    # Convert input to lowercase for consistency
    day = day.lower()
    meal = meal.lower()
    
    # Check if the day and meal are valid
    if day not in day_column_map or meal not in meal_row_map:
        return "Invalid day or meal type. Please try again."

    # Get the column index for the day and row range for the meal
    column_index = day_column_map[day]
    row_range = meal_row_map[meal]
    
    # Extract the items from the DataFrame
    menu_items = df.iloc[row_range, column_index].dropna().tolist()
    # print ( type(menu_items))
    # Return the list of menu items
    return menu_items if menu_items else "No items found for the specified day and meal."

# Example usage
day = 'tuesday'
meal = 'breakfast'
menu_items = get_menu(day, meal)
print(f"{day.capitalize()} {meal.capitalize()} menu:")
for i in menu_items:
    print(i)
