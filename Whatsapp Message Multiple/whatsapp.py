import pywhatkit as kit
import time

# List of phone numbers in the format: +CountryCodePhoneNumber
phone_numbers = ['+918073215402','+916364171253']

# The message you want to send
message = "Hello! This is a test message sent using Python."

# Loop through each phone number and send the message
for number in phone_numbers:
    kit.sendwhatmsg_instantly(number, message)
    print(f"Message sent to {number}")
    
    # Wait a bit before sending the next message to avoid spamming
    time.sleep(5)  # Adjust time based on your needs (avoid sending too quickly)
