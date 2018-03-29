#intialization section; todo: pull all changable info from a text config file

import shutil, os, datetime
watchdir = os.path.join('C:\\','Move testing','Test Source Folder') # folder where you drop the shit you want organized
dirlist = ["DBCA", "Category 1"], ["ABCD", "Category 2"] # a library of project codes and destination folder names
filelist = os.listdir(watchdir) #captures a list of the files in the watch dirrectory in order to itterate over them
todaysdate = str(datetime.date.today())
defaultfolder = "Test Destination Folder"
# to make adding cetegories easier have a check durrin intialization to make sure each item in dirlist have a corresponding folder created already or create it. that way all you need to do to add new types is edit the config file


for startfilename in filelist: #itterates over the list of files in the watch dirrectory, sorts them by project code, renames with a date appended, and moves them to the appropriate folder
    
    fileext = os.path.splitext(startfilename)
    endfilename = fileext[0] + "_" + todaysdate + fileext[1]
    justname = fileext[0] 

    if dirlist[0][0] in justname : #this is not an exact match situation... is that going to be a problem?
        destfolder = dirlist[0][1]
    elif dirlist[1][0] in justname :
        destfolder = dirlist[1][1]
    else:
        destfolder = defaultfolder

    dstpath = str(os.path.join('C:\\', 'Move testing',destfolder))
    src = os.path.join(watchdir ,startfilename)
    dstlist = os.listdir(dstpath)
    

    # makes sure to append a number to end to prevent overwriting if final name will be the same as a file in the destination folder; I think the the If is redundant but it works this way
    if any(endfilename in s for s in dstlist):
        dupnameinc = 0
        while endfilename in dstlist:
            dupnameinc = dupnameinc + 1
            endfilename = fileext[0] + "_" + todaysdate + "_" + str(dupnameinc) + fileext[1]

    # finalizes the destination of the move            
    dst = os.path.join('C:\\', 'Move testing',destfolder,endfilename)

    #performs the move and rename
    shutil.move(src,dst)
