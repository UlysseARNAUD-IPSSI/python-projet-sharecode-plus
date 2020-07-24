
CREATE TABLE IF NOT EXISTS `codes`(
    `uid` INTEGER PRIMARY KEY AUTOINCREMENT,
    `content` TEXT NOT NULL DEFAULT '# Write your code here...',
    `language` VARCHAR(16) NOT NULL DEFAULT 'text',
    `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    `updated_at` TIMESTAMP
);
