# Write your MySQL query statement below

select a.product_id, a.product_name
from Product a 
inner join Sales b on a.product_id = b.product_id 
where UNIX_TIMESTAMP(b.sale_date) >= UNIX_TIMESTAMP('2019-01-01')
and UNIX_TIMESTAMP(b.sale_date) <= UNIX_TIMESTAMP('2019-03-31')
and a.product_id not in (
    select product_id 
    from Sales 
    where (UNIX_TIMESTAMP(sale_date) > UNIX_TIMESTAMP('2019-03-31')
           or 
           UNIX_TIMESTAMP(sale_date) < UNIX_TIMESTAMP('2019-01-01')
    )
)
group by a.product_id, a.product_name