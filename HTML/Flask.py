from flask import Flask, render_template, request, flash, redirect
import json
import QRGenerator
import QRScanner

jsonStand = "standsDatabase.json"
jsonGuest = "guestDatabase.json"

# Read file contents
def ReadFile():
    with open(jsonGuest, "r") as gRFile:
        dataG = json.load(gRFile)
    with open(jsonStand, "r") as sRFile:
        dataS = json.load(sRFile)
    return dataG, dataS

# Make every object able to modify.
def ModifyFree():
    for comDataG in ReadFile.dataG["Guests"]:
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

        # extract the information per stand
    for comDataS in ReadFile.dataS["Stands"]:
        for standNr in comDataS:
            stName = standNr["StandName"]
            stBio = standNr["StandBio"]
            BankDet = standNr["StandBank"]
            KVK = standNr["KVK"]
            WebComp = standNr["CompanyWeb"]
            stPop = standNr["StandPop"]
            for population in stPop:
                popCount += 1
                popList += [population]

#HTML operation
app = Flask(__name__)
app.secret_key = "TheUltimatelySecretKey"

#Gathering data from registration form Guests and redirecting registered guest to login page
@app.route("/gReg", methods=['POST', 'GET'])
def GDR(): #stands for GuestDetailsRegistery
    fNameReg = str(request.form["firstname"])
    lNameReg = str(request.form["lastname"])
    ageReg = str(request.form["age"])
    genUseReg = str(request.form["gender"])
    strReg = str(request.form["addressStr"])
    houseNrReg = str(request.form["addressHouseNr"])
    zipReg = str(request.form["addressZip"])
    phoneReg = str(request.form["phone"])
    emailReg = str(request.form["email"])
    passwordReg = str(request.form["password"])
    resUseReg = str(request.form["useResidence"])
    ageUseReg = str(request.form["useAge"])
    phoneUseReg = str(request.form["usePhone"])
    emailUseReg = str(request.form["useEmail"])
    if (emailUseReg == "False") and (phoneUseReg == "False"):
        flash("Graag hebben wij één van uw contactgegevens voor u te bereiken.")
    else:
        return redirect("Inloggen.html")
    return render_template("Registreren.html")
        
#Gathering data from registration form Stands and redirecting registered standhost to guest page
@app.route("/sReg")
def StandDetails(): #stands for StandDetailsRegistery
    standNameReg = str(request.form["companyName"])
    standBioReg = str(request.form["standBio"])
    standBankReg = str(request.form["standBank"])
    kvkReg = str(request.form["KVK"])
    compWeb = str(request.form["companyWeb"])
    if (standNameReg == "") or (standBioReg == "") or (standBankReg == "") or (kvkReg == "") or (compWeb == ""):
        flash("Alstublieft vul alles in van bovenstaande registratie formulier om registratie te voltooien")
    else:
        redirect("Guest.html")
    return render_template("RegisterenStand.html"), 

#Login function, redirects towards guestpage
@app.route("/Login")
def Login():
    loginEmail= request.form['email']
    loginPassword = request.form['wachtwoord']

    if request.method == 'post':
        if loginEmail != ModifyFree.email and loginPassword != ModifyFree.password:
            flash('Incorrecte login gegevens, probeer het opnieuw')
        elif loginEmail == 'Admin' and loginPassword == 'Admin':
            return redirect('HiddenAdmin.html')
        else:
            return redirect('Guest.html')
    return render_template('Inloggen.html')

@app.route("/QR")
def QRPrint():
    searchEmail = Login.loginEmail
    data = ReadFile.dataG
    for guest in data["Guests"]:
        if data["Guests"][guest]["Email"] == searchEmail:
            firstName = data["Guests"][guest]["FirstName/CompanyName"]
            lastName = data["Guests"][guest]["LastName"]
            pngSearch = firstName[0] + lastName + ".png"
    return render_template("Guest.html", QR_Image=pngSearch)

@app.route("/")
def 

if __name__ == "__main__":
    app.debug = True
    app.run(host = "0.0.0.0", port = 5000)