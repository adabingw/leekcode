# Write your MySQL query statement below

SELECT Email
FROM (
  SELECT Email, count(Email) as num
  FROM Person
  group by Email
) as emails
WHERE num > 1;