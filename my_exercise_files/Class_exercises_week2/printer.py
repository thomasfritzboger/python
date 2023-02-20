import argparse

file = "my_csv_file.csv"

def print_file_content(file):
    with open(file) as file_object:
        content = file_object.readlines()
    
    for line in content[1:]:
        print(line.strip().split(','))

print_file_content(file)

def write_list_to_file(output_file,*args):
    with open (output_file,"w") as output:
        print(args)
        for a in args:
            output.write(a+"\n") 

my_list = list(("Hans","Egon","Erik"))

write_list_to_file("output.txt", "Hans","Jens","Egon","Erik")

def copy(path, filename):
    with open(path, "r") as file_object:
        with open(filename, "w") as second_file:
            content = file_object.readlines()
            for line in content[:]:
               second_file.write(line)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='A program that reads from one csv file and writes to another file')
    parser.add_argument('path', help='The path to the CSV file')
    parser.add_argument('-f', '--file', help='What should the new filename be')
    

    args = parser.parse_args()
    print('path:', args.path)
    print('File:', args.file)

    if not args.file == None:
        copy(args.path, args.file)



