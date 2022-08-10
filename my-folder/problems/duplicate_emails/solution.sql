# Write your MySQL query statement below
SELECT  email AS Email
FROM (
SELECT count(email) AS cont,email 
    FROM Person
    GROUP BY email

) AS B
WHERE  B.cont>1