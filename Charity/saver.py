import csv
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
    "A Place To Heal": "info@aplacetoheal.co.uk"
}

with open("businesses.csv", "w") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Business", "Email"])
    for business, email in sent_recipients.items():
        writer.writerow([business, email])
