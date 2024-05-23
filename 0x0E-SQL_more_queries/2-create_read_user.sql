-- creates a database
-- a script that creates a database and a user
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
CREATE USER IF NOT EXISTS 'user_0d_2'@'hbtn_0d_2';
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'hbtn_0d_2';

FLUSH PRIVILEGES;
