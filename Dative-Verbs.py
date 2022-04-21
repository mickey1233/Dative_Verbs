import random


def DativeVerbs(s):
    total_score = len(s)
    result = 0
    print("總分:", result)
    while s:
        dativeverb = random.choice(list(s.keys()))
        print(dativeverb)
        prep = input("請輸入介係詞:")
        if s[dativeverb] == prep:
            result += 1
            print(total_score, '/', result)
            del s[dativeverb]
        else:
            print('輸入錯誤答案為:', s[dativeverb])
            print(total_score, '/', result)
            del s[dativeverb]
    print('最後分數為: ', total_score, '/', result)


if __name__ == "__main__":
    dic = {}
    with open('Dative-Verbs.txt') as f:
        for line in f.readlines():
            temp = line.split()
            dic[temp[0]] = temp[1]
    DativeVerbs(dic)
