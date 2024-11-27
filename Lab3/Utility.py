def inputValue(msg,start= 0 ,end = None ):
    while True:
        inp = input(msg)
        if not inp.isdecimal():
            print("Nieprawidłowe dane wejsciowe!")
        elif start is not None and end is not None:
            if not (start <= int(inp) <= end):
                print(f"Wybierz opcje spośród 1 do 5")
            else:
                return int(inp)
        else:
            return int(inp)



