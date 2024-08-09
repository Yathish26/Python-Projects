import random
import time


class BankApp:
    def __init__(self):
        self.accounts = {}
        self.balances = {}
        self.debit_cards = {}

    def main_menu(self):
        print("Welcome to Pluto Banking")
        while True:
            print("\n1. Create a New Account")
            print("2. Deposit")
            print("3. Withdrawal")
            print("4. Balance Info")
            print("5. Apply for a Debit Card")
            print("6. Apply for a Credit Card")
            print("\033[3m7. Admin\033[0m")  # Italic font for "Admin"
            choice = input("Please select an option (1-7): ")
            if choice == '1':
                self.create_account()
            elif choice == '2':
                self.deposit()
            elif choice == '3':
                self.withdrawal()
            elif choice == '4':
                self.balance_info()
            elif choice == '5':
                self.apply_debit_card()
            elif choice == '6':
                self.apply_credit_card()
            elif choice == '7':
                self.admin_menu()
            else:
                print("Invalid choice. Please select a valid option.")

    def admin_menu(self):
        password_attempts = 0
        while password_attempts < 3:
            password = input("Enter the Password: ")
            if password == "Pass@123":
                while True:
                    print("\n1. Total Bank Net Assets")
                    print("2. List the Account Holders")
                    admin_choice = input("Please select an option (1-2): ")
                    if admin_choice == '1':
                        self.total_bank_assets()
                    elif admin_choice == '2':
                        self.list_account_holders()
                    else:
                        print("Invalid choice. Returning to the main menu.")
                        return
                return
            else:
                password_attempts += 1
                print("Incorrect password. Please try again.")
        print("Failed to authenticate. Returning to the main menu.")

    def total_bank_assets(self):
        total_assets = sum(self.balances.values())
        print(f"\nTotal Bank Net Assets: {total_assets}")

    def list_account_holders(self):
        print("\nList of Account Holders:")
        for acc_num, acc_details in self.accounts.items():
            balance = self.balances[acc_num]
            print(f"{acc_details['name']} {acc_num} {balance}")

    def create_account(self):
        print("\n1. Personal Savings Account")
        print("2. Current Account")
        acc_type = input("Please select an account type (1-2): ")
        if acc_type == '1':
            name = input("Enter your full name: ")
            dob = input("Enter your date of birth: ")
            address = input("Enter your home address: ")
            contact = input("Enter your Contact Number: ")
            aadhar = input("Enter your Aadhar card number: ")
            pan = input("Enter your PAN card number: ")
            self.process_loading(4)
            account_number = self.generate_account_number()
            ifsc_code = self.generate_ifsc_code()
            self.accounts[account_number] = {
                'name': name,
                'dob': dob,
                'address': address,
                'contact': contact,
                'aadhar': aadhar,
                'pan': pan,
                'account_type': 'Personal Savings'
            }
            self.balances[account_number] = 0
            print(
                f"Your account has been created successfully!\nHere is your account info:\nYour Bank A/C No: {account_number} and IFSC Code: {ifsc_code}")
        elif acc_type == '2':
            name = input("Enter your full name: ")
            dob = input("Enter your date of birth: ")
            address = input("Enter your home address: ")
            contact = input("Enter your Contact Number: ")
            aadhar = input("Enter your Aadhar card number: ")
            pan = input("Enter your PAN card number: ")
            self.process_loading(2)
            print("Enter Your Business Information: ")
            business_name = input("Enter Your Business Name: ")
            business_registration_number = input("Enter Business Registration Number (GSTIN No): ")
            nature_of_business = input("Enter Your Nature of Business: ")
            self.process_loading(4)
            account_number = self.generate_account_number()
            ifsc_code = self.generate_ifsc_code()
            self.accounts[account_number] = {
                'name': name,
                'dob': dob,
                'address': address,
                'contact': contact,
                'aadhar': aadhar,
                'pan': pan,
                'business_name': business_name,
                'business_registration_number': business_registration_number,
                'nature_of_business': nature_of_business,
                'account_type': 'Current Account'
            }
            self.balances[account_number] = 0
            print(
                f"Your account has been created successfully!\nHere is your account info:\nYour Bank A/C No: {account_number} and IFSC Code: {ifsc_code}")

    def deposit(self):
        account_number = input("Enter your 16 digit account number: ")
        if account_number in self.accounts:
            amount = float(input("How much money would you like to deposit: "))
            self.process_loading(3)
            self.balances[account_number] += amount
            print(f"Your deposit is complete. Your current balance is {self.balances[account_number]}")
        else:
            print("Invalid account number.")

    def withdrawal(self):
        print("How would you like to withdraw?")
        print("1. Account Number")
        print("2. Debit Card Number")
        choice = input("Please select an option (1-2): ")
        if choice == '1':
            account_number = input("Enter your 16 digit account number: ")
            if account_number in self.accounts:
                self.perform_withdrawal(account_number)
            else:
                print("Invalid account number.")
        elif choice == '2':
            card_number = input("Enter your 16 digit debit card number: ")
            account_number = self.get_account_from_debit_card(card_number)
            if account_number:
                self.perform_withdrawal(account_number)
            else:
                print("Invalid debit card number.")
        else:
            print("Invalid choice. Please select a valid option.")

    def perform_withdrawal(self, account_number):
        print(f"Hello {self.accounts[account_number]['name']}")
        amount = float(input("How much money would you like to withdraw: "))
        if amount <= self.balances[account_number]:
            self.process_loading(3)
            self.balances[account_number] -= amount
            print(f"Your money has been withdrawn. {amount} Rs has been withdrawn and remaining balance is {self.balances[account_number]}")
        else:
            print("Insufficient balance.")

    def apply_credit_card(self):
        pan = input("Enter your PAN card number: ")
        self.process_loading(3)
        print("Checking for eligibility...")
        self.process_loading(5)
        print("Congratulations! You are eligible for the Credit Card. Kindly ask the Bank Teller for an Application form.")

    def apply_debit_card(self):
        account_number = input("Enter your 16 digit account number: ")
        if account_number in self.accounts:
            apply = input("Would you like to apply for a Debit card (Y/N)? ")
            if apply.lower() == 'y':
                print("\n1. Would you like to receive a Virtual Debit Card now (Instantly)")
                print("2. Would like to order a Physical Card (Takes one week to deliver)")
                card_choice = input("Please select an option (1-2): ")
                if card_choice == '1':
                    self.process_loading(4)
                    card_number = self.generate_card_number()
                    expiry_date = self.generate_expiry_date()
                    cvv = self.generate_cvv()
                    network = random.choice(['Visa', 'Mastercard', 'Rupay'])
                    self.debit_cards[card_number] = account_number
                    print(f"Congratulations! Here is your Virtual Debit Card\nYour Card Number: {card_number}\nYour Card Expiry Date: {expiry_date}\nYour Card CVV Number: {cvv}\nYour Card Network: {network}\nSoftcopy has been shared to your email ID. If you wish to get a Physical Card, kindly go through the menu again.")
                elif card_choice == '2':
                    print("Thank you for applying! Your Physical Debit Card will be shipped soon to your home address.")
            else:
                print("Returning to the main menu.")
        else:
            print("Invalid account number.")

    def balance_info(self):
        account_number = input("Enter your 16 digit account number: ")
        if account_number in self.accounts:
            self.process_loading(2)
            print(f"Your current balance is {self.balances[account_number]}")
        else:
            print("Invalid account number.")

    def process_loading(self, seconds):
        for _ in range(seconds):
            print("Processing", end="", flush=True)
            for _ in range(3):
                time.sleep(1)
                print(".", end="", flush=True)
            print()

    def generate_account_number(self):
        return ''.join([str(random.randint(0, 9)) for _ in range(16)])

    def generate_ifsc_code(self):
        return f"UTIB{random.randint(10000, 99999)}"

    def generate_card_number(self):
        return ' '.join([''.join([str(random.randint(0, 9)) for _ in range(4)]) for _ in range(4)])

    def generate_expiry_date(self):
        month = str(random.randint(1, 12)).zfill(2)
        year = str(random.randint(24, 29))  # Assuming cards expire between 2024 and 2029
        return f"{month}/{year}"

    def generate_cvv(self):
        return ''.join([str(random.randint(0, 9)) for _ in range(3)])

    def get_account_from_debit_card(self, card_number):
        return self.debit_cards.get(card_number.replace(" ", ""))


if __name__ == "__main__":
    app = BankApp()
    app.main_menu()
