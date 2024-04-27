input_str =  "Hi My name is Logunathan J . my age is 21" # input()

input_str = input_str.replace(",",".").replace("and",".")

input_ls = input_str.split(".")

key = ["name","age"]

helper = ["hi","my","is"];

pairs = {}

for j in input_ls:
    ls = j.split(" ")
    keystr = ""
    for i in range(len(ls)):
        if(ls[i].lower() in helper):
            ls[i] = ""
        elif(ls[i].lower() in key):
            keystr+=ls[i]+" ";
            ls[i] = ""
    pairs[keystr] = " ".join(ls).strip();
print(pairs)

            

