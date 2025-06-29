CREATE TABLE roles (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL UNIQUE,          
    description VARCHAR(255)                   
);

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    first_names VARCHAR(100) NOT NULL,
    first_lastname VARCHAR(100) NOT NULL,
    second_lastname VARCHAR(100),
    email VARCHAR(120) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    role_id INT NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY (role_id) REFERENCES roles(id)
);

INSERT INTO roles (name, description) VALUES
('admin', 'Administrator with full access'),
('coustomer', 'Customer with basic access'),
('waiter', 'Waiter with access to orders and tables');


Insert into users (first_names, first_lastname, second_lastname, email, password, role_id) values
('Admin', 'User', 'System', 'admin@example.com', 'password123', 1),
('Customer', 'User', 'Example', 'customer@example.com', 'password12345', 2),
('Waiter', 'User', 'Example', 'waiter@example.com', 'password1234567', 3);

