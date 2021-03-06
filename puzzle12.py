"""  Work on advanced module puzzle """

# Imports
import zipfile
import re
import os

# CONSTANTS
PUZZLEZIP = "unzip_me_for_instructions.zip"
SOLUTION = 2

def unzipit(fname):
    """ Unzip puzzle file to FS """
    tmppath = 'tmp'
    zipf = zipfile.ZipFile(fname, 'r')
    zipf.extractall(tmppath)
    return tmppath

def searchpath(path, pattern):
    """ Search all of the files in the specified tree for files containing the
    compiled regex pattern
    Return a list with the filename and the matched line
    """
    matches = []
    for folder, _, files in os.walk(path):
        # debug
        print(f'In: {folder}')
        for fname in files:
            with open(folder + '\\\\' + fname) as f:
                for line in f:
                    if match := pattern.search(line):
                        matches.append((folder, fname, line, match.group()))
    return matches

def cleanup(path):
    """ Cleanup the temp path we extracted """
    print(f"Cleanup {path} by hand")

def search_zip(fname, pattern):
    """ Search a zip file for files that match a given pattern """
    matches = []
    zipf = zipfile.ZipFile(fname, 'r')
    for name in zipf.namelist():
        with zipf.open(name) as f:
            for line in f.readlines():
                if match := pattern.search(line):
                    matches.append((fname, name, line, match.group().decode()))
    return matches

if __name__ == "__main__":
    phone_pattern = r'(\d{3})-(\d{3})-(\d{4})'

    print(f'Running Solution #{SOLUTION}')
    if SOLUTION == 1:  # Basic solution - unzip it and traverse the tree
        phonere = re.compile(phone_pattern)
        puzdir = unzipit(PUZZLEZIP)
        matches = searchpath(puzdir, phonere)
        for folder, fname, _, line in matches:
            print(f'Match found in {folder}\\\\{fname}:  {line}')
        cleanup(puzdir)

    elif SOLUTION == 2: # Open the zip and search via the stream
        phonere = re.compile(phone_pattern.encode())
        matches = search_zip(PUZZLEZIP, phonere)
        for folder, fname, _, line in matches:
            print(f'Match found in {folder}\\\\{fname}:  {line}')
