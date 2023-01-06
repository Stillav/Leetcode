# Write your MySQL query statement below
SELECT a.email as Email
    FROM Person a
GROUP BY a.email
HAVING count(*) >= 2