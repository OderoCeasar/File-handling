# Creating a simple project for note saving


def write_note():
    note = input("Enter your note: ")
    try:
        with open("note.txt", "a") as f:
            f.write(note + "\n")
    except IOError:
        print("Error writing the file")  

def view_notes():
    try:
        with open("note.txt", "r") as f:
            content = f.read()
            if content.strip():
                print("--- Here are your notes --- ")
                print("")
                print(content)
            else:
                print("No notes found")
    except FileNotFoundError:
        print("'note.txt' not found")
    except IOError:
        print("Error reading the file")

def main():
    while True:
        print("--- Notes Saver App ---\n")
        print("1. Write a note")
        print("2. View notes")
        print("3. Exit")

        try:
            choice = int(input("Choose an option (1-3): "))
        except ValueError:
            print("Invalid option")     
            continue

        if choice == 1:
            write_note()   
        elif choice == 2:
            view_notes()
        elif choice == 3:
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter (1-3)")

if __name__ == "__main__":
    main() 