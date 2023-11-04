DROP USER admin_ecocents@localhost;
FLUSH PRIVILEGES;
CREATE USER 'admin_ecocents'@'localhost' IDENTIFIED BY 'admin@password@ecocents';
DROP DATABASE IF EXISTS ecocents;
CREATE DATABASE ecocents;
GRANT ALL PRIVILEGES ON ecocents.* TO 'admin_ecocents'@'localhost';
FLUSH PRIVILEGES;

USE ecocents;

-- Create the 'user' table with emailid as the primary key
CREATE TABLE users (
    emailid VARCHAR(255) PRIMARY KEY,
    name VARCHAR(255),
    password VARCHAR(255),
    phone INT
);

-- Create the 'project' table
CREATE TABLE project (
    proj_id VARCHAR(255),
    proj_name VARCHAR(255),
    comp_name VARCHAR(255),
    minimum_rate INT,
    shares_available INT,
    PRIMARY KEY (proj_id)
);

-- Create the 'share' table
CREATE TABLE share (
    share_id VARCHAR(255) PRIMARY KEY,
    project_id VARCHAR(255),
    FOREIGN KEY (project_id) REFERENCES project(proj_id)
);
-- Create the 'share_purchase' table with emailid as the foreign key
CREATE TABLE share_purchase (
    purchase_id INT AUTO_INCREMENT PRIMARY KEY,
    user_emailid VARCHAR(255), -- Use a different name for the foreign key column
    share_id VARCHAR(255),
    qty INT,
    total INT,
    FOREIGN KEY (user_emailid) REFERENCES users(emailid),
    FOREIGN KEY (share_id) REFERENCES share(share_id)
);

-- Create the 'points' table with 'points' as the primary key
CREATE TABLE points (
    points INT PRIMARY KEY,
    user_emailid VARCHAR(255), -- Use a different name for the foreign key column
    FOREIGN KEY (user_emailid) REFERENCES users(emailid)
);

-- Create the 'money' table with 'money' as the primary key
CREATE TABLE money (
    money INT PRIMARY KEY,
    user_emailid VARCHAR(255), -- Use a different name for the foreign key column
    FOREIGN KEY (user_emailid) REFERENCES users(emailid)
);

