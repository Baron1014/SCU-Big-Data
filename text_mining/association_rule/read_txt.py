f = open("test.txt", encoding='utf-8')
files = f.read()
file_list2 = files.encode('utf-8').decode('utf-8-sig').split("split")
f_list = list()
#target_list = [int(x) for x in lines.split('],[')]

for i in file_list2:
    f_list.append(i)

print(file_list2)
