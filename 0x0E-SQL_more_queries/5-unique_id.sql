-- script creates the table unique_id on my MySQL server.
-- unique_id desc: id INT, default value 1 and is unique, name VARCHAR(256)
-- If the table unique_id already exists, script does not fail
CREATE TABLE IF NOT EXISTS `unique_id`
(
	id INT DEFAULT 1 UNIQUE,
	name VARCHAR(256)
);
