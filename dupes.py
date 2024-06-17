#!/usr/bin/python3
import os
import hashlib

def find_duplicates(start_dir):
    """Finds and removes duplicate MP3 files in a given directory and its subdirectories."""
    
    hash_dict = {}  # Dictionary to store file hashes (key) and paths (value)

    for dirpath, dirnames, filenames in os.walk(start_dir): # Walks through all the directories and their subdirectories 
        for filename in filenames: # Iterates over the filenames in the directory.
            if filename.endswith('.mp3'):  # Process only MP3 files
                full_path = os.path.join(dirpath, filename) # gets the full file path, by joining the directory path with the filename.
                hash_obj = hashlib.md5() # MD5 hash object for file hashing.
                with open(full_path, 'rb') as file: # Opens file in binary mode to calculate its hash.
                    for chunk in iter(lambda: file.read(4096), b""):  # Reads file in chunks for efficiency.
                        hash_obj.update(chunk)
                file_id = (hash_obj.digest(), os.path.getsize(full_path)) #  Combines the hash and file size to identify duplicates.
                duplicate = hash_dict.get(file_id, None) #  If the same file ID (hash and size combination) was encountered, it retrieves the path to a duplicate that was found earlier.
                if duplicate: # Checks if a duplicate was found
                    print(f"Duplicate found: {full_path} and {duplicate}")
                    os.remove(full_path)  # Removes the duplicate file
                else:
                    hash_dict[file_id] = full_path # stores the file in the dictionary

# Start the de-duplication process!
find_duplicates("/path/to/your/files") # Calls the find_duplicates method to start the process of finding and removing duplicates.

