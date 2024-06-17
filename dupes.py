#!/usr/bin/python3
import os
import hashlib

def find_duplicates(start_dir):
    hash_dict = {}
    for dirpath, dirnames, filenames in os.walk(start_dir):
        for filename in filenames:
            if filename.endswith('.mp3'):  # Only process mp3 files
                full_path = os.path.join(dirpath, filename)
                hash_obj = hashlib.md5()
                with open(full_path, 'rb') as file:
                    for chunk in iter(lambda: file.read(4096), b""):
                        hash_obj.update(chunk)
                file_id = (hash_obj.digest(), os.path.getsize(full_path))
                duplicate = hash_dict.get(file_id, None)
                if duplicate:
                    print(f"Duplicate found: {full_path} and {duplicate}")
                    os.remove(full_path)
                else:
                    hash_dict[file_id] = full_path

# Let's go
find_duplicates("/path/to/the/directory")
