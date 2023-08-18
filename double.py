def double_char(s):
    x=None
    for i in s:
        if x is None:
            x=(i*2)
        else:
            x=x+(i*2)       
    return x

while True:
    inp=input('I am a cave. Yell at me: ')
    if inp == 'done':
        break
    else:
        echo=double_char(inp)
        print(echo)
print('Stop yelling at me')