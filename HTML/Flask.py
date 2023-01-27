from flask import Flask, render_template, request, flash

app = Flask(__name__)

def Registration():
    flash(
        request.form[""]
    )
    return render_template("registreren.html")

