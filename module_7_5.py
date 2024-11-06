import os, subprocess, time
#
# print('Текущая директория:', os.getcwd())
# if os.path.exists('second'):
#     os.chdir('second')
# else:
#     os.mkdir('second')
#     os.chdir('second')
# # os.makedirs(r'third/fourth')
# print('Текущая директория:', os.getcwd())
# print(os.listdir())
# # for i in os.walk('.'):
# #     print(i)
# os.chdir('/Users/andrey_perov/PycharmProjects/1/second')
# print('Текущая директория:', os.getcwd())
# file = [f for f in os.listdir() if os.path.isfile(f)]
# dirs = [d for d in os.listdir() if os.path.isdir(d)]
# print(dirs)
# print(file)
# print(os.stat(file[1]).st_size)
# subprocess.call(["open", file[1]])
directory = '/Users/andrey_perov/PycharmProjects/1/second'

for root, dirs, files in os.walk(directory):
    for file in files:
        filepath = os.path.join(root, file)
        filetime = os.path.getmtime(filepath)
        formated_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
        filesize = os.path.getsize(filepath)
        parent_dir = os.path.dirname(filepath)
        print(f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, '
              f'Время изменения: {formated_time}, Родительская директория: {parent_dir}')