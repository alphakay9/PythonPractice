import os
import datetime

DIARY_FOLDER = "diary_entries"

def create_diary_entry(title, content):
    timestamp = datetime.datetime.now()
    #entry_filename = f"{timestamp.strftime('%Y-%m-%d_%H-%M-%S')}.txt"
    entry_filename = f"{title}.txt"
    
    entry_path = os.path.join(DIARY_FOLDER, entry_filename)
    with open(entry_path, "w") as f:
        f.write(f"Title: {title}\n")
        f.write(f"Timestamp: {timestamp}\n\n")
        f.write(content)

def list_diary_entries():
    entries = os.listdir(DIARY_FOLDER)
    for entry in entries:
        entry_path = os.path.join(DIARY_FOLDER, entry)
        with open(entry_path, "r") as f:
            content = f.readlines()
            print (entry+' -> '+content[0]+content[1])
            

def view_diary_entry(entry_filename):
    entry_path = os.path.join(DIARY_FOLDER, entry_filename)
    with open(entry_path, "r") as f:
        content = f.read()
        print(content)

def search_diary_entries(keyword):
    matching_entries = []
    entries = os.listdir(DIARY_FOLDER)
    for entry in entries:
        entry_path = os.path.join(DIARY_FOLDER, entry)
        with open(entry_path, "r") as f:
            content = f.read()
            if keyword in content:
                matching_entries.append(entry)
    
    if matching_entries:
        for entry in matching_entries:
            print(entry)
    else:
        print("No matching entries found.")

def delete_diary_entry(entry_filename):
    entry_path = os.path.join(DIARY_FOLDER, entry_filename)
    if os.path.exists(entry_path):
        os.remove(entry_path)
        print("Entry deleted.")
    else:
        print("Entry not found.")

def main():
    if not os.path.exists(DIARY_FOLDER):
        os.mkdir(DIARY_FOLDER)
    
    while True:
        print("\n Diary Application")
        print("1. Add Entry")
        print("2. List Entries")
        print("3. View Entry")
        print("4. Search Entries")
        print("5. Delete Entry")
        print("6. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            title = input("Enter the title: ")
            entry_file= title+".txt"
            path1 = os.path.join(DIARY_FOLDER, entry_file)
            if os.path.exists(path1):
                print("File Already EXISTS")
            else:
                content = input("Enter the content: ")
                create_diary_entry(title, content)
                print("Entry added.")
        elif choice == "2":
            list_diary_entries()
        elif choice == "3":
            entry_filename = input("Enter the entry filename: ")
            view_diary_entry(entry_filename)
        elif choice == "4":
            keyword = input("Enter a keyword to search for: ")
            search_diary_entries(keyword)
        elif choice == "5":
            entry_filename = input("Enter the entry filename: ")
            delete_diary_entry(entry_filename)
        elif choice == "6":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
    