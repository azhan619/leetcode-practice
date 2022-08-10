# Write your MySQL query statement below

SELECT E.name AS Employee, maxSal AS Salary, A.name AS Department
FROM Employee E JOIN (

SELECT D.id,D.name,MAX(salary) AS maxSal
FROM Employee A JOIN Department D
ON A.departmentId = D.id
GROUP BY A.departmentId    



) AS A

ON E.departmentId = A.id
WHERE A.maxSal = salary AND E.departmentID = A.id
