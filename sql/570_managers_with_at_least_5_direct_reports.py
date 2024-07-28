# Write your MySQL query statement below

select name
from (
    Employee as e join
    (
        select ManagerId
        from Employee
        Group by ManagerId
        having count(ManagerId) >= 5
    ) m
    on e.id = m.ManagerId
)