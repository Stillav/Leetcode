# Write your MySQL query statement below

SELECT a.player_id, a.event_date as first_login
FROM 
(SELECT *
FROM Activity a
order by UNIX_TIMESTAMP(a.event_date) asc
limit 10000
) a
GROUP BY a.player_id