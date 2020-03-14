test_cases = int(input())
for x in range(test_cases):
    seq = input()

    querie_cases = int(input())

    for j in range(querie_cases):
        is_sub = False
        sub_seq = input()
        i=0
        for letter in seq:
            if(letter) == sub_seq[i]:
                i+=1
                if(i == len(sub_seq)):
                    is_sub = True
                    break
        if(is_sub):
            print('Yes')
        else:
            print('No')
