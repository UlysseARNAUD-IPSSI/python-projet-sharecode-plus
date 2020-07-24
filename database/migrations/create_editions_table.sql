
CREATE TABLE IF NOT EXISTS `editions`(
    `uid` VARCHAR PRIMARY KEY,
    `ip` VARCHAR NOT NULL,
    `user_agent` VARCHAR NOT NULL,
    `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    `updated_at` TIMESTAMP
);
