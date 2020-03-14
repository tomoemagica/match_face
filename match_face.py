import face_recognition
from shutil import move
import os
from os import path
import sys
from pathlib import Path, PureWindowsPath

# Usage: py match_face.py data_src\aligned\00000_0.jpg etc.

# Set up commmand line args
file_to_recognize = sys.argv[1]
target_dir = os.getcwd()
target_dir = os.path.join(target_dir, 'data_src')
target_dir = os.path.join(target_dir, 'aligned')


#Validate source file
if not path.isfile(file_to_recognize):
    print("ERROR: File " + str(file_to_recognize) + " isn't valid")
    exit()

#Validate target directory
if not path.isdir(target_dir):
    print("ERROR: Path " + str(target_dir) + " isn't a valid directory")
    exit()

#Count how many files in the directory
file_count = len(os.listdir(target_dir))

#Show some stats
#print("Using " + str(file_to_recognize) + " as source")
print("Checking " + str(file_count) + " files")

#Setup the output directory for matching faces
match_path = os.path.join(target_dir, 'match')

#Make sure the path exists and if not, create it.
if not path.isdir(match_path):
    try:
        os.mkdir(match_path)
    except OSError:
        print("Creation of the directory %s failed" % match_path)
    else:
        print("Successfully created the directory %s " % match_path)


# Create an encoding of my facial features that can be compared to other faces
if os.path.isfile(file_to_recognize):
    picture_of_me = face_recognition.load_image_file(file_to_recognize)
    my_face_encoding = face_recognition.face_encodings(picture_of_me)[0]

# Iterate through all the 10,460 pictures
for thisFile in os.listdir(target_dir):
   
    file_name = os.path.join(target_dir, thisFile)
    if os.path.isfile(file_name):
        file_name = os.path.join(target_dir, thisFile)

        # Load this picture
        new_picture = face_recognition.load_image_file(file_name)

        # Iterate through every face detected in the new picture
        for face_encoding in face_recognition.face_encodings(new_picture):

        # Run the algorithm of face comaprison for the detected face, with 0.5 tolerance
            results = face_recognition.compare_faces(
                [my_face_encoding], face_encoding, 0.5)

            # Save the image to a seperate folder if there is a match
            if results[0] == True:
                match_file = os.path.join(match_path, thisFile)
                if os.path.isfile(file_name):
                    move(
                        file_name, match_file)
