CREATE DATABASE blood_bank_db;

USE blood_bank_db;

CREATE TABLE donors (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    blood_type VARCHAR(10) NOT NULL,
    contact_info VARCHAR(100) NOT NULL
);

CREATE TABLE blood_requests (
    id INT AUTO_INCREMENT PRIMARY KEY,
    blood_type VARCHAR(10) NOT NULL,
    quantity INT NOT NULL,
    requestor_name VARCHAR(100) NOT NULL,
    contact_info VARCHAR(100) NOT NULL
);
