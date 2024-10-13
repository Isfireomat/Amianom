import os

folder_path = 'Scriptores'

def execute_python_files(folder):
    results = []
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        if filename.endswith('.py'):
            print(f'Выполнение файла: {filename}')
            try:
                with open(file_path, 'r') as file:
                    code = file.read()
                    globals_dict = {}
                    exec(code, globals_dict)
                    exec_result =  globals_dict.get('result', None)
                    results.append((filename, exec_result))
            except Exception as e:
                print(f'Ошибка при выполнении файла {filename}: {e}')
    return results

results = execute_python_files(folder_path)

for filename, result in results:
    print(f'Результат выполнения файла {filename}: {result}')