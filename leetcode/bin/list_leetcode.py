import os


LEETCODE_DIR="../"

def list_leetcode(directory):
    abs_path=os.path.abspath(directory)
    files=os.listdir(abs_path)
    index=0
    for _file in files:
        if os.path.isfile(os.path.join(abs_path,_file)):
            filename=_file.split(".")[0]
            if filename:
                index+=1
                print "%d. %s" % (index,_file.split(".")[0])
    
list_leetcode(LEETCODE_DIR)
