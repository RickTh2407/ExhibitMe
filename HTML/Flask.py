from flask import Flask, render_template, request, flash

app = Flask(__name__)

@app.route("/gSubmit")
def GuestDetails():
    fNameReg = request.form["firstname"]
    lNameReg = request.form["lastname"]
    ageReg = request.form["age"]
    strReg = request.form["addressStr"]
    houseNrReg = request.form["addressHouseNr"]
    zipReg = request.form["addressZip"]
    phoneReg = request.form["phone"]
    emailReg = request.form["email"]
    passwordReg = request.form["password"]
    genUseReg = request.form["gender"]
    resUseReg = request.form["useResidence"]
    ageUseReg = request.form["useAge"]
    phoneUseReg = request.form["usePhone"]
    emailUseReg = request.form["useEmail"]

@app.Route("/sSubmit")
def StandDetails():
    standNameReg = request.form["companyName"]
    standBioReg = request.form["standBio"]
    kvkReg = request.form["KVK"]
