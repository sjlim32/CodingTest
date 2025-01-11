import sys
print = sys.stdout.write

diary = list(input().split())
vowel = ("a", "e", "o", "u", "i")
answer = []

for word in diary:
  new_word = ""
  idx = 0
  while idx < len(word):
    if word[idx] in vowel:
      new_word += word[idx]
      idx += 3
    else:
      new_word += word[idx]
      idx += 1
  answer.append(new_word)

for ans in answer:
  print(f"{ans} ")

# OPTIMIZING
e=input()
d=""
i=0
while 1:
    if i>=len(e): break
    d+=e[i]
    i+=1+(e[i] in 'aeiou')*2
print(d)