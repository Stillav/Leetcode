# Write your MySQL query statement below

SELECT DISTINCT
  A.player_id,
  LAST_VALUE(A.event_date) OVER (
    PARTITION BY
      A.player_id
    ORDER BY
      A.event_date DESC RANGE BETWEEN UNBOUNDED PRECEDING
      AND UNBOUNDED FOLLOWING
  ) AS first_login
FROM
  Activity A