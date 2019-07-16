-- script lists all records with a score >= 10 in second_table of db hbtn_0c_0.
-- results display both score and name (in this order) ordered by top score.
SELECT score, `name`
FROM second_table
WHERE score >= 10
ORDER BY score DESC;
