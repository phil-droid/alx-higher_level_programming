--create user
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
--grant priviledges, provide users with broad superuser privileges akin to the root user’s privileges
GRANT ALL PRIVILEDGES ON *.* TO 'user_0d_1'@'localhost';
--flush, reloads the grant tables to ensure that the new privileges are put into effect
FLUSH PRIVILEDGES;
