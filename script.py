import sqlite3
 
# Replace 'example.db' with the path to your SQLite database file
db_file = 'taxi.db'

# Establish a connection to the SQLite database
conn = sqlite3.connect(db_file)

# Create a cursor object to interact with the database
cursor = conn.cursor()

# SQL script containing table creation and data insertion statements
sql_script = """
PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS TAXI ( 
    Taxi_id INTEGER PRIMARY KEY, 
    Registration_no TEXT UNIQUE, 
    Model TEXT, 
    Taxi_Year DATE, 
    Taxi_type TEXT, 
    Taxi_status TEXT, 
    Driver_id INTEGER,
    FOREIGN KEY (Driver_id) REFERENCES DRIVER(Driver_id) ON DELETE CASCADE
); 

CREATE TABLE IF NOT EXISTS USER_TBL ( 
    Usr_id INTEGER PRIMARY KEY, 
    F_name TEXT, 
    L_name TEXT, 
    Contat_no INTEGER, 
    Gender TEXT, 
    USR_Address TEXT, 
    Taxi_id INTEGER,
    FOREIGN KEY (Taxi_id) REFERENCES TAXI(Taxi_id) ON DELETE CASCADE
); 

CREATE TABLE IF NOT EXISTS DRIVER ( 
    Driver_id INTEGER PRIMARY KEY, 
    F_name TEXT, 
    L_name TEXT, 
    Gender TEXT, 
    Contact_no TEXT, 
    Rating INTEGER, 
    Age INTEGER 
); 

CREATE TABLE IF NOT EXISTS TRIP_DETAILS ( 
    Trip_id INTEGER PRIMARY KEY, 
    Trip_date DATE, 
    Trip_amt DECIMAL(10,2), 
    Driver_id INTEGER NOT NULL, 
    Usr_id INTEGER NOT NULL, 
    Taxi_id INTEGER NOT NULL, 
    Strt_time DATETIME, 
    End_time DATETIME,
    T_Source VARCHAR(20),
    T_Destination VARCHAR(20), 
    FOREIGN KEY (Driver_id) REFERENCES DRIVER(Driver_id) ON DELETE NO ACTION,
    FOREIGN KEY (Usr_id) REFERENCES USER_TBL(Usr_id) ON DELETE NO ACTION,
    FOREIGN KEY (Taxi_id) REFERENCES TAXI(Taxi_id) ON DELETE NO ACTION
); 

CREATE TABLE IF NOT EXISTS BILL_DETAILS ( 
    Bill_no INTEGER PRIMARY KEY, 
    Bill_date DATE, 
    Advance_amt DECIMAL(10,2), 
    Discount_amt DECIMAL(10,2), 
    Total_amt DECIMAL(10,2), 
    Usr_id INTEGER, 
    Trip_id INTEGER, 
    FOREIGN KEY (Usr_id) REFERENCES USER_TBL(Usr_id) ON DELETE CASCADE,
    FOREIGN KEY (Trip_id) REFERENCES TRIP_DETAILS(Trip_id) ON DELETE NO ACTION
); 

CREATE TABLE IF NOT EXISTS CUSTOMER_SERVICE ( 
    Emp_id INTEGER PRIMARY KEY, 
    F_name TEXT, 
    L_name TEXT 
); 

CREATE TABLE IF NOT EXISTS FEEDBACK ( 
    Fbk_id INTEGER PRIMARY KEY, 
    Message TEXT, 
    Email TEXT, 
    Emp_id INTEGER, 
    Usr_id INTEGER, 
    Trip_id INTEGER, 
    F_Type TEXT,
    FOREIGN KEY (Emp_id) REFERENCES CUSTOMER_SERVICE(Emp_id) ON DELETE CASCADE,
    FOREIGN KEY (Usr_id) REFERENCES USER_TBL(Usr_id) ON DELETE NO ACTION,
    FOREIGN KEY (Trip_id) REFERENCES TRIP_DETAILS(Trip_id) ON DELETE CASCADE
); 

CREATE TABLE IF NOT EXISTS OWNS ( 
    Owner_id INTEGER PRIMARY KEY, 
    No_Cars INTEGER 
);

CREATE TABLE IF NOT EXISTS OWNER_TAXI ( 
    Owner_id INTEGER, 
    Taxi_id INTEGER, 
    PRIMARY KEY (Owner_id, Taxi_id),
    FOREIGN KEY (Owner_id) REFERENCES OWNS(Owner_id) ON DELETE CASCADE,
    FOREIGN KEY (Taxi_id) REFERENCES TAXI(Taxi_id) ON DELETE CASCADE
); 

CREATE TABLE IF NOT EXISTS INDIVIDUAL ( 
    Ssn INTEGER PRIMARY KEY, 
    Name TEXT, 
    Owner_id INTEGER,
    FOREIGN KEY (Owner_id) REFERENCES OWNS(Owner_id) ON DELETE CASCADE
); 

CREATE TABLE IF NOT EXISTS TAXI_SERVICE_COMPANY ( 
    Tsc_id INTEGER PRIMARY KEY, 
    Tsc_name TEXT, 
    Owner_id INTEGER,
    FOREIGN KEY (Owner_id) REFERENCES OWNS(Owner_id) ON DELETE CASCADE
);

CREATE TABLE TMP_TRIP_DETAILS AS
SELECT * FROM TRIP_DETAILS;

DROP TABLE TRIP_DETAILS;

CREATE TABLE TRIP_DETAILS ( 
    Trip_id INTEGER PRIMARY KEY, 
    Trip_date DATE, 
    Trip_amt DECIMAL(10,2), 
    Driver_id INTEGER NOT NULL, 
    Usr_id INTEGER NOT NULL, 
    Taxi_id INTEGER NOT NULL, 
    Strt_time DATETIME, 
    End_time DATETIME,
    T_Source VARCHAR(20),
    T_Destination VARCHAR(20), 
    FOREIGN KEY (Driver_id) REFERENCES DRIVER(Driver_id) ON DELETE NO ACTION,
    FOREIGN KEY (Usr_id) REFERENCES USER_TBL(Usr_id) ON DELETE NO ACTION,
    FOREIGN KEY (Taxi_id) REFERENCES TAXI(Taxi_id) ON DELETE NO ACTION
);

INSERT INTO TRIP_DETAILS SELECT * FROM TMP_TRIP_DETAILS;

DROP TABLE TMP_TRIP_DETAILS;

"""
# Adding Constaints 
# Constraints are added during table creation in SQLite, so no modifications needed


# Adding the data into tables 
print("Table created successfully")
print("Inserting Data into Tables")

#  TAXI Insertion 
cursor.execute("INSERT OR IGNORE INTO TAXI (Taxi_id, Registration_no, Model, Taxi_Year, Taxi_type, Taxi_status, Driver_id) VALUES (1, 'GJ152004', 'BENZE', '2024-03-11', 'SUV', 'Available', NULL)")
cursor.execute("INSERT OR IGNORE INTO TAXI (Taxi_id, Registration_no, Model, Taxi_Year, Taxi_type, Taxi_status, Driver_id) VALUES (2, 'MH432010', 'MARUTI', '2024-03-12', 'Hatchback', 'Available', NULL)")
cursor.execute("INSERT OR IGNORE INTO TAXI (Taxi_id, Registration_no, Model, Taxi_Year, Taxi_type, Taxi_status, Driver_id) VALUES (3, 'DL678003', 'HYUNDAI', '2024-03-13', 'Sedan', 'Available', NULL)")
cursor.execute("INSERT OR IGNORE INTO TAXI (Taxi_id, Registration_no, Model, Taxi_Year, Taxi_type, Taxi_status, Driver_id) VALUES (4, 'KA987007', 'TATA', '2024-03-14', 'SUV', 'Available', NULL)")
cursor.execute("INSERT OR IGNORE INTO TAXI (Taxi_id, Registration_no, Model, Taxi_Year, Taxi_type, Taxi_status, Driver_id) VALUES (5, 'UP765005', 'MAHINDRA', '2024-03-15', 'SUV', 'Available', NULL)")
cursor.execute("INSERT OR IGNORE INTO TAXI (Taxi_id, Registration_no, Model, Taxi_Year, Taxi_type, Taxi_status, Driver_id) VALUES (6, 'TN876006', 'TOYOTA', '2024-03-16', 'Sedan', 'Available', NULL)")
cursor.execute("INSERT OR IGNORE INTO TAXI (Taxi_id, Registration_no, Model, Taxi_Year, Taxi_type, Taxi_status, Driver_id) VALUES (7, 'AP543001', 'HONDA', '2024-03-17', 'Hatchback', 'Available', NULL)")
cursor.execute("INSERT OR IGNORE INTO TAXI (Taxi_id, Registration_no, Model, Taxi_Year, Taxi_type, Taxi_status, Driver_id) VALUES (8, 'PB234008', 'FORD', '2024-03-18', 'SUV', 'Available', NULL)")
cursor.execute("INSERT OR IGNORE INTO TAXI (Taxi_id, Registration_no, Model, Taxi_Year, Taxi_type, Taxi_status, Driver_id) VALUES (9, 'HR654009', 'VOLKSWAGEN', '2024-03-19', 'Hatchback', 'Available', NULL)")
cursor.execute("INSERT OR IGNORE INTO TAXI (Taxi_id, Registration_no, Model, Taxi_Year, Taxi_type, Taxi_status, Driver_id) VALUES (10, 'MP876002', 'CHEVROLET', '2024-03-20', 'SUV', 'Available', NULL)")



# USER_TBL Insertion 
cursor.execute("INSERT OR IGNORE INTO USER_TBL VALUES(1, 'Yash', 'Taneja', 7987845578, 'Male', 'Chhindwara', 1)")
cursor.execute("INSERT OR IGNORE INTO USER_TBL VALUES(2, 'Riya', 'Sharma', 9090909090, 'Female', 'Delhi', 2)")
cursor.execute("INSERT OR IGNORE INTO USER_TBL VALUES(3, 'Amit', 'Singh', 9876543210, 'Male', 'Mumbai', 3)")
cursor.execute("INSERT OR IGNORE INTO USER_TBL VALUES(4, 'Priya', 'Patel', 8765432109, 'Female', 'Ahmedabad', 4)")
cursor.execute("INSERT OR IGNORE INTO USER_TBL VALUES(5, 'Kunal', 'Gupta', 7654321098, 'Male', 'Bangalore', 5)")

# TRIP_DETAILS Insertion */
cursor.execute("INSERT OR IGNORE INTO TRIP_DETAILS VALUES(1, '2024-03-11', 150.45, 1, 1, 1, '2024-03-11 12:00:00', '2024-03-11 13:05:00', 'Chhindwara', 'Sendhwa')")
cursor.execute("INSERT OR IGNORE INTO TRIP_DETAILS VALUES(2, '2024-03-13', 175.50, 2, 2, 2, '2024-03-13 12:00:00', '2024-03-13 13:05:00', 'Delhi', 'Mumbai')")
cursor.execute("INSERT OR IGNORE INTO TRIP_DETAILS VALUES(3, '2024-03-14', 200.00, 3, 3, 3, '2024-03-14 12:00:00', '2024-03-14 13:05:00', 'Kolkata', 'Chennai')")
cursor.execute("INSERT OR IGNORE INTO TRIP_DETAILS VALUES(4, '2024-03-15', 120.75, 4, 4, 4, '2024-03-15 12:00:00', '2024-03-15 13:05:00', 'Bangalore', 'Hyderabad')")
cursor.execute("INSERT OR IGNORE INTO TRIP_DETAILS VALUES(5, '2024-03-16', 95.25, 5, 5, 5, '2024-03-16 12:00:00', '2024-03-16 13:05:00', 'Pune', 'Ahmedabad')")

#  BILL_DETAILS Insertion */
cursor.execute("INSERT OR IGNORE INTO BILL_DETAILS VALUES(1, '2024-03-11', 100, 0, 50.45, 1, 1)")
cursor.execute("INSERT OR IGNORE INTO BILL_DETAILS VALUES(2, '2024-03-13', 100, 0, 75.50, 2, 2)")
cursor.execute("INSERT OR IGNORE INTO BILL_DETAILS VALUES(3, '2024-03-14', 100, 0, 200.00, 3, 3)")
cursor.execute("INSERT OR IGNORE INTO BILL_DETAILS VALUES(4, '2024-03-15', 100, 0, 20.75, 4, 4)")
cursor.execute("INSERT OR IGNORE INTO BILL_DETAILS VALUES(5, '2024-03-16', 0, 0, 95.25, 5, 5)")
 

# Customer_Service Insertion */
cursor.execute("INSERT OR IGNORE INTO CUSTOMER_SERVICE VALUES(1, 'Madhav', 'Patel')")
cursor.execute("INSERT OR IGNORE INTO CUSTOMER_SERVICE VALUES(2, 'Aarav', 'Shah')")
cursor.execute("INSERT OR IGNORE INTO CUSTOMER_SERVICE VALUES(3, 'Diya', 'Verma')")
cursor.execute("INSERT OR IGNORE INTO CUSTOMER_SERVICE VALUES(4, 'Rohan', 'Singh')")
cursor.execute("INSERT OR IGNORE INTO CUSTOMER_SERVICE VALUES(5, 'Neha', 'Gupta')")

# FEEDBACK Insertion */
cursor.execute("INSERT OR IGNORE INTO FEEDBACK VALUES(1, 'so good', 'abhi@gmail.com', 1, 1, 1, 'good')")
cursor.execute("INSERT OR IGNORE INTO FEEDBACK VALUES(2, 'bad experience', 'john@example.com', 2, 2, 2, 'bad')")
cursor.execute("INSERT OR IGNORE INTO FEEDBACK VALUES(3, 'could be better', 'jane@example.com', 3, 3, 3, 'bad')")
cursor.execute("INSERT OR IGNORE INTO FEEDBACK VALUES(4, 'excellent service', 'smith@example.com', 4, 4, 4, 'good')")
cursor.execute("INSERT OR IGNORE INTO FEEDBACK VALUES(5, 'friendly staff', 'emma@example.com', 5, 5, 5, 'good')")


# owns Insertion */
cursor.execute("INSERT OR IGNORE INTO OWNS VALUES(1, 1)")
cursor.execute("INSERT OR IGNORE INTO OWNS VALUES(2, 2)")
cursor.execute("INSERT OR IGNORE INTO OWNS VALUES(3, 3)")
cursor.execute("INSERT OR IGNORE INTO OWNS VALUES(4, 4)")
cursor.execute("INSERT OR IGNORE INTO OWNS VALUES(5, 5)")

# OWNER_TAXI Insertion  */
cursor.execute("INSERT OR IGNORE INTO OWNER_TAXI VALUES (1, 1)")
cursor.execute("INSERT OR IGNORE INTO OWNER_TAXI VALUES (2, 2)")
cursor.execute("INSERT OR IGNORE INTO OWNER_TAXI VALUES (3, 3)")
cursor.execute("INSERT OR IGNORE INTO OWNER_TAXI VALUES (4, 4)")
cursor.execute("INSERT OR IGNORE INTO OWNER_TAXI VALUES (5, 5)")

# INDIVIDUAL Insertion
cursor.execute("INSERT OR IGNORE INTO INDIVIDUAL VALUES (123, 'abhi owner ind', 1)")
cursor.execute("INSERT OR IGNORE INTO INDIVIDUAL VALUES (456, 'john owner ind', 2)")
cursor.execute("INSERT OR IGNORE INTO INDIVIDUAL VALUES (789, 'harsh owner ind', 3)")
cursor.execute("INSERT OR IGNORE INTO INDIVIDUAL VALUES (101112, 'shan owner ind', 4)")
cursor.execute("INSERT OR IGNORE INTO INDIVIDUAL VALUES (131415, 'ramesh owner ind', 5)")

# TAXI_SERVICE_COMPANY Insertion
cursor.execute("INSERT OR IGNORE INTO TAXI_SERVICE_COMPANY VALUES (1, 'abhi taxi comp', 2)")
cursor.execute("INSERT OR IGNORE INTO TAXI_SERVICE_COMPANY VALUES (2, 'Raj Taxi Services', 3)")
cursor.execute("INSERT OR IGNORE INTO TAXI_SERVICE_COMPANY VALUES (3, 'Mumbai Cabs Pvt Ltd', 4)")
cursor.execute("INSERT OR IGNORE INTO TAXI_SERVICE_COMPANY VALUES (4, 'Delhi Taxi Solutions', 5)")
cursor.execute("INSERT OR IGNORE INTO TAXI_SERVICE_COMPANY VALUES (5, 'Bangalore Taxi Corp', 5)")

print("All data inserted successfully")

print("Running Queries")
print()

#Aggregate Functions: 
print("Agreggate Functions")
print()
cursor.execute("SELECT COUNT(DISTINCT Model) AS Total_Taxi_Models FROM TAXI;")
total_taxi_models = cursor.fetchone()[0]
print("Total number of taxi models available:", total_taxi_models)

# Query 2: Calculate the total number of trips made by a specific driver
cursor.execute("""
    SELECT DRIVER.Driver_id, COUNT(TRIP_DETAILS.Trip_id) AS Total_Trips
    FROM DRIVER
    LEFT JOIN TRIP_DETAILS ON DRIVER.Driver_id = TRIP_DETAILS.Driver_id
    GROUP BY DRIVER.Driver_id;
""")
driver_trips = cursor.fetchall()
print("Total trips made by each driver:")
for row in driver_trips:
    print("Driver ID:", row[0], "- Total Trips:", row[1])

# Query 3: Calculate the average age of drivers in the system
cursor.execute("SELECT AVG(Age) AS Average_Driver_Age FROM DRIVER;")
average_driver_age = cursor.fetchone()[0]
print("Average age of drivers:", average_driver_age)

# Query 4: Find the minimum trip amount recorded in the system
cursor.execute("SELECT MIN(Trip_amt) AS Min_Trip_Amount FROM TRIP_DETAILS;")
min_trip_amount = cursor.fetchone()[0]
print("Minimum trip amount recorded:", min_trip_amount)

# Query 5: Find the maximum rating achieved by any driver in the system
cursor.execute("SELECT MAX(Rating) AS Max_Driver_Rating FROM DRIVER;")
max_driver_rating = cursor.fetchone()[0]
print("Maximum rating achieved by any driver:", max_driver_rating)

# Query 6: Calculate the total number of trips made by each taxi type
cursor.execute("""
    SELECT TAXI.Taxi_type, COUNT(TRIP_DETAILS.Trip_id) AS Total_Trips
    FROM TAXI 
    INNER JOIN TRIP_DETAILS ON TAXI.Taxi_id = TRIP_DETAILS.Taxi_id 
    GROUP BY TAXI.Taxi_type;
""")
taxi_type_trips = cursor.fetchall()
print("Total trips made by each taxi type:")
for row in taxi_type_trips:
    print("Taxi Type:", row[0], "- Total Trips:", row[1])

# Query 7: Find the taxi types with more than 10 trips recorded
cursor.execute("""
    SELECT TAXI.Taxi_type, COUNT(TRIP_DETAILS.Trip_id) AS Total_Trips
    FROM TAXI 
    INNER JOIN TRIP_DETAILS ON TAXI.Taxi_id = TRIP_DETAILS.Taxi_id 
    GROUP BY TAXI.Taxi_type 
    HAVING COUNT(TRIP_DETAILS.Trip_id) > 10;
""")
taxi_type_more_than_10_trips = cursor.fetchall()
print("Taxi types with more than 10 trips recorded:")
for row in taxi_type_more_than_10_trips:
    print("Taxi Type:", row[0], "- Total Trips:", row[1])

# Query 8: List all unique taxi models available in the system
cursor.execute("SELECT DISTINCT Model FROM TAXI;")
unique_taxi_models = cursor.fetchall()
print("Unique taxi models available in the system:")
for row in unique_taxi_models:
    print(row[0])

# Joins
print()
print("Joins queries")
print()
cursor.execute("""
    SELECT TD.Trip_id, TD.Trip_date, TD.Strt_time, TD.End_time, 
    D.F_name AS Driver_FirstName, D.L_name AS Driver_LastName,
    D.Gender AS Driver_Gender, D.Conatct_no AS Driver_Contact, 
    U.F_name AS User_FirstName, U.L_name AS User_LastName, 
    U.Gender AS User_Gender, U.Contat_no AS User_Contact 
    FROM TRIP_DETAILS TD 
    INNER JOIN DRIVER D ON TD.Driver_id = D.Driver_id 
    INNER JOIN USER_TBL U ON TD.Usr_id = U.Usr_id;
""")
inner_join_result = cursor.fetchall()
print("Inner Join Result:")
for row in inner_join_result:
    print(row)

# Query 2: Left Join
cursor.execute("""
    SELECT T.Taxi_id, T.Registration_no, T.Model, T.Taxi_Year, 
    T.Taxi_type, T.Taxi_status, D.F_name AS Driver_FirstName, 
    D.L_name AS Driver_LastName, D.Gender AS Driver_Gender, 
    D.Conatct_no AS Driver_Contact 
    FROM TAXI T 
    LEFT JOIN DRIVER D ON T.Driver_id = D.Driver_id;
""")
left_join_result = cursor.fetchall()
print("\nLeft Join Result:")
for row in left_join_result:
    print(row)

# Query 3: Right Join
cursor.execute("""
    SELECT D.Driver_id, D.F_name, D.L_name, D.Gender, D.Conatct_no, 
    TD.Trip_id, TD.Trip_date, TD.Strt_time, TD.End_time 
    FROM DRIVER D 
    RIGHT JOIN TRIP_DETAILS TD ON D.Driver_id = TD.Driver_id;
""")
right_join_result = cursor.fetchall()
print("\nRight Join Result:")
for row in right_join_result:
    print(row)

# Query 4: Full Outer Join
cursor.execute("""
    SELECT T.Taxi_id, T.Registration_no, T.Model, T.Taxi_Year, 
    T.Taxi_type, T.Taxi_status, D.Driver_id, D.F_name AS Driver_FirstName, 
    D.L_name AS Driver_LastName, D.Gender AS Driver_Gender, 
    D.Conatct_no AS Driver_Contact, TD.Trip_id, TD.Trip_date, 
    TD.Strt_time, TD.End_time 
    FROM TAXI T 
    FULL OUTER JOIN DRIVER D ON T.Driver_id = D.Driver_id 
    FULL OUTER JOIN TRIP_DETAILS TD ON T.Taxi_id = TD.Taxi_id;
""")
full_outer_join_result = cursor.fetchall()
print("\nFull Outer Join Result:")
for row in full_outer_join_result:
    print(row)

# Set operations
print()
print("Set Operations")
print()
cursor.execute("""
    SELECT F_name AS Entity_Name FROM DRIVER 
    UNION 
    SELECT F_name AS Entity_Name FROM CUSTOMER_SERVICE;
""")
query1_result = cursor.fetchall()
print("Query 1 Result:")
for row in query1_result:
    print(row)

# Query 2: Find All Taxi Models Owned by Individual Owners but Not Owned by Taxi Service Companies
cursor.execute("""
    SELECT Name AS Entity_Name FROM INDIVIDUAL 
    EXCEPT 
    SELECT Tsc_name AS Entity_Name FROM TAXI_SERVICE_COMPANY;
""")
query2_result = cursor.fetchall()
print("\nQuery 2 Result:")
for row in query2_result:
    print(row)

# Query 3: Intersection of taxi IDs owned by individual owners and taxi IDs in the general taxi pool
cursor.execute("""
    SELECT Taxi_id FROM TAXI
    INTERSECT
    SELECT Taxi_id FROM OWNER_TAXI;
""")
query3_result = cursor.fetchall()
print("\nQuery 3 Result:")
for row in query3_result:
    print(row)

# Query 4: Retrieve a list of all unique taxi IDs, including those owned by individual owners and those managed by the taxi service company
cursor.execute("""
    SELECT Taxi_id FROM TAXI
    UNION
    SELECT Taxi_id FROM OWNER_TAXI;
""")
query4_result = cursor.fetchall()
print("\nQuery 4 Result:")
for row in query4_result:
    print(row)

# Group by and having clause
print()
print("Group by and having clause")
print()
# Query 1: Total number of trips made by each taxi, along with the average trip amount for taxis that have completed more than 10 trips
cursor.execute("""
    SELECT T.Taxi_id, COUNT(TD.Trip_id) AS Total_Trips, AVG(TD.Trip_amt) AS Average_Trip_Amount 
    FROM TAXI T 
    LEFT JOIN TRIP_DETAILS TD ON T.Taxi_id = TD.Taxi_id 
    GROUP BY T.Taxi_id 
    HAVING COUNT(TD.Trip_id) > 10;
""")
query1_result = cursor.fetchall()
print("Query 1 Result:")
for row in query1_result:
    print(row)

# Query 2: Total number of trips completed by each driver, along with their average rating
cursor.execute("""
    SELECT D.Driver_id, D.F_name, D.L_name, COUNT(TD.Trip_id) AS Total_Trips, AVG(D.Rating) AS Average_Rating 
    FROM DRIVER D 
    LEFT JOIN TRIP_DETAILS TD ON D.Driver_id = TD.Driver_id 
    GROUP BY D.Driver_id, D.F_name, D.L_name;
""")
query2_result = cursor.fetchall()
print("\nQuery 2 Result:")
for row in query2_result:
    print(row)

# Query 3: Users who have taken more than 5 trips and have spent a total amount greater than $500 on trips
cursor.execute("""
    SELECT U.Usr_id, U.F_name, U.L_name, COUNT(TD.Trip_id) AS Total_Trips, SUM(BD.Total_amt) AS Total_Amount_Spent 
    FROM USER_TBL U 
    LEFT JOIN TRIP_DETAILS TD ON U.Usr_id = TD.Usr_id 
    LEFT JOIN BILL_DETAILS BD ON U.Usr_id = BD.Usr_id 
    GROUP BY U.Usr_id, U.F_name, U.L_name 
    HAVING COUNT(TD.Trip_id) > 5 AND SUM(BD.Total_amt) > 500;
""")
query3_result = cursor.fetchall()
print("\nQuery 3 Result:")
for row in query3_result:
    print(row)

# Simple Queries
print()
print("Simple Queries")
print()
# Query 1: Retrieve the registration number, taxi model, and status of taxis driven by female drivers under the age of 30
cursor.execute("""
    SELECT T.Registration_no, T.Model, T.Taxi_status 
    FROM TAXI T 
    INNER JOIN DRIVER D ON T.Driver_id = D.Driver_id 
    WHERE D.Gender = 'Female' AND D.Age < 30;
""")
query1_result = cursor.fetchall()
print("Query 1 Result:")
for row in query1_result:
    print(row)

# Query 2: Retrieve the names and contact numbers of drivers who have received feedback messages containing the word "excellent"
cursor.execute("""
    SELECT D.F_name, D.L_name, D.Conatct_no 
    FROM DRIVER D 
    INNER JOIN FEEDBACK F ON D.Driver_id = F.Emp_id 
    WHERE F.Message LIKE '%excellent%';
""")
query2_result = cursor.fetchall()
print("\nQuery 2 Result:")
for row in query2_result:
    print(row)

# Query 3: Retrieve the names and addresses of users who have taken trips in taxis registered in 2022
cursor.execute("""
    SELECT U.F_name, U.L_name, U.USR_Address 
    FROM USER_TBL U 
    INNER JOIN TRIP_DETAILS TD ON U.Usr_id = TD.Usr_id 
    INNER JOIN TAXI T ON TD.Taxi_id = T.Taxi_id 
    WHERE T.Taxi_Year = '2022';
""")
query3_result = cursor.fetchall()
print("\nQuery 3 Result:")
for row in query3_result:
    print(row)

# Query 4: Retrieve the owner names and the total number of taxis they own, excluding owners who do not have any taxis
cursor.execute("""
    SELECT I.Name AS Owner_Name, O.No_Cars AS Total_Taxis_Owned 
    FROM INDIVIDUAL I 
    INNER JOIN OWNS O ON I.Owner_id = O.Owner_id 
    WHERE O.No_Cars > 0;
""")
query4_result = cursor.fetchall()
print("\nQuery 4 Result:")
for row in query4_result:
    print(row)

# Query 5: Retrieve all feedback provided by users and sort them based on the feedback, bad to good
cursor.execute("""
    SELECT F.Fbk_id, F.Message, F.Email, 
           CASE 
               WHEN F.Message LIKE '%poor%' THEN 'Poor'
               WHEN F.Message LIKE '%bad%' THEN 'Bad'
               WHEN F.Message LIKE '%average%' THEN 'Average'
               WHEN F.Message LIKE '%better%' THEN 'Average'
               WHEN F.Message LIKE '%good%' THEN 'Good'
               WHEN F.Message LIKE '%excellent%' THEN 'Excellent'
               WHEN F.Message LIKE '%best%' THEN 'Excellent'
               ELSE 'Unknown' 
           END AS Feedback_Rating
    FROM FEEDBACK F
    ORDER BY Feedback_Rating DESC;
""")
query5_result = cursor.fetchall()
print("\nQuery 5 Result:")
for row in query5_result:
    print(row)

# Nested Queries
print()
print("Nested Queries")
print()
# Query 1: Retrieve the names of users who have taken trips using taxis owned by individuals named "John"
cursor.execute("""
    SELECT DISTINCT U.F_name, U.L_name 
    FROM USER_TBL U 
    WHERE U.Usr_id IN ( 
        SELECT TD.Usr_id 
        FROM TRIP_DETAILS TD 
        WHERE TD.Taxi_id IN ( 
            SELECT OT.Taxi_id 
            FROM OWNER_TAXI OT 
            JOIN INDIVIDUAL I ON OT.Owner_id = I.Owner_id 
            WHERE I.Name = 'John' 
        )
    );
""")
query1_result = cursor.fetchall()
print("Query 1 Result:")
for row in query1_result:
    print(row)

# Query 2: Retrieve the total number of trips taken by users who have given feedback with a message containing the word "complaint"
cursor.execute("""
    SELECT COUNT(*) 
    FROM TRIP_DETAILS 
    WHERE Usr_id IN ( 
        SELECT DISTINCT Usr_id 
        FROM FEEDBACK 
        WHERE Message LIKE '%complaint%' 
    );
""")
query2_result = cursor.fetchone()
print("\nQuery 2 Result:")
print("Total trips taken by users who gave feedback with a complaint message:", query2_result[0])

# Query 3: Retrieve the names and contact numbers of drivers who have received feedback from users residing in "Chhindwara"
cursor.execute("""
    SELECT DISTINCT D.F_name, D.L_name, D.Conatct_no 
    FROM DRIVER D 
    WHERE D.Driver_id IN ( 
        SELECT DISTINCT F.Emp_id 
        FROM FEEDBACK F 
        JOIN USER_TBL U ON F.Usr_id = U.Usr_id 
        WHERE U.USR_Address LIKE '%Chhindwara%' 
    );
""")
query3_result = cursor.fetchall()
print("\nQuery 3 Result:")
for row in query3_result:
    print(row)

# Query 4: Retrieve the registration numbers of taxis driven by male drivers under the age of 25
cursor.execute("""
    SELECT DISTINCT T.Registration_no 
    FROM TAXI T 
    WHERE T.Driver_id IN ( 
        SELECT DISTINCT Driver_id 
        FROM DRIVER 
        WHERE Gender = 'Male' AND Age < 25 
    );
""")
query4_result = cursor.fetchall()
print("\nQuery 4 Result:")
for row in query4_result:
    print(row)

# update queries
print()
print("Update queries")
print()
# Update Driver's Contact Number
# driver_id = 'Driver_ID'
# new_contact_number = 'New_Contact_Number'
# cursor.execute("""
#     UPDATE DRIVER 
#     SET Conatct_no = ? 
#     WHERE Driver_id = ?
# """, (new_contact_number, driver_id))
# conn.commit()
# print("Driver's contact number updated successfully.")

# # Change Taxi Model for a Specific Taxi
# taxi_id = 'Taxi_ID'
# new_taxi_model = 'New_Taxi_Model'
# cursor.execute("""
#     UPDATE TAXI 
#     SET Model = ? 
#     WHERE Taxi_id = ?
# """, (new_taxi_model, taxi_id))
# conn.commit()
# print("Taxi model updated successfully.")

# # Update Trip Amount for a Specific Trip
# trip_id = 'Trip_ID'
# new_trip_amount = 'New_Trip_Amount'
# cursor.execute("""
#     UPDATE TRIP_DETAILS 
#     SET Trip_amt = ? 
#     WHERE Trip_id = ?
# """, (new_trip_amount, trip_id))
# conn.commit()
# print("Trip amount updated successfully.")

# # Update User's Address
# user_id = 'User_ID'
# new_address = 'New_Address'
# cursor.execute("""
#     UPDATE USER_TBL 
#     SET USR_Address = ? 
#     WHERE Usr_id = ?
# """, (new_address, user_id))
# conn.commit()
# print("User's address updated successfully.")

# # Change Taxi Status
# taxi_type = 'Taxi_Type'
# new_taxi_status = 'Unavailable'
# cursor.execute("""
#     UPDATE TAXI 
#     SET Taxi_status = ? 
#     WHERE Taxi_type = ?
# """, (new_taxi_status, taxi_type))

print()
print("Delete Queries")
print()
# Delete a Specific Taxi
# taxi_id = 'Taxi_ID'
# cursor.execute("DELETE FROM TAXI WHERE Taxi_id = ?", (taxi_id,))
# conn.commit()
# print("Taxi record deleted successfully.")

# # Remove a Driver Record
# driver_id = 'Driver_ID'
# cursor.execute("DELETE FROM DRIVER WHERE Driver_id = ?", (driver_id,))
# conn.commit()
# print("Driver record deleted successfully.")

# # Delete a User Record
# user_id = 'User_ID'
# cursor.execute("DELETE FROM USER_TBL WHERE Usr_id = ?", (user_id,))
# conn.commit()
# print("User record deleted successfully.")

# # Cancel a Trip
# trip_id = 'Trip_ID'
# cursor.execute("DELETE FROM TRIP_DETAILS WHERE Trip_id = ?", (trip_id,))
# conn.commit()
# print("Trip cancelled successfully.")

# # Remove an Individual Owner
# owner_id = 'Owner_ID'
# cursor.execute("DELETE FROM INDIVIDUAL WHERE Owner_id = ?", (owner_id,))
# conn.commit()
# print("Individual owner removed successfully.")

# Execute the SQL script
# cursor.executescript(sql_script)

# Commit the transaction
conn.commit()
print("Completed Successfully")
# Close the cursor and connection when done
cursor.close()
conn.close()
