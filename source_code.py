import PySimpleGUI as sg
import json

PASSWORD_FILE = 'passwords.json'

def save_passwords(passwords):
    with open(PASSWORD_FILE, 'w') as file:
        json.dump(passwords, file)

def load_passwords():
    try:
        with open(PASSWORD_FILE, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def main():
    layout = [
        [sg.Text('Website:'), sg.Input(key='-WEBSITE-')],
        [sg.Text('Username:'), sg.Input(key='-USERNAME-')],
        [sg.Text('Password:'), sg.Input(key='-PASSWORD-')],
        [sg.Button('Save'), sg.Button('Retrieve'), sg.Button('Exit')]
    ]

    window = sg.Window('Password Manager', layout)

    passwords = load_passwords()

    while True:
        event, values = window.read()

        if event == sg.WINDOW_CLOSED or event == 'Exit':
            break

        if event == 'Save':
            website = values['-WEBSITE-']
            username = values['-USERNAME-']
            password = values['-PASSWORD-']
            passwords[website] = {'username': username, 'password': password}
            save_passwords(passwords)
            sg.popup('Password saved successfully!')

        if event == 'Retrieve':
            website = values['-WEBSITE-']
            if website in passwords:
                username = passwords[website]['username']
                password = passwords[website]['password']
                sg.popup(f'Website: {website}\nUsername: {username}\nPassword: {password}')
            else:
                sg.popup('No password found for this website.')

    window.close()

if __name__ == '__main__':
    main()
