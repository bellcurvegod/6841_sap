# 6841 Something Awesome Project
E2E Encrypted Chat System

## Installation Guide 
### Prerequisites
- **npm** and **Node.js** installed on your system
- **Python 3.x** installed on your system
- Required Python packages:
  - `requests`
  - `cryptography`
  - `x3dh`
  - `flask`

### Steps to Set Up and Run the Code 
1. **Clone the repository**: Open a terminal in your code editor and run the following commands:
   ```bash
   git clone <repository-url>
   cd <repository-directory>

## Description
The goal of this project is to design and implement a secure chat system with end-to-end encryption. The chat system will ensure that messages are encrypted on the sender’s device and only decrypted by the intended recipient. This means that even if an adversary intercepts the communication (e.g., over a network), they cannot read the messages. The project will focus on developing cryptographic techniques for key exchange, secure message encryption, and potential defenses against common attack vectors like man-in-the-middle (MITM) attacks.

## Key Features 
- One-on-one messaging 
- End-to-end encryption using the Signal Protocol

## Technologies Used
**Languages** 
- Python
- JavaScript

**Frameworks**
- Flask
- React 

Implementing the X3DH (Extended Triple Diffie-Hellman) protocol involves several steps. Here’s a structured approach in pseudocode format to guide you through the implementation:

### Step 1: Define User Class
- **Attributes**:
  - Identity Key Pair (IK_s, IK_p)
  - Signed PreKey Pair (SPK_s, SPK_p, SPK_sig)
  - One-time PreKeys (OPKs)
  - Public keys for each user to store their key bundles
- **Methods**:
  - `publish()`: Return the user's key bundle (IK_p, SPK_p, SPK_sig, OPKs).

### Step 2: Key Generation
- Create identity keys using ECDH.
- Generate a signed prekey and its signature.
- Generate a set of one-time prekeys.

### Step 3: Establish Session
- **Initiator (Alice)**:
  - Request Bob's key bundle from the server.
  - Generate an ephemeral key pair (EK_s, EK_p).
  - Compute shared secret key (SK) using ECDH and combine it with Bob's keys (IK_p, SPK_p, OPK_p) using a KDF (Key Derivation Function).

### Step 4: Build Initial Message
- Format the message containing:
  - IK_pb (Bob's Identity Key)
  - EK_pa (Alice's Ephemeral Key)
  - OPK_pb (Bob's One-time PreKey)
  - Additional Data (AD)
  - Sign the message with Alice's identity key.

### Step 5: Send Message
- Encrypt the message using a symmetric encryption algorithm (e.g., AES) with the derived shared key (SK).
- Send the encrypted message to Bob.

### Step 6: Responding to the Initial Message (Bob)
- **Receiver (Bob)**:
  - Receive Alice's initial message.
  - Retrieve Alice's key bundle from the server.
  - Derive the shared secret key (SK) using ECDH with the keys provided in the message.

### Step 7: Decrypt and Verify Message
- Decrypt the received message using AES with the shared key.
- Verify the signature of the message to confirm the sender's identity and integrity.

### Step 8: Continuation of the Session
- If necessary, generate new ephemeral keys for subsequent messages.
- Use the Double Ratchet algorithm to update keys for ongoing communication, maintaining forward secrecy.

### Step 9: Error Handling
- Include checks for key mismatches, signature verification failures, and encryption/decryption errors.

### Final Notes
- Ensure the use of secure libraries for cryptographic operations, such as `cryptography` or `PyCryptodome`.
- Document the process clearly, and consider edge cases, such as handling offline scenarios or key compromise.

This structured approach will help you implement the X3DH protocol in Python. You can expand each step into actual code, following the principles outlined in the pseudocode.

For more detailed information, consider reviewing the Signal Protocol documentation and relevant cryptographic principles that underpin X3DH. You may also find the IETF RFCs valuable for understanding the standard protocols involved.