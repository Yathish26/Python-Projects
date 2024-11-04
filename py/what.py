import pywhatkit as kit
import datetime

# Get the current time to schedule the message
now = datetime.datetime.now()

# Set the hour and minute for the message (for example, in 1 minute)
hour = now.hour
minute = now.minute + 1  # Sending message one minute from now

# Send the message
contact_num = "+916364171253"
message = "Hey"

# Send WhatsApp message
kit.sendwhatmsg(contact_num, message, hour, minute)
