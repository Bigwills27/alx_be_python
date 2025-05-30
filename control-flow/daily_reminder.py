task = input("Enter your task: ")

priority = input("Priority (high/medium/low): ").lower()

time_bound = input("Is it time-bound? (yes/no): ").lower()

reminder_message = ""

match priority:
    case 'high':
        reminder_message = f"Reminder: '{task}' is a high priority task"
    case 'medium':
        reminder_message = f"Reminder: '{task}' is a medium priority task"
    case 'low':
        reminder_message = f"Note: '{task}' is a low priority task"
    case _:
        reminder_message = f"Reminder: '{task}' has an unrecognized priority"

if time_bound == 'yes':
    if priority == 'high' or priority == 'medium':
        reminder_message += " that requires immediate attention today!"
    else:
        reminder_message += " and is time-bound. Try to complete it today!"
elif time_bound == 'no':
    if priority == 'low':
        reminder_message += ". Consider completing it when you have free time."
    else:
        reminder_message += "."
else:
    reminder_message += " (Time-bound status not recognized)."

print(reminder_message)