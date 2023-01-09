# Write your MySQL query statement below

select a.class
from Courses a 
group by a.class
having count(*) >=5;