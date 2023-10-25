use db;

CREATE TABLE students(
    studentID int NOT NULL auto_increment,
    FirstName varchar(50) NOT NULL,
    LastName varchar(50) NOT NULL,
    PRIMARY KEY(studentID)
);

INSERT INTO students(FirstName,LastName)
VALUES ("Rohit","Sharma"),("Ankit","Verma");