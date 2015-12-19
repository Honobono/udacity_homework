#  Mini-project to show a secret message
#  This one is for my husband. It spelt out "You are the one"

import os

def secret_message():
    folder = os.listdir("/Users/ruiyingliu/Downloads/alphabet/secret_message")
    current_dir = os.getcwd()
    print("Current Working Directory is " + current_dir)
    os.chdir("/Users/ruiyingliu/Downloads/alphabet/secret_message")
    for file_name in folder:
        # for debugging purposes, print file names before and after the changes.
        print "Old file name is " + file_name
        print "New file name is now " + file_name.translate(None, "0123456789")
        os.rename(file_name, file_name.translate(None, "0123456789"))
    os.chdir(current_dir)
secret_message()
