# A3Q1
Assignment 2 Question 1 done by Artem Pankratov (101240886)
Video Link: https://youtu.be/mQNwAOqM9KE
To run this application:

* Make sure you have Python and PostgreSQL installed
* Open pgAdmin and create a new database named "school"
* Open the Query Tool and run this SQL to create the students table:

CREATE TABLE students (
  student_id SERIAL PRIMARY KEY,
  first_name TEXT NOT NULL, 
  last_name TEXT NOT NULL,
  email TEXT NOT NULL UNIQUE,
  enrollment_date DATE
);

* Run this SQL to insert the initial data:

INSERT INTO students (first_name, last_name, email, enrollment_date) 
VALUES
('John', 'Doe', 'john.doe@example.com', '2023-09-01'),
('Jane', 'Smith', 'jane.smith@example.com', '2023-09-01'), 
('Jim', 'Beam', 'jim.beam@example.com', '2023-09-02');


* Update the get_db_connection function in app.py with your PostgreSQL user/password
* Set up the database using the SQL commands provided
* Run the app with: python app.py
