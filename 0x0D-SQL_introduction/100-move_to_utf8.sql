-- script that converts hbtn_0c_0 database to UTF8
-- Convert database to UTF-8-- Convert database to UTF-8

DROP TABLE IF EXISTS `first_table`;

CREATE TABLE `first_table` (
  `id` int DEFAULT NULL,
  `name` varchar(256) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `score` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
