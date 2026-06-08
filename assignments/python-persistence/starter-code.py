import sqlite3

DB_FILE = "contacts.db"


def create_connection():
    return sqlite3.connect(DB_FILE)


def create_table(conn):
    cursor = conn.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS contacts (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            phone TEXT NOT NULL
        )
        """
    )
    conn.commit()


def add_contact(conn, name, email, phone):
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO contacts (name, email, phone) VALUES (?, ?, ?)",
        (name, email, phone),
    )
    conn.commit()


def get_all_contacts(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, email, phone FROM contacts")
    return cursor.fetchall()


def update_contact(conn, contact_id, name, email, phone):
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE contacts SET name = ?, email = ?, phone = ? WHERE id = ?",
        (name, email, phone, contact_id),
    )
    conn.commit()


def delete_contact(conn, contact_id):
    cursor = conn.cursor()
    cursor.execute("DELETE FROM contacts WHERE id = ?", (contact_id,))
    conn.commit()


def print_contacts(contacts):
    for contact in contacts:
        print(f"ID: {contact[0]}, Name: {contact[1]}, Email: {contact[2]}, Phone: {contact[3]}")


if __name__ == "__main__":
    conn = create_connection()
    create_table(conn)

    add_contact(conn, "Alex Morgan", "alex@example.com", "555-0101")
    add_contact(conn, "Jamie Lee", "jamie@example.com", "555-0102")
    add_contact(conn, "Sam Rivera", "sam@example.com", "555-0103")

    print("Contacts after insert:")
    print_contacts(get_all_contacts(conn))

    update_contact(conn, 2, "Jamie Lee", "jamie.lee@example.com", "555-0202")
    print("\nContacts after update:")
    print_contacts(get_all_contacts(conn))

    delete_contact(conn, 1)
    print("\nContacts after delete:")
    print_contacts(get_all_contacts(conn))

    conn.close()
