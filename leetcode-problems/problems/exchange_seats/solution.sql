# Write your MySQL query statement below
SELECT (
CASE
    WHEN id%2 != 0 AND id != lastID THEN id + 1
    WHEN id%2 != 0 AND id = lastID THEN id
    ELSE id - 1
END
) AS id, student
FROM Seat,(SELECT count(id) AS lastID FROM Seat) AS lastID
ORDER BY id ASC