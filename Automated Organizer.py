#INTIALIZATION
import shutil, os, datetime, configparser
todaysdate = str(datetime.date.today())


#IMPORT FROM CONFIG.INI
parser = configparser.ConfigParser()
parser.read('config.ini')
watchdir = str(parser.get('dir','watchdir'))
defaultfolder = str(parser.get('dir','defaultfolder'))
parentdir = str(parser.get('dir','parentdir'))
dirlist = {}
for code, folder in parser['projectcodes'].items():
    dirlist[code] = folder

#MAIN SORT LOOP
filelist = os.listdir(watchdir) 
for startfilename in filelist:    
    fileext = os.path.splitext(startfilename) 
    endfilename = fileext[0] + "_" + todaysdate + fileext[1] 
    justname = fileext[0]
    justnamelower = justname.lower() 

    #CODE PARSING AND SORTING LOOP
    destfolder = defaultfolder
    for projcode in dirlist.keys():
        if projcode in justnamelower:
            destfolder = dirlist.get(projcode)        

    #CREATE FOLDER IF NEEDED
    dstpath = parentdir + destfolder
    if os.path.isdir(dstpath) != True:
        os.makedirs(dstpath)
        
    dstlist = os.listdir(dstpath)
    

    #OVERWRITE PREVENTION LOOP
    if any(endfilename in s for s in dstlist):
        dupnameinc = 0
        while endfilename in dstlist:
            dupnameinc = dupnameinc + 1
            endfilename = fileext[0] + "_" + todaysdate + "_" + str(dupnameinc) + fileext[1]

    #MOVE       
    src = os.path.join(watchdir ,startfilename)
    dst = os.path.join(parentdir,destfolder,endfilename)
    shutil.move(src,dst)
