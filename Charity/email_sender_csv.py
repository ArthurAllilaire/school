import csv
from email_sender import send_email, send_to_recipients
with open('Potential_businesses.csv', 'r') as f:
    reader = csv.reader(f)
    recipients = {rows[0]: rows[1] for rows in reader}
    send_to_recipients(recipients)
