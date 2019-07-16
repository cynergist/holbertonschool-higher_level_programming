--  script lists all records of second_table of database
-- rows without a name value not listed
-- results display the score and the name (in this order)
-- Records listed by descending score
SELECT score, name
FROM second_table
WHERE name is NOT NULL
ORDER BY score DESC;
