from spot import Spot
from session import Session
import json

spots = []
sessions = []

def add_spot():
    name = input("Enter spot name: ")
    location = input("Enter the location: ")
    difficulty = input("Enter difficulty: ")
    spot = Spot(name, location, difficulty)
    spots.append(spot)
    save_data()
    print(f"{name} has been added to your spots! 🤙")

def view_spots():
    if not spots:
        print("There are no spots saved")
        return
    for spot in spots:
        print(spot)
    answer = get_valid_yes_or_no("Would you like to delete a spot? (y/n): ")
    if answer == "y":
        delete_spot()
    elif answer == "n":
        return

def log_session():
    date = input("Enter Date: ") 
    time = input("Enter Time: ")
    wave_height = input("Enter Wave Height: ") 
    wind = input("Enter Wind: ") 
    tide = input("Enter Tide: ") 
    crowd = input("Enter Crowd: ") 
    uv = input("Enter UV: ") 
    board = input("Enter Board: ") 
    fins = input("Enter Fins: ") 
    duration = input("Enter Duration: ") 
    rating = get_valid_rating()
    notes = input("Enter Notes: ")
    session = Session(date, time, wave_height, wind, tide, crowd, uv, board, fins, duration, rating, notes)
    sessions.append(session)
    save_data()
    print(f"Session on {date} has been added! 🤙")

def get_valid_rating():
    while True:
        try:
            rating = int(input("Enter Rating: ")) 
            if rating < 1 or rating > 10:
                print("Rating must be between 1 and 10")
                continue
            return rating
        except ValueError:
            print("Please enter a number!")

def get_valid_yes_or_no(prompt):
    while True:
        answer = input(prompt).lower()
        if answer not in ["y", "n"]:
            print("Answer must be y or n")
            continue
        return answer

def view_sessions():
    if not sessions:
        print("There are no sessions saved")
        return
    for session in sessions:
        print(session)
    answer = get_valid_yes_or_no("Would you like to delete a session? (y/n): ")
    if answer == "y":
        delete_session()
    elif answer == "n":
        return

def view_stats():
    if not sessions:
        print("There are no sessions saved")
        return
    total_sessions = len(sessions)
    avg_rating = sum(session.rating for session in sessions) / total_sessions
    print(f"Total Sessions: {total_sessions}")
    print(f"Average Rating: {avg_rating:.1f}")

def save_data():
    data = {
        "spots": [spot.to_dict() for spot in spots],
        "sessions": [session.to_dict() for session in sessions]
    }

    with open("data.json", "w") as f:
        json.dump(data, f)
    print("Data saved! 🤙")

def load_data():
    try:
        with open("data.json", "r") as f:
            data = json.load(f)
        spots.clear()
        spots.extend([Spot(s["name"], s["location"], s["difficulty"]) for s in data["spots"]])

        sessions.clear()
        sessions.extend([Session(s["date"], s["time"], s["wave_height"], s["wind"], s["tide"], s["crowd"], s["uv"], s["board"], s["fins"], s["duration"], s["rating"], s["notes"]) for s in data["sessions"]])
  
    except FileNotFoundError:
        print("No saved data found, starting fresh!")

def delete_spot():
    if not spots:
        print("There are no spots saved")
        return
    for index, spot in enumerate(spots, 1):
        print(f"{index}. {spot.name} - {spot.location}")
    print("0. Cancel")
    while True:
        try:
            index = int(input("Select a spot: ")) 
            if index < 0 or index > len(spots):
                print("Please enter the correct spot")
                continue
            if index == 0:
                return
            spot_name = spots[index -1].name
            spots.pop(index - 1)
            print(f"{spot_name} has been deleted") 
            save_data()
            break
        except ValueError:
            print("Please enter a number!")

def delete_session():
    if not sessions:
        print("There are no sessions saved")
        return
    for index, session in enumerate(sessions, 1):
        print(f"{index}. {session.date} - {session.time}")
    print("0. Cancel")
    while True:
        try:
            index = int(input("Select a session: ")) 
            if index < 0 or index > len(sessions):
                print("Please enter the correct session")
                continue
            if index == 0:
                return
            session_date = sessions[index -1].date
            sessions.pop(index - 1)
            print(f"Surf session on {session_date} has been deleted") 
            save_data()
            break
        except ValueError:
            print("Please enter a number!")
 

def main():
    load_data()
    while True:
        print("\nHowzit? Welcome to Surf Log 🏄")
        print("1. Add a surf spot")
        print("2. Log a session")
        print("3. View all spots")
        print("4. View sessions at a spot")
        print("5. View stats")
        print("6. Quit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            add_spot()
        elif choice == "2":
            log_session()
        elif choice == "3":
            view_spots()
        elif choice == "4":
            view_sessions()
        elif choice == "5":
            view_stats()
        elif choice == "6":
            print("Later, surfer! 🤙")
            break
        else:
            print("Invalid choice, please try again.")
main()