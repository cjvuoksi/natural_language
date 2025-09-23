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
    PRIMARY KEY(`location_id`),
    FOREIGN KEY(`product_id`) REFERENCES `Product`(`id`),
    FOREIGN KEY(`location_id`) REFERENCES `Location`(`id`)
);
CREATE TABLE `Person`(
    `id` BIGINT UNSIGNED NOT NULL PRIMARY KEY,
    `contact_id` BIGINT NOT NULL,
    `address_id` BIGINT NOT NULL,
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
    FOREIGN KEY(`address_id`) REFERENCES `Address`(`id`)
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
    `sale_id` BIGINT NOT NULL,
    `food_id` BIGINT UNSIGNED NOT NULL,
    `customer_id` BIGINT NOT NULL,
    `quantity` BIGINT NOT NULL,
    PRIMARY KEY(`sale_id`),
    FOREIGN KEY(`food_id`) REFERENCES `Food`(`id`),
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