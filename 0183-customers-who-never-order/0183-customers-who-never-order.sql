# Write your MySQL query statement below
SELECT a.name as Customers
FROM Customers a
WHERE a.id not in (SELECT customerId FROM Orders)