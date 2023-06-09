roman_account = {
        'account_no': '12345',
        'full_name': 'roman reigns',
        'user_name': 'underdog',
        'password' : '123',
        'ballance': 3000,
        'additional_ballance': 1000
}

jason_account = {
    'account_no': '67890',
    'full_name': 'jason wall',
    'user_name': 'tiger',
    'password': '123',
    'ballance': 5000,
    'additional_ballance': 1000
}


hunter_account = {
    'account_no': '192837',
    'full_name': 'hunter patrick',
    'user_name': 'killer',
    'password': '123',
    'ballance': 8000,
    'additional_ballance': 1000
}

users = [roman_account, jason_account, hunter_account]

def withdraw_money(account: dict, amount: int):
    if account['ballance'] >= amount:
        account['ballance'] -= amount
        print("Don't forget to take your money..!")
        ballance_result(account)
    else:
        total_ballance = account['ballance'] + account['additional_ballance']

        if total_ballance >= amount:
            use_additianol_ballance= input('Insufficent ballance, Use additianol ballance')

            if use_additianol_ballance == 'yes':
                amount_used_additional_account = amount - account['ballance']
                account['ballance'] = 0
                account['additional_ballance'] -= amount_used_additional_account
                ballance_result(account)
            elif use_additianol_ballance == 'no':
                print('Process has ben cancaled')
                ballance_result(account)
            else:
                print('Please tyep "yes" or "no".')
        else:
                print('Insufficent Total balance. Transcation cancaled.')
                ballance_result(account)



def ballance_result(account: dict) -> None:
    print(f" You have{account['ballanced_']} TL account number {account['account_no']}.\nAdditional ballance has {account['additional_ballance']} TL.")

def show_account_information(account: dict):
    print(f'Account Information\n'
          f"===============\n"
          f"name: {account['full_name']}\n"
          f"Account_No: {account['account_no']}\n"
          f"User_Name: {account['user_name']}\n"
          f"Password: {account['password']}\n"
          f"Additional Balance: {account['additional_ballance']}")

def log_in(user_name: str, password: str) -> dict:
    account = {}
    for user in users:
        if user ['user_name'] == user_name and user ['password'] == password:
            account = user
            break

    return account

def menu(auth_account: dict) -> None:
    print(f"""
            welcome, {auth_account ['user_name']}
            =====================================
            withdraw Money      ==> 1
            Deposit             ==> 2
            Account Information ==> 3
            Show Balance        ==> 4
            EFT                 ==> 5
            Exit                ==> 6
            """)

def deposit_money(account: dict, amount: int) -> None:
    account['ballance'] += amount
    ballance_result(account)

    main()

def eft_process(sender_account: dict, reviever_account_no: str, ammount: int):
    process_is_valid = False

    for user in users:
        if user['account_no'] == reviever_account_no:
            user['ballance'] += ammount
            process_is_valid = True
            break
    if process_is_valid:
        ballance_result(sender_account)
    else:
        print('Process faild. Check your information')


def main():
    auth_account = log_in(input('User_name: '), input('Password: '))
    while True:
        if auth_account != {}:
            menu(auth_account)

            process = input('Please choose a process: ')

            if process == '6':
                print('Exit,')
                break
            elif process == '3':
                show_account_information(auth_account)
            elif process == '4':
                ballance_result(auth_account)
            elif process == '1':
                withdraw_money(auth_account, int(input('Amount: ')))
            elif process == '2':
                withdraw_money(auth_account, int(input('Amount: ')))
            elif process == '5':
                eft_process(auth_account,
                            input('Reviever Account No:'),
                            int(input('Amount: ')))
        else:
            print('Check your information')

main()
