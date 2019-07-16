-- script creates the MySQL server user user_0d_1
-- with all privileges on my  MySQL server and their password is set to
-- user_0d_1_pwd. If user_0d_1 already exists, script does not fail
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED by 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON * . * TO 'user_0d_1'@'localhost';
