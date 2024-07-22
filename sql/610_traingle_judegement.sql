# Write your MySQL query statement below

select x, y, z,
case 
    when x + y <= z or x + z <= y or y + z <= x then 'No'
    else 'Yes'
end as triangle
from Triangle;
