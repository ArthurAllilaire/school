from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
import smtplib
import os
import re

MY_ADDRESS = "a.allilaire@cityoflondonschool.org.uk"         # Replace with yours
MY_PASSWORD = "jingleBells1"      # Replace with yours
RECIPIENT_ADDRESS = "chloeallilaire@icloud.com"  # Replace with yours


HOST_ADDRESS = 'smtp-mail.outlook.com'   # Replace with yours
HOST_PORT = 587                          # Replace with yours


# All the HTML at the bottom of the email
# {} are: Name, title, department, email, email, email, city of london school thumbnail, twitter, facebook, insta, linkedin
def get_base64_files(directory):
    """
    Based on the first one of this list: https://www.geeksforgeeks.org/how-to-iterate-over-files-in-directory-using-python/ all are good this is just the most common.
    """
    result = {}
    for filename in os.listdir(directory):
        full_name = os.path.join(directory, filename)
        if os.path.isfile(full_name):
            with open(full_name, 'r') as f:
                result[filename] = f.read()

    return result


def format_image_dict(images):
    """
    Used: https://stackoverflow.com/questions/4406501/change-the-name-of-a-key-in-dictionary
    https://regexr.com/
    Need to capitalise the string
    Mistake done:
    for key in images:
        images[key.upper()] = images.pop(key)
    return images

    regex: 

    """
    result = {}
    for key in images:
        new_key = re.search(r"[^.]+", key)
        result[new_key.group().upper()] = images[key]
    return result


def get_whole_email(filepath1, filepath2):
    global MY_ADDRESS
    images = get_base64_files('assets/text_versions')
    # Problem the image file names are the full file but we want only the filename and capitalised
    images = format_image_dict(images)

    with open(filepath1, "r") as f1:
        contents = f1.read().format(**{"BUSINESS_NAME": "Chloe"})
        with open(filepath2, "r") as f2:
            format_vals = {
                "NAME": "Arthur Allilaire & Bryan Lo",
                "MY_ADDRESS": MY_ADDRESS,
                "TITLE": "Charity Co-Chairs",
                "DEPARTMENT": "Charity Executive Committee",
                "MAIL_THUMBNAIL": "assets/mail_thumbnail.png",
            }
            # Append the images dictionary
            format_vals.update(images)
            footer = f2.read().format(**format_vals)

    EMAIL = contents + footer
    return EMAIL


def send_email():
    # Connection with the server
    server = smtplib.SMTP(host=HOST_ADDRESS, port=HOST_PORT)
    server.starttls()
    server.login(MY_ADDRESS, MY_PASSWORD)

    # Creation of the MIMEMultipart Object
    message = MIMEMultipart('related')

    # Setup of MIMEMultipart Object Header
    message['Subject'] = "Raffle Prize fundraising for Papyrus"
    message['From'] = MY_ADDRESS
    message['To'] = RECIPIENT_ADDRESS
    # message['Cc'] = MY_ADDRESS

    # Creation of a MIMEText Part
    htmlPart = MIMEText(
        # The html needs to have a header and src="cid:image1"
        get_whole_email("EMAIL_NOT_BEEN.html", "TABLE.html"), 'html')

    # Part attachment
    message.attach(htmlPart)

    # Send Email and close connection
    server.send_message(message)
    server.quit()


for i in range(1):
    send_email()
    print(f"Sending email number {i}")
