
CREATE TABLE IF NOT EXISTS `logs`(
    `uid` VARCHAR PRIMARY KEY,
    `address_ip` VARCHAR NOT NULL,
    `user_agent` VARCHAR NOT NULL,
    `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    `updated_at` TIMESTAMP
);
