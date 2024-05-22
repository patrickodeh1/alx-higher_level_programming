-- script that converts hbtn_0c_0 database to UTF8
-- Convert database to UTF-8-- Convert database to UTF-8
ALTER DATABASE `hbtn_0c_0` CHARACTER SET = utf8mb4 COLLATE = utf8mb4_unicode_ci;
ALTER TABLE `hbtn_0c_0`.`first_table` COLLATE utf8mb4_unicode_ci;
ALTER TABLE `hbtn_0c_0`.`first_table` MODIFY `name` VARCHAR(256) COLLATE utf8mb4_unicode_ci;
