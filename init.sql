CREATE DATABASE ttl;
CREATE USER 'ttl_user'@'%' IDENTIFIED BY 'ttl_pass';
GRANT ALL ON ttl.* TO 'ttl_user'@'%';
FLUSH PRIVILEGES;
