from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.write_file import write_file

"""
print("\nTest 1: get_files_info")
print(get_files_info("calculator","."))
print("\nTest 2: get_files_info")
print(get_files_info("calculator","pkg"))
print("\nTest 3: get_files_info")
print(get_files_info("calculator","/bin"))
print("\nTest 4: get_files_info")
print(get_files_info("calculator","../"))
print("\nTest lorem: get_file_content")
print(get_file_content("calculator","lorem.txt"))
print("\nTest 1: get_file_content")
print(get_file_content("calculator","main.py"))
print("\nTest 2: get_file_content")
print(get_file_content("calculator","pkg/calculator.py"))
print("\nTest 3: get_file_content")
print(get_file_content("calculator","/bin/cat"))
"""
print("Test 1: write_function")
print(write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum"))
print("Test 2: write_function")
print(write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet"))
print("Test 3: write_function")
print(write_file("calculator", "/tmp/temp.txt", "this should not be allowed"))
