# Results

## Question 1

_What type of food is purchased most frequently across all stores?_

SQL Response:
```sqlite
WITH totals AS (
  SELECT f.name, SUM(s.quantity) AS total_quantity
  FROM Sale s
  JOIN Product p ON p.id = s.product_id
  JOIN Food f ON f.id = p.food_id
  GROUP BY f.id, f.name
)
SELECT name
FROM totals
WHERE total_quantity = (SELECT MAX(total_quantity) FROM totals);
WITH totals AS (
  SELECT f.name, SUM(s.quantity) AS total_quantity
  FROM Sale s
  JOIN Product p ON p.id = s.product_id
  JOIN Food f ON f.id = p.food_id
  GROUP BY f.id, f.name
)
SELECT name
FROM totals
WHERE total_quantity = (SELECT MAX(total_quantity) FROM totals);
```
In addition to its success, including the quantity in its calculation
was cool. It selected the correct answer and did it in the correct way. 
