
from collections import deque

def amount(word):
    stack = deque()
    aux = 0
    for char in word:
        if char == '<':
            stack.append(char)
        
        elif char == '>':
            if len(stack) > 0 and stack[0] == '<':
                stack.pop()
                aux += 1
            
        
    return aux


i = int(input().strip())
awnser = []
    
for j in range(i):
    word = input().strip()
    awnser.append(amount(word))

j = 0
while j < i:
    print(awnser[j])
    j += 1

