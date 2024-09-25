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

## Signal Protocol
### Reasoning for Using the Signal Protocol in my E2E Messaging System ###

### Key Protocols and Algorithms Used ###

### Pros and Cons of Using the Signal Protocol ###
## References
### Overview of Encryption
[Cloudflare](https://www.cloudflare.com/learning/ssl/what-is-encryption/)

### On Encryption Protocols
[Signal](https://signal.org/docs/)
[Signal Double Ratchet Algorithm](https://signal.org/docs/specifications/doubleratchet/)
[Signal X3DH Key Agreement Protocol](https://signal.org/docs/specifications/x3dh/)
[Diffie-Hellman Algorithm Implementation](https://www.scaler.in/diffie-hellman-algorithm-implementation/)
[Diffie-Hellman Algorithm Implementation 2](https://www.geeksforgeeks.org/implementation-diffie-hellman-algorithm/)
[Reference Signal Protocol Implementation](https://github.com/narayanpai1/Signal-Protocol-Implementation)