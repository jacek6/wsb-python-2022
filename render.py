import subprocess
import os

import fire

PREFIX_FILE = 'plik(`'


def run_file(file_path: str):
    file_path = fix_filepath(file_path)
    result = subprocess.run(['C:\\Users\\hp\\PycharmProjects\\pythonProject1\\venv\\Scripts\\python.exe',
                             file_path], stdout=subprocess.PIPE)
    return result.stdout.decode('utf-8')


def fix_filepath(file_path):
    if not file_path.endswith('.py'):
        file_path += '.py'
    return file_path


def read_code(filepath):
    filepath = fix_filepath(filepath)
    with open(filepath, 'r') as fp:
        return fp.read()


def render_section_python_run(filepath):
    result = f"""\n\n
### Program {os.path.basename(filepath)}

Kod programu:
```python
{read_code(filepath)}
```
\n
"""
    if 'input(' not in read_code(filepath) and 'auto_backup1' not in filepath:
        result += f"""
Output:
```
{run_file(filepath)}
```\n\n
"""
    return result


def render_notatki(folder, input_filename, output_filename):
    result = subprocess.run(['C:\\Users\\hp\\PycharmProjects\\pythonProject1\\venv\\Scripts\\python.exe',
                             os.path.join(folder, 'przyklad_while1.py')], stdout=subprocess.PIPE)
    print('wygenerowano: ')
    print(result.stdout.decode('utf-8'))
    nr_zadania = 1
    with open(os.path.join(folder, input_filename), 'r') as ifp:
        with open(os.path.join(folder, output_filename), 'w') as ofp:
            for orig_line in ifp:
                line = orig_line.strip()
                if line.startswith(PREFIX_FILE):
                    file = line[len(PREFIX_FILE):-2]
                    print(f'program {file}')
                    ofp.write(render_section_python_run(os.path.join(folder, file)))
                elif line.lower() == 'zadanie':
                    ofp.write(f'## zadanie {nr_zadania}\n\n')
                    nr_zadania += 1
                else:
                    ofp.write(orig_line.replace('•', ' - '))


if __name__ == '__main__':
    render_notatki('C:\\Users\\hp\\PycharmProjects\\pythonProject1\\wsb\\zajecia_16_10', 'notatki_raw.md', 'notatki.md')
    print('done')