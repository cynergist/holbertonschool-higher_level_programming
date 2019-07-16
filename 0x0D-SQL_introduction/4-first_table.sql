-- a script that creates first_table in the current database in my MySQL server.
-- disallowed to use the SELECT or SHOW statements.
CREATE TABLE IF NOT EXISTS `first_table`
(
	id INT,
	name VARCHAR(256)
);
