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
    print("Table is ready.")


# 🔹 Insert or Update using procedure
def upsert_contact():
    name = input("Enter name: ")
    phone = input("Enter phone: ")

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("CALL upsert_contact1(%s, %s)", (name, phone))

    conn.commit()
    cur.close()
    conn.close()
    print("Contact inserted/updated.")


# 🔹 Search using function
def search_contacts():
    pattern = input("Enter search pattern: ")

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT * FROM search_contacts1(%s)", (pattern,))
    rows = cur.fetchall()

    print_results(rows)

    cur.close()
    conn.close()


# 🔹 Pagination
def pagination():
    limit = int(input("Enter limit: "))
    offset = int(input("Enter offset: "))

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT * FROM get_contacts_paginated1(%s, %s)", (limit, offset))
    rows = cur.fetchall()

    print_results(rows)

    cur.close()
    conn.close()


# 🔹 Delete
def delete_contact():
    value = input("Enter name or phone to delete: ")

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("CALL delete_contact_proc1(%s)", (value,))

    conn.commit()
    cur.close()
    conn.close()
    print("Deleted.")


# 🔹 Insert many
def insert_many():
    names = input("Enter names (comma separated): ").split(",")
    phones = input("Enter phones (comma separated): ").split(",")

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("CALL insert_many1(%s, %s)", (names, phones))

    conn.commit()
    cur.close()
    conn.close()
    print("Bulk insert done.")


# 🔹 Show all
def show_all():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT * FROM phonebook")
    rows = cur.fetchall()

    print_results(rows)

    cur.close()
    conn.close()


def print_results(rows):
    if rows:
        print("ID | Name                | Phone")
        print("-------------------------------")
        for row in rows:
            print(f"{row[0]:<2} | {row[1]:<18} | {row[2]}")
    else:
        print("No data found.")


def menu():
    while True:
        print("""
1. Create table
2. Insert/Update contact
3. Search
4. Pagination
5. Delete
6. Insert many
7. Show all
8. Exit
        """)

        choice = input("Choose: ")

        if choice == "1":
            create_table()
        elif choice == "2":
            upsert_contact()
        elif choice == "3":
            search_contacts()
        elif choice == "4":
            pagination()
        elif choice == "5":
            delete_contact()
        elif choice == "6":
            insert_many()
        elif choice == "7":
            show_all()
        elif choice == "8":
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    menu()