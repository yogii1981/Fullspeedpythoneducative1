proLang = ['python', 'C', 'C++', 'java', 'PHP', 'C#', 'Javascript']
try:
    index = int(input("Enter a  program langauge:"))
    print(proLang[index])
except:
    print('Out of range')
