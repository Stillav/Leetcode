# Write your MySQL query statement below

select author_id as id 
from Views a
where a.author_id = a.viewer_id
group by a.author_id
order by a.author_id asc;