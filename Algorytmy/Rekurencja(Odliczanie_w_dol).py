
def countdown(i):
    print (i)
        #przypadek podstawowy
    if i <= 0:
        return
    else:
        #przypadek rekurencyjny
        countdown(i-1)

countdown(20)

