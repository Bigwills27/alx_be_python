def display_menu():
    """
    Displays the main menu options to the user.
    """
    print("\n--- Shopping List Manager ---")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")
    print("---------------------------")

def main():
    """
    Main function to run the shopping list manager application.
    It initializes an empty shopping list and provides a loop
    for user interaction based on the menu options.
    """
    shopping_list = []

    while True:
        display_menu()
        choice = input("Enter your choice: ").strip()

        if choice == '1':
            item = input("Enter the item to add: ").strip()
            if item:
                shopping_list.append(item)
                print(f"'{item}' added to the list.")
            else:
                print("Item name cannot be empty. Please try again.")
        elif choice == '2':
            if not shopping_list:
                print("Your shopping list is already empty. Nothing to remove.")
                continue

            item = input("Enter the item to remove: ").strip()
            if item in shopping_list:
                shopping_list.remove(item) 
                print(f"'{item}' removed from the list.")
            else:
                print(f"'{item}' not found in the shopping list.")
        elif choice == '3':
            if not shopping_list:
                print("Your shopping list is empty.")
            else:
                print("\n--- Your Shopping List ---")
                for i, item in enumerate(shopping_list, 1):
                    print(f"{i}. {item}")
                print("--------------------------")
        elif choice == '4':
            print("Goodbye! Your shopping list has been saved (for this session).")
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
