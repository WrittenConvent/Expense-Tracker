import sys

#testcase
cost={}

#cleans the prefixes in sample.txt
def clean():
    with open("sample.txt", "r") as file:
        lines=file.readlines()

    with open("sample.txt","w") as file:
        for line in lines:
            if line.startswith("name="):
                file.write(line[5:])
            elif line.startswith("price="):
                file.write(line[6:])

#stores the user input in output.txt
def outputfile():
    out_path='output.txt'
    with open(out_path,'w') as f:
        og=sys.stdout
    sys.stdout=f
    for a,b in cost.items():
        print(f"Name:{a} Price:{b}")
    sys.stdout

#reads sample.txt and uses it as input instead of stdin
def inputfile():
    og=sys.stdin
    with open("sample.txt","r") as file:
        sys.stdin = file #read input from sample.txt
        lines=file.readlines()

    sys.stdin=og #restores input to stdin 

inputfile()