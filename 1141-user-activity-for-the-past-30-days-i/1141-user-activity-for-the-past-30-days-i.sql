# Write your MySQL query statement below
select a.activity_date as day, count(*) as active_users
from 
(select a.user_id, a.session_id, a.activity_date 
from Activity a
where UNIX_TIMESTAMP(activity_date) > UNIX_TIMESTAMP('2019-06-27')
and UNIX_TIMESTAMP(activity_date) < UNIX_TIMESTAMP('2019-07-27')
group by a.user_id, a.activity_date) a
group by a.activity_date