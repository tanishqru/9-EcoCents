DROP USER admin_ecocents@localhost;
FLUSH PRIVILEGES;
CREATE USER 'admin_ecocents'@'localhost' IDENTIFIED BY 'admin@password@ecocents';
DROP DATABASE IF EXISTS ecocents;
CREATE DATABASE ecocents;
GRANT ALL PRIVILEGES ON ecocents.* TO 'admin_ecocents'@'localhost';
FLUSH PRIVILEGES;

USE ecocents;
-- Users table 
CREATE TABLE users (
    uid INT PRIMARY KEY,
    name VARCHAR(255),
    password VARCHAR(255),
    emailid VARCHAR(255),
    phone INT,
    points INT DEFAULT NULL, -- New column for points
    money FLOAT DEFAULT NULL-- New column for money
);


-- Porject table
CREATE TABLE project (
    project_id INT AUTO_INCREMENT PRIMARY KEY,
    project_name VARCHAR(255),
    company_name VARCHAR(255),
    minimum_rate FLOAT,
    maximum_rate FLOAT,
    shares_available INT
);

-- Share table
CREATE TABLE share (
    share_id INT AUTO_INCREMENT PRIMARY KEY,
    company_name VARCHAR(255),
    project_id INT,
    shares_available INT,
    rate FLOAT,
    FOREIGN KEY (project_id) REFERENCES project(project_id)
);

-- Share purchase table
CREATE TABLE share_purchase (
    share_purchase_id INT AUTO_INCREMENT PRIMARY KEY,
    uid INT,
    date_of_purchase DATE,
    share_id INT,
    rate FLOAT,
    qty INT,
    total FLOAT,
    total_analysis FLOAT,
    FOREIGN KEY (uid) REFERENCES users(uid),
    FOREIGN KEY (share_id) REFERENCES share(share_id)
);

CREATE TABLE bills (
    bill_id INT AUTO_INCREMENT PRIMARY KEY,
    uid INT,
    share_purchase_id INT,
    date_of_purchase DATE,
    bill_url VARCHAR(255),
    amount FLOAT,
    FOREIGN KEY (uid) REFERENCES users(uid),
    FOREIGN KEY (share_purchase_id) REFERENCES share_purchase(share_purchase_id)
);

--points table
CREATE TABLE Points (
    points_id INT AUTO_INCREMENT PRIMARY KEY,
    uid INT,
    initial_points INT DEFAULT 1000,
    points_credited INT,
    points_debited INT,
    balance_points INT
);

-- Create the Money table
CREATE TABLE Money (
    money_id INT AUTO_INCREMENT PRIMARY KEY,
    uid INT,
    initial_money FLOAT DEFAULT 0,
    money_credited FLOAT,
    money_debited FLOAT,
    balance_money FLOAT
);

