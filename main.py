import tkinter as tk
import requests

def send_data():
    user_input = entry.get()
    #response = requests.post("http://127.0.0.1:8000/submit", json={"data": user_input})
    response = requests.post("http://172.18.0.2:8000/submit", json={"data": user_input})
    if response.status_code == 200:
        label.config(text="Данные отправлены успешно!")
    else:
        label.config(text="Ошибка при отправке данных.")

def get_data():
    #response = requests.get("http://127.0.0.1:8000/data")
    response = requests.get("http://172.18.0.2:8000/data")
    if response.status_code == 200:
        data = response.text
        result_text.delete(1.0, tk.END)  # Очищаем поле результата
        result_text.insert(tk.END, data)  # Вставляем данные
    else:
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, "Ошибка при получении данных.")

# Создаем основное окно
root = tk.Tk()
root.title("Форма ввода данных")

# Создаем первое поле для ввода текста
entry = tk.Entry(root, width=50)
entry.pack(pady=10)

# Создаем кнопку отправки
send_button = tk.Button(root, text="Отправить", command=send_data)
send_button.pack(pady=5)

# Метка для отображения статуса
label = tk.Label(root, text="")
label.pack(pady=10)

# Создаем второе поле для получения данных
get_button = tk.Button(root, text="Получить данные", command=get_data)
get_button.pack(pady=5)

# Поле для отображения полученных данных
result_text = tk.Text(root, width=60, height=15)
result_text.pack(pady=10)

# Запускаем основной цикл приложения
root.mainloop()