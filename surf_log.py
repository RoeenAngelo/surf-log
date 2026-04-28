from spot import Spot
from session import Session

spots = []
sessions = []

def add_spot():
    name = input("Enter spot name: ")
    location = input("Enter the location: ")
    difficulty = input("Enter difficulty: ")
    spot = Spot(name, location, difficulty)
    spots.append(spot)
    print(f"{name} has been added to your spots! 🤙")

def view_spots():
    if not spots:
        print("There are no spots saved")
        return
    for spot in spots:
        print(spot)


def main():
    while True:
        print("\nHowzit? Welcome to Surf Log 🏄")
        print("1. Add a surf spot")
        print("2. Log a session")
        print("3. View all spots")
        print("4. View sessions at a spot")
        print("5. View stats")
        print("6. Quit")

        choice = input("\nEnter your choice:")

        if choice == "1":
            add_spot()
        elif choice == "2":
            print("Log a session")
        elif choice == "3":
            view_spots()
        elif choice == "4":
            print("Showing Sessions")
        elif choice == "5":
            print("Showing Stats")
        elif choice == "6":
            print("Later, surfer! 🤙")
            break
        else:
            print("Invalid choice, please try again.")
main()