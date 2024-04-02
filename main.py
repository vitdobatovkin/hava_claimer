import requests

def send_put_request(cosmos_address):
    url = 'https://havacoin.xyz/api/v2/opt-in'
    payload = {'cosmos': cosmos_address}

    try:
        response = requests.put(url, json=payload)
        if response.status_code == 200:
            print(f'PUT запрос для {cosmos_address} успешно отправлен.')
        else:
            print(f'Ошибка при отправке PUT запроса для {cosmos_address}. Код статуса: {response.status_code}')
    except requests.exceptions.RequestException as e:
        print(f'Ошибка при выполнении запроса: {e}')

def read_cosmos_addresses(filename):
    try:
        with open(filename, 'r') as file:
            addresses = file.readlines()
            addresses = [address.strip() for address in addresses if address.strip()]
            return addresses
    except FileNotFoundError:
        print(f'Файл {filename} не найден.')
        return []

def main():
    cosmos_addresses_file = 'cosmos_addresses.txt'
    cosmos_addresses = read_cosmos_addresses(cosmos_addresses_file)

    if cosmos_addresses:
        for address in cosmos_addresses:
            send_put_request(address)

if __name__ == '__main__':
    main()
