num = int(input())
card = list(map(int, input().split()))
s,b,i = 0,0,0
while len(card) > 0:
    if i % 2 == 0:
        s += card.pop(0) if card[0] > card[-1] else card.pop(-1)
    else:
        b += card.pop(0) if card[0] > card[-1] else card.pop(-1)
    i += 1
print(s,b)
