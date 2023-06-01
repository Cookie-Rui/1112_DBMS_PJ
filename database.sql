/*
load data的部分需要把檔案位址改成自己的本機檔案位址
*/

DROP DATABASE IF EXISTS PROJECT;

CREATE SCHEMA PROJECT;

use PROJECT;

CREATE TABLE Teacher(
    t_name VARCHAR(45) NOT NULL,
    t_id INT PRIMARY KEY,
    t_department_id CHAR(3) NOT NULL,
    gender VARCHAR(10)
);

CREATE TABLE Department(
    d_name VARCHAR(45) NOT NULL,
    d_id CHAR(3) PRIMARY KEY
);

CREATE TABLE Building(
    b_name VARCHAR(45) not NULL,
    b_id CHAR(3) PRIMARY KEY
);

CREATE TABLE Student(
    s_name VARCHAR(45) NOT NULL,
    s_id CHAR(9) PRIMARY KEY,
    gender VARCHAR(6),
    grade VARCHAR(10) NOT NULL,
    major_Did CHAR(3) NOT NULL,
    haveSecondary tinyint(1) NOT NULL
);

CREATE TABLE Course(
    c_name VARCHAR(45) NOT NULL,
    c_id CHAR(9) PRIMARY KEY,
    max_people INT NOT NULL,
    choose_amount INT NOT NULL,
    teacher_id INT NOT NULL,
    building_id CHAR(3) NOT NULL,
    c_time VARCHAR(10) NOT NULL,
    c_department_id CHAR(3) NOT NULL,
    credit INT NOT NULL,
    c_type VARCHAR(10) NOT NULL
);

CREATE TABLE SecondDepartment(
    student_id CHAR(9) NOT NULL,
    department_id CHAR(3) NOT NULL,
    isMajor tinyint(1),
    CONSTRAINT pk_sd PRIMARY KEY (student_id,department_id)
);

CREATE TABLE SelectCourse(
    student_id CHAR(9) NOT NULL,
    course_id CHAR(9) NOT NULL,
    c_rank INT NOT NULL,
    CONSTRAINT pk_sc PRIMARY KEY (student_id,course_id)
);

ALTER TABLE SecondDepartment ADD FOREIGN KEY (student_id) REFERENCES Student(s_id);
ALTER TABLE SecondDepartment ADD FOREIGN KEY (department_id) REFERENCES Department(d_id);
ALTER TABLE SelectCourse ADD FOREIGN KEY (student_id) REFERENCES Student(s_id);
ALTER TABLE SelectCourse ADD FOREIGN KEY (course_id) REFERENCES Course(c_id);
ALTER TABLE Student ADD FOREIGN KEY (major_Did) REFERENCES Department(d_id);
ALTER TABLE Course ADD FOREIGN KEY (teacher_id) REFERENCES Teacher(t_id);
ALTER TABLE Course ADD FOREIGN KEY (building_id) REFERENCES Building(b_id);
ALTER TABLE Course ADD FOREIGN KEY (c_department_id) REFERENCES Department(d_id);


SET GLOBAL local_infile = on;


LOAD DATA local INFILE '你的檔案位址/init_data/Department.csv' INTO TABLE Department
  FIELDS TERMINATED BY ',' 
  ENCLOSED BY '"'
  LINES TERMINATED BY '\n'
  IGNORE 1 LINES;

LOAD DATA local INFILE '你的檔案位址/init_data/Teacher.csv' INTO TABLE Teacher
  FIELDS TERMINATED BY ',' 
  ENCLOSED BY '"'
  LINES TERMINATED BY '\n'
  IGNORE 1 LINES;

LOAD DATA local INFILE '你的檔案位址/init_data/Building.csv' INTO TABLE building
  FIELDS TERMINATED BY ',' 
  ENCLOSED BY '"'
  LINES TERMINATED BY '\n'
  IGNORE 1 LINES;
  
LOAD DATA local INFILE '你的檔案位址/init_data/Student.csv' INTO TABLE student
  FIELDS TERMINATED BY ',' 
  ENCLOSED BY '"'
  LINES TERMINATED BY '\n'
  IGNORE 1 LINES;
  
LOAD DATA local INFILE '你的檔案位址/init_data/Course.csv' INTO TABLE course
  FIELDS TERMINATED BY ',' 
  ENCLOSED BY '"'
  LINES TERMINATED BY '\n'
  IGNORE 1 LINES;
  
LOAD DATA local INFILE '你的檔案位址/init_data/SelectCourse.csv' INTO TABLE selectcourse
  FIELDS TERMINATED BY ',' 
  ENCLOSED BY '"'
  LINES TERMINATED BY '\n'
  IGNORE 1 LINES;
  
LOAD DATA local INFILE '你的檔案位址/init_data/SecondDepartment.csv' INTO TABLE seconddepartment
  FIELDS TERMINATED BY ',' 
  ENCLOSED BY '"'
  LINES TERMINATED BY '\n'
  IGNORE 1 LINES;