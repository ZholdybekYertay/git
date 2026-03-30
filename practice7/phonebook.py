import csv
from connect import get_connection

def create_table():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS phonebook (
        id SERIAL PRIMARY KEY,
        name TEXT,
        phone TEXT
    )
    """)

    conn.commit()
    cur.close()
    conn.close()
    print("Table ready")

def insert_from_csv(filename):
    conn = get_connection()
    cur = conn.cursor()

    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            cur.execute(
                "INSERT INTO phonebook (name, phone) VALUES (%s, %s)",
                (row['name'], row['phone'])
            )

    conn.commit()
    cur.close()
    conn.close()
    print("CSV data inserted")

def insert_from_console():
    name = input("Enter name: ")
    phone = input("Enter phone: ")

    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO phonebook (name, phone) VALUES (%s, %s)",
        (name, phone)
    )

    conn.commit()
    cur.close()
    conn.close()
    print("Inserted from console")

def update_contact():
    name = input("Enter name to update: ")
    new_phone = input("Enter new phone: ")

    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "UPDATE phonebook SET phone = %s WHERE name = %s",
        (new_phone, name)
    )

    conn.commit()
    cur.close()
    conn.close()
    print("Updated")
    
def query_contacts():
    choice = input("Search by (1-name / 2-phone prefix): ")

    conn = get_connection()
    cur = conn.cursor()

    if choice == "1":
        name = input("Enter name: ")
        cur.execute("SELECT * FROM phonebook WHERE name = %s", (name,))
    elif choice == "2":
        prefix = input("Enter phone prefix: ")
        cur.execute("SELECT * FROM phonebook WHERE phone LIKE %s", (prefix + "%",))
    else:
        print("Invalid choice!")
        return

    rows = cur.fetchall()

    if not rows:
        print("No results found")
    else:
        print("\nResults:")
        for row in rows:
            print(f"ID: {row[0]}, Name: {row[1]}, Phone: {row[2]}")

    cur.close()
    conn.close()

def delete_contact():
    choice = input("Delete by (1-name / 2-phone): ")

    conn = get_connection()
    cur = conn.cursor()

    if choice == "1":
        name = input("Enter name: ")
        cur.execute("DELETE FROM phonebook WHERE name = %s", (name,))
    elif choice == "2":
        phone = input("Enter phone: ")
        cur.execute("DELETE FROM phonebook WHERE phone = %s", (phone,))
    else:
        print("Invalid choice!")
        return

    conn.commit()
    cur.close()
    conn.close()
    print("Deleted")

def show_all_contacts():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT * FROM phonebook")
    rows = cur.fetchall()

    if not rows:
        print("PhoneBook is empty")
    else:
        print("\nAll contacts:")
        for row in rows:
            print(f"ID: {row[0]}, Name: {row[1]}, Phone: {row[2]}")

    cur.close()
    conn.close()

def menu():
    while True:
        print("""
1. Create table
2. Insert from CSV
3. Insert from console
4. Update contact
5. Query contacts
6. Delete contact
7. Show all contacts
8. Exit
        """)

        choice = input("Choose: ")

        if choice == "1":
            create_table()
        elif choice == "2":
            insert_from_csv("contacts.csv")
        elif choice == "3":
            insert_from_console()
        elif choice == "4":
            update_contact()
        elif choice == "5":
            query_contacts()
        elif choice == "6":
            delete_contact()
        elif choice == "7":
            show_all_contacts()
        elif choice == "8":
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    menu()