import sys
import sqlite3
from datetime import datetime, timedelta
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QPushButton, QLabel, QLineEdit, QTextEdit, QInputDialog, QMessageBox,
    QStackedWidget
)
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt

conn = sqlite3.connect("library.db")
cursor = conn.cursor()
cursor.execute("PRAGMA foreign_keys = ON;")

# sample data for prepopulating tables
branch_data = [
    ('1234567890', 'Maple Grove Library', '456 King St, Toronto, ON', '416-987-6543'),
    ('2345678901', 'North Park Library', '789 Bathurst St, Toronto, ON', '416-123-4567'),
    ('3456789012', 'Riverdale Reading Room', '123 Yonge St, Toronto, ON', '416-555-6789'),
    ('4567890123', 'Parkview Branch Library', '321 Bloor St, Toronto, ON', '416-246-8901'),
    ('5678901234', 'High Park Literary Hub', '654 Ossington Ave, Toronto, ON', '416-135-7982'),
    ('6789012345', 'Danforth Community Library', '987 Queen St, Toronto, ON', '416-753-1234'),
    ('7890123456', 'Beaches Book Corner', '456 St Clair Ave, Toronto, ON', '416-864-2468'),
    ('8901234567', 'Annex Reading Centre', '321 Spadina Ave, Toronto, ON', '416-654-7890'),
    ('9012345678', 'Harbourfront Library', '123 Front St, Toronto, ON', '416-975-4321'),
    ('0123456789', 'Junction Literary Commons', '234 Jarvis St, Toronto, ON', '416-246-7890')
]

personnel_data = [
    ('1030012345', 'John', 'Doe', 'Librarian', '2020-06-15', 85000, '416-123-4567', '1234567890', 0),
    ('1040023456', 'Jane', 'Smith', 'Library Assistant', '2021-02-10', 55000, '416-234-5678', '2345678901', 1),
    ('1050034567', 'James', 'Brown', 'Archivist', '2019-08-22', 60000, '416-345-6789', '3456789012', 0),
    ('1060045678', 'Emily', 'Davis', 'Librarian', '2022-04-05', 85000, '416-456-7890', '4567890123', 0),
    ('1070056789', 'Michael', 'Miller', 'IT Specialist', '2020-11-11', 95000, '416-567-8901', '5678901234', 0),
    ('1080067890', 'Sarah', 'Wilson', 'Library Technician', '2021-07-30', 50000, '416-678-9012', '6789012345', 1),
    ('1090054321', 'David', 'Moore', 'Cataloging Specialist', '2020-09-13', 72000, '416-789-0123', '7890123456', 0),
    ('1020065432', 'Jessica', 'Taylor', 'Library Director', '2021-01-25', 80000, '416-890-1234', '8901234567', 0),
    ('1010076543', 'Chris', 'Anderson', 'Library Assistant', '2022-03-02', 55000, '416-901-2345', '9012345678', 1),
    ('1020087654', 'Patricia', 'Thomas', 'Librarian', '2019-05-18', 90000, '416-012-3456', '0123456789', 0)
]

item_data = [
    ('9876543210', 'The Future of AI', 'Book', 'Checked Out', 'Tech Publishers', 'Technology', '2025-03-01', '1234567890'),
    ('8765432109', 'Introduction to Programming', 'DVD', 'Checked Out', 'CodeMasters', 'Education', '2024-12-15', '2345678901'),
    ('7654321098', 'Digital Transformation', 'Book', 'Checked Out', 'Future Press', 'Business', '2023-06-10', '3456789012'),
    ('6543210987', 'Advanced Python', 'Book', 'Checked Out', 'Code Books', 'Education', '2023-11-01', '4567890123'),
    ('5432109876', 'Data Science 101', 'DVD', 'Checked Out', 'Tech World', 'Education', '2024-08-20', '5678901234'),
    ('4321098765', 'Cloud Computing Basics', 'Book', 'Checked Out', 'Cloud Press', 'Technology', '2025-02-05', '6789012345'),
    ('3210987654', 'AI and Machine Learning', 'Book', 'Checked Out', 'AI Books', 'Technology', '2024-10-25', '7890123456'),
    ('2109876543', 'JavaScript for Beginners', 'DVD', 'Checked Out', 'Programming Masters', 'Education', '2023-05-12', '8901234567'),
    ('1098765432', 'The History of AI', 'Book', 'Checked Out', 'History Books', 'Technology', '2025-01-19', '9012345678'),
    ('0987654321', 'The Cloud Revolution', 'Book', 'Checked Out', 'Cloud Innovations', 'Business', '2024-07-30', '0123456789'),
    ('8754323211', 'Cybersecurity Essentials', 'Book', 'Available', 'Security Press', 'Technology', '2023-09-10', '5678901234'),
    ('9825427212', 'Blockchain Basics', 'Book', 'Available', 'Crypto Publishers', 'Technology', '2024-05-22', '5678901234'),
    ('9871475832', 'Machine Learning Fundamentals', 'DVD', 'Available', 'ML Academy', 'Education', '2025-06-18', '8901234567'),
    ('5432122214', 'Networking for Beginners', 'Book', 'Available', 'IT Publishers', 'Technology', '2024-02-14', '8901234567'),
    ('9876543215', 'Quantum Computing Explained', 'Book', 'Available', 'FutureTech', 'Technology', '2023-12-01', '5678901234'),
    ('9882843216', 'Ethical Hacking 101', 'DVD', 'Available', 'CyberSafe', 'Security', '2024-08-05', '3456789012'),
    ('8383432127', 'Introduction to Robotics', 'Book', 'Available', 'Robot Press', 'Technology', '2025-01-15', '3456789012'),
    ('1767652138', 'Deep Learning with Python', 'Book', 'Available', 'AI Insights', 'Education', '2023-07-20', '7890123456'),
    ('1698765519', 'Cloud Security Fundamentals', 'DVD', 'Available', 'Cloud Secure', 'Technology', '2024-11-03', '8901234567'),
    ('9264343220', 'Big Data Analytics', 'Book', 'Available', 'Data Science Press', 'Business', '2025-04-10', '0123456789')
]

member_data = [
    ('1000000000', 'Alice', 'Johnson', '123 Maple Street', '416-321-4321', 'alice.johnson@spammail.com', '2021-05-15', '1234567890'),
    ('2043251122', 'Bob', 'Martin', '456 Oak Avenue', '416-432-5432', 'bob.martin@spammail.com', '2020-11-20', '2345678901'),
    ('4433034856', 'Carol', 'Lee', '789 Pine Road', '416-543-6543', 'carol.lee@spammail.com', '2022-01-10', '3456789012'),
    ('4832957132', 'David', 'Walker', '101 Birch Blvd', '416-654-7654', 'david.walker@spammail.com', '2021-07-25', '4567890123'),
    ('4123875892', 'Eva', 'Harris', '202 Cedar Crescent', '416-765-8765', 'eva.harris@spammail.com', '2023-03-05', '5678901234'),
    ('1312890592', 'Frank', 'Martinez', '303 Elm Street', '416-876-9876', 'frank.martinez@spammail.com', '2022-08-15', '6789012345'),
    ('9896457833', 'Grace', 'White', '404 Willow Lane', '416-987-0987', 'grace.white@spammail.com', '2020-09-30', '7890123456'),
    ('4728396831', 'Harry', 'Thompson', '505 Fir Avenue', '416-098-2098', 'harry.thompson@spammail.com', '2021-04-12', '8901234567'),
    ('5347896932', 'Ivy', 'Roberts', '606 Redwood Drive', '416-209-3120', 'ivy.roberts@spammail.com', '2022-02-18', '9012345678'),
    ('6378432934', 'Jack', 'Davis', '707 Cedar Park', '416-312-4231', 'jack.davis@spammail.com', '2020-12-08', '0123456789')
]

loan_data = [
    ('1478392967', '2023-01-10', '2023-01-24', '2023-01-25', '9876543210', '1000000000'),
    ('2043251167', '2023-02-15', '2023-03-01', '2023-03-02', '8765432109', '4433034856'),
    ('4433034867', '2023-03-05', '2023-03-19', None, '7654321098', '4433034856'),
    ('4832957167', '2023-04-10', '2023-04-24', '2023-04-25', '6543210987', '4832957132'),
    ('4123875867', '2023-05-01', '2023-05-15', None, '5432109876', '4123875892'),
    ('1312890567', '2023-06-20', '2023-07-04', '2023-07-05', '4321098765', '1312890592'),
    ('9896457867', '2023-07-10', '2023-07-24', None, '3210987654', '9896457833'),
    ('4728396867', '2023-08-01', '2023-08-15', '2023-08-16', '2109876543', '4728396831'),
    ('5347896967', '2023-09-15', '2023-09-29', '2023-09-30', '1098765432', '5347896932'),
    ('6378432967', '2023-10-01', '2023-10-15', None, '0987654321', '5347896932')
]

futureacquisition_data = [
    ('8291043756', 'Modern Web Design', 'Book', 'Design House', '2025-05-20', '1234567890', '2025-04-10', '2025-06-01'),
    ('3751902846', 'Quantum Computing', 'DVD', 'Future Tech', '2025-07-15', '2345678901', '2025-05-05', '2025-08-01'),
    ('9583704612', 'History of Robotics', 'Book', 'Robo Press', '2024-09-10', '3456789012', '2024-08-01', '2024-10-01'),
    ('1647382950', 'Sustainable Energy', 'Magazine', 'Green Media', '2023-12-01', '4567890123', '2023-11-01', '2024-01-01'),
    ('5079182634', 'Artificial Intelligence', 'Book', 'AI Publishers', '2025-01-25', '5678901234', '2024-12-15', '2025-02-15'),
    ('2837465910', 'Modern Art Trends', 'DVD', 'Art House', '2023-10-05', '6789012345', '2023-09-01', '2023-11-01'),
    ('6904821753', 'Space Exploration', 'Book', 'Cosmos Books', '2024-03-20', '7890123456', '2024-02-10', '2024-04-10'),
    ('8473629150', 'Medical Breakthroughs', 'Magazine', 'Health Media', '2024-08-15', '8901234567', '2024-07-10', '2024-09-10'),
    ('3918572046', 'Philosophy Today', 'Book', 'Thinkers Press', '2023-11-30', '9012345678', '2023-10-25', '2023-12-01'),
    ('5647382910', 'Environmental Studies', 'DVD', 'EcoVision', '2024-05-10', '0123456789', '2024-04-01', '2024-06-01')
]

fine_data = [
    ('1478392967', 5.00,  'Late Return',      '2023-01-25', '2023-02-10', 1),
    ('2043251167', 10.50, 'Book Damage',      '2023-03-02', '2023-03-16', 0),
    ('4433034867', 3.75,  'Overdue Fine',     '2023-03-22', '2023-04-05', 1),
    ('4832957167', 8.00,  'Late Return',      '2023-04-25', '2023-05-10', 0),
    ('4123875867', 6.50,  'Misplaced Item',   '2023-05-16', '2023-06-01', 1),
    ('1312890567', 12.00, 'Damaged Cover',    '2023-07-05', '2023-07-20', 0),
    ('9896457867', 4.25,  'Overdue Fine',     '2023-07-25', '2023-08-10', 1),
    ('4728396867', 7.00,  'Late Return',      '2023-08-16', '2023-09-01', 0),
    ('5347896967', 9.50,  'Book Damage',      '2023-09-30', '2023-10-15', 1),
    ('6378432967', 11.00, 'Overdue Fine',     '2023-10-16', '2023-10-31', 0)
]

socialroom_data = [
    ('7583920417', 'Reading Room A',    30, '1234567890'),
    ('2948175036', 'Study Hall',        25, '2345678901'),
    ('8374619205', 'Quiet Corner',      15, '3456789012'),
    ('9152048376', 'Media Lounge',      40, '4567890123'),
    ('6029381745', 'Children’s Corner', 20, '5678901234'),
    ('4817290356', 'Digital Lab',       35, '6789012345'),
    ('7391824650', 'Fiction Forum',     50, '7890123456'),
    ('5647381029', 'Nonfiction Nook',   30, '8901234567'),
    ('9283746501', 'Multimedia Room',   45, '9012345678'),
    ('8172635409', 'Community Hub',     60, '0123456789')
]

event_data = [
    ('9348510276', 'Tech Talk',         'Seminar',    '2023-11-10', 30, 4, 'Adults',      '7583920417'),
    ('8124753096', 'Book Club',         'Discussion', '2023-12-05', 25, 0, 'All Ages',    '2948175036'),
    ('6792053841', 'Art Workshop',      'Workshop',   '2023-10-15', 15, 0, 'Teens',       '8374619205'),
    ('5618392740', 'History Lecture',   'Seminar',    '2023-09-20', 40, 0, 'Adults',      '9152048376'),
    ('4205739182', 'Kids Storytime',    'Reading',    '2023-08-30', 20, 1, 'Children',    '6029381745'),
    ('3891762540', 'Digital Literacy',  'Workshop',   '2023-07-25', 35, 0, 'Adults',      '4817290356'),
    ('7483921560', 'Fiction Fest',      'Festival',   '2023-11-20', 50, 0, 'Young Adults','7391824650'),
    ('9357164820', 'Nonfiction Night',  'Discussion', '2023-12-15', 30, 5, 'Adults',      '5647381029'),
    ('6028471935', 'Multimedia Expo',   'Exhibition', '2023-10-05', 45, 0, 'All Ages',    '9283746501'),
    ('7491038265', 'Community Meetup',  'Social',     '2023-09-15', 60, 8, 'All Ages',    '8172635409')
]

attendance_data = [
    ('9348510276', '1000000000'), ('8124753096', '2043251122'), ('6792053841', '4433034856'),
    ('5618392740', '4832957132'), ('4205739182', '4123875892'), ('3891762540', '1312890592'),
    ('7483921560', '9896457833'), ('9357164820', '4728396831'), ('6028471935', '5347896932'),
    ('7491038265', '6378432934')
]

requests_data = [
    ('8392017465', '1000000000', '1030012345', 'Inquiry about new arrivals', 0),
    ('5602839174', '2043251122', '1040023456', 'Request for extended borrowing period', 1),
    ('4791028563', '4433034856', '1050034567', 'Assistance with digital catalog', 0),
    ('9384756102', '4832957132', '1060045678', 'Question about late fee policy', 1),
    ('1203948576', '4123875892', '1070056789', 'Help with research resources', 0),
    ('8573920146', '1312890592', '1080067890', 'Assistance with account login', 1),
    ('2938475610', '9896457833', '1090054321', 'Request for book reservation', 0),
    ('6710293845', '4728396831', '1020065432', 'Inquiry about interlibrary loan', 1),
    ('4857260193', '5347896932', '1010076543', 'Assistance with overdue fine', 0),
    ('7501923846', '6378432934', '1020087654', 'Question about membership renewal', 1)
]


def create_tables():
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS BRANCH (
        branchID TEXT PRIMARY KEY, branchName TEXT NOT NULL,
        branchAddress TEXT NOT NULL, phoneNum TEXT NOT NULL)""")
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS MEMBER (
        memberID TEXT PRIMARY KEY, firstName TEXT NOT NULL, lastName TEXT NOT NULL,
        memberAddress TEXT NOT NULL, phoneNum TEXT NOT NULL, email TEXT NOT NULL,
        membershipDate TEXT NOT NULL CHECK(membershipDate GLOB '[0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]'),
        branchID TEXT NOT NULL, FOREIGN KEY(branchID) REFERENCES BRANCH(branchID))""")
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS PERSONNEL (
        personnelID TEXT PRIMARY KEY, firstName TEXT NOT NULL, lastName TEXT NOT NULL,
        jobTitle TEXT NOT NULL, hireDate TEXT NOT NULL CHECK(hireDate GLOB '[0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]'),
        salary INTEGER NOT NULL, phoneNum TEXT NOT NULL, branchID TEXT NOT NULL,
        volunteer BOOLEAN DEFAULT 0, FOREIGN KEY(branchID) REFERENCES BRANCH(branchID))""")
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS ITEM (
        itemID TEXT PRIMARY KEY, title TEXT NOT NULL, media TEXT NOT NULL,
        itemStatus TEXT NOT NULL, publisher TEXT NOT NULL, genre TEXT NOT NULL,
        publicationDate TEXT NOT NULL CHECK(publicationDate GLOB '[0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]'),
        branchID TEXT NOT NULL, FOREIGN KEY(branchID) REFERENCES BRANCH(branchID))""")
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS FUTUREACQUISITION (
        acquisitionID TEXT PRIMARY KEY, title TEXT NOT NULL, media TEXT NOT NULL,
        publisher TEXT NOT NULL, publicationDate TEXT NOT NULL CHECK(publicationDate GLOB '[0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]'),
        branchID TEXT NOT NULL, requestDate TEXT NOT NULL CHECK(requestDate GLOB '[0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]'),
        expectedArrival TEXT NOT NULL CHECK(expectedArrival GLOB '[0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]'),
        FOREIGN KEY(branchID) REFERENCES BRANCH(branchID))""")
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS LOAN (
        loanID TEXT PRIMARY KEY, borrowDate TEXT NOT NULL CHECK(borrowDate GLOB '[0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]'),
        dueDate TEXT NOT NULL CHECK(dueDate GLOB '[0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]'),
        returnDate TEXT DEFAULT NULL CHECK(returnDate IS NULL OR returnDate GLOB '[0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]'),
        itemID TEXT NOT NULL, memberID TEXT NOT NULL,
        FOREIGN KEY(itemID) REFERENCES ITEM(itemID), FOREIGN KEY(memberID) REFERENCES MEMBER(memberID))""")
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS FINE (
        loanID TEXT PRIMARY KEY, fineAmount REAL NOT NULL, reason TEXT NOT NULL,
        issueDate TEXT NOT NULL CHECK(issueDate GLOB '[0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]'),
        dueDate TEXT NOT NULL CHECK(dueDate GLOB '[0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]'),
        paid BOOLEAN DEFAULT 0, FOREIGN KEY(loanID) REFERENCES LOAN(loanID))""")
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS SOCIALROOM (
        roomID TEXT PRIMARY KEY, roomName TEXT NOT NULL, capacity INTEGER NOT NULL,
        branchID TEXT NOT NULL, FOREIGN KEY(branchID) REFERENCES BRANCH(branchID))""")
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS EVENT (
        eventID TEXT PRIMARY KEY, eventName TEXT NOT NULL, eventType TEXT NOT NULL,
        eventDate TEXT NOT NULL CHECK(eventDate GLOB '[0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]'),
        eventCapacity INTEGER NOT NULL, eventEnrolment INTEGER DEFAULT 0, recommendedAudience TEXT NOT NULL,
        roomID TEXT NOT NULL, FOREIGN KEY(roomID) REFERENCES SOCIALROOM(roomID))""")
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS ATTENDANCE (
        eventID TEXT NOT NULL, memberID TEXT NOT NULL, PRIMARY KEY (eventID, memberID),
        FOREIGN KEY(eventID) REFERENCES EVENT(eventID), FOREIGN KEY(memberID) REFERENCES MEMBER(memberID))""")
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS REQUESTS (
        requestID TEXT PRIMARY KEY, memberID TEXT NOT NULL, personnelID TEXT NOT NULL,
        requestDetails TEXT NOT NULL, requestComplete BOOLEAN DEFAULT 0,
        FOREIGN KEY(memberID) REFERENCES MEMBER(memberID), FOREIGN KEY(personnelID) REFERENCES PERSONNEL(personnelID))""")
    conn.commit()

# app functions
def db_find_item(search_term):
    cursor.execute("SELECT itemID, title, media, itemStatus FROM ITEM WHERE title LIKE ?", ('%' + search_term + '%',))
    return cursor.fetchall()

def db_borrow_item(member_id, item_id):
    if not (item_id and item_id.isdigit()):
        return "Error: Item ID must be a valid number."
        
    cursor.execute("SELECT itemStatus FROM ITEM WHERE itemID = ?", (item_id,))
    item = cursor.fetchone()
    if item and item[0].lower() == "available":
        loan_id = str(int(datetime.now().timestamp() * 1000))[:10]
        borrow_date = datetime.now().strftime("%Y-%m-%d")
        due_date = (datetime.now() + timedelta(days=30)).strftime("%Y-%m-%d")
        cursor.execute("INSERT INTO LOAN VALUES (?, ?, ?, ?, ?, ?)", (loan_id, borrow_date, due_date, None, item_id, member_id))
        cursor.execute("UPDATE ITEM SET itemStatus = 'Checked Out' WHERE itemID = ?", (item_id,))
        conn.commit()
        return f"Item successfully checked out. Your Loan ID is: {loan_id}"
    return "Error: Item is not available or does not exist."

def db_return_item(loan_id):
    if not (loan_id and loan_id.isdigit()):
        return "Error: Loan ID must be a valid number."
        
    cursor.execute("SELECT itemID FROM LOAN WHERE loanID = ? AND returnDate IS NULL", (loan_id,))
    result = cursor.fetchone()
    if result:
        item_id = result[0]
        return_date = datetime.now().strftime("%Y-%m-%d")
        cursor.execute("UPDATE LOAN SET returnDate = ? WHERE loanID = ?", (return_date, loan_id))
        cursor.execute("UPDATE ITEM SET itemStatus = 'Available' WHERE itemID = ?", (item_id,))
        conn.commit()
        return "Item returned successfully."
    return "Error: Active loan not found with that ID."

def db_donate_item(member_id, title, media, publisher, pub_date):
    try:
        # check iso8601
        datetime.strptime(pub_date, "%Y-%m-%d")
    except ValueError:
        return "Error: Invalid date format. Please use YYYY-MM-DD."

    acquisition_id = str(int(datetime.now().timestamp() * 1000))[:10]
    cursor.execute("SELECT branchID FROM MEMBER WHERE memberID = ?", (member_id,))
    branch_id = cursor.fetchone()[0]
    request_date = datetime.now().strftime("%Y-%m-%d")
    expected_arrival = (datetime.now() + timedelta(days=7)).strftime("%Y-%m-%d")
    
    cursor.execute("""
    INSERT INTO FUTUREACQUISITION (acquisitionID, title, media, publisher, publicationDate, branchID, requestDate, expectedArrival)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, (acquisition_id, title, media, publisher, pub_date, branch_id, request_date, expected_arrival))
    conn.commit()
    return "Thank you for your donation! It has been registered for future acquisition."

def db_find_event(search_term):
    cursor.execute("SELECT eventID, eventName, eventType, eventDate, eventCapacity, eventEnrolment FROM EVENT WHERE eventName LIKE ?", ('%' + search_term + '%',))
    return cursor.fetchall()

def db_register_for_event(member_id, event_id):
    if not (event_id and event_id.isdigit()):
        return "Error: Event ID must be a valid number."

    cursor.execute("SELECT eventCapacity, eventEnrolment FROM EVENT WHERE eventID = ?", (event_id,))
    result = cursor.fetchone()
    if not result:
        return "Error: Event not found."
    if result[1] >= result[0]:
        return "Sorry, unable to register as the event is full."
    try:
        cursor.execute("INSERT INTO ATTENDANCE (eventID, memberID) VALUES (?, ?)", (event_id, member_id))
        cursor.execute("UPDATE EVENT SET eventEnrolment = eventEnrolment + 1 WHERE eventID = ?", (event_id,))
        conn.commit()
        return "Registered for the event successfully."
    except sqlite3.IntegrityError:
        return "Error: You are already registered for this event."

def db_volunteer_for_library(member_id):
    cursor.execute("SELECT firstName, lastName, phoneNum, branchID FROM MEMBER WHERE memberID = ?", (member_id,))
    member = cursor.fetchone()
    first_name, last_name, phone_num, branch_id = member
    
    # check if the member already has a personnel record
    cursor.execute("SELECT personnelID FROM PERSONNEL WHERE firstName = ? AND lastName = ? AND phoneNum = ?", (first_name, last_name, phone_num))
    if cursor.fetchone():
        return "You already have a personnel or volunteer record with us!"

    new_personnel_id = str(int(member_id) + 8888)
    cursor.execute("""
        INSERT INTO PERSONNEL (personnelID, firstName, lastName, jobTitle, hireDate, salary, phoneNum, branchID, volunteer)
        VALUES (?, ?, ?, 'Volunteer', ?, 0, ?, ?, 1)
    """, (new_personnel_id, first_name, last_name, datetime.now().strftime("%Y-%m-%d"), phone_num, branch_id))
    conn.commit()
    return f"Thank you for volunteering! A staff member will contact you. Your provisional personnel ID is: {new_personnel_id}"

def db_ask_for_help(member_id, request_details):
    cursor.execute("SELECT personnelID FROM PERSONNEL WHERE jobTitle = 'Librarian' ORDER BY RANDOM() LIMIT 1")
    personnel_id_tuple = cursor.fetchone()
    if not personnel_id_tuple:
        return "Error: No librarians are available to handle requests at this time."
    personnel_id = personnel_id_tuple[0]
    request_id = str(int(datetime.now().timestamp() * 1000))[:10]
    cursor.execute("INSERT INTO REQUESTS VALUES (?, ?, ?, ?, 0)", (request_id, member_id, personnel_id, request_details))
    conn.commit()
    return "Your help request has been submitted. A librarian will get back to you soon."

def db_view_activity(member_id):
    # active loans
    cursor.execute("""
        SELECT LOAN.loanID, ITEM.title, LOAN.borrowDate, LOAN.dueDate
        FROM LOAN JOIN ITEM ON LOAN.itemID = ITEM.itemID
        WHERE LOAN.memberID = ? AND LOAN.returnDate IS NULL
    """, (member_id,))
    active_loans = cursor.fetchall()
    # unpaid fines
    cursor.execute("""
        SELECT L.loanID, F.fineAmount, F.reason, F.dueDate
        FROM FINE F JOIN LOAN L ON F.loanID = L.loanID
        WHERE L.memberID = ? AND F.paid = 0
    """, (member_id,))
    fines = cursor.fetchall()
    # registered events
    cursor.execute("""
        SELECT E.eventName, E.eventDate, E.eventType
        FROM EVENT E JOIN ATTENDANCE A ON E.eventID = A.eventID
        WHERE A.memberID = ?
        ORDER BY E.eventDate
    """, (member_id,))
    registered_events = cursor.fetchall()
    # volunteer status by checking for a matching personnel record
    cursor.execute("SELECT firstName, lastName, phoneNum FROM MEMBER WHERE memberID = ?", (member_id,))
    member_details = cursor.fetchone()
    volunteer_status = None
    if member_details:
        first_name, last_name, phone_num = member_details
        cursor.execute("""
            SELECT personnelID, hireDate FROM PERSONNEL
            WHERE firstName = ? AND lastName = ? AND phoneNum = ? AND volunteer = 1
        """, (first_name, last_name, phone_num))
        volunteer_record = cursor.fetchone()
        if volunteer_record:
            volunteer_status = volunteer_record

    return active_loans, fines, registered_events, volunteer_status

def db_login(user_id_input):
    if not (user_id_input and user_id_input.isdigit() and len(user_id_input) == 10):
        return None, "Invalid input. Please enter a valid 10-digit NUMERIC Member ID."
    cursor.execute("SELECT memberID, firstName FROM MEMBER WHERE memberID = ?", (user_id_input,))
    member_record = cursor.fetchone()
    if member_record:
        return member_record, f"Welcome back, {member_record[1]}!"
    return None, "Member not found. Please try again."

# qt6 ui
class LibraryUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.current_user_id = None
        self.current_user_name = None
        self.setWindowTitle("Toronto Alternative Library")
        self.setGeometry(100, 100, 900, 600)
        
        self.stacked_widget = QStackedWidget()
        self.setCentralWidget(self.stacked_widget)
        
        self.init_login_ui()
        self.init_main_ui()

    def init_login_ui(self):
        login_widget = QWidget()
        layout = QVBoxLayout(login_widget)
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.setSpacing(15)

        title = QLabel("Toronto Alternative Library Login")
        title.setFont(QFont("Arial", 24))
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        self.member_id_input = QLineEdit()
        self.member_id_input.setPlaceholderText("Enter your 10-digit member ID (e.g., 1000000000)")
        self.member_id_input.setFont(QFont("Arial", 12))
        self.member_id_input.setFixedWidth(400)
        self.member_id_input.returnPressed.connect(self.handle_login) # gotta let the user press enter to log in
        
        login_button = QPushButton("Log In")
        login_button.setFont(QFont("Arial", 12))
        login_button.setFixedWidth(200)
        login_button.clicked.connect(self.handle_login)
        
        layout.addWidget(title)
        layout.addWidget(self.member_id_input, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(login_button, alignment=Qt.AlignmentFlag.AlignCenter)
        
        self.stacked_widget.addWidget(login_widget)

    def init_main_ui(self):
        main_widget = QWidget()
        main_layout = QHBoxLayout(main_widget)
        
        controls_layout = QVBoxLayout()
        controls_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        controls_layout.setSpacing(10)
        
        self.welcome_label = QLabel()
        self.welcome_label.setFont(QFont("Arial", 16, QFont.Weight.Bold))
        
        # buttons for the menu
        buttons = {
            "View My Activity": self.handle_view_activity,
            "Find an Item": self.handle_find_item,
            "Borrow an Item": self.handle_borrow_item,
            "Return an Item": self.handle_return_item,
            "Find an Event": self.handle_find_event,
            "Register for Event": self.handle_register_for_event,
            "Donate an Item": self.handle_donate_item,
            "Volunteer With Us": self.handle_volunteer,
            "Ask for Help": self.handle_ask_for_help,
            "Log Out": self.handle_logout
        }

        controls_layout.addWidget(self.welcome_label)

        for text, handler in buttons.items():
            button = QPushButton(text)
            button.setFont(QFont("Arial", 11))
            button.clicked.connect(handler)
            controls_layout.addWidget(button)

        # display portion of the ui
        display_layout = QVBoxLayout()
        display_title = QLabel("Results")
        display_title.setFont(QFont("Arial", 16, QFont.Weight.Bold))
        self.results_display = QTextEdit()
        self.results_display.setReadOnly(True)
        self.results_display.setFont(QFont("Courier New", 11))
        
        display_layout.addWidget(display_title)
        display_layout.addWidget(self.results_display)
        
        main_layout.addLayout(controls_layout, 1) # controls get the left quarter
        main_layout.addLayout(display_layout, 3)  # info/display gets the rest
        
        self.stacked_widget.addWidget(main_widget)

    def handle_login(self):
        user_id = self.member_id_input.text().strip()
        user_record, message = db_login(user_id)
        
        if user_record:
            self.current_user_id, self.current_user_name = user_record
            self.welcome_label.setText(f"Welcome, {self.current_user_name}!")
            self.results_display.setText("Select an option from the left to get started.")
            QMessageBox.information(self, "Login Successful", message)
            self.stacked_widget.setCurrentIndex(1) # switch to the main ui
        else:
            QMessageBox.warning(self, "Login Failed", message)
        self.member_id_input.clear()

    def handle_logout(self):
        self.current_user_id = None
        self.current_user_name = None
        self.stacked_widget.setCurrentIndex(0) # switch back to the login page
        QMessageBox.information(self, "Logged Out", "You have been successfully logged out.")

    def handle_view_activity(self):
        loans, fines, events, volunteer_status = db_view_activity(self.current_user_id)
        
        output = "--- YOUR ACTIVE LOANS ---\n"
        if loans:
            for loan in loans:
                output += f"  Loan ID: {loan[0]}\n  Title: {loan[1]}\n  Borrowed: {loan[2]}, Due: {loan[3]}\n\n"
        else:
            output += "No active loans found.\n\n"
        
        output += "--- YOUR UNPAID FINES ---\n"
        if fines:
            for fine in fines:
                output += f"  Loan ID: {fine[0]}\n  Amount: ${fine[1]:.2f}\n  Reason: {fine[2]}\n  Due: {fine[3]}\n\n"
        else:
            output += "No unpaid fines found.\n\n"

        output += "--- YOUR REGISTERED EVENTS ---\n"
        if events:
            for event in events:
                output += f"  Event: {event[0]} ({event[2]})\n  Date: {event[1]}\n\n"
        else:
            output += "You are not registered for any upcoming events.\n\n"

        output += "--- YOUR VOLUNTEER STATUS ---\n"
        if volunteer_status:
            output += f"You are a registered volunteer!\n  Personnel ID: {volunteer_status[0]}\n  Start Date: {volunteer_status[1]}\n"
        else:
            output += "You are not currently registered as a volunteer.\n"
            
        self.results_display.setText(output)

    def handle_find_item(self):
        text, ok = QInputDialog.getText(self, "Find Item", "Enter title or keyword:")
        if ok and text:
            results = db_find_item(text)
            if results:
                output = "--- ITEMS FOUND ---\n"
                for item in results:
                    output += f"ID: {item[0]}\nTitle: {item[1]}\nMedia: {item[2]}, Status: {item[3]}\n\n"
                self.results_display.setText(output)
            else:
                self.results_display.setText("No items found matching your search.")

    def handle_borrow_item(self):
        text, ok = QInputDialog.getText(self, "Borrow Item", "Enter the Item ID to borrow:")
        if ok and text:
            message = db_borrow_item(self.current_user_id, text)
            QMessageBox.information(self, "Borrow Status", message)
            self.handle_view_activity() # refresh

    def handle_return_item(self):
        text, ok = QInputDialog.getText(self, "Return Item", "Enter your Loan ID to return:")
        if ok and text:
            message = db_return_item(text)
            QMessageBox.information(self, "Return Status", message)
            self.handle_view_activity() # refresh

    def handle_find_event(self):
        text, ok = QInputDialog.getText(self, "Find Event", "Enter event name or keyword:")
        if ok and text:
            results = db_find_event(text)
            if results:
                output = "--- EVENTS FOUND ---\n"
                for event in results:
                    output += f"ID: {event[0]}\nName: {event[1]}\nType: {event[2]}, Date: {event[3]}\n"
                    output += f"  Capacity: {event[4]}, Enrolled: {event[5]}\n\n"
                self.results_display.setText(output)
            else:
                self.results_display.setText("No events found matching your search.")

    def handle_register_for_event(self):
        text, ok = QInputDialog.getText(self, "Register for Event", "Enter the Event ID to register for:")
        if ok and text:
            message = db_register_for_event(self.current_user_id, text)
            QMessageBox.information(self, "Event Registration", message)
            self.handle_view_activity() # refresh

    def handle_donate_item(self):
        title, ok1 = QInputDialog.getText(self, "Donate Item - Step 1/4", "Enter Title:")
        if not ok1 or not title: return
        
        media, ok2 = QInputDialog.getText(self, "Donate Item - Step 2/4", "Enter Media Type (Book, DVD, etc.):")
        if not ok2 or not media: return

        publisher, ok3 = QInputDialog.getText(self, "Donate Item - Step 3/4", "Enter Publisher:")
        if not ok3 or not publisher: return

        pub_date, ok4 = QInputDialog.getText(self, "Donate Item - Step 4/4", "Enter Item Publication Date (YYYY-MM-DD):")
        if not ok4 or not pub_date: return

        message = db_donate_item(self.current_user_id, title, media, publisher, pub_date)
        QMessageBox.information(self, "Donation Status", message)

    def handle_volunteer(self):
        reply = QMessageBox.question(self, "Volunteer", "Are you sure you want to register as a volunteer?", 
                                     QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        if reply == QMessageBox.StandardButton.Yes:
            message = db_volunteer_for_library(self.current_user_id)
            QMessageBox.information(self, "Volunteer Registration", message)
            self.handle_view_activity() # refresh

    def handle_ask_for_help(self):
        text, ok = QInputDialog.getMultiLineText(self, "Help Request", "Please describe your help request:")
        if ok and text:
            message = db_ask_for_help(self.current_user_id, text)
            QMessageBox.information(self, "Help Request Submitted", message)

    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Exit', 'Are you sure you want to exit?',
                                     QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
                                     QMessageBox.StandardButton.No)
        if reply == QMessageBox.StandardButton.Yes:
            conn.close()
            event.accept()
        else:
            event.ignore()

def setup_database():
    create_tables()
    cursor.execute("SELECT COUNT(*) FROM BRANCH")
    if cursor.fetchone()[0] == 0:
        print("Database is empty. Populating with dummy data...")
        cursor.executemany("INSERT INTO BRANCH VALUES (?, ?, ?, ?)", branch_data)
        cursor.executemany("INSERT INTO PERSONNEL VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", personnel_data)
        cursor.executemany("INSERT INTO ITEM VALUES (?, ?, ?, ?, ?, ?, ?, ?)", item_data)
        cursor.executemany("INSERT INTO MEMBER VALUES (?, ?, ?, ?, ?, ?, ?, ?)", member_data)
        cursor.executemany("INSERT INTO LOAN VALUES (?, ?, ?, ?, ?, ?)", loan_data)
        cursor.executemany("INSERT INTO FUTUREACQUISITION VALUES (?, ?, ?, ?, ?, ?, ?, ?)", futureacquisition_data)
        cursor.executemany("INSERT INTO FINE VALUES (?, ?, ?, ?, ?, ?)", fine_data)
        cursor.executemany("INSERT INTO SOCIALROOM VALUES (?, ?, ?, ?)", socialroom_data)
        cursor.executemany("INSERT INTO EVENT VALUES (?, ?, ?, ?, ?, ?, ?, ?)", event_data)
        cursor.executemany("INSERT INTO ATTENDANCE VALUES (?, ?)", attendance_data)
        cursor.executemany("INSERT INTO REQUESTS VALUES (?, ?, ?, ?, ?)", requests_data)
        conn.commit()
        print("Data population complete.")

if __name__ == '__main__':
    # load the database if it exists, or create a new one
    setup_database()
    
    app = QApplication(sys.argv)
    window = LibraryUI()
    window.show()
    sys.exit(app.exec())