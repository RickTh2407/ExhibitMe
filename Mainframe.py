import json

jsonStand = "standsDatabase.json"
jsonGuest = "guestDatabase.json"
entryG = ""
entryS = ""

# Read file contents
def ReadFile():
    with open(jsonGuest, "r") as gRFile:
        dataG = json.load(gRFile)
    with open(jsonStand, "r") as sRFile:
        dataS = json.load(sRFile)
    return dataG, dataS

# Make every object able to modify.
def ModifyFree():
    guestData = ReadFile.dataG
    standData = ReadFile.dataS

    for comDataG in guestData["Guests"]:
        for guestNr in comDataG:
        # extract the information per guest
            caseNumber = guestNr["guestNr"]
            fName = guestNr["FirstName/CompanyName"]
            lName = guestNr["LastName"]
            age = guestNr["Age"]
            gender = guestNr["Gender"]
            email = guestNr["Email"]
            adressStr = guestNr["AdressStreet"]
            adressNr = guestNr["AdressHouseNr"]
            adressZip = guestNr["AdressZip"]
            phone = guestNr["PhoneNr"]
            password = guestNr["Password"]

    for comDataS in standData["Stands"]:
        for standNr in comDataS:
            stName = standNr["StandName"]
            stBio = standNr["StandBio"]
            stPop = standNr["StandPop"]
            for population in stPop:
                popCount += 1
                popList += [population]
                # Insert new standguest who has checked in.

# Update json object
def UpdateFileGuest(updateG, updateS):
    updateG = ReadFile.dataG.append(entryG)
    updateS = ReadFile.dataS.append(entryS)    

# Write json file
def WriteFile():
    with open(jsonGuest, "w") as gWFile:
        json.dump(ReadFile.dataG, ReadFile.gWFile)
    with open(jsonStand, "w") as sWFile:
        json.dump(ReadFile.dataS, ReadFile.sWFile)