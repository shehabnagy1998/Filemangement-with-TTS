import pyttsx3;

class fileMangement:

    def readFile(self, file):
        try:
            with open(file, 'r') as f:
                return f.read()
        except Exception as e:
            print('file not found, try another file')

    def createFile(self, file, content=''):
        with open(file, 'w') as f:
            f.write(content)

    def appendFile(self, file, content=''):
        with open(file, 'a') as f:
            f.write('\n' + content)

    def copyToFile(self, file1, file2):
        with open(file1, 'r') as f1:
            self.appendFile(file2, f1.read())

    def sayText(self, text):
        engine = pyttsx3.init()
        engine.setProperty('vioce', 1)
        engine.setProperty('rate', 90)
        engine.say(text)
        engine.runAndWait()



file = fileMangement()
while True:
    print('\nchoose what you want: \n1: read file \n2: create file \n3: write to file')
    i = input('=> ')
    if i == '1':
        name = input('\nenter file path: ')
        if file.readFile(name):
            if int(input('\n1: print on screen \n2: speak it \n=> ')) == 1:
                print(file.readFile(name))
            else:
                file.sayText(file.readFile(name))
    elif i == '2':
        name = input('\nenter file path: ')
        file.createFile(name)
    elif i == '3':
        while True:
             print('\nchoose what you want: \n1: write regular text \n2: write from file')
             i = input('-> ')
             if i == '1':
                text = input('\nenter text: ')
                name = input('enter file path: ')
                file.appendFile(name, text)
                break
             elif i == '2':
                name1 = input('\nenter file path to copy from: ')
                name2 = input('enter file path to write to: ')
                file.copyToFile(name1, name2)
                break
             else:
                 print('\nwrong choice, try again')
    else: 
        print('\nwrong choice, try again')

    if input('\nenter y to repeat: ') != 'y':
        break
