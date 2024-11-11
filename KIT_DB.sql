

CREATE TABLE IF NOT EXISTS students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    age INT,
    prn VARCHAR(15) UNIQUE,
    address VARCHAR(255),
    department VARCHAR(100),
    academic_year VARCHAR(10)
);
