import csv
import speech_recognition as sr

# Initialize the recognizer
r = sr.Recognizer()

# Use the microphone as a source of input
with sr.Microphone() as source:
    print("What is the name of the file?")
    audio = r.listen(source)

try:
    # Convert speech to text
    file_name = r.recognize_google(audio)
    print("You said:", file_name)

    # Ask for the column name
    with sr.Microphone() as source:
        print("What is the name of the column?")
        audio = r.listen(source)

    # Convert speech to text
    column_name = r.recognize_google(audio)
    print("You said:", column_name)

    # Open the CSV file
    csv_file =open(file_name + ".csv")  
    reader = csv.DictReader(csv_file)

        # Print the contents of the specified column\
    i=0
    for row in reader:
        if(i<=10):
            print(row[column_name])
        i+=1

except sr.UnknownValueError:
    print("Could not understand audio")

except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))
    
except KeyError:
    print(f"Could not find column {column_name} in file {file_name}.")
