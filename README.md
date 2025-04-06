# Links for:
- Secure data transmission : https://shorturl.at/84BrZ
- Creation of digital signatures : https://shorturl.at/A6vdN

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

# Digital Signature System

A secure system for creating and verifying digital signatures using RSA encryption and SHA-256 hashing.

## Overview

This project implements a digital signature system using the RSA algorithm for asymmetric cryptography and SHA-256 for secure hashing. It consists of two main components:

1. **Signature Generation**: Creates RSA key pairs, signs messages with the private key, and saves both the message and signature
2. **Signature Verification**: Verifies the authenticity of messages using the public key and signature

## Features

- 2048-bit RSA key generation for strong security
- SHA-256 hashing for message integrity
- PKCS#1 v1.5 signature scheme
- Simple command-line interface
- Secure storage of keys, messages, and signatures

## Requirements

- Python 3.6+
- pycryptodome library

## Installation

1. Install the required dependencies:

```bash
pip install pycryptodome
```

2. Clone this repository or download the source files:

```bash
git clone https://github.com/yourusername/digital-signature-system.git
cd digital-signature-system
```

## Usage

### Generating Keys and Signing Messages

Run the signing script to:
- Generate a new RSA key pair
- Sign a message with your private key
- Save the message and signature

```bash
python sign_message.py
```

The script will:
1. Generate a new RSA key pair (2048-bit)
2. Save the public key to `public_key.pem`
3. Save the private key to `private_key.pem`
4. Prompt you to enter a message
5. Sign the message using your private key
6. Save the message to `message.txt`
7. Save the signature to `signature.bin`

### Verifying Signatures

Run the verification script to check if a message is authentic:

```bash
python verify_signature.py
```

The script will:
1. Load the public key from `public_key.pem`
2. Load the message from `message.txt`
3. Load the signature from `signature.bin`
4. Verify if the signature is valid for the message
5. Display the verification result and the message content

## Security Considerations

- **Private Key Protection**: Keep your `private_key.pem` file secure. Anyone with access to this file can create signatures that appear to be from you.
- **Key Management**: In a production environment, consider using a secure key management system rather than storing keys as files.
- **File Handling**: The current implementation stores messages and signatures as files. In a production system, consider more secure transfer methods.

## How It Works

1. **Key Generation**:
   - An RSA key pair is generated with a 2048-bit key length
   - The private key is used for signing messages
   - The public key is shared with recipients for verification

2. **Signing Process**:
   - The message is hashed using SHA-256
   - The hash is signed using the RSA private key
   - Both the message and signature are saved to files

3. **Verification Process**:
   - The message is hashed using the same SHA-256 algorithm
   - The signature is verified against the hash using the RSA public key
   - If verification succeeds, the message is authentic and unchanged

# Secure Data Transmission System

A secure message exchange system using RSA asymmetric encryption with PKCS#1 OAEP padding scheme.

## Overview

This project implements a secure data transmission system using RSA asymmetric encryption. It consists of two main components:

1. **Receiver** (`receiver.py`): Generates RSA key pairs and decrypts incoming messages using the private key
2. **Sender** (`sender.py`): Encrypts messages using the receiver's public key

The system ensures that only the intended recipient can read the message, as decryption requires the private key which is never shared.

## Features

- 2048-bit RSA encryption for strong security
- PKCS#1 OAEP (Optimal Asymmetric Encryption Padding) for secure encryption
- Simple command-line interface
- Key pair generation and management
- File-based encrypted message exchange

## Requirements

- Python 3.6+
- pycryptodome library

## Installation

1. Install the required dependencies:

```bash
pip install pycryptodome
```

2. Clone this repository or download the source files:

```bash
git clone https://github.com/yourusername/secure-transmission.git
cd secure-transmission
```

## Usage

### Step 1: Generate Keys (Receiver)

Run the receiver script first to generate the key pair (if not already created):

```bash
python receiver.py
```

This will:
- Generate a new 2048-bit RSA key pair
- Save the private key to `private.pem` (kept by the receiver)
- Save the public key to `public.pem` (shared with senders)

Note: If the script doesn't find an encrypted message, it will show an error. This is expected on first run.

### Step 2: Share Public Key

Share the `public.pem` file with anyone who wants to send you encrypted messages.

### Step 3: Send Encrypted Messages (Sender)

To send a message, the sender should have the receiver's `public.pem` file in their directory. Then run:

```bash
python sender.py
```

The script will:
- Load the receiver's public key
- Prompt for a message to encrypt
- Encrypt the message using the public key
- Save the encrypted message to `encrypted_message.bin`

### Step 4: Decrypt Messages (Receiver)

To decrypt a received message (saved as `encrypted_message.bin`), run:

```bash
python receiver.py
```

This will:
- Load the private key
- Decrypt the message
- Display the original message

## How It Works

### Encryption Process

1. The sender loads the recipient's public key
2. The sender's message is encrypted using PKCS1_OAEP padding scheme and RSA
3. The encrypted message is saved to a file

### Decryption Process

1. The recipient loads their private key
2. The encrypted message is loaded from the file
3. The message is decrypted using the private key

## Security Considerations

- **Private Key Protection**: Keep the `private.pem` file secure. Anyone with this file can decrypt messages intended for you.
- **Key Size**: 2048-bit RSA keys provide strong security for most applications, but can be increased to 4096-bit for more sensitive data.
- **Message Size Limitation**: RSA can only encrypt data up to a certain size (typically around 245 bytes for 2048-bit RSA with OAEP). For larger messages, consider using hybrid encryption (RSA + symmetric encryption).
- **Key Rotation**: For enhanced security, generate new key pairs periodically.

## Example

### Generating Keys (Receiver):
```
$ python receiver.py
RSA key pair generated.
Error: No encrypted message found. Expecting file: encrypted_message.bin
```

### Sending a Message (Sender):
```
$ python sender.py
Enter message to send securely: This is a confidential message!
Message encrypted and saved to 'encrypted_message.bin'
```

### Decrypting the Message (Receiver):
```
$ python receiver.py
Key pair already exists.
Decrypted Message: This is a confidential message!
```

## Extending the Project

- Add hybrid encryption to support larger messages
- Implement digital signatures for authentication
- Add file integrity verification
- Create a graphical user interface
- Implement secure key exchange protocols

