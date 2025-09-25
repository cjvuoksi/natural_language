zero-shot
================================================================
Query: Use the following schema and respond with sqlite syntax: 

`...schema... `

What is the most purchased food?

Sql response: 
```
SELECT f.id, f.name, SUM(s.quantity) AS total_quantity
FROM Food AS f
JOIN Product AS p ON p.food_id = f.id
JOIN Sale AS s ON s.product_id = p.id
GROUP BY f.id, f.name
ORDER BY total_quantity DESC
LIMIT 1;
```
Database results: [(1, 'apple', 20)]
Natural Question and Answer: What is the most purchased food? The most purchased food is apple, with 20 units sold.
----------------------------------------------------------------------
Query: Use the following schema and respond with sqlite syntax: 
CREATE TABLE `Food`(
    `id` BIGINT UNSIGNED NOT NULL PRIMARY KEY,
    `name` TEXT NOT NULL
);
CREATE TABLE `Location`(
    `id` BIGINT UNSIGNED NOT NULL PRIMARY KEY,
    `aisle` INT NOT NULL,
    `shelf` INT NOT NULL
);
CREATE TABLE `ProductLocation`(
    `product_id` BIGINT UNSIGNED NOT NULL,
    `location_id` BIGINT NOT NULL,
    FOREIGN KEY(`product_id`) REFERENCES `Product`(`id`),
    FOREIGN KEY(`location_id`) REFERENCES `Location`(`id`)
);
CREATE TABLE `Person`(
    `id` BIGINT UNSIGNED NOT NULL PRIMARY KEY,
    `contact_id` BIGINT NOT NULL,
    `address_id` BIGINT NOT NULL,
    `first_name` TEXT NOT NULL,
    `last_name` TEXXT NOT NULL,
    FOREIGN KEY(`contact_id`) REFERENCES `Contact`(`id`),
    FOREIGN KEY(`address_id`) REFERENCES `Address`(`id`)
);
CREATE TABLE `Address`(
    `id` BIGINT UNSIGNED NOT NULL PRIMARY KEY,
    `city` TEXT NOT NULL,
    `street` TEXT NOT NULL,
    `zip` BIGINT NOT NULL,
    `state` CHAR(2) NOT NULL
);
CREATE TABLE `Customer`(
    `id` BIGINT UNSIGNED NOT NULL PRIMARY KEY,
    `member_since` DATE NOT NULL,
    `fuel_points` BIGINT NOT NULL,
    FOREIGN KEY(`id`) REFERENCES `Person`(`id`)
);
CREATE TABLE `Employee`(
    `id` BIGINT UNSIGNED NOT NULL PRIMARY KEY,
    `salary` BIGINT NOT NULL,
    `role` TEXT NOT NULL,
    `store_id` BIGINT NOT NULL,
    FOREIGN KEY(`id`) REFERENCES `Person`(`id`),
    FOREIGN KEY(`store_id`) REFERENCES `Store`(`id`)
);
CREATE TABLE `Store`(
    `id` BIGINT UNSIGNED NOT NULL PRIMARY KEY,
    `address_id` BIGINT NOT NULL,
    `contact_id` BIGINT NOT NULL,
    FOREIGN KEY(`address_id`) REFERENCES `Address`(`id`),
    FOREIGN KEY(`contact_id`) REFERENCES `Contact`(`id`)
);
CREATE TABLE `Contact`(
    `id` BIGINT UNSIGNED NOT NULL PRIMARY KEY,
    `email` TEXT NOT NULL,
    `phone_number` BIGINT NOT NULL
);
CREATE TABLE `ProductStore`(
    `product_id` BIGINT NOT NULL,
    `store_id` BIGINT UNSIGNED NOT NULL,
    PRIMARY KEY(`product_id`),
    FOREIGN KEY(`product_id`) REFERENCES `Product`(`id`),
    FOREIGN KEY(`store_id`) REFERENCES `Store`(`id`)
);
CREATE TABLE `Sale`(
    `id` BIGINT NOT NULL,
    `product_id` BIGINT UNSIGNED NOT NULL,
    `customer_id` BIGINT NOT NULL,
    `quantity` BIGINT NOT NULL,
    PRIMARY KEY(`id`),
    FOREIGN KEY(`product_id`) REFERENCES `Product`(`id`),
    FOREIGN KEY(`customer_id`) REFERENCES `Customer`(`id`)
);
CREATE TABLE `Product`(
    `food_id` BIGINT NOT NULL,
    `id` BIGINT UNSIGNED NOT NULL PRIMARY KEY,
    `amount` BIGINT NOT NULL,
    `price` BIGINT NOT NULL,
    `next_rotation_date` DATE NOT NULL,
    FOREIGN KEY(`food_id`) REFERENCES `Food`(`id`)
);

Where can you purchase beef?
Sql response: SELECT DISTINCT
  s.id AS store_id,
  a.street,
  a.city,
  a.state,
  a.zip,
  c.email AS store_email,
  c.phone_number AS store_phone,
  l.aisle,
  l.shelf
FROM Food f
JOIN Product p ON p.food_id = f.id
JOIN ProductStore ps ON ps.product_id = p.id
JOIN Store s ON s.id = ps.store_id
LEFT JOIN Address a ON a.id = s.address_id
LEFT JOIN Contact c ON c.id = s.contact_id
LEFT JOIN ProductLocation pl ON pl.product_id = p.id
LEFT JOIN Location l ON l.id = pl.location_id
WHERE lower(f.name) = 'beef';
Database results: [(1, '123 main st', 'orem', 'ut', 55555, 'store@a.com', 52083555555, 1, 1), (1, '123 main st', 'orem', 'ut', 55555, 'store@a.com', 52083555555, 3, 1)]
Natural Question and Answer: Where can you purchase beef? You can purchase beef at Store 1, located at 123 Main St, Orem, UT 55555 (contact: store@a.com, 52083555555).
----------------------------------------------------------------------
Query: Use the following schema and respond with sqlite syntax: 
CREATE TABLE `Food`(
    `id` BIGINT UNSIGNED NOT NULL PRIMARY KEY,
    `name` TEXT NOT NULL
);
CREATE TABLE `Location`(
    `id` BIGINT UNSIGNED NOT NULL PRIMARY KEY,
    `aisle` INT NOT NULL,
    `shelf` INT NOT NULL
);
CREATE TABLE `ProductLocation`(
    `product_id` BIGINT UNSIGNED NOT NULL,
    `location_id` BIGINT NOT NULL,
    FOREIGN KEY(`product_id`) REFERENCES `Product`(`id`),
    FOREIGN KEY(`location_id`) REFERENCES `Location`(`id`)
);
CREATE TABLE `Person`(
    `id` BIGINT UNSIGNED NOT NULL PRIMARY KEY,
    `contact_id` BIGINT NOT NULL,
    `address_id` BIGINT NOT NULL,
    `first_name` TEXT NOT NULL,
    `last_name` TEXXT NOT NULL,
    FOREIGN KEY(`contact_id`) REFERENCES `Contact`(`id`),
    FOREIGN KEY(`address_id`) REFERENCES `Address`(`id`)
);
CREATE TABLE `Address`(
    `id` BIGINT UNSIGNED NOT NULL PRIMARY KEY,
    `city` TEXT NOT NULL,
    `street` TEXT NOT NULL,
    `zip` BIGINT NOT NULL,
    `state` CHAR(2) NOT NULL
);
CREATE TABLE `Customer`(
    `id` BIGINT UNSIGNED NOT NULL PRIMARY KEY,
    `member_since` DATE NOT NULL,
    `fuel_points` BIGINT NOT NULL,
    FOREIGN KEY(`id`) REFERENCES `Person`(`id`)
);
CREATE TABLE `Employee`(
    `id` BIGINT UNSIGNED NOT NULL PRIMARY KEY,
    `salary` BIGINT NOT NULL,
    `role` TEXT NOT NULL,
    `store_id` BIGINT NOT NULL,
    FOREIGN KEY(`id`) REFERENCES `Person`(`id`),
    FOREIGN KEY(`store_id`) REFERENCES `Store`(`id`)
);
CREATE TABLE `Store`(
    `id` BIGINT UNSIGNED NOT NULL PRIMARY KEY,
    `address_id` BIGINT NOT NULL,
    `contact_id` BIGINT NOT NULL,
    FOREIGN KEY(`address_id`) REFERENCES `Address`(`id`),
    FOREIGN KEY(`contact_id`) REFERENCES `Contact`(`id`)
);
CREATE TABLE `Contact`(
    `id` BIGINT UNSIGNED NOT NULL PRIMARY KEY,
    `email` TEXT NOT NULL,
    `phone_number` BIGINT NOT NULL
);
CREATE TABLE `ProductStore`(
    `product_id` BIGINT NOT NULL,
    `store_id` BIGINT UNSIGNED NOT NULL,
    PRIMARY KEY(`product_id`),
    FOREIGN KEY(`product_id`) REFERENCES `Product`(`id`),
    FOREIGN KEY(`store_id`) REFERENCES `Store`(`id`)
);
CREATE TABLE `Sale`(
    `id` BIGINT NOT NULL,
    `product_id` BIGINT UNSIGNED NOT NULL,
    `customer_id` BIGINT NOT NULL,
    `quantity` BIGINT NOT NULL,
    PRIMARY KEY(`id`),
    FOREIGN KEY(`product_id`) REFERENCES `Product`(`id`),
    FOREIGN KEY(`customer_id`) REFERENCES `Customer`(`id`)
);
CREATE TABLE `Product`(
    `food_id` BIGINT NOT NULL,
    `id` BIGINT UNSIGNED NOT NULL PRIMARY KEY,
    `amount` BIGINT NOT NULL,
    `price` BIGINT NOT NULL,
    `next_rotation_date` DATE NOT NULL,
    FOREIGN KEY(`food_id`) REFERENCES `Food`(`id`)
);

In which states do employees live?
Sql response: SELECT DISTINCT a.state
FROM Employee e
JOIN Person p ON p.id = e.id
JOIN Address a ON a.id = p.address_id
ORDER BY a.state;
Database results: [('ca',), ('ny',), ('ut',)]
Natural Question and Answer: In which states do employees live? Employees live in CA, NY, and UT.
----------------------------------------------------------------------
Query: Use the following schema and respond with sqlite syntax: 
CREATE TABLE `Food`(
    `id` BIGINT UNSIGNED NOT NULL PRIMARY KEY,
    `name` TEXT NOT NULL
);
CREATE TABLE `Location`(
    `id` BIGINT UNSIGNED NOT NULL PRIMARY KEY,
    `aisle` INT NOT NULL,
    `shelf` INT NOT NULL
);
CREATE TABLE `ProductLocation`(
    `product_id` BIGINT UNSIGNED NOT NULL,
    `location_id` BIGINT NOT NULL,
    FOREIGN KEY(`product_id`) REFERENCES `Product`(`id`),
    FOREIGN KEY(`location_id`) REFERENCES `Location`(`id`)
);
CREATE TABLE `Person`(
    `id` BIGINT UNSIGNED NOT NULL PRIMARY KEY,
    `contact_id` BIGINT NOT NULL,
    `address_id` BIGINT NOT NULL,
    `first_name` TEXT NOT NULL,
    `last_name` TEXXT NOT NULL,
    FOREIGN KEY(`contact_id`) REFERENCES `Contact`(`id`),
    FOREIGN KEY(`address_id`) REFERENCES `Address`(`id`)
);
CREATE TABLE `Address`(
    `id` BIGINT UNSIGNED NOT NULL PRIMARY KEY,
    `city` TEXT NOT NULL,
    `street` TEXT NOT NULL,
    `zip` BIGINT NOT NULL,
    `state` CHAR(2) NOT NULL
);
CREATE TABLE `Customer`(
    `id` BIGINT UNSIGNED NOT NULL PRIMARY KEY,
    `member_since` DATE NOT NULL,
    `fuel_points` BIGINT NOT NULL,
    FOREIGN KEY(`id`) REFERENCES `Person`(`id`)
);
CREATE TABLE `Employee`(
    `id` BIGINT UNSIGNED NOT NULL PRIMARY KEY,
    `salary` BIGINT NOT NULL,
    `role` TEXT NOT NULL,
    `store_id` BIGINT NOT NULL,
    FOREIGN KEY(`id`) REFERENCES `Person`(`id`),
    FOREIGN KEY(`store_id`) REFERENCES `Store`(`id`)
);
CREATE TABLE `Store`(
    `id` BIGINT UNSIGNED NOT NULL PRIMARY KEY,
    `address_id` BIGINT NOT NULL,
    `contact_id` BIGINT NOT NULL,
    FOREIGN KEY(`address_id`) REFERENCES `Address`(`id`),
    FOREIGN KEY(`contact_id`) REFERENCES `Contact`(`id`)
);
CREATE TABLE `Contact`(
    `id` BIGINT UNSIGNED NOT NULL PRIMARY KEY,
    `email` TEXT NOT NULL,
    `phone_number` BIGINT NOT NULL
);
CREATE TABLE `ProductStore`(
    `product_id` BIGINT NOT NULL,
    `store_id` BIGINT UNSIGNED NOT NULL,
    PRIMARY KEY(`product_id`),
    FOREIGN KEY(`product_id`) REFERENCES `Product`(`id`),
    FOREIGN KEY(`store_id`) REFERENCES `Store`(`id`)
);
CREATE TABLE `Sale`(
    `id` BIGINT NOT NULL,
    `product_id` BIGINT UNSIGNED NOT NULL,
    `customer_id` BIGINT NOT NULL,
    `quantity` BIGINT NOT NULL,
    PRIMARY KEY(`id`),
    FOREIGN KEY(`product_id`) REFERENCES `Product`(`id`),
    FOREIGN KEY(`customer_id`) REFERENCES `Customer`(`id`)
);
CREATE TABLE `Product`(
    `food_id` BIGINT NOT NULL,
    `id` BIGINT UNSIGNED NOT NULL PRIMARY KEY,
    `amount` BIGINT NOT NULL,
    `price` BIGINT NOT NULL,
    `next_rotation_date` DATE NOT NULL,
    FOREIGN KEY(`food_id`) REFERENCES `Food`(`id`)
);

Which employees live in the same state as the store they work at and what is their role?
Sql response: SELECT e.id,
       p.first_name,
       p.last_name,
       e.role
FROM Employee e
JOIN Person p ON p.id = e.id
JOIN Address pa ON pa.id = p.address_id
JOIN Store s ON s.id = e.store_id
JOIN Address sa ON sa.id = s.address_id
WHERE pa.state = sa.state;
Database results: [(1, 'Alice', 'Jones', 'Bagger')]
Natural Question and Answer: Which employees live in the same state as the store they work at and what is their role? Alice Jones works as a Bagger and lives in the same state as the store she works at.
----------------------------------------------------------------------
double-shot, single domain
================================================================
Query: Use the following schema and respond with sqlite syntax: 
CREATE TABLE `Food`(
    `id` BIGINT UNSIGNED NOT NULL PRIMARY KEY,
    `name` TEXT NOT NULL
);
CREATE TABLE `Location`(
    `id` BIGINT UNSIGNED NOT NULL PRIMARY KEY,
    `aisle` INT NOT NULL,
    `shelf` INT NOT NULL
);
CREATE TABLE `ProductLocation`(
    `product_id` BIGINT UNSIGNED NOT NULL,
    `location_id` BIGINT NOT NULL,
    FOREIGN KEY(`product_id`) REFERENCES `Product`(`id`),
    FOREIGN KEY(`location_id`) REFERENCES `Location`(`id`)
);
CREATE TABLE `Person`(
    `id` BIGINT UNSIGNED NOT NULL PRIMARY KEY,
    `contact_id` BIGINT NOT NULL,
    `address_id` BIGINT NOT NULL,
    `first_name` TEXT NOT NULL,
    `last_name` TEXXT NOT NULL,
    FOREIGN KEY(`contact_id`) REFERENCES `Contact`(`id`),
    FOREIGN KEY(`address_id`) REFERENCES `Address`(`id`)
);
CREATE TABLE `Address`(
    `id` BIGINT UNSIGNED NOT NULL PRIMARY KEY,
    `city` TEXT NOT NULL,
    `street` TEXT NOT NULL,
    `zip` BIGINT NOT NULL,
    `state` CHAR(2) NOT NULL
);
CREATE TABLE `Customer`(
    `id` BIGINT UNSIGNED NOT NULL PRIMARY KEY,
    `member_since` DATE NOT NULL,
    `fuel_points` BIGINT NOT NULL,
    FOREIGN KEY(`id`) REFERENCES `Person`(`id`)
);
CREATE TABLE `Employee`(
    `id` BIGINT UNSIGNED NOT NULL PRIMARY KEY,
    `salary` BIGINT NOT NULL,
    `role` TEXT NOT NULL,
    `store_id` BIGINT NOT NULL,
    FOREIGN KEY(`id`) REFERENCES `Person`(`id`),
    FOREIGN KEY(`store_id`) REFERENCES `Store`(`id`)
);
CREATE TABLE `Store`(
    `id` BIGINT UNSIGNED NOT NULL PRIMARY KEY,
    `address_id` BIGINT NOT NULL,
    `contact_id` BIGINT NOT NULL,
    FOREIGN KEY(`address_id`) REFERENCES `Address`(`id`),
    FOREIGN KEY(`contact_id`) REFERENCES `Contact`(`id`)
);
CREATE TABLE `Contact`(
    `id` BIGINT UNSIGNED NOT NULL PRIMARY KEY,
    `email` TEXT NOT NULL,
    `phone_number` BIGINT NOT NULL
);
CREATE TABLE `ProductStore`(
    `product_id` BIGINT NOT NULL,
    `store_id` BIGINT UNSIGNED NOT NULL,
    PRIMARY KEY(`product_id`),
    FOREIGN KEY(`product_id`) REFERENCES `Product`(`id`),
    FOREIGN KEY(`store_id`) REFERENCES `Store`(`id`)
);
CREATE TABLE `Sale`(
    `id` BIGINT NOT NULL,
    `product_id` BIGINT UNSIGNED NOT NULL,
    `customer_id` BIGINT NOT NULL,
    `quantity` BIGINT NOT NULL,
    PRIMARY KEY(`id`),
    FOREIGN KEY(`product_id`) REFERENCES `Product`(`id`),
    FOREIGN KEY(`customer_id`) REFERENCES `Customer`(`id`)
);
CREATE TABLE `Product`(
    `food_id` BIGINT NOT NULL,
    `id` BIGINT UNSIGNED NOT NULL PRIMARY KEY,
    `amount` BIGINT NOT NULL,
    `price` BIGINT NOT NULL,
    `next_rotation_date` DATE NOT NULL,
    FOREIGN KEY(`food_id`) REFERENCES `Food`(`id`)
);
Which employees are also customers?
Select first_name, last_name from employee join person on employee.id = person.id join customer on person.id = customer.id;
What is the most purchased food?
Sql response: WITH totals AS (
  SELECT f.name, SUM(s.quantity) AS total_quantity
  FROM Sale s
  JOIN Product p ON p.id = s.product_id
  JOIN Food f ON f.id = p.food_id
  GROUP BY f.id, f.name
)
SELECT name, total_quantity
FROM totals
WHERE total_quantity = (SELECT MAX(total_quantity) FROM totals);
Database results: [('apple', 20)]
Natural Question and Answer: What is the most purchased food? The most purchased food is apple, with 20 units sold.
----------------------------------------------------------------------
Query: Use the following schema and respond with sqlite syntax: 
CREATE TABLE `Food`(
    `id` BIGINT UNSIGNED NOT NULL PRIMARY KEY,
    `name` TEXT NOT NULL
);
CREATE TABLE `Location`(
    `id` BIGINT UNSIGNED NOT NULL PRIMARY KEY,
    `aisle` INT NOT NULL,
    `shelf` INT NOT NULL
);
CREATE TABLE `ProductLocation`(
    `product_id` BIGINT UNSIGNED NOT NULL,
    `location_id` BIGINT NOT NULL,
    FOREIGN KEY(`product_id`) REFERENCES `Product`(`id`),
    FOREIGN KEY(`location_id`) REFERENCES `Location`(`id`)
);
CREATE TABLE `Person`(
    `id` BIGINT UNSIGNED NOT NULL PRIMARY KEY,
    `contact_id` BIGINT NOT NULL,
    `address_id` BIGINT NOT NULL,
    `first_name` TEXT NOT NULL,
    `last_name` TEXXT NOT NULL,
    FOREIGN KEY(`contact_id`) REFERENCES `Contact`(`id`),
    FOREIGN KEY(`address_id`) REFERENCES `Address`(`id`)
);
CREATE TABLE `Address`(
    `id` BIGINT UNSIGNED NOT NULL PRIMARY KEY,
    `city` TEXT NOT NULL,
    `street` TEXT NOT NULL,
    `zip` BIGINT NOT NULL,
    `state` CHAR(2) NOT NULL
);
CREATE TABLE `Customer`(
    `id` BIGINT UNSIGNED NOT NULL PRIMARY KEY,
    `member_since` DATE NOT NULL,
    `fuel_points` BIGINT NOT NULL,
    FOREIGN KEY(`id`) REFERENCES `Person`(`id`)
);
CREATE TABLE `Employee`(
    `id` BIGINT UNSIGNED NOT NULL PRIMARY KEY,
    `salary` BIGINT NOT NULL,
    `role` TEXT NOT NULL,
    `store_id` BIGINT NOT NULL,
    FOREIGN KEY(`id`) REFERENCES `Person`(`id`),
    FOREIGN KEY(`store_id`) REFERENCES `Store`(`id`)
);
CREATE TABLE `Store`(
    `id` BIGINT UNSIGNED NOT NULL PRIMARY KEY,
    `address_id` BIGINT NOT NULL,
    `contact_id` BIGINT NOT NULL,
    FOREIGN KEY(`address_id`) REFERENCES `Address`(`id`),
    FOREIGN KEY(`contact_id`) REFERENCES `Contact`(`id`)
);
CREATE TABLE `Contact`(
    `id` BIGINT UNSIGNED NOT NULL PRIMARY KEY,
    `email` TEXT NOT NULL,
    `phone_number` BIGINT NOT NULL
);
CREATE TABLE `ProductStore`(
    `product_id` BIGINT NOT NULL,
    `store_id` BIGINT UNSIGNED NOT NULL,
    PRIMARY KEY(`product_id`),
    FOREIGN KEY(`product_id`) REFERENCES `Product`(`id`),
    FOREIGN KEY(`store_id`) REFERENCES `Store`(`id`)
);
CREATE TABLE `Sale`(
    `id` BIGINT NOT NULL,
    `product_id` BIGINT UNSIGNED NOT NULL,
    `customer_id` BIGINT NOT NULL,
    `quantity` BIGINT NOT NULL,
    PRIMARY KEY(`id`),
    FOREIGN KEY(`product_id`) REFERENCES `Product`(`id`),
    FOREIGN KEY(`customer_id`) REFERENCES `Customer`(`id`)
);
CREATE TABLE `Product`(
    `food_id` BIGINT NOT NULL,
    `id` BIGINT UNSIGNED NOT NULL PRIMARY KEY,
    `amount` BIGINT NOT NULL,
    `price` BIGINT NOT NULL,
    `next_rotation_date` DATE NOT NULL,
    FOREIGN KEY(`food_id`) REFERENCES `Food`(`id`)
);
Which employees are also customers?
Select first_name, last_name from employee join person on employee.id = person.id join customer on person.id = customer.id;
Where can you purchase beef?
Sql response: SELECT p.first_name, p.last_name
FROM Employee e
JOIN Person p ON p.id = e.id
JOIN Customer c ON c.id = p.id;

SELECT DISTINCT s.id AS store_id, a.street, a.city, a.state, a.zip
FROM Food f
JOIN Product pr ON pr.food_id = f.id
JOIN ProductStore ps ON ps.product_id = pr.id
JOIN Store s ON s.id = ps.store_id
JOIN Address a ON a.id = s.address_id
WHERE f.name LIKE '%beef%';
You can only execute one statement at a time.
Natural Question and Answer: Where can you purchase beef? Error
----------------------------------------------------------------------
Query: Use the following schema and respond with sqlite syntax: 
CREATE TABLE `Food`(
    `id` BIGINT UNSIGNED NOT NULL PRIMARY KEY,
    `name` TEXT NOT NULL
);
CREATE TABLE `Location`(
    `id` BIGINT UNSIGNED NOT NULL PRIMARY KEY,
    `aisle` INT NOT NULL,
    `shelf` INT NOT NULL
);
CREATE TABLE `ProductLocation`(
    `product_id` BIGINT UNSIGNED NOT NULL,
    `location_id` BIGINT NOT NULL,
    FOREIGN KEY(`product_id`) REFERENCES `Product`(`id`),
    FOREIGN KEY(`location_id`) REFERENCES `Location`(`id`)
);
CREATE TABLE `Person`(
    `id` BIGINT UNSIGNED NOT NULL PRIMARY KEY,
    `contact_id` BIGINT NOT NULL,
    `address_id` BIGINT NOT NULL,
    `first_name` TEXT NOT NULL,
    `last_name` TEXXT NOT NULL,
    FOREIGN KEY(`contact_id`) REFERENCES `Contact`(`id`),
    FOREIGN KEY(`address_id`) REFERENCES `Address`(`id`)
);
CREATE TABLE `Address`(
    `id` BIGINT UNSIGNED NOT NULL PRIMARY KEY,
    `city` TEXT NOT NULL,
    `street` TEXT NOT NULL,
    `zip` BIGINT NOT NULL,
    `state` CHAR(2) NOT NULL
);
CREATE TABLE `Customer`(
    `id` BIGINT UNSIGNED NOT NULL PRIMARY KEY,
    `member_since` DATE NOT NULL,
    `fuel_points` BIGINT NOT NULL,
    FOREIGN KEY(`id`) REFERENCES `Person`(`id`)
);
CREATE TABLE `Employee`(
    `id` BIGINT UNSIGNED NOT NULL PRIMARY KEY,
    `salary` BIGINT NOT NULL,
    `role` TEXT NOT NULL,
    `store_id` BIGINT NOT NULL,
    FOREIGN KEY(`id`) REFERENCES `Person`(`id`),
    FOREIGN KEY(`store_id`) REFERENCES `Store`(`id`)
);
CREATE TABLE `Store`(
    `id` BIGINT UNSIGNED NOT NULL PRIMARY KEY,
    `address_id` BIGINT NOT NULL,
    `contact_id` BIGINT NOT NULL,
    FOREIGN KEY(`address_id`) REFERENCES `Address`(`id`),
    FOREIGN KEY(`contact_id`) REFERENCES `Contact`(`id`)
);
CREATE TABLE `Contact`(
    `id` BIGINT UNSIGNED NOT NULL PRIMARY KEY,
    `email` TEXT NOT NULL,
    `phone_number` BIGINT NOT NULL
);
CREATE TABLE `ProductStore`(
    `product_id` BIGINT NOT NULL,
    `store_id` BIGINT UNSIGNED NOT NULL,
    PRIMARY KEY(`product_id`),
    FOREIGN KEY(`product_id`) REFERENCES `Product`(`id`),
    FOREIGN KEY(`store_id`) REFERENCES `Store`(`id`)
);
CREATE TABLE `Sale`(
    `id` BIGINT NOT NULL,
    `product_id` BIGINT UNSIGNED NOT NULL,
    `customer_id` BIGINT NOT NULL,
    `quantity` BIGINT NOT NULL,
    PRIMARY KEY(`id`),
    FOREIGN KEY(`product_id`) REFERENCES `Product`(`id`),
    FOREIGN KEY(`customer_id`) REFERENCES `Customer`(`id`)
);
CREATE TABLE `Product`(
    `food_id` BIGINT NOT NULL,
    `id` BIGINT UNSIGNED NOT NULL PRIMARY KEY,
    `amount` BIGINT NOT NULL,
    `price` BIGINT NOT NULL,
    `next_rotation_date` DATE NOT NULL,
    FOREIGN KEY(`food_id`) REFERENCES `Food`(`id`)
);
Which employees are also customers?
Select first_name, last_name from employee join person on employee.id = person.id join customer on person.id = customer.id;
In which states do employees live?
Sql response: SELECT DISTINCT a.state
FROM Employee e
JOIN Person p ON e.id = p.id
JOIN Address a ON p.address_id = a.id;
Database results: [('ut',), ('ny',), ('ca',)]
Natural Question and Answer: In which states do employees live? Employees live in UT, NY, and CA.
----------------------------------------------------------------------
Query: Use the following schema and respond with sqlite syntax: 
CREATE TABLE `Food`(
    `id` BIGINT UNSIGNED NOT NULL PRIMARY KEY,
    `name` TEXT NOT NULL
);
CREATE TABLE `Location`(
    `id` BIGINT UNSIGNED NOT NULL PRIMARY KEY,
    `aisle` INT NOT NULL,
    `shelf` INT NOT NULL
);
CREATE TABLE `ProductLocation`(
    `product_id` BIGINT UNSIGNED NOT NULL,
    `location_id` BIGINT NOT NULL,
    FOREIGN KEY(`product_id`) REFERENCES `Product`(`id`),
    FOREIGN KEY(`location_id`) REFERENCES `Location`(`id`)
);
CREATE TABLE `Person`(
    `id` BIGINT UNSIGNED NOT NULL PRIMARY KEY,
    `contact_id` BIGINT NOT NULL,
    `address_id` BIGINT NOT NULL,
    `first_name` TEXT NOT NULL,
    `last_name` TEXXT NOT NULL,
    FOREIGN KEY(`contact_id`) REFERENCES `Contact`(`id`),
    FOREIGN KEY(`address_id`) REFERENCES `Address`(`id`)
);
CREATE TABLE `Address`(
    `id` BIGINT UNSIGNED NOT NULL PRIMARY KEY,
    `city` TEXT NOT NULL,
    `street` TEXT NOT NULL,
    `zip` BIGINT NOT NULL,
    `state` CHAR(2) NOT NULL
);
CREATE TABLE `Customer`(
    `id` BIGINT UNSIGNED NOT NULL PRIMARY KEY,
    `member_since` DATE NOT NULL,
    `fuel_points` BIGINT NOT NULL,
    FOREIGN KEY(`id`) REFERENCES `Person`(`id`)
);
CREATE TABLE `Employee`(
    `id` BIGINT UNSIGNED NOT NULL PRIMARY KEY,
    `salary` BIGINT NOT NULL,
    `role` TEXT NOT NULL,
    `store_id` BIGINT NOT NULL,
    FOREIGN KEY(`id`) REFERENCES `Person`(`id`),
    FOREIGN KEY(`store_id`) REFERENCES `Store`(`id`)
);
CREATE TABLE `Store`(
    `id` BIGINT UNSIGNED NOT NULL PRIMARY KEY,
    `address_id` BIGINT NOT NULL,
    `contact_id` BIGINT NOT NULL,
    FOREIGN KEY(`address_id`) REFERENCES `Address`(`id`),
    FOREIGN KEY(`contact_id`) REFERENCES `Contact`(`id`)
);
CREATE TABLE `Contact`(
    `id` BIGINT UNSIGNED NOT NULL PRIMARY KEY,
    `email` TEXT NOT NULL,
    `phone_number` BIGINT NOT NULL
);
CREATE TABLE `ProductStore`(
    `product_id` BIGINT NOT NULL,
    `store_id` BIGINT UNSIGNED NOT NULL,
    PRIMARY KEY(`product_id`),
    FOREIGN KEY(`product_id`) REFERENCES `Product`(`id`),
    FOREIGN KEY(`store_id`) REFERENCES `Store`(`id`)
);
CREATE TABLE `Sale`(
    `id` BIGINT NOT NULL,
    `product_id` BIGINT UNSIGNED NOT NULL,
    `customer_id` BIGINT NOT NULL,
    `quantity` BIGINT NOT NULL,
    PRIMARY KEY(`id`),
    FOREIGN KEY(`product_id`) REFERENCES `Product`(`id`),
    FOREIGN KEY(`customer_id`) REFERENCES `Customer`(`id`)
);
CREATE TABLE `Product`(
    `food_id` BIGINT NOT NULL,
    `id` BIGINT UNSIGNED NOT NULL PRIMARY KEY,
    `amount` BIGINT NOT NULL,
    `price` BIGINT NOT NULL,
    `next_rotation_date` DATE NOT NULL,
    FOREIGN KEY(`food_id`) REFERENCES `Food`(`id`)
);
Which employees are also customers?
Select first_name, last_name from employee join person on employee.id = person.id join customer on person.id = customer.id;
Which employees live in the same state as the store they work at and what is their role?
Sql response: SELECT p.first_name, p.last_name
FROM Employee e
JOIN Person p ON e.id = p.id
JOIN Customer c ON p.id = c.id;

SELECT p.first_name, p.last_name, e.role
FROM Employee e
JOIN Person p ON e.id = p.id
JOIN Address pa ON p.address_id = pa.id
JOIN Store s ON e.store_id = s.id
JOIN Address sa ON s.address_id = sa.id
WHERE pa.state = sa.state;
You can only execute one statement at a time.
Natural Question and Answer: Which employees live in the same state as the store they work at and what is their role? Error
----------------------------------------------------------------------
single-shot, cross domain
================================================================
Query: Use the following schema and respond with sqlite syntax: 
CREATE TABLE `Food`(
    `id` BIGINT UNSIGNED NOT NULL PRIMARY KEY,
    `name` TEXT NOT NULL
);
CREATE TABLE `Location`(
    `id` BIGINT UNSIGNED NOT NULL PRIMARY KEY,
    `aisle` INT NOT NULL,
    `shelf` INT NOT NULL
);
CREATE TABLE `ProductLocation`(
    `product_id` BIGINT UNSIGNED NOT NULL,
    `location_id` BIGINT NOT NULL,
    FOREIGN KEY(`product_id`) REFERENCES `Product`(`id`),
    FOREIGN KEY(`location_id`) REFERENCES `Location`(`id`)
);
CREATE TABLE `Person`(
    `id` BIGINT UNSIGNED NOT NULL PRIMARY KEY,
    `contact_id` BIGINT NOT NULL,
    `address_id` BIGINT NOT NULL,
    `first_name` TEXT NOT NULL,
    `last_name` TEXXT NOT NULL,
    FOREIGN KEY(`contact_id`) REFERENCES `Contact`(`id`),
    FOREIGN KEY(`address_id`) REFERENCES `Address`(`id`)
);
CREATE TABLE `Address`(
    `id` BIGINT UNSIGNED NOT NULL PRIMARY KEY,
    `city` TEXT NOT NULL,
    `street` TEXT NOT NULL,
    `zip` BIGINT NOT NULL,
    `state` CHAR(2) NOT NULL
);
CREATE TABLE `Customer`(
    `id` BIGINT UNSIGNED NOT NULL PRIMARY KEY,
    `member_since` DATE NOT NULL,
    `fuel_points` BIGINT NOT NULL,
    FOREIGN KEY(`id`) REFERENCES `Person`(`id`)
);
CREATE TABLE `Employee`(
    `id` BIGINT UNSIGNED NOT NULL PRIMARY KEY,
    `salary` BIGINT NOT NULL,
    `role` TEXT NOT NULL,
    `store_id` BIGINT NOT NULL,
    FOREIGN KEY(`id`) REFERENCES `Person`(`id`),
    FOREIGN KEY(`store_id`) REFERENCES `Store`(`id`)
);
CREATE TABLE `Store`(
    `id` BIGINT UNSIGNED NOT NULL PRIMARY KEY,
    `address_id` BIGINT NOT NULL,
    `contact_id` BIGINT NOT NULL,
    FOREIGN KEY(`address_id`) REFERENCES `Address`(`id`),
    FOREIGN KEY(`contact_id`) REFERENCES `Contact`(`id`)
);
CREATE TABLE `Contact`(
    `id` BIGINT UNSIGNED NOT NULL PRIMARY KEY,
    `email` TEXT NOT NULL,
    `phone_number` BIGINT NOT NULL
);
CREATE TABLE `ProductStore`(
    `product_id` BIGINT NOT NULL,
    `store_id` BIGINT UNSIGNED NOT NULL,
    PRIMARY KEY(`product_id`),
    FOREIGN KEY(`product_id`) REFERENCES `Product`(`id`),
    FOREIGN KEY(`store_id`) REFERENCES `Store`(`id`)
);
CREATE TABLE `Sale`(
    `id` BIGINT NOT NULL,
    `product_id` BIGINT UNSIGNED NOT NULL,
    `customer_id` BIGINT NOT NULL,
    `quantity` BIGINT NOT NULL,
    PRIMARY KEY(`id`),
    FOREIGN KEY(`product_id`) REFERENCES `Product`(`id`),
    FOREIGN KEY(`customer_id`) REFERENCES `Customer`(`id`)
);
CREATE TABLE `Product`(
    `food_id` BIGINT NOT NULL,
    `id` BIGINT UNSIGNED NOT NULL PRIMARY KEY,
    `amount` BIGINT NOT NULL,
    `price` BIGINT NOT NULL,
    `next_rotation_date` DATE NOT NULL,
    FOREIGN KEY(`food_id`) REFERENCES `Food`(`id`)
);
Example database: create table person (
    person_id integer primary key,
    name varchar(20) not null
);

create table phone (
    phone_id integer primary key,
    person_id integer not null,
    area_code int not null,
    number int not null,
    can_recieve_sms tinyint not null,
    foreign key (person_id) references person (person_id)
);

create table address (
    address_id integer primary key,
    person_id integer not null,
    street varchar(50),
    zip integer not null
);

create table zip (
    zip integer primary key,
    city varchar(35),
    state_two_letter_code char(2)
);

create table dog (
    dog_id integer primary key,
    name varchar(35),
    breed varchar(35),
    birth_date date
);

create table award (
    award_id integer primary key,
    dog_id integer not null,
    event_date date,
    award_name varchar(25) not null,
    foreign key (dog_id) references dog (dog_id)
);

create table person_dog (
    dog_id integer,
    person_id integer,
    foreign key (dog_id) references dog (dog_id),
 foreign key (person_id) references person (person_id)
);
Who doesn't have a way for us to text them?  
SELECT p.person_id, p.name
FROM person p
LEFT JOIN phone ph ON p.person_id = ph.person_id AND ph.can_recieve_sms = 1
WHERE ph.phone_id IS NULL;
What is the most purchased food?
Sql response: WITH food_totals AS (
  SELECT f.id, f.name, SUM(s.quantity) AS total_purchased
  FROM Sale s
  JOIN Product p ON p.id = s.product_id
  JOIN Food f ON f.id = p.food_id
  GROUP BY f.id, f.name
)
SELECT id, name, total_purchased
FROM food_totals
WHERE total_purchased = (SELECT MAX(total_purchased) FROM food_totals);
Database results: [(1, 'apple', 20)]
Natural Question and Answer: What is the most purchased food? The most purchased food is apple, with 20 units sold.
----------------------------------------------------------------------
Query: Use the following schema and respond with sqlite syntax: 
CREATE TABLE `Food`(
    `id` BIGINT UNSIGNED NOT NULL PRIMARY KEY,
    `name` TEXT NOT NULL
);
CREATE TABLE `Location`(
    `id` BIGINT UNSIGNED NOT NULL PRIMARY KEY,
    `aisle` INT NOT NULL,
    `shelf` INT NOT NULL
);
CREATE TABLE `ProductLocation`(
    `product_id` BIGINT UNSIGNED NOT NULL,
    `location_id` BIGINT NOT NULL,
    FOREIGN KEY(`product_id`) REFERENCES `Product`(`id`),
    FOREIGN KEY(`location_id`) REFERENCES `Location`(`id`)
);
CREATE TABLE `Person`(
    `id` BIGINT UNSIGNED NOT NULL PRIMARY KEY,
    `contact_id` BIGINT NOT NULL,
    `address_id` BIGINT NOT NULL,
    `first_name` TEXT NOT NULL,
    `last_name` TEXXT NOT NULL,
    FOREIGN KEY(`contact_id`) REFERENCES `Contact`(`id`),
    FOREIGN KEY(`address_id`) REFERENCES `Address`(`id`)
);
CREATE TABLE `Address`(
    `id` BIGINT UNSIGNED NOT NULL PRIMARY KEY,
    `city` TEXT NOT NULL,
    `street` TEXT NOT NULL,
    `zip` BIGINT NOT NULL,
    `state` CHAR(2) NOT NULL
);
CREATE TABLE `Customer`(
    `id` BIGINT UNSIGNED NOT NULL PRIMARY KEY,
    `member_since` DATE NOT NULL,
    `fuel_points` BIGINT NOT NULL,
    FOREIGN KEY(`id`) REFERENCES `Person`(`id`)
);
CREATE TABLE `Employee`(
    `id` BIGINT UNSIGNED NOT NULL PRIMARY KEY,
    `salary` BIGINT NOT NULL,
    `role` TEXT NOT NULL,
    `store_id` BIGINT NOT NULL,
    FOREIGN KEY(`id`) REFERENCES `Person`(`id`),
    FOREIGN KEY(`store_id`) REFERENCES `Store`(`id`)
);
CREATE TABLE `Store`(
    `id` BIGINT UNSIGNED NOT NULL PRIMARY KEY,
    `address_id` BIGINT NOT NULL,
    `contact_id` BIGINT NOT NULL,
    FOREIGN KEY(`address_id`) REFERENCES `Address`(`id`),
    FOREIGN KEY(`contact_id`) REFERENCES `Contact`(`id`)
);
CREATE TABLE `Contact`(
    `id` BIGINT UNSIGNED NOT NULL PRIMARY KEY,
    `email` TEXT NOT NULL,
    `phone_number` BIGINT NOT NULL
);
CREATE TABLE `ProductStore`(
    `product_id` BIGINT NOT NULL,
    `store_id` BIGINT UNSIGNED NOT NULL,
    PRIMARY KEY(`product_id`),
    FOREIGN KEY(`product_id`) REFERENCES `Product`(`id`),
    FOREIGN KEY(`store_id`) REFERENCES `Store`(`id`)
);
CREATE TABLE `Sale`(
    `id` BIGINT NOT NULL,
    `product_id` BIGINT UNSIGNED NOT NULL,
    `customer_id` BIGINT NOT NULL,
    `quantity` BIGINT NOT NULL,
    PRIMARY KEY(`id`),
    FOREIGN KEY(`product_id`) REFERENCES `Product`(`id`),
    FOREIGN KEY(`customer_id`) REFERENCES `Customer`(`id`)
);
CREATE TABLE `Product`(
    `food_id` BIGINT NOT NULL,
    `id` BIGINT UNSIGNED NOT NULL PRIMARY KEY,
    `amount` BIGINT NOT NULL,
    `price` BIGINT NOT NULL,
    `next_rotation_date` DATE NOT NULL,
    FOREIGN KEY(`food_id`) REFERENCES `Food`(`id`)
);
Example database: create table person (
    person_id integer primary key,
    name varchar(20) not null
);

create table phone (
    phone_id integer primary key,
    person_id integer not null,
    area_code int not null,
    number int not null,
    can_recieve_sms tinyint not null,
    foreign key (person_id) references person (person_id)
);

create table address (
    address_id integer primary key,
    person_id integer not null,
    street varchar(50),
    zip integer not null
);

create table zip (
    zip integer primary key,
    city varchar(35),
    state_two_letter_code char(2)
);

create table dog (
    dog_id integer primary key,
    name varchar(35),
    breed varchar(35),
    birth_date date
);

create table award (
    award_id integer primary key,
    dog_id integer not null,
    event_date date,
    award_name varchar(25) not null,
    foreign key (dog_id) references dog (dog_id)
);

create table person_dog (
    dog_id integer,
    person_id integer,
    foreign key (dog_id) references dog (dog_id),
 foreign key (person_id) references person (person_id)
);
Who doesn't have a way for us to text them?  
SELECT p.person_id, p.name
FROM person p
LEFT JOIN phone ph ON p.person_id = ph.person_id AND ph.can_recieve_sms = 1
WHERE ph.phone_id IS NULL;
Where can you purchase beef?
Sql response: SELECT DISTINCT s.id AS store_id, a.street, a.city, a.state, a.zip
FROM Store s
JOIN Address a ON a.id = s.address_id
JOIN ProductStore ps ON ps.store_id = s.id
JOIN Product p ON p.id = ps.product_id
JOIN Food f ON f.id = p.food_id
WHERE lower(f.name) LIKE '%beef%';
Database results: [(1, '123 main st', 'orem', 'ut', 55555)]
Natural Question and Answer: Where can you purchase beef? Beef can be purchased at 123 main st, orem, ut 55555.
----------------------------------------------------------------------
Query: Use the following schema and respond with sqlite syntax: 
CREATE TABLE `Food`(
    `id` BIGINT UNSIGNED NOT NULL PRIMARY KEY,
    `name` TEXT NOT NULL
);
CREATE TABLE `Location`(
    `id` BIGINT UNSIGNED NOT NULL PRIMARY KEY,
    `aisle` INT NOT NULL,
    `shelf` INT NOT NULL
);
CREATE TABLE `ProductLocation`(
    `product_id` BIGINT UNSIGNED NOT NULL,
    `location_id` BIGINT NOT NULL,
    FOREIGN KEY(`product_id`) REFERENCES `Product`(`id`),
    FOREIGN KEY(`location_id`) REFERENCES `Location`(`id`)
);
CREATE TABLE `Person`(
    `id` BIGINT UNSIGNED NOT NULL PRIMARY KEY,
    `contact_id` BIGINT NOT NULL,
    `address_id` BIGINT NOT NULL,
    `first_name` TEXT NOT NULL,
    `last_name` TEXXT NOT NULL,
    FOREIGN KEY(`contact_id`) REFERENCES `Contact`(`id`),
    FOREIGN KEY(`address_id`) REFERENCES `Address`(`id`)
);
CREATE TABLE `Address`(
    `id` BIGINT UNSIGNED NOT NULL PRIMARY KEY,
    `city` TEXT NOT NULL,
    `street` TEXT NOT NULL,
    `zip` BIGINT NOT NULL,
    `state` CHAR(2) NOT NULL
);
CREATE TABLE `Customer`(
    `id` BIGINT UNSIGNED NOT NULL PRIMARY KEY,
    `member_since` DATE NOT NULL,
    `fuel_points` BIGINT NOT NULL,
    FOREIGN KEY(`id`) REFERENCES `Person`(`id`)
);
CREATE TABLE `Employee`(
    `id` BIGINT UNSIGNED NOT NULL PRIMARY KEY,
    `salary` BIGINT NOT NULL,
    `role` TEXT NOT NULL,
    `store_id` BIGINT NOT NULL,
    FOREIGN KEY(`id`) REFERENCES `Person`(`id`),
    FOREIGN KEY(`store_id`) REFERENCES `Store`(`id`)
);
CREATE TABLE `Store`(
    `id` BIGINT UNSIGNED NOT NULL PRIMARY KEY,
    `address_id` BIGINT NOT NULL,
    `contact_id` BIGINT NOT NULL,
    FOREIGN KEY(`address_id`) REFERENCES `Address`(`id`),
    FOREIGN KEY(`contact_id`) REFERENCES `Contact`(`id`)
);
CREATE TABLE `Contact`(
    `id` BIGINT UNSIGNED NOT NULL PRIMARY KEY,
    `email` TEXT NOT NULL,
    `phone_number` BIGINT NOT NULL
);
CREATE TABLE `ProductStore`(
    `product_id` BIGINT NOT NULL,
    `store_id` BIGINT UNSIGNED NOT NULL,
    PRIMARY KEY(`product_id`),
    FOREIGN KEY(`product_id`) REFERENCES `Product`(`id`),
    FOREIGN KEY(`store_id`) REFERENCES `Store`(`id`)
);
CREATE TABLE `Sale`(
    `id` BIGINT NOT NULL,
    `product_id` BIGINT UNSIGNED NOT NULL,
    `customer_id` BIGINT NOT NULL,
    `quantity` BIGINT NOT NULL,
    PRIMARY KEY(`id`),
    FOREIGN KEY(`product_id`) REFERENCES `Product`(`id`),
    FOREIGN KEY(`customer_id`) REFERENCES `Customer`(`id`)
);
CREATE TABLE `Product`(
    `food_id` BIGINT NOT NULL,
    `id` BIGINT UNSIGNED NOT NULL PRIMARY KEY,
    `amount` BIGINT NOT NULL,
    `price` BIGINT NOT NULL,
    `next_rotation_date` DATE NOT NULL,
    FOREIGN KEY(`food_id`) REFERENCES `Food`(`id`)
);
Example database: create table person (
    person_id integer primary key,
    name varchar(20) not null
);

create table phone (
    phone_id integer primary key,
    person_id integer not null,
    area_code int not null,
    number int not null,
    can_recieve_sms tinyint not null,
    foreign key (person_id) references person (person_id)
);

create table address (
    address_id integer primary key,
    person_id integer not null,
    street varchar(50),
    zip integer not null
);

create table zip (
    zip integer primary key,
    city varchar(35),
    state_two_letter_code char(2)
);

create table dog (
    dog_id integer primary key,
    name varchar(35),
    breed varchar(35),
    birth_date date
);

create table award (
    award_id integer primary key,
    dog_id integer not null,
    event_date date,
    award_name varchar(25) not null,
    foreign key (dog_id) references dog (dog_id)
);

create table person_dog (
    dog_id integer,
    person_id integer,
    foreign key (dog_id) references dog (dog_id),
 foreign key (person_id) references person (person_id)
);
Who doesn't have a way for us to text them?  
SELECT p.person_id, p.name
FROM person p
LEFT JOIN phone ph ON p.person_id = ph.person_id AND ph.can_recieve_sms = 1
WHERE ph.phone_id IS NULL;
In which states do employees live?
Sql response: SELECT DISTINCT a.state
FROM Employee e
JOIN Person p ON p.id = e.id
JOIN Address a ON a.id = p.address_id
ORDER BY a.state;
Database results: [('ca',), ('ny',), ('ut',)]
Natural Question and Answer: In which states do employees live? Employees live in CA, NY, and UT.
----------------------------------------------------------------------
Query: Use the following schema and respond with sqlite syntax: 
CREATE TABLE `Food`(
    `id` BIGINT UNSIGNED NOT NULL PRIMARY KEY,
    `name` TEXT NOT NULL
);
CREATE TABLE `Location`(
    `id` BIGINT UNSIGNED NOT NULL PRIMARY KEY,
    `aisle` INT NOT NULL,
    `shelf` INT NOT NULL
);
CREATE TABLE `ProductLocation`(
    `product_id` BIGINT UNSIGNED NOT NULL,
    `location_id` BIGINT NOT NULL,
    FOREIGN KEY(`product_id`) REFERENCES `Product`(`id`),
    FOREIGN KEY(`location_id`) REFERENCES `Location`(`id`)
);
CREATE TABLE `Person`(
    `id` BIGINT UNSIGNED NOT NULL PRIMARY KEY,
    `contact_id` BIGINT NOT NULL,
    `address_id` BIGINT NOT NULL,
    `first_name` TEXT NOT NULL,
    `last_name` TEXXT NOT NULL,
    FOREIGN KEY(`contact_id`) REFERENCES `Contact`(`id`),
    FOREIGN KEY(`address_id`) REFERENCES `Address`(`id`)
);
CREATE TABLE `Address`(
    `id` BIGINT UNSIGNED NOT NULL PRIMARY KEY,
    `city` TEXT NOT NULL,
    `street` TEXT NOT NULL,
    `zip` BIGINT NOT NULL,
    `state` CHAR(2) NOT NULL
);
CREATE TABLE `Customer`(
    `id` BIGINT UNSIGNED NOT NULL PRIMARY KEY,
    `member_since` DATE NOT NULL,
    `fuel_points` BIGINT NOT NULL,
    FOREIGN KEY(`id`) REFERENCES `Person`(`id`)
);
CREATE TABLE `Employee`(
    `id` BIGINT UNSIGNED NOT NULL PRIMARY KEY,
    `salary` BIGINT NOT NULL,
    `role` TEXT NOT NULL,
    `store_id` BIGINT NOT NULL,
    FOREIGN KEY(`id`) REFERENCES `Person`(`id`),
    FOREIGN KEY(`store_id`) REFERENCES `Store`(`id`)
);
CREATE TABLE `Store`(
    `id` BIGINT UNSIGNED NOT NULL PRIMARY KEY,
    `address_id` BIGINT NOT NULL,
    `contact_id` BIGINT NOT NULL,
    FOREIGN KEY(`address_id`) REFERENCES `Address`(`id`),
    FOREIGN KEY(`contact_id`) REFERENCES `Contact`(`id`)
);
CREATE TABLE `Contact`(
    `id` BIGINT UNSIGNED NOT NULL PRIMARY KEY,
    `email` TEXT NOT NULL,
    `phone_number` BIGINT NOT NULL
);
CREATE TABLE `ProductStore`(
    `product_id` BIGINT NOT NULL,
    `store_id` BIGINT UNSIGNED NOT NULL,
    PRIMARY KEY(`product_id`),
    FOREIGN KEY(`product_id`) REFERENCES `Product`(`id`),
    FOREIGN KEY(`store_id`) REFERENCES `Store`(`id`)
);
CREATE TABLE `Sale`(
    `id` BIGINT NOT NULL,
    `product_id` BIGINT UNSIGNED NOT NULL,
    `customer_id` BIGINT NOT NULL,
    `quantity` BIGINT NOT NULL,
    PRIMARY KEY(`id`),
    FOREIGN KEY(`product_id`) REFERENCES `Product`(`id`),
    FOREIGN KEY(`customer_id`) REFERENCES `Customer`(`id`)
);
CREATE TABLE `Product`(
    `food_id` BIGINT NOT NULL,
    `id` BIGINT UNSIGNED NOT NULL PRIMARY KEY,
    `amount` BIGINT NOT NULL,
    `price` BIGINT NOT NULL,
    `next_rotation_date` DATE NOT NULL,
    FOREIGN KEY(`food_id`) REFERENCES `Food`(`id`)
);
Example database: create table person (
    person_id integer primary key,
    name varchar(20) not null
);

create table phone (
    phone_id integer primary key,
    person_id integer not null,
    area_code int not null,
    number int not null,
    can_recieve_sms tinyint not null,
    foreign key (person_id) references person (person_id)
);

create table address (
    address_id integer primary key,
    person_id integer not null,
    street varchar(50),
    zip integer not null
);

create table zip (
    zip integer primary key,
    city varchar(35),
    state_two_letter_code char(2)
);

create table dog (
    dog_id integer primary key,
    name varchar(35),
    breed varchar(35),
    birth_date date
);

create table award (
    award_id integer primary key,
    dog_id integer not null,
    event_date date,
    award_name varchar(25) not null,
    foreign key (dog_id) references dog (dog_id)
);

create table person_dog (
    dog_id integer,
    person_id integer,
    foreign key (dog_id) references dog (dog_id),
 foreign key (person_id) references person (person_id)
);
Who doesn't have a way for us to text them?  
SELECT p.person_id, p.name
FROM person p
LEFT JOIN phone ph ON p.person_id = ph.person_id AND ph.can_recieve_sms = 1
WHERE ph.phone_id IS NULL;
Which employees live in the same state as the store they work at and what is their role?
Sql response: SELECT
  p.id AS employee_id,
  p.first_name,
  p.last_name,
  e.role
FROM Employee e
JOIN Person p ON p.id = e.id
JOIN Address pa ON pa.id = p.address_id
JOIN Store s ON s.id = e.store_id
JOIN Address sa ON sa.id = s.address_id
WHERE pa.state = sa.state;
Database results: [(1, 'Alice', 'Jones', 'Bagger')]
Natural Question and Answer: Which employees live in the same state as the store they work at and what is their role? Alice Jones works as a Bagger.
----------------------------------------------------------------------

Process finished with exit code 0
