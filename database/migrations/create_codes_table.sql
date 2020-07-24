
CREATE TABLE IF NOT EXISTS `codes`(
    `uid` VARCHAR PRIMARY KEY,
    `content` TEXT NOT NULL DEFAULT '# Write your code here...',
    `language` VARCHAR(16) NOT NULL DEFAULT 'Plain text',
    `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    `updated_at` TIMESTAMP
);
