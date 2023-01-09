# Write your MySQL query statement below

select *
from Patients a 
where a.conditions like '% DIAB1%' or 
      a.conditions like 'DIAB1%';