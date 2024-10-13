import itertools
import string

def generate_codes(length, include_text, include_numbers):
    characters = ''
    
    if include_text:
        characters += string.ascii_letters  # A-Z, a-z
    if include_numbers:
        characters += string.digits  # 0-9
    
    # Generate all possible combinations
    codes = [''.join(code) for code in itertools.product(characters, repeat=length)]
    return codes

def save_to_file(codes, filename='codes.txt'):
    with open(filename, 'w') as file:
        for code in codes:
            file.write(code + '\n')
    print(f"Generated codes saved to {filename}")

def main():
    try:
        length = int(input("Enter the length of the code: "))
        include_text = input("Include text (y/n): ").strip().lower() == 'y'
        include_numbers = input("Include numbers (y/n): ").strip().lower() == 'y'

        codes = generate_codes(length, include_text, include_numbers)
        save_to_file(codes)
        
    except ValueError:
        print("Invalid input! Please enter a valid length.")

if __name__ == "__main__":
    main()
