CREATE USER 'admin_ecocents'@'localhost' IDENTIFIED BY 'admin@password@ecocents';
DROP DATABASE IF EXISTS ecocents;
CREATE DATABASE ecocents;
GRANT ALL PRIVILEGES ON ecocents.* TO 'admin_ecocents'@'localhost';
FLUSH PRIVILEGES;

-- Users table 
CREATE TABLE ecocents.users (
    uid INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    phone INT,
    emailid VARCHAR(255),
    dob DATE,
    username VARCHAR(255),
    password VARCHAR(255),
    used_ref_code INT,
    points INT, -- New column for points
    money FLOAT, -- New column for money
    FOREIGN KEY (uid) REFERENCES ecocents.points(uid), -- Link to balance_points
    FOREIGN KEY (uid) REFERENCES ecocents.money(uid) -- Link to balance_money
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
CREATE TABLE ecocents.points (
    points_id INT AUTO_INCREMENT PRIMARY KEY,
    uid INT,
    initial_points INT DEFAULT 1000,
    points_credited INT,
    points_debited INT,
    balance_points INT
);

-- Create the Money table
CREATE TABLE ecocents.money (
    money_id INT AUTO_INCREMENT PRIMARY KEY,
    uid INT,
    initial_money FLOAT DEFAULT 0,
    money_credited FLOAT,
    money_debited FLOAT,
    balance_money FLOAT
);

