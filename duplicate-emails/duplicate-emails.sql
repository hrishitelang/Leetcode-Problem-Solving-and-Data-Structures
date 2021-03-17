# Write your MySQL query statement below
SELECT DISTINCT email AS Email
FROM Person
GROUP BY email
HAVING count(Email) > 1