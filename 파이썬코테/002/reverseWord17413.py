import sys
words = sys.stdin.readline().strip()

# 입력 받은 문장을 구분하여 저장할 list
words_list = []

temp = []
i = 0
# 입력 받은 문장에 대하여 
while i < len(words):
    # 입력이 < 이면
    if words[i] == '<':
        if temp:
            words_list.append(''.join(temp[::-1]))
            temp = []
        temp.append(words[i])
        i += 1
        while words[i] != '>':
            temp.append(words[i])
            i += 1
        # temp에 >가 나올때 까지 저장
        temp.append(words[i])
        i += 1
        # 그 후에 join으로 문자열로 만들어 wordlist에 저장
        words_list.append(''.join(temp))
        temp = []
    # 아니면 뒤집어서 wordlist에 저장
    else:
        if words[i] == ' ':
            words_list.append(''.join(temp[::-1]))
            words_list.append(' ')
            temp = []
            i += 1
        temp.append(words[i])
        i += 1

words_list.append(''.join(temp[::-1]))

print(''.join(words_list))
    

# 단어 입력 받을때 split으로 공백구분. => <> 내부 공백 구분 불가, 오류
# --> 입력 받은 문자열 for문으로 반복하며 직접 리스트화
# <로 시작하면 다음 > 까지 모두 한 요소로 리스트에 append
# 태그가 아닌 단어는 공백으로 구분

# 출력하면서 슬라이싱[::-1]으로 뒤집어 출력.
# <>일때는 그냥 출력하도록 