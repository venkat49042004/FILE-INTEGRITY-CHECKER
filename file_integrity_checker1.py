import hashlib
import os
import json

HASH_FILE = 'file_hashes.json'

def calculate_hash(file_path):
    """Calculate SHA-256 hash of the given file."""
    sha256_hash = hashlib.sha256()
    try:
        with open(file_path, "rb") as f:
            for byte_block in iter(lambda: f.read(4096), b""):
                sha256_hash.update(byte_block)
        return sha256_hash.hexdigest()
    except FileNotFoundError:
        print(f"[ERROR] File not found: {file_path}")
        return None

def save_hashes(file_list):
    """Save hashes of files to a JSON file."""
    hashes = {}
    for file_path in file_list:
        file_hash = calculate_hash(file_path)
        if file_hash:
            hashes[file_path] = file_hash
    with open(HASH_FILE, "w") as f:
        json.dump(hashes, f, indent=4)
    print(f"[INFO] Hashes saved to {HASH_FILE}")

def check_integrity():
    """Check file integrity by comparing hashes."""
    try:
        with open(HASH_FILE, "r") as f:
            stored_hashes = json.load(f)
    except FileNotFoundError:
        print(f"[ERROR] Hash file '{HASH_FILE}' not found.")
        return

    for file_path, original_hash in stored_hashes.items():
        current_hash = calculate_hash(file_path)
        if current_hash:
            if current_hash == original_hash:
                print(f"[OK] {file_path} - No change")
            else:
                print(f"[ALERT] {file_path} - File has been modified!")
        else:
            print(f"[MISSING] {file_path} - File not found")

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="File Integrity Checker")
    parser.add_argument("--save", nargs="+", help="List of files to hash and save")
    parser.add_argument("--check", action="store_true", help="Check integrity using saved hashes")
    
    args = parser.parse_args()

    if args.save:
        save_hashes(args.save)
    elif args.check:
        check_integrity()
    else:
        parser.print_help()
