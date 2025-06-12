from functions.get_files_info import get_files_info

print(f'TEST 1: \n{get_files_info("calculator", ".")}\n\n')
print(f'TEST 2: \n{get_files_info("calculator", "pkg")}\n\n')
print(f'TEST 3: \n{get_files_info("calculator", "/bin")}\n\n')
print(f'TEST 4: \n{get_files_info("calculator", "../")}\n\n')