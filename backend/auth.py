from flask import Blueprint, request, jsonify
import bcrypt  
import sqlite3

# Creates and returns SQL database connection 
def create_conn():
    conn = sqlite3.connect('data/chat.db')
    return conn

# Create users table to be used for user login and registration
def create_users_table():
    conn = create_conn()
    curr = conn.cursor()

    curr.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            username VARCHAR(255) NOT NULL,
            password VARCHAR(255) NOT NULL
        )    
    """)

    conn.commit()
    conn.close()

# Hash the password using bcrypt with automatic salting
def hash_password(password):
    # Generate bcrypt salt and hash the password
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    return hashed_password

def store_user(username, password):
    conn = create_conn()
    curr = conn.cursor()

    # Hash password with bcrypt (includes salt generation)
    hashed_password = hash_password(password)

    # Store username and hashed password (bcrypt stores the salt inside the hash)
    # Decode to store as a string
    curr.execute("""
        INSERT INTO users (username, password) VALUES (?, ?)
    """, (username, hashed_password.decode('utf-8')))  

    conn.commit()
    conn.close()

# Check the password during login
def check_password(stored_password, provided_password):
    # Compare hashed password with the user-provided password
    return bcrypt.checkpw(provided_password.encode('utf-8'), stored_password.encode('utf-8'))
