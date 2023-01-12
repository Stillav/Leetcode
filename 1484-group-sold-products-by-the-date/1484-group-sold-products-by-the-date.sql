# Write your MySQL query statement below

SELECT a.sell_date, count(DISTINCT(product)) as num_sold, GROUP_CONCAT(DISTINCT(product)) as products
FROM Activities a 
group by a.sell_date