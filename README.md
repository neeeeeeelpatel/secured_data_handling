# Secure Data Storage System

A database application that securely stores sensitive user information using AES-256 encryption.

## Overview

This project demonstrates secure data storage practices by encrypting sensitive information before storing it in a MySQL database. It uses AES-256 encryption in CBC mode with secure key management to protect user data from unauthorized access.

## Features

- AES-256 bit encryption in CBC mode
- Secure key generation and management
- Transparent encryption/decryption of sensitive data
- Persistence using MySQL database
- Command-line interface for data entry and retrieval

## Requirements

- Python 3.6+
- pycryptodome library
- mysql-connector-python library
- MySQL server

## Installation

1. Install the required dependencies:

```bash
pip install pycryptodome mysql-connector-python
```

2. Set up the MySQL database:

```sql
CREATE DATABASE sample;
USE sample;
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name TEXT NOT NULL,
    age INT NOT NULL
);
```

3. Clone this repository or download the source file:

```bash
git clone https://github.com/yourusername/secure-data-storage.git
cd secure-data-storage
```

4. Update the database connection parameters in the script to match your MySQL configuration:

```python
conn = mysql.connector.connect(
    host="localhost",      
    user="your_username",
    password="your_password", 
    database="sample"
)
```

## Usage

Run the script to start adding and viewing encrypted user data:

```bash
python secure_data_storage.py
```

The application will:

1. Connect to the MySQL database
2. Generate or load an AES encryption key
3. Prompt you to enter user information (name and age)
4. Encrypt the name before storing it in the database
5. Allow you to view all stored users with decrypted information
6. Type 'exit' when prompted for a name to stop adding users and view all stored data

## How It Works

### Key Management

- The system generates a random 256-bit (32-byte) AES key on first run
- The key is stored locally in `aes_key.bin` for subsequent use
- In a production environment, this key should be stored more securely (e.g., using environment variables, a key management service, or a hardware security module)

### Data Encryption

1. **Encryption Process**:
   - A new AES cipher is created in CBC mode with a random IV
   - The data is padded to match the AES block size (16 bytes)
   - The data is encrypted using the AES key
   - The IV is prepended to the encrypted data (for decryption)
   - The result is base64-encoded for safe storage in the database

2. **Decryption Process**:
   - The base64-encoded data is decoded
   - The IV is extracted from the first 16 bytes
   - An AES cipher is initialized with the key and the extracted IV
   - The data is decrypted and unpadded
   - The original plaintext is returned

### Database Operations

- Only encrypted data is stored in the database
- Decryption happens on-the-fly when data is retrieved
- Non-sensitive data (like age) is stored as plaintext

## Security Considerations

- **Key Protection**: The encryption key is critical for security. In production, use a more secure storage method than a local file.
- **Database Access**: Secure your MySQL server with strong authentication and authorization.
- **Memory Management**: Sensitive data in memory is not explicitly cleared in this demo.
- **Password Handling**: Consider using a secure password input method like `getpass` for production use.
- **Transport Security**: Ensure database connections use TLS/SSL in production environments.


