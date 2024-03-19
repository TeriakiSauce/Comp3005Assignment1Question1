This a project that demonstrates interactions between a PosgreSQL database and Python application using the pyscopg2 library

To install the dependency:
pip install psycopg2

Below is a video explaining how this code works:
https://youtu.be/8_rmzRM1Ies

Here are the DDL statements used to initialize the database:

--Tarik Beldjehem 101187965
CREATE TABLE IF NOT EXISTS students(
	student_id                      SERIAL          PRIMARY KEY,
	first_name                      TEXT            NOT NULL,
	last_name                       TEXT            NOT NULL,
	email                           TEXT,
	enrollment_date                 DATE
);

INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES
('John', 'Doe', 'john.doe@example.com', '2023-09-01'),
('Jane', 'Smith', 'jane.smith@example.com', '2023-09-01'),
('Jim', 'Beam', 'jim.beam@example.com', '2023-09-02');

SELECT * FROM students;