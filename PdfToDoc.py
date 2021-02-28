import os
import subprocess

filepath = input("Write your file path: ")

for top, dirs, files in os.walk(filepath):
    for filename in files:
        if filename.endswith('.pdf'):
            abspath = os.path.join(top, filename)
            subprocess.call('lowriter --invisible --convert-to doc "{}"'
                            .format(abspath), shell=True)