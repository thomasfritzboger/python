import utils

file_names = list(("../02_4_exercise/02_4_cli.py","../02_4_exercise/__init__.py","../02_4_exercise/webget.py","../02_7_exercise/my_utilities.py","email.py")) 

md_files = ("./markdown_files/markdown1.md","./markdown_files/markdown2.md")

utils.get_file_names("../02_3_exercise")
utils.get_all_file_names("../")
utils.print_line_one(file_names)
utils.print_emails(file_names)
utils.write_headlines(md_files)
#utils.file_names = get_file_names2("../")
