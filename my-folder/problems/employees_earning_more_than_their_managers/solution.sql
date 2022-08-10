# Write your MySQL query statement below

SELECT A.name AS Employee
FROM Employee A JOIN Employee B
ON A.managerID = B.ID
WHERE A.salary > B.Salary