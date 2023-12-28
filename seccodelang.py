coding = int(input("For coding enter 1 and 0 for decoding \n"))
if(coding == 1):
    nwords = []
    str = input("Enter a message \n")
    words = str.split(" ")
    # print(words)
    for word in words:
      if(len(word)>=3):
        r1= "dsfa"
        r2= "ghog"
        strnew = r1 + word[1:] + word[0] + r2
        nwords.append(strnew)
      else:
        nwords.append(word[::-1])
    print(" ".join(nwords))


else:
  nwords = []
  str = input("Enter a message")
  words = str.split(" ")
  for word in words:
    if(len(word) < 3 ):
      strnew = word[::-1]
      nwords.append(strnew)
    else:
      strnew = word[4:-4]
      strnew = strnew[-1] + strnew[:-1]
      nwords.append(strnew)

  print(" ".join(nwords))











