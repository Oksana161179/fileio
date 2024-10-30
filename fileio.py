from tkinter import *
from tkinter import filedialog as fd
from tkinter import messagebox as mb
from tkinter import ttk
import requests#запросы к файлу, которые мы будем делать
import pyperclip
import json
import os

history_file = "upload_history.json"#создаем файл с историей наших загрузок(history_file).
# текстовый файл в формате json

def save_history(file_path, link):#создаем функцию сохранения файлов.
    # функция будет принимать путь к файлу(file_path) и ссылку(link)
    history = []#изначально это будет пустой список
    if os.path.exists(history_file):#проверяем, что файл существует в нашей папке
        with open(history_file, 'r') as f:#если он существует, тогда открываем его для чтения
            history = json.load(f)#в наш список-history загружаем файл
    history.append({"file_path": os.path.basename(file_path), "download_link": link})
    #обрабатываем наш файл: "file_path": os.path.basename(file_path)-ключ значение и ссылка-link
    with open(history_file, 'w') as f:#открываем файл для записи, запись добавляем в конец файла
        json.dump(history, f, indent=4)#добавляем новый загруженный файл-f и делаем 4 отступа-indent=4

def upload():#создаем функцию загрузки файлов
    try:#попробовать
        filepath = fd.askopenfilename()#получаем путь к файлу-filepath, который будем загружать
        if filepath:#проверяем, если переменная-filepath не пустая
            with open(filepath, 'rb') as f:#открываем файл в режиме чтения байтов-rb
                files = {'file': f}#открываем файл в режиме чтения байтов-rb
                response = requests.post('https://file.io', files=files)#получаем ответ-response,
                # отправляя запрос-requests
                response.raise_for_status()#строчка позволяет проверить не было ли ошибок
                link = response.json()['link']#и мы можем в ссылку положить то,
                # что нам прислали в ответ. указав ключ-['link']
                entry.delete(0, END)#очищаем поле ввода,
                # перед тем как вставить ссылку, от начала и до конца
                entry.insert(0, link)#выводим в поле ввода,
                # с начальной позицией ноль и вставляем ссылку-link
                pyperclip.copy(link)#отправляем ссылку-link в буфер обмена
                save_history(filepath, link)#сохраняем нашу ссылку
                mb.showinfo("Ссылка скопирована", f"Ссылка {link} успешно скопирована в буфер обмена")
                #сообщаем об этом пользователю с помощью окна с сообщением и указываем конкретную ссылку-{link}
    except Exception as e:#обрабатываем исключения
        mb.showerror("Ошибка", f"Произошла ошибка: {e}")#создаем окно, которое оповестит об ошибке


window = Tk()#создаем окно
window.title("Сохранение файлов в облаке")#задаем заголовок окну
window.geometry("400x200")#задаем размер окну

button = ttk.Button(text="Загрузить файл", command=upload)#создаем кнопку с названием
# и задаем ей команду о загрузке-upload
button.pack()

entry = ttk.Entry()#создаем поле ввода
entry.pack()

window.mainloop()





