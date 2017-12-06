import time
import pickle
started = True
credentials = open("user.py","rb")
if credentials == "Uninstalled":
    print("Welcome to the LabelleOS setup page. First you will need to choose a username and password")
    setupusername = input("Username:")
    setuppassword = input("Password:")
    pickle.dump(setupusername,setuppassword,credentials)
if credentials != "Uninstalled":
    console = "Focus"
    while console == "Focus":
        currentcommand = input("{}@{}".format(setupusername,setuppassword))
    
