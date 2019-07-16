# 0x0E. SQL - More queries <br />

## Resources <br />

[How To Create a New User and Grant Permissions in MySQL](https://www.digitalocean.com/community/tutorials/how-to-create-a-new-user-and-grant-permissions-in-mysql) <br />
[How To Use MySQL GRANT Statement To Grant Privileges To a User](http://www.mysqltutorial.org/mysql-grant.aspx) <br />
[MySQL constraints](http://zetcode.com/databases/mysqltutorial/constraints/) <br />
[SQL technique: subqueries](https://web.csulb.edu/colleges/coe/cecs/dbdesign/dbdesign.php?page=sql/subqueries.php) <br />
[Basic query operation: the join](https://web.csulb.edu/colleges/coe/cecs/dbdesign/dbdesign.php?page=sql/join.php) <br />
[SQL Joins](https://www.w3schools.com/sql/sql_join.asp) <br />
[SQL technique: multiple joins and the distinct keyword](https://web.csulb.edu/colleges/coe/cecs/dbdesign/dbdesign.php?page=sql/multijoin.php) <br />
[SQL technique: join types](https://web.csulb.edu/colleges/coe/cecs/dbdesign/dbdesign.php?page=sql/jointypes.php) <br />
[SQL technique: union and minus](https://web.csulb.edu/colleges/coe/cecs/dbdesign/dbdesign.php?page=sql/setops.php) <br />
[The Seven Types of SQL Joins](https://teamsql.io/blog/?p=923) <br />
[MySQL Tutorial](https://www.youtube.com/watch?v=yPu6qV5byu4) <br />
[SQL Style Guide](https://www.sqlstyle.guide/) <br />
[MySQL 5.7 SQL Statement Syntax](https://dev.mysql.com/doc/refman/5.7/en/sql-syntax.html) <br />
[(My)SQL Cheat Sheet](http://www.sqltutorial.org/sql-cheat-sheet/) <br />

## Learning Objectives <br />
- How to create a new MySQL user
- How to manage privileges for a user to a database or table
- What’s a `PRIMARY KEY`
- What’s a `FOREIGN KEY`
- How to use `NOT NULL` and `UNIQUE` constraints
- How to retrieve datas from multiple tables in one request
- What are subqueries
- What are `JOIN` and `UNION`

## Tasks <br />

0. 0-privileges.sql // a script that lists all privileges of the MySQL users `user_0d_1` and `user_0d_2` on my server.

1. 1-create_user.sql // a script that creates the MySQL server user `user_0d_1`.

- `user_0d_1` has all privileges on my MySQL server
-  the `user_0d_1` password is set to `user_0d_1_pwd`
-  if the user `user_0d_1` already exists, my script does not fail

2. 2-create_read_user.sql // a script that creates the database `hbtn_0d_2` and the user `user_0d_2`.

- `user_0d_2` has only SELECT privilege in the database `hbtn_0d_2`
- `user_0d_2`'s password is set to `user_0d_2_pwd`
- if the database `hbtn_0d_2` already exists, my script does not fail
- if the user `user_0d_2` already exists, my script does not fail

3. 3-force_name.sql // a script that creates the table `force_name` on my MySQL server.

4. 4-never_empty.sql //  a script that creates the table `id_not_null` on my MySQL server.

5. 5-unique_id.sql // a script that creates the table `unique_id` on my MySQL server.

6. 6-states.sql // a  script that creates the database `hbtn_0d_usa` and the table states (in the database hbtn_0d_usa) on my MySQL server.

7. 7-cities.sql // a script that creates the database `hbtn_0d_usa` and the table cities (in the database hbtn_0d_usa) on my MySQL server.

8. 8-cities_of_california_subquery.sql // a script that lists all the cities of California that can be found in the database `hbtn_0d_usa`.

9. 9-cities_by_state_join.sql // a script that lists all cities contained in the database `hbtn_0d_usa`.

10. 10-genre_id_by_show.sql // a script that lists all shows contained in `hbtn_0d_tvshows` that have at least one genre linked.

11. 11-genre_id_all_shows.sql // a script that lists all shows contained in the database `hbtn_0d_tvshows`

12. 12-no_genre.sql // a script that lists all shows contained in `hbtn_0d_tvshows` without a genre linked.

13. 13-count_shows_by_genre.sql // a script that lists all genres from `hbtn_0d_tvshows` and displays the number of shows linked to each.

14. 14-my_genres.sql // a script that uses the `hbtn_0d_tvshows` database to lists all genres of the show `Dexter`.

15. 15-comedy_only.sql // a script that lists all Comedy shows in the database `hbtn_0d_tvshows`.

16. 16-shows_by_genre.sql // a script that lists all shows, and all genres linked to that show, from the database `hbtn_0d_tvshows`.

17. 100-not_my_genres.sql // a script that uses the `hbtn_0d_tvshows` database to list all genres not linked to the show `Dexter`.

18. 101-not_a_comedy.sql // a script that lists all shows without the genre Comedy in the database `hbtn_0d_tvshows`.

19. 102-rating_shows.sql // a script that lists all shows from `hbtn_0d_tvshows_rate` by their rating.

20. 103-rating_genres.sql // a script that lists all genres in the database `hbtn_0d_tvshows_rate` by their rating.

21. A [blog post I wrote](link here) on [How SQL Database Engines Work](https://www.youtube.com/watch?time_continue=1&v=Z_cX3bzkExE)
