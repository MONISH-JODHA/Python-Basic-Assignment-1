import hashlib
import os

def calculate_hash(file_path):
    hasher = hashlib.sha256()
    with open(file_path, 'rb') as file:
        while chunk := file.read(1024):
            hasher.update(chunk)
    return hasher.hexdigest()

def find_duplicates(directory):
    hashes = {}
    duplicates = {}

    for root, _, files in os.walk(directory):
        for file in files:
            path = os.path.join(root, file)
            file_hash = calculate_hash(path)

            if file_hash in hashes:
                duplicates.setdefault(file_hash, []).append(path)
            else:
                hashes[file_hash] = path

    return duplicates

def show_duplicates(duplicates):
    index_map = {}
    index = 1

    for file_hash, paths in duplicates.items():
        print(f"\nHash: {file_hash}")
        for path in paths:
            print(f"  [{index}] {path}")
            index_map[index] = path
            index += 1

    return index_map

directory = "/home/monish/assignments/scripts/python_basic"
while True:
    duplicate_map = show_duplicates(find_duplicates(directory))

    if not duplicate_map:
        print("No duplicates found.")
        break

    choice = input("Enter file index to delete (0 to exit): ")
    
    if choice == "0":
        break
    if choice.isdigit() and int(choice) in duplicate_map:
        os.remove(duplicate_map[int(choice)])
        print("File deleted successfully.")
        break
    else:
        print("Invalid choice. Try again.")
