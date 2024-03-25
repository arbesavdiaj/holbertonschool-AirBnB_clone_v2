-- Use the root user to perform administrative tasks
-- Create the 'hbnb_dev_db' database if it does not exist
CREATE DATABASE IF NOT EXISTS hbnb_test_db;

-- Create the 'hbnb_dev' user with the specified password if it does not exist
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';

-- Grant all privileges on 'hbnb_dev_db' to 'hbnb_dev' user
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';

-- Grant SELECT privilege on 'performance_schema' to 'hbnb_dev' user
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';

-- Apply the changes made by the GRANT statements
FLUSH PRIVILEGES;