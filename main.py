import json

jsonStand = "standsDatabase.json"
jsonGuest = "guestDatabase.json"
entryG = ""
entryS = ""

# Read file contents
def ReadFile():
    with open(jsonGuest, "r") as gFile:
        dataG = json.load(gFile)
    with open(jsonStand, "r") as sFile:
        dataS = json.load(sFile)
    return dataG, dataS

# Make every object able to modify.
def ModifyFree():
    guestData = ReadFile.dataG
    standData = ReadFile.dataS

    for comDataG in guestData:
    #insert thing that makes everything in to a variable

    for comDataS in standData:
    #also insert thing that makes everything in to a variable

# Update json object
def UpdateFile():
    ReadFile.dataG.append(entryG)
    ReadFile.dataS.append(entryS)

# Write json file
def WriteFile():
    with open(jsonGuest, "w") as gFile:
        json.dump(ReadFile.dataG, ReadFile.gFile)
    with open(jsonStand, "w") as sFile:
        json.dump(ReadFile.dataS, ReadFile.sFile)

# Operating HTML file for GUI function
def GuiMainframe():
    import flask
    open("Gui.html")
    