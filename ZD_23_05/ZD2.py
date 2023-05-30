import os

file = os.stat("pan_tadeusz.txt")
file_size = file.st_size

print(f' Rozmiar pliku to {file_size}')