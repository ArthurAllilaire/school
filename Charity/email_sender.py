import csv
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
import smtplib
import os
import re

MY_ADDRESS = "a.allilaire@cityoflondonschool.org.uk"         # Replace with yours
MY_PASSWORD = "jingleBells12"      # Replace with yours
RECIPIENT_ADDRESS = "a.allilaire@cityoflondonschool.org.uk"  # Replace with yours


HOST_ADDRESS = 'smtp-mail.outlook.com'   # Replace with yours
HOST_PORT = 587                          # Replace with yours

FORMAT_VALS = {
    "NAME": "Arthur Allilaire & Bryan Lo",
    "MY_ADDRESS": MY_ADDRESS,
    "TITLE": "Charity Co-Chairs",
    "DEPARTMENT": "Charity Executive Committee",
}


def get_whole_email(filepath1, filepath2):
    """
    Returns the full text html, with filepath1 as the content and filepath2 as the footer.
    """
    with open(filepath1, "r") as f1:
        contents = f1.read()
        with open(filepath2, "r") as f2:
            footer = f2.read()

    return f"""
    <html>
    <head></head>
    <body style="background-color: inherit;">
    {contents}
    {footer}
    </body>
    </html>"""


def attach_images(message, directory, format_vals):
    """
    Params:

    returns: the updated format_vals, directly changes the message object by attaching all the photos.
    Based on the first one of this list: https://www.geeksforgeeks.org/how-to-iterate-over-files-in-directory-using-python/ all are good this is just the most common.
    for cid stuff: https://stackoverflow.com/questions/52186048/send-html-email-with-embedded-image-using-python-script
    """
    imgs = {}
    for filename in os.listdir(directory):
        full_name = os.path.join(directory, filename)
        if os.path.isfile(full_name):
            with open(full_name, 'rb') as f:
                msgImage = MIMEImage(f.read(), _subtype="png")

            # Define the image's CID tag
            img_name = format_image_name(filename)
            # msgImage.add_header('Content-Disposition',
            #                     'attachment', filename=f'{img_name}.png')
            msgImage.add_header('Content-ID', f'<{img_name}>')
            msgImage.add_header('Content-Disposition',
                                'inline', filename=img_name)
            imgs[img_name] = msgImage
            # Now add the image cid:tag to the source by appending it to the format_vals dict
            format_vals[img_name] = f"cid:{img_name}"
            # with open(full_name, 'rb') as f:
            #     msgImage = MIMEImage(f.read(), _subtype="png")
            #     # add required header data:
            #     msgImage.add_header('Content-Disposition',
            #                         'attachment', filename=filename)
            #     # msgImage.add_header('X-Attachment-Id', '0')
            #     msgImage.add_header('Content-ID', f'<filename>')
            #     # read attachment file content into the MIMEBase object
            #     msgImage.set_payload(f.read())
            #     # encode with base64

            #     # add MIMEBase object to MIMEMultipart object
            #     message.attach(msgImage)

    return (format_vals, imgs)


def format_image_name(filename):
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
    new_key = re.search(r"[^.]+", filename)
    return new_key.group().upper()


def format_email(message, html_msg, format_vals, directory):
    """
    Takes a message object and a html_msg and a directory with all the 
    params:
    message - the email object - will attach images to it


    returns the message object
    """
    format_vals, imgs = attach_images(message, directory, format_vals)
    # Creation of a MIMEText Part
    htmlPart = MIMEText(html_msg.format(**format_vals), 'html')

    # Part attachment
    message.attach(htmlPart)

    for key, img in imgs.items():
        message.attach(img)

    return message


def send_email(business_name, recipient_address, type="D"):
    """ type = D OR F OR T """
    global FORMAT_VALS
    format_vals = FORMAT_VALS.copy()
    format_vals["BUSINESS_NAME"] = business_name
    # Connection with the server
    server = smtplib.SMTP(host=HOST_ADDRESS, port=HOST_PORT)
    server.starttls()
    server.login(MY_ADDRESS, MY_PASSWORD)

    # Creation of the MIMEMultipart Object
    message = MIMEMultipart('related')

    # Setup of MIMEMultipart Object Header
    message['From'] = f"Arthur Allilaire <{MY_ADDRESS}>"
    message['To'] = recipient_address
    message['Cc'] = "b.lo@cityoflondonschool.org.uk"
    # So I need to get the whole email in html tags and body tags, with keywords still in brackets
    if type == "F":
        message['Subject'] = "Raffle Prize fundraising for Papyrus"
        html_msg = get_whole_email("Form.html", "TABLE.html")
    elif type == "T":
        message['Subject'] = "Thank you for you donation!"
        html_msg = get_whole_email("Thank_you.html", "TABLE.html")
    else:
        message['Subject'] = "Raffle Prize fundraising for Papyrus"
        html_msg = get_whole_email("EMAIL_NOT_BEEN.html", "TABLE.html")

    message = format_email(message, html_msg, format_vals, 'assets')

    # Send Email and close connection
    server.send_message(message)
    server.quit()


sent_recipients = {
    "Cabbote": "amira@cabotte.co.uk",
    "Natural Kitchen": "joanna@naturalkitchen.co.uk",
    "Gousto": "info@gousto.co.uk",
    "Digme fitness": "bank@digmefitness.com",
    # Also sent through their customer enquiry website form
    "Pret": "press@pret.com",
    # Not the actual address just emailed to put into contact form - contact form didn't work
    "Costa": "press@costa.co.uk",
    "Duck and Waffle": "dwlondon@duckandwaffle.com",
    # Sent it to all the locations within the city using their site, didn't find any email - about 7
    "Ivy": "a.allilaire@cityoflondonschool.org.uk",
    # Through website as well
    "Fitness First": "a.allilaire@cityoflondonschool.org.uk",
    # Their straits kitchen is next to liverpool street
    "Pan Pacific": "enquiry.pplon@panpacific.com",
    # Applied through the website too
    "Dirty martini": "bookings@dirtymartini.uk.com",
    "Broadleaf": "info@broadleaflondon.com",
    # Mediteranian restaurant several locations in city - not sure if it went through
    "Haz": "a.allilaire@cityoflondonschool.org.uk",
    # Sent through their form
    "Joe and the Juice": "a.allilaire@cityoflondonschool.org.uk",
    # chique restaurant
    "14 Hills": "hello@14hills.co.uk",
    "Harry's": "info@harrys.co.uk",
    "Vintry": "TheVintry@fullers.co.uk",
    "Vintry": "thevintry.events@fullers.co.uk",
    "Starbucks": ["proUK@starbucks.com"],
    "M&S": "ghislaine.allilaire@gmail.com",
    "Coq d'Argent": "coqdargent@danddlondon.com",
    "The Ned": "enquiries@thened.com",
    "Rudds": "info@ruddsblackfriars.co.uk",
    "Paternoster Chop House": "paternosterr@danddlondon.com",
    "1Rebel": ["STMARYAXE@1REBEL.COM", "BROADGATE@1REBEL.COM", "ANGEL@1REBEL.COM", "HOLBORN@1REBEL.COM", "SOUTHBANK@1REBEL.COM"],
    "Blok": "laura@bloklondon.com",
    "Core Collective": "info@core-collective.co.uk",
    "Equinox": "Concierge@Equinox.com",
    "Aire": "a.allilaire@cityoflondonschool.org.uk",
    "Sea Containers": "a.allilaire@cityoflondonschool.org.uk",
    # All part of the berkeley
    "Berkeley": ["dining@the-berkeley.co.uk", "dining@the-berkeley.co.uk", "haybarn@the-berkeley.co.uk", "reservations@marcusrestaurant.com"],
    "Knut Wylde": "kwylde@the-berkeley.co.uk",
    "Paula Fitzherbert": "pfitzherbert@maybourne.com",
    "Varinder Singh": "vsingh@maybourne.com",
    "La Mer": "info@lamer.com",
    "Four Seasons": "info@fourseasons.com",
    "Lanserhof": "info.lans@lanserhof.com",
    "A Place To Heal": "info@aplacetoheal.co.uk",
    "Waitrose": "customerserviceteam@waitrose.co.uk",
    "Byron Burgers": "hello@byronburgers.co.uk",
    "Itsu": "aaron.moore-saxton@itsu.com",
    "Hollister": "a.allilaire@cityoflondonschool.org.uk",
    "Uzumaki London": "hello@uzumakilondon.com",
    "Charles Tyrwhitt": "info@ctshirts.co.uk",
    "JD Sports": "onlinehelp@jdsports.co.uk",
    "Dion": "stpauls@dionlondon.co.uk",
    "Wasabi": ["peter@berryandgreen.com", "chloe@berryandgreen.com"],
    "Abercrombie & Fitch": "giveback@anfcorp.com",
    "Selfridges & Co.": "press.office@selfridges.co.uk",
    "L'Oreal": "corporateaffairsuk@loreal.com",
    "Procter & Gamble": "pgpress.im@pg.com",
    "LVMH": "a.allilaire@cityoflondonschool.org.uk"
}
recipients = {

}
Donators = {
    "Sonia": "sonia.hicks@panpacific.com",

}

# recipients = {
#     "Arthur": ["a.allilaire@cityoflondonschool.org.uk", "arthur.allilaire@gmail.com"]
# }


def send_to_recipients(recipients):
    """ Recipients is a dict {business -> email} """
    for name, emails in recipients.items():
        if isinstance(emails, list):
            for email in emails:
                print(name, email)
                send_email(name, email)
                print(f"Sent email to {name}")
        else:
            if emails == "a.allilaire@cityoflondonschool.org.uk":
                # Prepare it to be sent through the form
                print(name, emails)
                send_email(name, emails, "F")
                print(f"Sent email to {name}")
            else:
                print(name, emails)
                send_email(name, emails)
                print(f"Sent email to {name}")


def send_to_donators(Donators):
    """ Recipients is a dict {business -> email} """
    for name, emails in Donators.items():
        if isinstance(emails, list):
            for email in emails:
                print(name, email)
                send_email(name, email, "T")
                print(f"Sent email to {name}")
        else:
            if emails == "a.allilaire@cityoflondonschool.org.uk":
                # Prepare it to be sent through the form
                print(name, emails)
                send_email(name, emails, "T")
                print(f"Sent email to {name}")
            else:
                print(name, emails)
                send_email(name, emails, "T")
                print(f"Sent email to {name}")


if __name__ == "__main__":
    for i in range(1):
        # send_to_recipients(recipients)
        send_to_donators(Donators)
