# default test user ID: 1000000000
# other values can be found as you go thru :)
# if you don't have library.db, our script will create it for you
# if you have it, it will just connect to it. make sure it's the one we provided so that the schema is correct!!!

import sqlite3
from datetime import datetime
from datetime import timedelta

conn = sqlite3.connect("library.db")
cursor = conn.cursor()

cursor.execute("PRAGMA foreign_keys = ON;")

# sample data
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
    ('9348510276', '1000000000'),
    ('8124753096', '2043251122'),
    ('6792053841', '4433034856'),
    ('5618392740', '4832957132'),
    ('4205739182', '4123875892'),
    ('3891762540', '1312890592'),
    ('7483921560', '9896457833'),
    ('9357164820', '4728396831'),
    ('6028471935', '5347896932'),
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
        branchID TEXT PRIMARY KEY,
        branchName TEXT NOT NULL,
        branchAddress TEXT NOT NULL,
        phoneNum TEXT NOT NULL
    )
    """)
    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS MEMBER (
        memberID TEXT PRIMARY KEY,
        firstName TEXT NOT NULL,
        lastName TEXT NOT NULL,
        memberAddress TEXT NOT NULL,
        phoneNum TEXT NOT NULL,
        email TEXT NOT NULL,
        membershipDate TEXT NOT NULL CHECK(membershipDate GLOB '[0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]'),
        branchID TEXT NOT NULL,
        FOREIGN KEY(branchID) REFERENCES BRANCH(branchID)
    )
    """)
    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS PERSONNEL (
        personnelID TEXT PRIMARY KEY,
        firstName TEXT NOT NULL,
        lastName TEXT NOT NULL,
        jobTitle TEXT NOT NULL,
        hireDate TEXT NOT NULL CHECK(hireDate GLOB '[0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]'),
        salary INTEGER NOT NULL,
        phoneNum TEXT NOT NULL,
        branchID TEXT NOT NULL,
        volunteer BOOLEAN DEFAULT 0,
        FOREIGN KEY(branchID) REFERENCES BRANCH(branchID)
    )
    """)
    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS ITEM (
        itemID TEXT PRIMARY KEY,
        title TEXT NOT NULL,
        media TEXT NOT NULL,
        itemStatus TEXT NOT NULL,
        publisher TEXT NOT NULL,
        genre TEXT NOT NULL,
        publicationDate TEXT NOT NULL CHECK(publicationDate GLOB '[0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]'),
        branchID TEXT NOT NULL,
        FOREIGN KEY(branchID) REFERENCES BRANCH(branchID)
    )
    """)
    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS FUTUREACQUISITION (
        acquisitionID TEXT PRIMARY KEY,
        title TEXT NOT NULL,
        media TEXT NOT NULL,
        publisher TEXT NOT NULL,
        publicationDate TEXT NOT NULL CHECK(publicationDate GLOB '[0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]'),
        branchID TEXT NOT NULL,
        requestDate TEXT NOT NULL CHECK(requestDate GLOB '[0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]'),
        expectedArrival TEXT NOT NULL CHECK(expectedArrival GLOB '[0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]'),
        FOREIGN KEY(branchID) REFERENCES BRANCH(branchID)
    )
    """)
    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS LOAN (
        loanID TEXT PRIMARY KEY,
        borrowDate TEXT NOT NULL CHECK(borrowDate GLOB '[0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]'),
        dueDate TEXT NOT NULL CHECK(dueDate GLOB '[0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]'),
        returnDate TEXT DEFAULT NULL CHECK(returnDate IS NULL OR returnDate GLOB '[0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]'),
        itemID TEXT NOT NULL,
        memberID TEXT NOT NULL,
        FOREIGN KEY(itemID) REFERENCES ITEM(itemID),
        FOREIGN KEY(memberID) REFERENCES MEMBER(memberID)
    )
    """)
    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS FINE (
        loanID TEXT PRIMARY KEY,
        fineAmount REAL NOT NULL,
        reason TEXT NOT NULL,
        issueDate TEXT NOT NULL CHECK(issueDate GLOB '[0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]'),
        dueDate TEXT NOT NULL CHECK(dueDate GLOB '[0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]'),
        paid BOOLEAN DEFAULT 0,
        FOREIGN KEY(loanID) REFERENCES LOAN(loanID)
    )
    """)
    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS SOCIALROOM (
        roomID TEXT PRIMARY KEY,
        roomName TEXT NOT NULL,
        capacity INTEGER NOT NULL,
        branchID TEXT NOT NULL,
        FOREIGN KEY(branchID) REFERENCES BRANCH(branchID)
    )
    """)
    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS EVENT (
        eventID TEXT PRIMARY KEY,
        eventName TEXT NOT NULL,
        eventType TEXT NOT NULL,
        eventDate TEXT NOT NULL CHECK(eventDate GLOB '[0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]'),
        eventCapacity INTEGER NOT NULL,
        eventEnrolment INTEGER DEFAULT 0,
        recommendedAudience TEXT NOT NULL,
        roomID TEXT NOT NULL,
        FOREIGN KEY(roomID) REFERENCES SOCIALROOM(roomID)
    )
    """)
    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS ATTENDANCE (
        eventID TEXT NOT NULL,
        memberID TEXT NOT NULL,
        PRIMARY KEY (eventID, memberID),
        FOREIGN KEY(eventID) REFERENCES EVENT(eventID),
        FOREIGN KEY(memberID) REFERENCES MEMBER(memberID)
    )
    """)
    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS REQUESTS (
        requestID TEXT PRIMARY KEY,
        memberID TEXT NOT NULL,
        personnelID TEXT NOT NULL,
        requestDetails TEXT NOT NULL,
        requestComplete BOOLEAN DEFAULT 0,
        FOREIGN KEY(memberID) REFERENCES MEMBER(memberID),
        FOREIGN KEY(personnelID) REFERENCES PERSONNEL(personnelID)
    )
    """)
    
    conn.commit()

# application functions

def find_item():
    search_term = input("Enter the title or keyword to search for an item: ")
    cursor.execute("SELECT itemID, title, media, itemStatus FROM ITEM WHERE title LIKE ?", ('%' + search_term + '%',))
    results = cursor.fetchall()
    if results:
        print("Items found:")
        for row in results:
            print(f"ID: {row[0]}, Title: {row[1]}, Media: {row[2]}, Status: {row[3]}")
    else:
        print("No items found.")

def borrow_item(user_id):
    member_id = user_id
    item_id = input("Enter the item ID of the item you want to borrow: ")
    # generate a new 10 digit loan ID
    loan_id = str(int(datetime.now().timestamp() * 1000))[:10]
    borrow_date = datetime.now().strftime("%Y-%m-%d")
    # due date in 30 days
    due_date = (datetime.now() + timedelta(days=30)).strftime("%Y-%m-%d")
    
    # check if item requested is available
    cursor.execute("SELECT itemStatus FROM ITEM WHERE itemID = ?", (item_id,))
    item = cursor.fetchone()
    if item and item[0].lower() == "available":
        # add record to loan table (using NULL for returnDate)
        cursor.execute("""
            INSERT INTO LOAN (loanID, borrowDate, dueDate, returnDate, itemID, memberID) 
            VALUES (?, ?, ?, ?, ?, ?)
        """, (loan_id, borrow_date, due_date, None, item_id, member_id))
        # mark item as Checked Out
        cursor.execute("UPDATE ITEM SET itemStatus = 'Checked Out' WHERE itemID = ?", (item_id,))
        conn.commit()
        print("Item successfully checked out.")
    else:
        print("Item is not available or does not exist.")

def return_item():
    loan_id = input("Enter your loan ID: ")
    # if loan is not found, return
    cursor.execute("SELECT * FROM LOAN WHERE loanID = ?", (loan_id,))
    if not cursor.fetchone():
        print("Loan not found.")
        return
    return_date = datetime.now().strftime("%Y-%m-%d")
    
    cursor.execute("UPDATE LOAN SET returnDate = ? WHERE loanID = ?", (return_date, loan_id))
    
    # mark item as available
    cursor.execute("SELECT itemID FROM LOAN WHERE loanID = ?", (loan_id,))
    result = cursor.fetchone()
    if result:
        item_id = result[0]
        cursor.execute("UPDATE ITEM SET itemStatus = 'Available' WHERE itemID = ?", (item_id,))
    conn.commit()
    print("Item returned successfully.")

def donate_item(user_id):
    # generate a new item ID
    acquisition_id = str(int(datetime.now().timestamp() * 1000))[:10]
    title = input("Enter the title: ")
    media = input("Enter the media type: ")
    publisher = input("Enter the publisher: ")
    publication_date = input("Enter the publication date (YYYY-MM-DD): ")
    # get branch ID from member ID
    member_id = user_id
    cursor.execute("SELECT branchID FROM MEMBER WHERE memberID = ?", (member_id,))
    branch_id = cursor.fetchone()[0]
    request_date = datetime.now().strftime("%Y-%m-%d")
    expected_arrival = (datetime.now() + timedelta(days=7)).strftime("%Y-%m-%d")
    
    # add record to future acquisition table
    cursor.execute("""
    INSERT INTO FUTUREACQUISITION (acquisitionID, title, media, publisher, publicationDate, requestDate, expectedArrival, branchID)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, (acquisition_id, title, media, publisher, publication_date, request_date, expected_arrival, branch_id))
    conn.commit()
    print("Thank you for your donation!")

def find_event():
    search_term = input("Enter event name or keyword to search for: ")
    cursor.execute("SELECT eventID, eventName, eventType, eventDate, eventCapacity, eventEnrolment FROM EVENT WHERE eventName LIKE ?", ('%' + search_term + '%',))
    results = cursor.fetchall()
    if results:
        print("Events found:")
        for row in results:
            print(f"ID: {row[0]}, Name: {row[1]}, Type: {row[2]}, Date: {row[3]}, Capacity: {row[4]}, Enrolment: {row[5]}")
    else:
        print("No events found.")

def register_for_event(user_id):
    member_id = user_id
    event_id = input("Enter the event ID to register for: ")
    # check if event exists
    cursor.execute("SELECT * FROM EVENT WHERE eventID = ?", (event_id,))
    if not cursor.fetchone():
        print("Event not found.")
        return
    # if event is full, return
    cursor.execute("SELECT eventCapacity, eventEnrolment FROM EVENT WHERE eventID = ?", (event_id,))
    result = cursor.fetchone()
    if result and result[1] >= result[0]:
        print("Sorry, unable to register as event is full.")
    try:
        cursor.execute("INSERT INTO ATTENDANCE (eventID, memberID) VALUES (?, ?)", (event_id, member_id))
        # increment event enrolment count
        cursor.execute("UPDATE EVENT SET eventEnrolment = eventEnrolment + 1 WHERE eventID = ?", (event_id,))
        conn.commit()
        print("Registered for event successfully.")
    except sqlite3.IntegrityError:
        print("Error: Either the event or member does not exist or you are already registered.")

def volunteer_for_library(user_id):
    # give the member a new personnel record with volunteer status
    member_id = user_id
    # get their existing details
    cursor.execute("SELECT firstName, lastName, phoneNum, branchID FROM MEMBER WHERE memberID = ?", (member_id,))
    member = cursor.fetchone()

    first_name, last_name, phone_num, branch_id = member
    try:
        # give the user a new personnelID equal to memberID + 8888
        new_personnel_id = str(int(member_id) + 8888)
    except ValueError:
        print("Invalid member ID format. It must be numeric.")
        return
    # add record to PERSONNEL table
    cursor.execute("""
        INSERT INTO PERSONNEL (personnelID, firstName, lastName, jobTitle, hireDate, salary, phoneNum, branchID, volunteer)
        VALUES (?, ?, ?, 'Volunteer', ?, 0, ?, ?, 1)
    """, (new_personnel_id, first_name, last_name, datetime.now().strftime("%Y-%m-%d"), phone_num, branch_id))

    conn.commit()
    print("Thank you for your interest in volunteering! A staff member will contact you to provide further information. Your provisional personnel ID is:", new_personnel_id)

def ask_for_help(user_id):
    member_id = user_id
    # randomly assign a personnel ID for the request
    cursor.execute("SELECT personnelID FROM PERSONNEL WHERE jobTitle = 'Librarian' ORDER BY RANDOM() LIMIT 1")
    personnel_id = cursor.fetchone()[0]
    # generate a new 10 digit request ID
    request_id = str(int(datetime.now().timestamp() * 1000))[:10]
    request_details = input("Describe your help request: ")

    cursor.execute("""
    INSERT INTO REQUESTS (requestID, memberID, personnelID, requestDetails, requestComplete)
    VALUES (?, ?, ?, ?, 0)
    """, (request_id, member_id, personnel_id, request_details))
    conn.commit()
    print("Your help request has been submitted. A librarian will get back to you soon.")

def view_loans_and_fines(user_id):
    member_id = user_id
    
    # get active loans
    cursor.execute("""
        SELECT LOAN.loanID, ITEM.title, LOAN.borrowDate, LOAN.dueDate, LOAN.returnDate
        FROM LOAN
        LEFT JOIN ITEM ON LOAN.itemID = ITEM.itemID
        WHERE LOAN.memberID = ? AND LOAN.returnDate IS NULL
    """, (member_id,))
    active_loans = cursor.fetchall()

    # get fines for ALL loans
    cursor.execute("""
        SELECT LOAN.loanID, FINE.fineAmount, FINE.reason
        FROM LOAN
        LEFT JOIN FINE ON LOAN.loanID = FINE.loanID
        WHERE LOAN.memberID = ? AND FINE.fineAmount IS NOT NULL AND FINE.paid = 0
    """, (member_id,))
    fines = cursor.fetchall()

    if active_loans:
        print("\nYour Active Loans:")
        for loan in active_loans:
            print(f"Loan ID: {loan[0]}, Title: {loan[1]}, Borrow Date: {loan[2]}, Due Date: {loan[3]}, Return Date: {loan[4]}")
    else:
        print("\nNo active loans.")

    if fines:
        print("\nYour Fines:")
        for fine in fines:
            print(f"Loan ID: {fine[0]}, Fine Amount: ${fine[1]:.2f}, Reason: {fine[2]}")
    else:
        print("\nNo fines.")

def menu():
    print("\nToronto Alternative Library\nLibrary Application Menu")
    print("1. Find an item")
    print("2. Borrow an item")
    print("3. View my loans and fines")
    print("4. Return a borrowed item")
    print("5. Donate an item")
    print("6. Find an event")
    print("7. Register for an event")
    print("8. Volunteer for the library")
    print("9. Ask for help from a librarian")
    print("0. Log out")
    print("X. Log out and exit the application")

def main():
    create_tables()
    
    # insert sample data if tables are empty
    cursor.execute("SELECT COUNT(*) FROM BRANCH")
    if cursor.fetchone()[0] == 0:
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

    while True:
        user_id_input = input("Enter your 10-digit member ID to log in: ").strip()
        if not user_id_input:
            print("Member ID must not be empty, please try again.")
            continue
        if not user_id_input.isdigit(): # bc all of the member IDs are 10 digit strings
            print("Invalid input. Please enter a valid 10-digit NUMERIC Member ID.")
            continue

        cursor.execute("SELECT memberID, firstName FROM MEMBER WHERE memberID = ?", (user_id_input,))
        member_record = cursor.fetchone()
        if member_record:
            user_id, user_first_name = member_record
            print(f"Welcome back, {user_first_name}!")
            break
        else:
            print("Member not found. Please try again.")

    while True:

        menu()
        choice = input("Select an option (1-9) and press enter: ")
        if choice == "1":
            find_item()
        elif choice == "2":
            borrow_item(user_id)
        elif choice == "3":
            view_loans_and_fines(user_id)
        elif choice == "4":
            return_item()
        elif choice == "5":
            donate_item(user_id)
        elif choice == "6":
            find_event()
        elif choice == "7":
            register_for_event(user_id)
        elif choice == "8":
            volunteer_for_library(user_id)
        elif choice == "9":
            ask_for_help(user_id)
        elif choice == "0":
            print("Logging out. Goodbye! Thanks for using Toronto Alternative Library.")
            main()
        elif choice == "X" or choice == "x":
            print("Goodbye! Thanks for using Toronto Alternative Library.")
            exit(0)
        else:
            print("Invalid option, please try again.")

if __name__ == '__main__':
    main()
    conn.close()