task = input("Enter your task: ")

priority = input("Priority (high/medium/low): ").lower()

time_bound = input("Is it time-bound? (yes/no): ").lower()

task_description_core = f"'{task}' is a"
message_prefix = ""

match priority:
    case 'high':
        task_description_core += " high priority task"
        message_prefix = "Reminder: "
    case 'medium':
        task_description_core += " medium priority task"
        message_prefix = "Reminder: "
    case 'low':
        task_description_core += " low priority task"
        message_prefix = "Note: "
    case _:
        task_description_core += " unrecognized priority task"

if time_bound == 'yes':
    if priority == 'high' or priority == 'medium':
        task_description_core += " that requires immediate attention today!"
    else:
        task_description_core += " and is time-bound. Try to complete it today!"
elif time_bound == 'no':
    if priority == 'low':
        task_description_core += ". Consider completing it when you have free time."
    else:
        task_description_core += "."
else:
    task_description_core += " (Time-bound status not recognized)."

print(f"{message_prefix}{task_description_core}")