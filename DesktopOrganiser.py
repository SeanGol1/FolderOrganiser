import os

# Configs
_directory = 'C:\\Users\\seang\\OneDrive\\Desktop\\Test'
_renameFile = False

def readFiles():
    fileNames = []
    inp = '_'

    # Get all files in Directory with {inp} in name
    thisdir = os.getcwd()
    for r, d, f in os.walk(_directory):
        for file in f:
            filepath = os.path.join(r, file)
            if inp in file:                
                fileNames.append(os.path.join(r, file))               
    print(f" {len(fileNames)} files found.")

    # Send each item to create a new folder
    for f in fileNames:
        newFolder(f)
        

def newFolder(fileName):   

    # Remove the file name
    fn = fileName.split('_')     
    fn = fn[:-1]
    fn = '\\'.join(fn)

    # Check if path exists and create
    #print('Changing ' + fn + ' to ' + pathname + '...')
    if not os.path.exists(fn):
        os.makedirs(fn)
        
    moveFiles(fileName,fn)

def moveFiles(file,folder):

    if(_renameFile):
        # Get file name
        fn = file.split('_')     
        name = fn[(len(fn) - 1)]
    else:
        fn = file.split('\\')
        name = fn[(len(fn) - 1)]

    print('Moving file: '+ name)
    print('From: ' + file)
    print('To: ' + folder)

    os.replace(file, folder + '\\' + name)


readFiles()