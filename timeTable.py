import os

import re

def validate_time(time):

    """Validate time format (HH:MMam/pm)"""

    return bool(re.match(r"^\d{1,2}:\d{2}[ap]m$", time))

def validate_activity(activity):

    """Validate activity name (non-empty string)"""

    return bool(activity.strip())

def validate_description(description):

    """Validate activity description (non-empty string)"""

    return bool(description.strip())

activities = []

while True:

    time = input("Enter activity time (HH:MMam/pm): ")

    while not validate_time(time):

        print("Invalid time format. Please enter time in the format HH:MMam/pm.")

        time = input("Enter activity time (HH:MMam/pm): ")

    activity = input("Enter activity name: ")

    while not validate_activity(activity):

        print("Activity name cannot be empty.")

        activity = input("Enter activity name: ")

    description = input("Enter activity description: ")

    while not validate_description(description):

        print("Activity description cannot be empty.")

        description = input("Enter activity description: ")

    activities.append({

        "time": time,

        "activity": activity,

        "description": description

    })

    more_activities = input("Add another activity? (y/n) ")

    if more_activities.lower() != "y":

        break

# Generate Markdown table

markdown_table = "| Time  | Activity | Description |\n|-------|----------|-------------|\n"

for activity in activities:

    markdown_table += f"| {activity['time']} | {activity['activity']} | {activity['description']} |\n"

# Save Markdown table to file

filename = input("Enter filename (without extension): ")

while not bool(re.match(r"^[A-Za-z0-9_\-]+$", filename)):

    print("Filename can only contain alphanumeric characters, underscores, and hyphens.")

    filename = input("Enter filename (without extension): ")

    

filepath = f"{filename}.md"

try:

    with open(filepath, "w") as file:

        file.write(markdown_table)

except OSError:

    print(f"Error: Could not write to file {os.path.abspath(filepath)}")

else:

    print(f"Markdown table saved to {os.path.abspath(filepath)}")

