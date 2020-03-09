# match_face
 match_face

Usage:

python <script file name> Steps to use: For this example I'll use it to sort for faces from the output of the "data_src extract faces" steps. 
 
It's pretty much the same flow for use against the data_dst images. Just change the commands accordingly.

Copy the code, and save it to a file.

I recommend you save it to your workspace folder. 

Doesn't matter what you name it, but we'll call it "match_face.py" for this example.

After you complete your "extract faces" you can run this on the "aligned" folder to do the sorting.

Find a clear image in the data_src\aligned folder to use as the source image for the match. I'll use 01680.jpg in this example

Open a command window and cd to the workspace folder where the script is Example Usage for source faces: 

python match_face.py data_src\aligned\01680.jpg

The script will move all matching faces to a folder name "match" in the target aligned folder.

It's not 100% accurate, but does a pretty good job.

Look through the remaining images in the data_src folder and delete any faces you don't want included.

Move the files that were relocated to the data_src/aligned/matched folder back to data_src/aligned

Move on to the next steps in the workflow

＃match_face  match_face
