-- Create new table for persons
CREATE TABLE IF NOT EXISTS person (
    id SERIAL PRIMARY KEY,
    cognito_id VARCHAR(50),
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    birthdate DATE,
    email VARCHAR(100),
    phone_number VARCHAR(20),
    system_role VARCHAR(10) CHECK (system_role IN ('Admin','User')),
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW(),
    consents TEXT,
    is_active BOOLEAN
);

--INSERT INTO person VALUES
--(default, 'abc123', 'John', 'Doe', '1990-01-01', 'john@email.com', '+1-234-567-8910', 'User', default, default, null, true),
--(default, 'xyz456', 'Jane', 'Smith', '1995-05-15', 'jane@email.com', '+1-234-567-8911', 'Admin', default, default, null, true);

----------------------------------------------------------------------------------------------------------------------------------

-- Create new table for companies
CREATE TABLE IF NOT EXISTS company (
    id SERIAL PRIMARY KEY,
    address TEXT,
    name VARCHAR(100),
    country VARCHAR(50),
    id_number VARCHAR(30),
    vat_number VARCHAR(30),
    industry VARCHAR(50),
    detailed_activity TEXT,
    company_site TEXT,
    size VARCHAR(20),
    bank_account_country VARCHAR(50),
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW(),
    is_active BOOLEAN
);

--INSERT INTO company VALUES
--(default, '123 Main St, New York, NY 10001', 'Acme Inc', 'USA', '12-3456789', 'AB1234567', 'Manufacturing', 'Widget production', 'www.acme.com', 'Small', 'USA', default, default, true),
--(default, '1 High St, London, UK W1A 1AA', 'Beta Ltd', 'UK', '98-7654321', 'XY9876543', 'Technology', 'Software development', 'www.beta.co.uk', 'Medium', 'UK', default, default, true);
