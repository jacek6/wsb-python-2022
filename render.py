import subprocess
import os

import fire

PREFIX_FILE = 'plik(`'


def run_file(file_path: str):
    file_path = fix_filepath(file_path)
    os.chdir(os.path.dirname(file_path))
    result = subprocess.run(['C:\\Users\\hp\\PycharmProjects\\pythonProject1\\venv\\Scripts\\python.exe',
                             file_path], stdout=subprocess.PIPE, )
    return result.stdout.decode('utf-8')


def fix_filepath(file_path):
    if not file_path.endswith('.py'):
        file_path += '.py'
    return file_path


def read_code(filepath):
    filepath = fix_filepath(filepath)
    with open(filepath, 'r', encoding='utf-8') as fp:
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
    if 'input(' not in read_code(filepath) and 'auto_backup1' not in filepath and 'import pygame' not in read_code(filepath):
        result += f"""
Output:
```
{run_file(filepath)}
```\n\n
"""
    return result


def render_notatki(folder, input_filename, output_filename):
    # result = subprocess.run(['C:\\Users\\hp\\PycharmProjects\\pythonProject1\\venv\\Scripts\\python.exe',
    #                          os.path.join(folder, 'przyklad_while1.py')], stdout=subprocess.PIPE)
    # print('wygenerowano: ')
    # print(result.stdout.decode('utf-8'))
    nr_zadania = 1
    with open(os.path.join(folder, input_filename), 'r', encoding='utf-8') as ifp:
        with open(os.path.join(folder, output_filename), 'w', encoding='utf-8') as ofp:
            for orig_line in ifp:
                line = orig_line.strip()
                if line.startswith(PREFIX_FILE):
                    file = line[len(PREFIX_FILE):-2]
                    print(f'program {file}')
                    render_source_code(file, folder, ofp)
                elif line.lower() == 'zadanie':
                    ofp.write(f'## zadanie {nr_zadania}\n\n')
                    nr_zadania += 1
                else:
                    ofp.write(orig_line.replace('•', ' - '))


def render_source_code(file, folder, ofp):
    if not file.endswith('X'):
        ofp.write(render_section_python_run(os.path.join(folder, file)))
    else:
        for i in range(1, 100):
            file_path = os.path.join(folder, f'{file[:-1]}{i}.py')
            if not os.path.exists(file_path):
                break
            ofp.write(render_section_python_run(file_path))




if __name__ == '__main__':
    # render_notatki('C:\\Users\\hp\\PycharmProjects\\pythonProject1\\wsb\\zajecia_16_10', 'notatki_raw.md', 'notatki.md')
    # render_notatki('C:\\Users\\hp\\PycharmProjects\\pythonProject1\\wsb\\zajecia_19_11', 'notatki_raw.md', 'notatki.md')
    # render_notatki('C:\\Users\\hp\\PycharmProjects\\pythonProject1\\wsb\\zajecia_20_11', 'notatki_raw.md', 'notatki.md')
    # render_notatki('C:\\Users\\hp\\PycharmProjects\\pythonProject1\\wsb\\zajecia_14_01', 'notatki_raw.md', 'notatki.md')
    render_notatki('C:\\Users\\hp\\PycharmProjects\\pythonProject1\\wsb\\zajecia_15_01', 'notatki_raw.md', 'notatki.md')
    print('done')