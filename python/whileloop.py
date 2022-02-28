while True:
    x = (input("Enter a number: "))
    if x == 'q' or x == 'quit':
        break
    else:
        x = int(x)
        y=1
        while True:
            print(y)
            y+=1
            if y>x:
                break