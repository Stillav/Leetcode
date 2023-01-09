# Write your MySQL query statement below

select a.name
from SalesPerson a 
where a.name not in 
(select a.name
from SalesPerson a
left outer join Orders b on a.sales_id = b.sales_id
left outer join Company c on b.com_id = c.com_id
where 1=1
and c.name like 'RED');