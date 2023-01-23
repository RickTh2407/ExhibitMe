import json
import qrcode
import os

# create the directory if it doesn't exist
if not os.path.exists("qr_codes"):
    os.mkdir("qr_codes")

# load the JSON file
with open("guestDatabase.json", "r") as f:
    gData = json.load(f)

# iterate through the guests
for guest in gData["Guests"]:
    for guestNr in guest:
    # extract the information per guest
        fName = guestNr["FirstName/CompanyName"]
        lName = guestNr["LastName"]
        age = guestNr["Age"]
        email = guestNr["Email"]
        adressStr = guestNr["AdressStreet"]
        adressNr = guestNr["AdressHouseNr"]
        phone = guestNr["PhoneNr"]
        if (guestNr["ShowResidence"] == "False") or (adressStr == ""):
            adressStr = "Classified/Unknown"
            adressNr = ""
        if (guestNr["ShowPhone"] == "False") or (phone == ""):
            phone = "Classified/Unknown"
        if (guestNr["ShowEmail"] == "False") or (email == ""):
            email = "Classified/Unknown"
        if (guestNr["UseAge"] == "False") or (age == ""):
            age = "Classified/Unknown"

    # create the QR code
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(f"Name: {fName} + {lName}\nAge: {age}\nEmail: {email}\nAdress: {adressStr} + {adressNr}\nPhone: {phone}")
    qr.make(fit=True)

    # create an image from the QR code
    img = qr.make_image(fill_color="black", back_color="white")

    # join the directory and file name and save the image
    img.save(os.path.join("qr_codes", f"{fName[0]} + {lName}.png", sep="_"))