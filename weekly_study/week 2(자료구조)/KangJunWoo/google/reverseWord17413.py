s=list(input())
tag=False
word=''
result=''
for i in s:
  #뒤집어서 출력
  if tag==False:
    if i=='<':
      tag=True
      word=word+i
    #중간점검
    elif i==' ':
      word=word+i
      result=result+word
      word=''
    else:
      word=i+word

  #정상적으로 출력
  elif tag==True:
    word=word+i
    if i=='>':
      tag=False
      result=result+word
      word=''

print(result+word)