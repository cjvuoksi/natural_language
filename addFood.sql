insert into contact (id, email, phone_number)
values
    (1, "a@a.com", 5555555555),
    (2, "b@a.com", 5555555555),
    (3, "c@a.com", 5555555555),
    (4, "d@a.com", 5555555555),
    (5, "store@a.com", 52083555555);

insert into address (id, city, street, zip, state)
values
    (1, "provo", "123 cougar", 55555, "ut"),
    (2, "new york", "123 wall st", 55555, "ny"),
    (3, "dallas", "123 main st", 55555, "tx"),
    (4, "sacramento", "123 main st", 55555, "ca"),
    (5, "orem", "123 main st", 55555, "ut");

insert into person (id, contact_id, address_id, first_name, last_name)
values
    (1, 1, 1, "Alice", "Jones"),
    (2, 2, 2, "Bob", "Smith"),
    (3, 3, 3, "Carl", "Smith"),
    (4, 4, 4, "Dave", "Jones");

insert into customer (id, member_since, fuel_points)
values
    (1, "2020-05-05", 100),
    (3, "2025-01-01", 200);

insert into store (id, address_id, contact_id)
values
    (1, 5, 5);

insert into employee (id, salary, role, store_id)
values
    (1, 10000, "Bagger", 1),
    (2, 70000, "Manager", 1),
    (4, 40000, "Cashier", 1);

insert into food (id, name)
values
    (1, "apple"),
    (2, "beef"),
    (3, "cabbage"),
    (4, "corn"),
    (5, "potato"),
    (6, "rice"),
    (7, "flour"),
    (8, "milk");

insert into product (food_id, id, amount, price, next_rotation_date)
values
    (1, 1, 20, 2, "2025-10-1"),
    (1, 2, 30, 2, "2025-10-15"),
    (2, 3, 20, 2, "2025-10-1"),
    (3, 4, 20, 2, "2025-10-1"),
    (4, 5, 20, 2, "2025-10-1"),
    (5, 6, 20, 2, "2025-10-1"),
    (6, 7, 20, 2, "2025-10-1"),
    (7, 8, 20, 2, "2025-10-1"),
    (8, 9, 20, 2, "2025-10-1"),
    (5, 10, 40, 2, "2025-10-15"),
    (8, 11, 40, 2, "2025-10-15"),
    (2, 12, 40, 2, "2025-10-15");

insert into productstore (product_id, store_id)
values
    (1, 1),
    (2, 1),
    (3, 1),
    (4, 1),
    (5, 1),
    (6, 1),
    (7, 1),
    (8, 1),
    (9, 1),
    (10, 1),
    (11, 1),
    (12, 1);

insert into location (id, aisle, shelf)
values
    (1, 1, 1),
    (2, 1, 2),
    (3, 2, 1),
    (4, 2, 2),
    (5, 3, 1);

insert into productlocation (product_id, location_id)
values
    (1, 1),
    (1, 3),
    (2, 2),
    (2, 4),
    (3, 1),
    (4, 1),
    (5, 2),
    (6, 2),
    (7, 3),
    (8, 3),
    (9, 4),
    (10, 4),
    (11, 5),
    (12, 5);

insert into sale (id, product_id, customer_id, quantity)
values
    (1, 1, 1, 10),
    (2, 2, 3, 10),
    (3, 8, 1, 3);



