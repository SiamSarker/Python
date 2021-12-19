n = int(input())
for i in range(0,n):
    word = str(input())
    word_len = len(word)
    if word_len > 10:
        print(word[0], end='')
        print(word_len-2, end='')
        print(word[word_len-1])
    else:
        print(word)



