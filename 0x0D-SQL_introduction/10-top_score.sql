-- script lists all records of second_table of the db hbtn_0c_0 in my server.
-- results display both score and name (in this order), ordered by top score.
SELECT score, `name`
FROM second_table
ORDER BY score DESC;
