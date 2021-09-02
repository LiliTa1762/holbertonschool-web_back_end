-- In and not out
CREATE TABLE IF NOT EXISTS `users` (
`id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT, 
`email` VARCHAR(255) NOT NULL, 
`name` VARCHAR(255),
`country` ENUM('US', 'CO', 'TN') NOT NULL DEFAULT 'US',
UNIQUE(`email`)
);
