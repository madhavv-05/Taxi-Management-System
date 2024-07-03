use Taxi_Service;
/* Table creation */

CREATE TABLE TAXI ( 
Taxi_id integer NOT NULL, 
Registration_no VARCHAR(20), 
Model VARCHAR(20), 
Taxi_Year DATE, 
Taxi_type VARCHAR(20), 
Taxi_status VARCHAR(20), 
Driver_id integer, 
PRIMARY KEY (Taxi_id), 
UNIQUE (Registration_no) 
); 


CREATE TABLE  USER_TBL ( 
Usr_id integer NOT NULL, 
F_name VARCHAR(20), 
L_name VARCHAR(20), 
Contat_no bigint, 
Gender VARCHAR(10), 
USR_Address VARCHAR(50), 
Taxi_id integer, 
PRIMARY KEY (Usr_id) 
); 

CREATE TABLE DRIVER ( 
Driver_id integer NOT NULL, 
F_name VARCHAR(10), 
L_name VARCHAR(20), 
Gender VARCHAR(10), 
Conatct_no VARCHAR(20), 
Rating integer, 
Age integer, 
PRIMARY KEY (Driver_id) 
); 

CREATE TABLE  TRIP_DETAILS ( 
Trip_id integer NOT NULL, 
Trip_date DATE, 
Trip_amt decimal(10,2), 
Driver_id integer, 
Usr_id integer, 
Taxi_id integer, 
Strt_time DATETIME, 
End_time DATETIME,
T_Source varchar(20),
T_Destination varchar(20), 
PRIMARY KEY (Trip_id) 
); 

CREATE TABLE BILL_DETAILS ( 
Bill_no integer NOT NULL, 
Bill_date DATE, 
Advance_amt decimal(10,2), 
Discount_amt decimal(10,2), 
Total_amt decimal(10,2), 
Usr_id integer, 
Trip_id integer, 
PRIMARY KEY (Bill_no), 
); 

CREATE TABLE  CUSTOMER_SERVICE ( 
Emp_id integer NOT NULL, 
F_name VARCHAR(20), 
L_name VARCHAR(20), 
PRIMARY KEY (Emp_id) 
); 

CREATE TABLE  FEEDBACK ( 
Fbk_id integer NOT NULL, 
Message VARCHAR(140), 
Email VARCHAR(50), 
Emp_id integer, 
Usr_id integer, 
Trip_id integer, 
F_Type varchar(10),
PRIMARY KEY (Fbk_id), 
); 

CREATE TABLE  OWNS ( 
Owner_id integer NOT NULL, 
No_Cars  integer, 
PRIMARY KEY (Owner_id) 
);

CREATE TABLE  OWNER_TAXI ( 
Owner_id integer NOT NULL, 
Taxi_id integer, 
PRIMARY KEY (Owner_id, Taxi_id) 
); 

CREATE TABLE INDIVIDUAL ( 
Ssn integer NOT NULL, 
Name VARCHAR(20), 
Owner_id integer, 
PRIMARY KEY (Ssn) 
); 

CREATE TABLE  TAXI_SERVICE_COMPANY ( 
Tsc_id integer NOT NULL, 
Tsc_name VARCHAR(20), 
Owner_id integer, 
PRIMARY KEY (Tsc_id) 
);


/* Modifying TRIP_DETAILS table for Driver_id to be not null */

ALTER TABLE TRIP_DETAILS
ALTER COLUMN Driver_id INTEGER NOT NULL;



/* Adding Constaints */

ALTER TABLE TAXI ADD CONSTRAINT fketadr FOREIGN KEY (Driver_id) 
REFERENCES DRIVER(Driver_id) ON DELETE CASCADE; 

ALTER TABLE USER_TBL ADD CONSTRAINT fkusta FOREIGN KEY (Taxi_id) 
REFERENCES TAXI(Taxi_id) ON DELETE CASCADE; 

ALTER TABLE TRIP_DETAILS ADD CONSTRAINT fkt FOREIGN KEY (Driver_id)
REFERENCES DRIVER(Driver_id) ON DELETE NO ACTION; 

ALTER TABLE TRIP_DETAILS ADD CONSTRAINT fktdusr FOREIGN KEY (Usr_id) 
REFERENCES USER_TBL(Usr_id) ON DELETE NO ACTION; 

ALTER TABLE TRIP_DETAILS ADD CONSTRAINT fktdtax FOREIGN KEY 
(Taxi_id) REFERENCES TAXI(Taxi_id) ON DELETE NO ACTION; 

ALTER TABLE BILL_DETAILS ADD CONSTRAINT fkbdtd FOREIGN KEY (Trip_id) 
REFERENCES TRIP_DETAILS(Trip_id) ON DELETE NO ACTION; 

ALTER TABLE BILL_DETAILS ADD CONSTRAINT fkbdusr FOREIGN KEY (Usr_id) 
REFERENCES USER_TBL(Usr_id) ON DELETE CASCADE;

ALTER TABLE FEEDBACK ADD CONSTRAINT fkfbemp FOREIGN KEY (Emp_id) 
REFERENCES CUSTOMER_SERVICE(Emp_id) ON DELETE CASCADE; 

ALTER TABLE FEEDBACK ADD CONSTRAINT fkfbtd FOREIGN KEY (Trip_id) 
REFERENCES TRIP_DETAILS(Trip_id) ON DELETE CASCADE; 

ALTER TABLE FEEDBACK ADD CONSTRAINT fkfbusr FOREIGN KEY (Usr_id) 
REFERENCES USER_TBL(Usr_id) ON DELETE NO ACTION; 

ALTER TABLE OWNER_TAXI ADD CONSTRAINT fkeowtax FOREIGN KEY (Taxi_id) 
REFERENCES TAXI(Taxi_id) ON DELETE CASCADE; 

ALTER TABLE OWNER_TAXI ADD CONSTRAINT fkeowowns FOREIGN KEY 
(Owner_id) REFERENCES OWNS(Owner_id) ON DELETE CASCADE; 

ALTER TABLE INDIVIDUAL ADD CONSTRAINT fkeinowns FOREIGN KEY 
(Owner_id) REFERENCES OWNS(Owner_id) ON DELETE CASCADE; 

ALTER TABLE TAXI_SERVICE_COMPANY ADD CONSTRAINT fketscowns FOREIGN 
KEY (Owner_id) REFERENCES OWNS(Owner_id) ON DELETE CASCADE; 



/* Adding the data into tables */

/* Driver table Insertion */
INSERT INTO DRIVER VALUES(1,'Abhi','Gowda','Male','8745201821',5,25); 
INSERT INTO DRIVER VALUES(2,'Rahul','Kumar','Male','9876543210',7,30);
INSERT INTO DRIVER VALUES(3,'Priya','Patel','Female','1234567890',4,28);
INSERT INTO DRIVER VALUES(4,'Amit','Sharma','Male','7890123456',6,32);
INSERT INTO DRIVER VALUES(5,'Neha','Singh','Female','8901234567',8,29);
INSERT INTO DRIVER VALUES(6,'Sandeep','Gupta','Male','9012345678',9,27);
INSERT INTO DRIVER VALUES(7,'Pooja','Verma','Female','6789012345',10,31);
INSERT INTO DRIVER VALUES(8,'Anil','Yadav','Male','5678901234',11,26);
INSERT INTO DRIVER VALUES(9,'Sunita','Mishra','Female','4567890123',12,33);
INSERT INTO DRIVER VALUES(10,'Vikas','Rajput','Male','3456789012',13,34);

/* TAXI table Insertion */
INSERT INTO TAXI VALUES(1,'GJ152004','BENZE','2024-3-11','SUV','Available',1);
INSERT INTO TAXI VALUES(2,'MH432010','MARUTI','2024-03-12','Hatchback','Available',2);
INSERT INTO TAXI VALUES(3,'DL678003','HYUNDAI','2024-03-13','Sedan','Available',3);
INSERT INTO TAXI VALUES(4,'KA987007','TATA','2024-03-14','SUV','Available',4);
INSERT INTO TAXI VALUES(5,'UP765005','MAHINDRA','2024-03-15','SUV','Available',5);
INSERT INTO TAXI VALUES(6,'TN876006','TOYOTA','2024-03-16','Sedan','Available',6);
INSERT INTO TAXI VALUES(7,'AP543001','HONDA','2024-03-17','Hatchback','Available',7);
INSERT INTO TAXI VALUES(8,'PB234008','FORD','2024-03-18','SUV','Available',8);
INSERT INTO TAXI VALUES(9,'HR654009','VOLKSWAGEN','2024-03-19','Hatchback','Available',9);
INSERT INTO TAXI VALUES(10,'MP876002','CHEVROLET','2024-03-20','SUV','Available',10);

/* USER_TBL Insertion */
INSERT INTO USER_TBL VALUES(1,'Yash','Taneja',7987845578,'Male','Chhindwara','1'); 
INSERT INTO USER_TBL VALUES(2, 'Riya', 'Sharma', 9090909090, 'Female', 'Delhi','2');
INSERT INTO USER_TBL VALUES(3, 'Amit', 'Singh', 9876543210, 'Male', 'Mumbai','3');
INSERT INTO USER_TBL VALUES(4, 'Priya', 'Patel', 8765432109, 'Female', 'Ahmedabad','4');
INSERT INTO USER_TBL VALUES(5, 'Kunal', 'Gupta', 7654321098, 'Male', 'Bangalore', '5');

/* TRIP_DETAILS Insertion */
INSERT INTO TRIP_DETAILS VALUES(1,'2024-03-11',150.45,1,1,1,'2024-03-11 12:00:00','2024-03-11 13:05:00','Chhindwara','Sendhwa')
INSERT INTO TRIP_DETAILS VALUES(2, '2024-03-13', 175.50, 2, 2, 2, '2024-03-13 12:00:00', '2024-03-13 13:05:00', 'Delhi', 'Mumbai');
INSERT INTO TRIP_DETAILS VALUES(3, '2024-03-14', 200.00, 3, 3, 3, '2024-03-14 12:00:00', '2024-03-14 13:05:00', 'Kolkata', 'Chennai');
INSERT INTO TRIP_DETAILS VALUES(4, '2024-03-15', 120.75, 4, 4, 4, '2024-03-15 12:00:00', '2024-03-15 13:05:00', 'Bangalore', 'Hyderabad');
INSERT INTO TRIP_DETAILS VALUES(5, '2024-03-16', 95.25, 5, 5, 5, '2024-03-16 12:00:00', '2024-03-16 13:05:00', 'Pune', 'Ahmedabad');

/* BILL_DETAILS Insertion */
INSERT INTO BILL_DETAILS VALUES(1,'2024-3-11',100,0,50.45,1,1); 
INSERT INTO BILL_DETAILS VALUES(2,'2024-3-13',100,0,75.50,2,2); 
INSERT INTO BILL_DETAILS VALUES(3,'2024-3-14',100,0,200.00,3,3); 
INSERT INTO BILL_DETAILS VALUES(4,'2024-3-15',100,0,20.75,4,4); 
INSERT INTO BILL_DETAILS VALUES(5,'2024-3-16',0,0,95.25,5,5); 

/* Customer_Service Insertion */
INSERT INTO CUSTOMER_SERVICE VALUES(1,'Madhav','Patel'); 
INSERT INTO CUSTOMER_SERVICE VALUES(2, 'Aarav', 'Shah');
INSERT INTO CUSTOMER_SERVICE VALUES(3, 'Diya', 'Verma');
INSERT INTO CUSTOMER_SERVICE VALUES(4, 'Rohan', 'Singh');
INSERT INTO CUSTOMER_SERVICE VALUES(5, 'Neha', 'Gupta');

/* FEEDBACK Insertion */
INSERT INTO FEEDBACK VALUES(1,'so good','abhi@gmail.com',1,1,1,'good');
INSERT INTO FEEDBACK VALUES(2, 'bad experience', 'john@example.com', 2, 2, 2, 'bad');
INSERT INTO FEEDBACK VALUES(3, 'could be better', 'jane@example.com', 3, 3, 3, 'bad');
INSERT INTO FEEDBACK VALUES(4, 'excellent service', 'smith@example.com', 4, 4, 4, 'good');
INSERT INTO FEEDBACK VALUES(5, 'friendly staff', 'emma@example.com', 5, 5, 5, 'good');

/* owns Insertion */
INSERT INTO OWNS VALUES(1,1);
INSERT INTO OWNS VALUES(2, 2);
INSERT INTO OWNS VALUES(3, 3);
INSERT INTO OWNS VALUES(4, 4);
INSERT INTO OWNS VALUES(5, 5);

/* OWNER_TAXI Insertion  */
INSERT INTO OWNER_TAXI values (1,1)
INSERT INTO OWNER_TAXI VALUES (2, 2);
INSERT INTO OWNER_TAXI VALUES (3, 3);
INSERT INTO OWNER_TAXI VALUES (4, 4);
INSERT INTO OWNER_TAXI VALUES (5, 5);

/* INDIVIDUAL Insertion */
INSERT INTO INDIVIDUAL VALUES(123,'abhi owner ind',1)
INSERT INTO INDIVIDUAL VALUES(456, 'john owner ind', 2);
INSERT INTO INDIVIDUAL VALUES(789, 'harsh owner ind', 3)
INSERT INTO INDIVIDUAL VALUES(101112, 'shan owner ind', 4)
INSERT INTO INDIVIDUAL VALUES(131415, 'ramesh owner ind', 5);

/* TAXI_SERVICE_COMPANY */
INSERT INTO TAXI_SERVICE_COMPANY VALUES (1,'abhi taxi comp',2)
INSERT INTO TAXI_SERVICE_COMPANY VALUES (2, 'Raj Taxi Services', 3)
INSERT INTO TAXI_SERVICE_COMPANY VALUES (3, 'Mumbai Cabs Pvt Ltd', 4);
INSERT INTO TAXI_SERVICE_COMPANY VALUES (4, 'Delhi Taxi Solutions', 5);
INSERT INTO TAXI_SERVICE_COMPANY VALUES (5, 'Bangalore Taxi Corp', 5);


/* Agrregate Functions */


/* Calculate the total number of taxi models available in the system. */
SELECT COUNT(DISTINCT Model) AS Total_Taxi_Models FROM TAXI; 

/* Calculate the total number of trips made by a specific driver  */
SELECT DRIVER.Driver_id, SUM(CASE WHEN TRIP_DETAILS.Trip_id IS NOT NULL THEN 1 ELSE 0 END) AS Total_Trips
FROM DRIVER
LEFT JOIN TRIP_DETAILS ON DRIVER.Driver_id = TRIP_DETAILS.Driver_id
GROUP BY DRIVER.Driver_id;

/* Calculate the average age of drivers in the system. */
SELECT AVG(Age) AS Average_Driver_Age FROM DRIVER; 

/* Find the minimum trip amount recorded in the system. */
SELECT MIN(Trip_amt) AS Min_Trip_Amount FROM TRIP_DETAILS; 

/* Find the maximum rating achieved by any driver in the system. */
SELECT MAX(Rating) AS Max_Driver_Rating FROM DRIVER; 

/* Calculate the total number of trips made by each taxi type. */
SELECT Taxi_type, COUNT(Trip_id) AS Total_Trips FROM TAXI INNER JOIN TRIP_DETAILS ON
TAXI.Taxi_id = TRIP_DETAILS.Taxi_id GROUP BY Taxi_type; 

/* Find the taxi types with more than 10 trips recorded. */
SELECT Taxi_type, COUNT(Trip_id) AS Total_Trips FROM TAXI INNER JOIN TRIP_DETAILS
ON TAXI.Taxi_id = TRIP_DETAILS.Taxi_id GROUP BY Taxi_type HAVING COUNT(Trip_id) > 10; 

/* List all unique taxi models available in the system. */
SELECT DISTINCT Model FROM TAXI; 



/* JOINS */


/* Inner Join The taxi service company wants to retrieve a list of all trips along 
with their corresponding driver and user details.  */
SELECT TD.Trip_id, TD.Trip_date, TD.Strt_time, TD.End_time, D.F_name AS Driver_FirstName, D.L_name AS Driver_LastName,
D.Gender AS Driver_Gender, D.Conatct_no AS Driver_Contact, 
U.F_name AS User_FirstName, U.L_name AS User_LastName, U.Gender AS User_Gender, U.Contat_no AS User_Contact 
FROM TRIP_DETAILS TD 
INNER JOIN DRIVER D ON TD.Driver_id = D.Driver_id 
INNER JOIN USER_TBL U ON TD.Usr_id = U.Usr_id; 

/* Left Join The taxi service company wants to list all taxis along with their associated driver information. 
Some taxis may not have assigned drivers yet. */
SELECT T.Taxi_id, T.Registration_no, T.Model, T.Taxi_Year, T.Taxi_type, T.Taxi_status, D.F_name AS Driver_FirstName,
D.L_name AS Driver_LastName, D.Gender AS Driver_Gender, D.Conatct_no AS Driver_Contact FROM TAXI T 
LEFT JOIN DRIVER D ON T.Driver_id = D.Driver_id; 

/* Right Join The taxi service company wants to see a list of all drivers along with the details of the
trips they have completed, even if some drivers haven't completed any trips yet.  */
SELECT D.Driver_id, D.F_name, D.L_name, D.Gender, D.Conatct_no, TD.Trip_id, TD.Trip_date, TD.Strt_time, TD.End_time 
FROM DRIVER D 
RIGHT JOIN TRIP_DETAILS TD ON D.Driver_id = TD.Driver_id; 

/* Full Outer Join  he taxi service company wants to generate a comprehensive report that lists
all taxis, drivers, and their associated trip details, regardless of whether each taxi has been 
assigned a driver or has completed any trips yet. */
SELECT T.Taxi_id, T.Registration_no, Model, T.Taxi_Year, T.Taxi_type, T.Taxi_status, 
D.Driver_id, D.F_name AS Driver_FirstName, D.L_name AS Driver_LastName, D.Gender AS Driver_Gender, D.Conatct_no AS Driver_Contact, 
TD.Trip_id, TD.Trip_date, TD.Strt_time, TD.End_time 
FROM TAXI T 
FULL OUTER JOIN DRIVER D ON T.Driver_id = D.Driver_id 
FULL OUTER JOIN TRIP_DETAILS TD ON T.Taxi_id = TD.Taxi_id; 



/* Set Operations */


--Query to Combine All Unique Driver Names from Two Tables: 
SELECT F_name AS Entity_Name FROM DRIVER 
UNION 
SELECT F_name AS Entity_Name FROM CUSTOMER_SERVICE; 

--Query to Find All Taxi Models Owned by Individual Owners but Not Owned by Taxi Service Companies: 
SELECT Name AS Entity_Name FROM INDIVIDUAL 
EXCEPT 
SELECT Tsc_name AS Entity_Name FROM TAXI_SERVICE_COMPANY;

--It finds the intersection of taxi IDs owned by individual owners and taxi IDs in the general taxi pool.
SELECT Taxi_id FROM TAXI
INTERSECT
SELECT Taxi_id FROM OWNER_TAXI;

--Retrieve a list of all unique taxi IDs, including those owned by individual owners and 
--those managed by the taxi service company, ensuring that each taxi ID is listed only once.
SELECT Taxi_id FROM TAXI
UNION
SELECT Taxi_id FROM OWNER_TAXI;



--Group by and having clause 


--The taxi service company wants to generate a report showing the total number of trips made by 
--each taxi, along with the average trip amount for taxis that have completed more than 10 trips.  
SELECT T.Taxi_id, COUNT(TD.Trip_id) AS Total_Trips, AVG(TD.Trip_amt) AS Average_Trip_Amount 
FROM TAXI T 
LEFT JOIN TRIP_DETAILS TD ON T.Taxi_id = TD.Taxi_id 
GROUP BY T.Taxi_id 
HAVING COUNT(TD.Trip_id) > 10; 

--The taxi service company wants to find out the total number of trips completed by each driver, 
--along with their average rating. 
SELECT D.Driver_id, D.F_name, D.L_name, COUNT(TD.Trip_id) AS Total_Trips, AVG(D.Rating) AS Average_Rating 
FROM DRIVER D 
LEFT JOIN TRIP_DETAILS TD ON D.Driver_id = TD.Driver_id 
GROUP BY D.Driver_id, D.F_name, D.L_name; 

--The taxi service company wants to identify users who have taken more than 5 trips and have spent a total amount
--greater than $500 on trips. 
SELECT U.Usr_id, U.F_name, U.L_name, COUNT(TD.Trip_id) AS Total_Trips, SUM(BD.Total_amt) AS Total_Amount_Spent 
FROM USER_TBL U 
LEFT JOIN TRIP_DETAILS TD ON U.Usr_id = TD.Usr_id 
LEFT JOIN BILL_DETAILS BD ON U.Usr_id = BD.Usr_id 
GROUP BY U.Usr_id, U.F_name, U.L_name 
HAVING COUNT(TD.Trip_id) > 5 AND SUM(BD.Total_amt) > 500; 



-- Simple Queries


--Retrieve the registration number, taxi model, and status of taxis driven by female drivers under the age of 30.
SELECT T.Registration_no, T.Model, T.Taxi_status 
FROM TAXI T, DRIVER D 
WHERE T.Driver_id = D.Driver_id AND D.Gender = 'Female' AND D.Age < 30; 

--Retrieve the names and contact numbers of drivers who have received feedback messages containing the word "excellent".
SELECT D.F_name, D.L_name, D.Conatct_no 
FROM DRIVER D, FEEDBACK F 
WHERE D.Driver_id = F.Emp_id AND F.Message LIKE '%excellent%'; 

--Retrieve the names and addresses of users who have taken trips in taxis registered in 2022.
SELECT U.F_name, U.L_name, U.USR_Address 
FROM USER_TBL U, TAXI T, TRIP_DETAILS TD 
WHERE U.Usr_id = TD.Usr_id AND TD.Taxi_id = T.Taxi_id AND T.Taxi_Year = '2022'; 

--Retrieve the owner names and the total number of taxis they own, excluding owners who do not have any taxis.
SELECT I.Name AS Owner_Name, O.No_Cars AS Total_Taxis_Owned 
FROM INDIVIDUAL I, OWNS O 
WHERE I.Owner_id = O.Owner_id AND O.No_Cars > 0; 

--To retrieve all feedback provided by users and sort them based on the feedback, bad to good
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


--Nested queries:


--Retrieve the names of users who have taken trips using taxis owned by individuals named "John".
SELECT DISTINCT U.F_name, U.L_name 
FROM USER_TBL U 
WHERE U.Usr_id IN ( 
	SELECT TD.Usr_id FROM TRIP_DETAILS TD 
    WHERE TD.Taxi_id IN ( 
	SELECT OT.Taxi_id FROM OWNER_TAXI OT 
   JOIN INDIVIDUAL I ON OT.Owner_id = I.Owner_id WHERE I.Name = 'John' 
    )); 

--Retrieve the total number of trips taken by users who have given feedback with a message containing the word "complaint". 
SELECT COUNT(*) 
FROM TRIP_DETAILS 
WHERE Usr_id IN ( 
    SELECT DISTINCT Usr_id 
    FROM FEEDBACK 
    WHERE Message LIKE '%complaint%' 
);  

--Retrieve the names and contact numbers of drivers who have received feedback from users residing in "Chhindwara".
SELECT DISTINCT D.F_name, D.L_name, D.Conatct_no 
FROM DRIVER D 
WHERE D.Driver_id IN ( 
    SELECT DISTINCT F.Emp_id 
	FROM FEEDBACK F 
    JOIN USER_TBL U ON F.Usr_id = U.Usr_id 
    WHERE U.USR_Address LIKE '%Chhindwara%' 
); 

--Retrieve the registration numbers of taxis driven by male drivers under the age of 25.
SELECT DISTINCT T.Registration_no 
FROM TAXI T 
WHERE T.Driver_id IN ( 
    SELECT DISTINCT Driver_id 
    FROM DRIVER 
    WHERE Gender = 'Male' AND Age < 25 
); 



--UPDATE QUERIES


--Update Driver's Contact Number
UPDATE DRIVER 
SET Conatct_no = 'New_Contact_Number' 
WHERE Driver_id = 'Driver_ID'; 

--Change Taxi Model for a Specific Taxi
UPDATE TAXI 
SET Model = 'New_Taxi_Model' 
WHERE Taxi_id = 'Taxi_ID';

--Update Trip Amount for a Specific Trip
UPDATE TRIP_DETAILS 
SET Trip_amt = 'New_Trip_Amount' 
WHERE Trip_id = 'Trip_ID';

--Update User's Address
UPDATE USER_TBL 
SET USR_Address = 'New_Address' 
WHERE Usr_id = 'User_ID'; 

--Change Taxi Status
UPDATE TAXI 
SET Taxi_status = 'Unavailable' 
WHERE Taxi_type = 'Taxi_Type';



--DELETE QUERIES


--Delete a Specific Taxi
DELETE FROM TAXI 
WHERE Taxi_id = 'Taxi_ID';

--Remove a Driver Record
DELETE FROM DRIVER 
WHERE Driver_id = 'Driver_ID';

--Delete a User Record
DELETE FROM USER_TBL 
WHERE Usr_id = 'User_ID'; 

--Cancel a Trip
DELETE FROM TRIP_DETAILS 
WHERE Trip_id = 'Trip_ID';

--Remove an Individual Owner
DELETE FROM INDIVIDUAL 
WHERE Owner_id = 'Owner_ID';










