# FILE-INTEGRITY-CHECKER

COMPANY: CODTECH IT SOLUTIONS

NAME: VENKATESH MOGALI

INTERN ID: CT08DL222

DOMAIN: CYBER SECURITY & ETHICAL HACKING

DURATION: 8 WEEKS

MENTOR: NEELA SANTOSH

DESCRIPTION: File integrity checking verifies that a file remains unchanged and free from corruption or tampering. This is typically done by comparing a file's current state (hash,
checksum, or signature) with a known, trusted baseline. This process is crucial for security, ensuring that software, operating system files, and data haven't been altered, potentially by
malicious actors.

CONCEPTS INVOLVED: 
FILE INTEGRITY: Ensures that a file has not been modified, deleted, or corrupted after its original creation.

HASHING: Converts file content into a fixed-length string of characters using cryptographic algorithms. Even a tiny change in the file changes the hash drastically.

SHA-256 ALGORITHM: A secure hashing algorithm from the SHA-2 family, commonly used in digital signatures and blockchain. It produces a 64-character hash value.

DATA COMPRESSION: Hashes are stored, and future checks involve comparing the current file hash against the saved one to detect tampering.

JSON STORAGE: File hashes are stored in a structured .json file, making them easy to read, update, and load programmatically.

COMMAND-LINE INTERFACE (CLI): The script uses argparse to allow users to interact with it via terminal commands (--save and --check).

TOOLS USED:

HASHLIB:	Generate SHA-256 hash of file content.

JSON:	Store and read hash data in a JSON file.

OS:	File path handling and access.

ARGPARSE:	Build the command-line interface.

PYTHON:	Programming language used.

PLATFORMS USED: Here we platforms like VS Code, Terminals like command prompt / powershell, and operating system.

VISUAL STUDIO CODE (VS CODE):	Used as the main IDE/editor to write and run the Python script. It supports extensions like Python IntelliSense, debugging, and terminal integration.

TERMINAL/COMMAND PROMPT/POWERSHELL:	Used to run the script with command-line arguments (--save, --check)

OPERATING SYSTEM:	Works on Windows, Linux, and macOS — cross-platform

SOME OF THE APPLICATIONS OF USING FILE INTEGRITY CHECKING ARE:

CYBERSECURITY: Detects if malicious software has altered critical system files.

DIGITAL FORENSICS: Verifies that evidence files have not been tampered with during investigation.

SYSTEM ADMINISTRATION: Monitor log files or configuration files to catch unauthorized changes.

BACKUP VERIFICATION: Confirm that backup copies are exactly the same as the originals.

SOFTWARE DISTRIBUTION: Ensures downloaded files are not corrupted or modified by comparing provided hashes.

/FILECOIN/IPFS: Use hashes to identify and verify the integrity of content.

COMPLIANCE & AUDITING: Useful in maintaining data integrity logs for legal and compliance purposes.
