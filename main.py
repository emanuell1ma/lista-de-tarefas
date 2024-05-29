print("-"*4,"Welcome to Bank ZeroUm","-"*4)

amount = 0
clients = []
attempts = 3
next_id = 1

class Client:
    def __init__(self, name, age, cpf, password):
        global next_id
        self.id = next_id
        next_id +=1
        self.name = name
        self.age = age
        self.cpf = cpf
        self.password = password
    
    def __str__(self):
        return f"ID: {self.id}, Name: {self.name}, Age: {self.age}, CPF: {self.cpf}, Password: {self.password}"

def register():
    global clients
    name = input("Name: ")
    age = int(input("Age: "))
    cpf = input("CPF: ")
    password = input("Password: ")
    new_client = Client(name, age, cpf, password)
    clients.append(new_client)
    print("Successful Registration")

def withdraw_money():
    global amount
    withdraw = float(input("How much would you like to withdraw: "))
    if amount > withdraw:
        print("Insuffient Balance")
    else:
        print("Successful withdrawal")

def deposit():
    global amount
    current_deposit = float(input("How much would you like to deposit: "))
    amount +=  current_deposit

def balance():
    global amount
    print(amount)

def bank_action():
    cpf_id = input("Type your CPF: ")
    password = input("Type your password: ")
    for client in clients:
        if client.cpf == cpf_id and client.password == password:
            print(f"Welcome {client.name}!")
            while True:
                print("Choose an option")
                print("1 - Deposit")
                print("2 - Withdraw")
                print("3 - Balance")
                print("4 - Exit")
                choose = int(input("Choose: "))
                match choose:
                    case 1: deposit()
                    case 2: withdraw_money()
                    case 3: balance()
                    case 4: print("Session ended, Thank you for using our services")
        else:
            print("Incorrect username or password")

account = input("Do you have an account: [1] - Yes / [2] - No ")

if account == "2":
    register()
    bank_action()
elif account == "1":
    while attempts > 0:
        if bank_action():
            break
        else:
            attempts -= 1
            if attempts == 0:
                print("Passwor Locked.")
                break
            else:
                print(f"Incorrect username or password, you have more {attempts} attempts.")