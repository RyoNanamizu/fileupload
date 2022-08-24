word = 'abcdefghijklmnopqrstwvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()'
with open('./test.txt', 'wb') as file:
    for j in range(1,10001):
        for i in range(len(word)):
            payload = (word[i]*10000).encode()
            file.write(payload)
        if j%10 == 0:
            file.write('\n'.encode())
            # print((word[i]*10).encode())