#This will check to see if Serval has pushed any GPS data (.txt, CSV, .json, .xml, ect.) to a specified folder on the server

import os
import time
import gmplot
import codecs

#Insert Linux folder to check in var x
# Test for MacBook Pro Directory
#x = '/Users/justindraughon/Google Drive/Lipscomb/Senior Fall Semester/CCT Senior Seminar/Python Programming/gpsTest/'
x = "/home/pi/Desktop/"

#Names of processed files (list car)
nameList = []
dataChanged = 0

latData = []
longData = []


while True:
    for files in os.listdir(x):
        print("Running Text Parser...")
        if files.endswith(".txt"):
            #Open File, parse it, close it, save file name somewhere that we did it, delete it, push data on to web app
            nameList.append(files)

            #Open and parse the file
            fileData = open(x + files, encoding = "utf-8")
            data1 = fileData.read()

            filteredData = data1.split(" ")
            fileData.close()


            #Delete the file
            os.remove(x + files)

            dataChanged = 1

            #This is the area where we will push the seperated data to the Web App...
            if dataChanged == 1:
                print("Running Mapping Solution...")

                int_list = []
                for q in filteredData:
                    print(q)
                    w = float(q)
                    int_list.append(w)

                latData.append(int_list[0])
                longData.append(int_list[1])

                # Drop the new gps coordinates here.
                pathlat = tuple(latData)
                pathlon = tuple(longData)

                gmap = gmplot.GoogleMapPlotter(36.105632000, -86.799990000, 16.9)
                #Declares mapping markers
                gmap.coloricon = "http://www.googlemapsmarkers.com/v1/%s/"

                #Takes in a tuple
                gmap.scatter(pathlat, pathlon, 'k', marker=True)

                gmap.draw('/var/www/html/index.html')



    #Slows the While True loop down
    time.sleep(.3)
    dataChanged = 0



