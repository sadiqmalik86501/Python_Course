# Build a File Organizer using Python that can automatically sort and organize files on your system. The program can categorize files into folders such as Images, Documents, Videos, Music, and Others, making your workspace clean and efficient.

import os 

def arrange_files(files,ext):
    file_with_ext=[file for file in files if file.endswith(ext)]
    
    # i=1
    # for file in file_with_ext:
    #     os.rename(file,f"photo-{i}{ext}")
    #     i+=1

    if not(os.path.exists("images")):
        os.mkdir("Images")   

    for i,file in enumerate(file_with_ext):
        os.rename(file,f"my_photo-{i+1}{ext}")

if __name__=="__main__":
    files=os.listdir()
    arrange_files(files,".jpg")