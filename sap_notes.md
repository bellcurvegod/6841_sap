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
3. **AES (Advanced Encryption Standard)**
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