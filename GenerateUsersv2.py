import os
from pathlib import Path




def generateUsers(amount, string):
    result = []
    if string.find("#") != -1:
        for i in range(1,amount + 1):
            result.append(string.replace("#", str(i)) + "\n") 
    else:
        for i in range(1,amount+1):
            result.append(string + str(i) + "\n") 


    return(result)
    
def openAndWriteToFile(filename, filepath, result):
    if filename == "":
        filename = defaultfilename

    if filepath == "":
        filepath = defaultFilepath
    
    if os.path.exists(filepath):
        file = open(os.path.join(filepath, filename), "w")
    else:
        path = Path.mkdir(filepath, parents=True)
        file = open(os.path.join(path, filename), "w")

    for string in result:
        file.write(string)





defaultfilename = "user_file_test.txt"
defaultFilepath = "./"
results=[]

inputString = input("Введите предпологаемое имя пользователя втребуемом формате,\n для того чтобы добавить порядковый номер используйте символ # в том месте строки где его предполагается добавить.\n") 

while True:
    try:
        amount = int(input("Введите требуемое колличество пользователей, принимаются только целые положительные числа\n"))
    
    except:
        print("Вы ввели не верное число, попробуйте ещё раз.\n")
        continue

    else:
        break

results = generateUsers(amount, inputString)

fileName = input("Введите имя файла с расширением, имя файла по умолчанию ""user_file_test.txt"" применяется если ничего не вводить\n")
filePath = input("Введите желаемый путь к файлу, если ничего не вводить файл будет создан в рабочей дректории скрипта\n")

openAndWriteToFile(fileName, filePath, results)