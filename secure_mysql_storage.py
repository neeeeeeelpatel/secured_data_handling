import mysql.connector
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import os
import base64
import getpass

def save_key(key, filename="aes_key.bin"):
    with open(filename, "wb") as f:
        f.write(key)

def load_key(filename="aes_key.bin"):
    if os.path.exists(filename):
        with open(filename, "rb") as f:
            return f.read()
    else:
        key = os.urandom(32)  # Generate new key
        save_key(key, filename)
        return key

# Generate a secure AES key (Store this securely!)
key = load_key()  # 256-bit key (Use environment variables in real-world applications)

# Function to encrypt data
def encrypt_data(plaintext, key):
    cipher = AES.new(key, AES.MODE_CBC)
    iv = cipher.iv
    encrypted_bytes = cipher.encrypt(pad(plaintext.encode(), AES.block_size))
    return base64.b64encode(iv + encrypted_bytes).decode()

# Function to decrypt data
def decrypt_data(encrypted_text, key):
    encrypted_bytes = base64.b64decode(encrypted_text)
    iv = encrypted_bytes[:16]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted_bytes = unpad(cipher.decrypt(encrypted_bytes[16:]), AES.block_size)
    return decrypted_bytes.decode()

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",      # Change this if using a remote database
    user = "root",
    password = "@Neelp9663", 
    database="sample"
)
cursor = conn.cursor()

# Insert encrypted data into MySQL
def insert_user(name, age):
    encrypted_name = encrypt_data(name, key)  # Encrypt name before storing
    cursor.execute("INSERT INTO users (name, age) VALUES (%s, %s)", (encrypted_name, age))
    conn.commit()
    print("User added successfully!")

# Retrieve and decrypt data from MySQL
def fetch_users():
    cursor.execute("SELECT id, name, age FROM users")
    for row in cursor.fetchall():
        decrypted_name = decrypt_data(row[1], key)  # Decrypt the stored name
        print(f"ID: {row[0]}, Name: {decrypted_name}, Age: {row[2]}")

# User input loop
while True:
    name = input("Enter name (or type 'exit' to stop): ")
    if name.lower() == "exit":
        break  # Stop taking input

    age = input("Enter age: ")

    insert_user(name, int(age))  # Store encrypted name in MySQL


print("\nStored Users:")
fetch_users()  # Retrieve and display decrypted data

# Close database connection
cursor.close()
conn.close()



