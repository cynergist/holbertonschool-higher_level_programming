-- script updates Bob's score to 10 in second_table.
-- disallowed: use Bob’s id value, only the name field.
UPDATE `second_table`
SET
`score` = 10
WHERE `second_table`.`name` = "Bob";
