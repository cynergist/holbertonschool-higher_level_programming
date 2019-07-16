-- script lists the number of records with the same score in second_table of
-- db hbtn_0c_0: result displays the score, the number of records for this score
-- with the label number, sorted by number of records in descending order.

SELECT `score`, COUNT(*) AS `number`
FROM second_table
GROUP by `score` DESC;
