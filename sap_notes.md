## What is Encryption and How Does it Work?
A mathematical process that alters data using an encryption algorithm and a key. 
Encryption algorithms convert plain text messages into a cipher text message
that cannot be easily unscrambled by an adversary that does not have a key. A key
is a formula that allows the other party to unscramble the message. 

Data can be encrypted when it is "at rest" - when it is stored, or "in transit" -
while it is being transmitted somewhere else.

There are **2** main types of encryption: symmetric encryption and asymmetric encryption (ie. public key encryption)

**Symmetric Encryption**: Only one key, all communicating parties use the same (secret) key for both encryption and decryption

**Asymmetric Encryption**: Two keys: One key for encryption, different key used for decryption.
Decryption key is kept private (ie. the private key), while the encryption key is shared publicly (ie. public key). 

## What are Encryption Protocols?
Encryption protocols are sets of rules and algorithms designed to ensure secure communication over networks by encrypting data so that only authorized parties can access it.

### Types of Encryption Protocol ###
- TLS (Transport Layer Security): Used for securing communication between a client (eg. web browser) and a server. 
- SSH (Secure Shell): Secures remote login and other network services (eg. UNSW CSE powershell).
- Signal Protocol: Provides end-to-end (E2E) encryption for instant messaging applications such as WhatsApp and Facebook Messenger. We will be using the Signal Protocol for this project. 

### Encryption Protocols used in E2E Messaging Systems ###
**Traits of Cryptographic Protocols Used in Instant Messaging**

**Examples**
1. Signal Protocol
    - Used by instant messaging apps 
2. OMEMO (OMEMO Multi-End Message and Object Encryption)
    - An extension of the Signal Protocol used for XMPP (Extensible Messaging and Presence Protocol) messaging
3. OTR (Off-the-Record Messaging)
4. ZRTP
5. Matrix Protocol

## Understanding the Diffie-Hellman Algorithm ##
Just an overview of how it works as the Signal Protocol uses a variation of it named X3DH.

A common analogy for the DH Algorithm is two people (Alice and Bob) mixing paint. Both agree on a random colour to start with. Alice and Bob then send each other a message and decide on yellow as their **common colour**. They then **set their own colour**, and do not tell the other party their choice. The next step is for both of them to **mix their secret colour with the yellow colour** they agreed on. After mixing, they **send the result to the other party**. Once they have received the mixed result, they **add their secret colour to it**. As a result, **both parties generate the same colour**. This shared colour is known as the **common secret**.

The important part of the DH key exchange is that both parties end up with the same result without ever needing to send the entirety of the common secret across the communication channel. It allows two parties to communicate over a potentially dangerous connection and still come up with a shared secret that they can use to make encryption keys for future communications.

## Signal Protocol
### Reasoning for Using the Signal Protocol in my E2E Messaging System ###

### Overview of Key Protocols and Algorithms Used ###
1. **Double Ratchet Algorithm**
    - The Double Ratchet algorithm is used by two parties (Alice and Bob) to exchange encrypted messages based on a shared secret key. The parties will use some key agreement protocol (X3DH for Signal Protocol) to agree on the shared secret key. Afterwards, the parties will use the Double Ratchet to send and receive encrypted messages. The parties g
2. **X3DH (Extended Triple Diffie-Hellman) Key Agreement**
    - The X3DH algorithm is a step-up from the DH algorithm as it allows for asynchronous communication, meaning that one party can send messages to another offline party. This is a key feature of today's instant messaging apps.
    - It has three phases: Bob publishes his identity key and prekeys to a server, Alice fetches a "prekey bundle" from the server, and uses it to send an inital message to Bob. Finally, Bob receives and processes Alice's initial message. 
    - 
3. **AES (Advanced Encryption Standard)**
    - 
4. **HMAC (Hash-based Message Authentication Code)**
5. **ECDH (Elliptic Curve Diffie-Hellman)**

**Note**: Due to time constraints, I intend on implementing the algorithms and protocols that form the core of the Signal Protocol so as to provide proof of concept. This includes the Double Ratchet Algorithm, the X3DH Key Agreement, and AES.

### Pros and Cons of Using the Signal Protocol ###

## References
### Overview of Encryption
[Cloudflare](https://www.cloudflare.com/learning/ssl/what-is-encryption/)

[Venafi](https://venafi.com/blog/how-do-encryption-protocols-work/)

### Signal Protocol
[Signal](https://signal.org/docs/)

[Signal Double Ratchet Algorithm](https://signal.org/docs/specifications/doubleratchet/)

[Signal X3DH Key Agreement Protocol](https://signal.org/docs/specifications/x3dh/)

[Diffie-Hellman Algorithm](https://www.simplilearn.com/tutorials/cryptography-tutorial/deffie-hellman-key-exchange)

[More Diffie-Hellman Algorithm](https://www.comparitech.com/blog/information-security/diffie-hellman-key-exchange/)

[Diffie-Hellman Algorithm Implementation](https://www.scaler.in/diffie-hellman-algorithm-implementation/)

[Diffie-Hellman Algorithm Implementation 2](https://www.geeksforgeeks.org/implementation-diffie-hellman-algorithm/)

[Generic Signal Protocol Specification and Implementation](https://web.eecs.umich.edu/~yit/signal.html)

[Reference Signal Protocol Implementation](https://github.com/narayanpai1/Signal-Protocol-Implementation)

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