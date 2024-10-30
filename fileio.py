from tkinter import *
from tkinter import filedialog as fd
from tkinter import messagebox as mb
from tkinter import ttk
import requests#запросы к файлу, которые мы будем делать
import pyperclip


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





