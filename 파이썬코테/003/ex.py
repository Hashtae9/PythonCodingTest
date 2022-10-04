for i in range(5):
    if i == 1: print(i)
    for j in range(5):
        if i == j:
            print(j)
            break
    else: print('?')
        