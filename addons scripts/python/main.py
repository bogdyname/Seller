import requests
import csv
import pandas as pd

def print_table(filename):
    df1 = pd.read_csv(filename, header=None)
    print("The dataframe is:")
    print(df1)
    df1.to_html("html_output.html")
    print("CSV file saved into html file.")

def req(api_key, client_id, url, data):
    # Добавляем заголовок с ключом доступа к API
    headers = {
        'Client-Id': client_id,
        'Api-Key': api_key,
        'Content-Type': 'application/json'
    }

    # Выполняем POST запрос к API
    response = requests.post(url, json=data, headers=headers)

    # Проверяем статус ответа
    if response.status_code == 200:
        # Обработка данных из ответа
        print("Status Code", response.status_code)
        print("JSON Response ", response.json())
    else:
        print(f'Ошибка при выполнении запроса: {response.status_code}')

def print_csv_as_table(file_path):
    with open(file_path, 'r', newline='', encoding='utf-8') as csvfile:
        csv_reader = csv.reader(csvfile)
        data = list(csv_reader)

        max_lengths = [max(len(str(row[i])) for row in data) for i in range(len(data[0]))]

        for row in data:
            print('| ' + ' | '.join(str(row[i]).ljust(max_lengths[i]) for i in range(len(row))) + ' |')

if __name__ == '__main__':
    #основные данные для аутентификации и авторизации
    api_key = '13efd5f3-f7b1-4a5a-b44d-43c49f49787d'
    client_id = '1556799'

    #-----------------------------------------------------------------
    # URL для запроса списка всех продаж
    url = 'https://api-seller.ozon.ru/v1/report/postings/create'
    # Параметры запроса, например, дата начала и конца периода
    data = {
        "filter": {
            "processed_at_from": "2023-12-01T01:00:54.861Z",
            "processed_at_to": "2023-12-31T17:10:54.861Z",
            "delivery_schema": [
            "fbo"
            ],
            "sku": [],
            "cancel_reason_id": [],
            "offer_id": "",
            "status_alias": [],
            "statuses": [],
            "title": ""
        },
        "language": "DEFAULT"
    }
    req(api_key, client_id, url, data)
    #--------------------------------------------------------------

    #--------------------------------------------------------------
    url = 'https://api-seller.ozon.ru/v1/report/info'
    data = { 'code': 'REPORT_seller_postings_1556799_1702823720_3d0162c6-9038-42f3-99ea-02b0456e92fb' }
    req(api_key, client_id, url, data)
    #--------------------------------------------------------------

    # Пример использования функции
    file_path = 'C:\\Users\\bogdy\\Downloads\\ff290f706cfd08c3ba609508bb29bcc3.csv'
    print_table(file_path)