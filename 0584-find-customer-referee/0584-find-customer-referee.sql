# Write your MySQL query statement below

select a.name
from Customer a
where 1=1
and (a.referee_id != 2 or a.referee_id is Null)