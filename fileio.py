from tkinter import *
from tkinter import filedialog as fd
from tkinter import ttk
import requests#запросы к файлу, которые мы будем делать


def upload():#создаем функцию загрузки файлов
    filepath = fd.askopenfilename()#получаем путь к файлу-filepath, который будем загружать
    if filepath:#проверяем, если переменная-filepath не пустая
        files = {'file': open(filepath, 'rb')}#открываем файл в режиме чтения байтов-rb
        response = requests.post('https://file.io', files=files)#получаем ответ-response,
        # отправляя запрос-requests
        if response.status_code == 200:#делаем проверку, если ответ-200, то все хорошо
            link = response.json()['link']#и мы можем в ссылку положить то,
            # что нам прислали в ответ. указав ключ-['link']
            entry.insert(0, link)#выводим в поле ввода, с начальной позицией ноль и вставляем ссылку-link


window = Tk()#создаем окно
window.title("Сохранение файлов в облаке")#задаем заголовок окну
window.geometry("400x200")#задаем размер окну

button = ttk.Button(text="Загрузить файл", command=upload)#создаем кнопку с названием
# и задаем ей команду о загрузке-upload
button.pack()

entry = ttk.Entry()#создаем поле ввода
entry.pack()

window.mainloop()





