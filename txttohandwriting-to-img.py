# Usage
# python txttohandwriting-to-img.py

from PIL import Image
BG = Image.open("Handwrittenwords\\bg.png")
sizeOfSheet =BG.width
gap, _  = 0,0
allowedChars = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM,.-?!() 1234567890'
def writee(char):
    global gap, _
    if char == '\n':
        pass
    else:
        char.lower()
        cases = Image.open("Handwrittenwords/%s.png"%char)
        BG.paste(cases, (gap, _))
        size = cases.width
        gap += size
        del cases

def letterwrite(word):
    global gap, _
    if gap > sizeOfSheet - 95*(len(word)):
        gap = 0
        _ += 200
    for letter in word:        
        if letter in allowedChars:
            if letter.islower():
                pass
            elif letter.isupper():
                letter = letter.lower()
                letter += 'upper'            
            elif letter == '.':
                letter = "fullstop"
            elif letter == '!':
                letter = 'exclamation'
            elif letter == '?':
                letter = 'question'
            elif letter == ',':
                letter = 'comma'
            elif letter == '(':
                letter = 'braketop'
            elif letter == ')':
                letter = 'braketclose'
            elif letter == '-':
                letter = 'hiphen'
            writee(letter)
def worddd(Input):
    wordlist=Input.split(' ')
    for i in wordlist:
        letterwrite(i)
        writee('space')
if __name__ == '__main__':
    try:
        with open('testfile.txt', 'r') as file:
            data = file.read().replace('\n', '')
        l=len(data)
        nn=len(data)//600
        chunks, chunk_size = len(data), len(data)//(nn+1)
        p=[ data[i:i+chunk_size] for i in range(0, chunks, chunk_size) ]
        
        for i in range(0,len(p)):
            worddd(p[i])
            writee('\n')
            BG.save('img/%doutt.png'%i)
            BG1= Image.open("Handwrittenwords/bg.png")
            BG=BG1
            gap = 0
            _ =0
    except ValueError as E:
        print("{}\nTry again".format(E))
