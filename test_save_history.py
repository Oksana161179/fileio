import json
import os

history_file = "test_save_history.json"#создаем тестовый файл

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

def test_save_history():#создаем тестовую функцию, которая будет нашу функцию запускать и проверять
    test_file_path = "test_file.txt"#создаем переменную
    test_download_link = "https://file.io/gxbchjk"#создаем вторую переменную

    save_history(test_file_path, test_download_link)#вызываем функцию-save_history

    with open("test_save_history.json", 'r') as f:#проверяем сработала ли наша функция,
    # для этого открываем файл и смотрим что у него внутри(открываем для чтения)
        history = json.load(f)#в переменную-history загружаем все содержимое файла
        assert len(history) == 1#записали одну пару: ключ, значение, длина которой равна единице
        assert history[0]['file_path'] == test_file_path#проверяем конкретные значения
        assert history[0]['download_link'] == test_download_link  # проверяем конкретные значения

    os.remove("test_save_history.json")#удаляем файл

test_save_history()