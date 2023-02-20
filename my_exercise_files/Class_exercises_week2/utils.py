import os

def get_file_names(folderpath, out="output.txt"):
    with open(out, "w") as dest:
        for file in os.listdir(folderpath):
            dest.write(file + '\n')

def get_all_file_names(folderpath,out="all_files_output.txt"):
    with open(out, "w") as dest:
        for root, subdirs, files in os.walk(folderpath):
            for file in files:
                dest.write(os.path.join(root,file) + '\n')

"""Virker ikke på byte filer, der skal laves en if guard"""
#def get_file_names2(folderpath):
#    file_names = list()
#    for root, subdirs, files in os.walk(folderpath):
#            for file in files:
#                file_names.append(os.path.join(root,file))
#    return file_names

def print_line_one(file_names):
    for file_name in file_names:
        with open(file_name, "r") as file:
            print(file.readline())

def print_emails(file_names):
    for file_name in file_names:
        with open(file_name,"r") as file:
            for line in file:
                if "@" in line:
                    print(line)

def write_headlines(md_files,out="md_output.txt"):
    with open(out, "w") as output_file:
        for md_file in md_files:
            with open(md_file, "r") as md:
                for line in md:
                    if line.startswith("#"):
                        output_file.write(line)


if __name__ == '__main__':
    file_names = list(("../02_4_exercise/02_4_cli.py","../02_4_exercise/__init__.py","../02_4_exercise/webget.py","../02_7_exercise/my_utilities.py","email.py")) 

    md_files = ("./markdown_files/markdown1.md","./markdown_files/markdown2.md")

    get_file_names("../02_3_exercise")
    get_all_file_names("../")
    print_line_one(file_names)
    print_emails(file_names)
    write_headlines(md_files)
    #file_names = get_file_names2("../")
