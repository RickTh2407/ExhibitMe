import os
import cv2
import json
from pyzbar import pyzbar
from tkinter import *
from PIL import Image, ImageTk

# specify the absolute path to save the scanned_codes.json file
path = os.path.join("C:\\Users\\rickt\\Desktop\\School file\\Rix&Co. Casusopdrachten\\ExhibitMe\\HTML\\registeredGuests.json")

# Create the GUI window
root = Tk()
root.title("QR Code Scanner")

# Create a label to display the webcam feed
lbl = Label(root)
lbl.pack()

# Open the webcam
cap = cv2.VideoCapture(0)

# create an empty list to store scanned codes
scanned_codes = []
# create an empty set to store already scanned codes
scanned_set = set()
def Camera():
    # Create a function to update the webcam feed
    def UpdateFrame():
        # Read a frame from the webcam
        ret, frame = cap.read()

        # Find QR codes in the frame
        codes = pyzbar.decode(frame)

        # Iterate over the codes
        for code in codes:
            # Extract the information from the code
            data = code.data.decode()
            if data not in scanned_set:
                scanned_set.add(data)
                scanned_codes.append(data)
                print(data)
                # Draw a bounding box around the code
                (x, y, w, h) = code.rect
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
                #save the guest automaticly
                save_codes()

        # Display the frame
        cv2_im = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(cv2_im)
        imgtk = ImageTk.PhotoImage(image=img)
        lbl.imgtk = imgtk
        lbl.configure(image=imgtk)
        lbl.after(10, UpdateFrame)

    # Show the webcam feed
    UpdateFrame()

    # Create a button to save the scanned codes to a JSON file
    def save_codes():
        formatted_codes = []
        for code in scanned_codes:
            code_parts = code.split("\n")
            code_dict = {}
            for part in code_parts:
                key, value = part.split(": ")
                code_dict[key] = value
            formatted_codes.append(code_dict)
        with open(path, "w") as f:
            json.dump(formatted_codes, f)

    # Run the GUI
    root.mainloop()

    # Release the webcam
    cap.release()