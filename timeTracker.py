import pandas as pd
import subprocess, csv, datetime, time, os


# creates new empty CSV file
def createCSV(file):
    open(file, "w")

# logs the start time to the CSV file
def startTimer(file):
    startDateTime = datetime.datetime.now()
    startTime = [startDateTime.strftime("%H:%M:%S")]
    with open(file, "a", newline='') as timeCSV:
        csvWriter = csv.writer(timeCSV)
        csvWriter.writerow(startTime)

# logs the end time to the CSV file
def endTimer(file):
    time.sleep(4)
    endDateTime = datetime.datetime.now()
    endTime = endDateTime.strftime("%H:%M:%S")
    endDate = endDateTime.strftime("%Y/%m/%d")
    lines = list()

    # reads the lines in a file and saves to a list
    with open(file, "r") as readCSV:
        myReader = csv.reader(readCSV)
        for row in myReader:
            currentRow = row

            # if the row is not empty save to list
            if row != []:
                lines.append(row)

        # removes the last row from the list
        lines.remove(currentRow)

    # writes the list containing all the rows to the same file
    with open(file, "w", newline='') as timeCSV:
        csvWriter = csv.writer(timeCSV)

        # creates a list of the start time and the end time and date
        currentRow.append(endTime)
        currentRow.append(endDate)
        lines.append(currentRow)

        # wirtes list to the file
        for row in lines:
            csvWriter.writerow(row)

# exports the csv file to excel document
def exportFile(file):
    read_file = pd.read_csv (file)
    read_file.to_excel (r'Book55.xlsx', index = None, header = True)

    # optional will open the file in excel after creation
    # subprocess.Popen('Book1.xlsx', shell=True)


fileLocation = r"C:\Users\charl\Documents\Python_Test\myNewCsv.csv"
startTimer(fileLocation)
endTimer(fileLocation)
exportFile(fileLocation)

