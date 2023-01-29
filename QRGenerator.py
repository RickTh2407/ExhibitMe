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
def JGD(): #stands for Json Guest Details
    for guestNr in gData["Guests"].values():
    # extract the information per guest
        gNumber = guestNr.get("CustomerNr")
        fName = guestNr.get("FirstName/CompanyName")
        lName = guestNr.get("LastName")
        age = guestNr.get("Age")
        gender = guestNr.get("Gender")
        addressStr = guestNr.get("AddressStreet")
        addressNr = guestNr.get("AddressHouseNr")
        addressZip = guestNr.get("AddressZip")
        phone = guestNr.get("PhoneNr")
        email = guestNr.get("Email")
        if (guestNr.get("ShowResidence") == "False") or (addressStr == ""):
            adressStr = "Classified/Unknown"
            adressNr = ""
        if (guestNr.get("ShowPhone") == "False") or (phone == ""):
            phone = "Classified/Unknown"
        if (guestNr.get("ShowEmail") == "False") or (email == ""):
            email = "Classified/Unknown"
        if (guestNr.get("UseAge") == "False") or (age == ""):
            age = "Classified/Unknown"
        
        # create the QR code
        qr = qrcode.QRCode(version=1, box_size=10, border=5)
        qr.add_data(f"GuestNR:"+ {gNumber}+ "\nName:"+ {fName}+ " "+ {lName}+"\nAge:"+ {age}+ "\nGender:"+ {gender}+ "\nAddress:"+ {addressStr}+ " "+ {addressNr}+ "\nZip:"+ {addressZip}+ "\nPhone:"+ {phone}+ "\nEmail:"+ {email})
        qr.make(fit=True)

        # create an image from the QR code
        img = qr.make_image(fill_color="black", back_color="white")

        # join the directory and file name and save the image
        img.save(os.path.join("qr_codes", f"{fName[0]}{lName}.png"))
JGD()