from collections import deque
file = open('22.txt')
import sys

sys.stdout = open('output.txt', 'w')

player1 = deque()
player2 = deque()
read_player2 = False
for line in file.readlines():
    stripped = line.strip()

    if stripped.startswith("Player"):
        continue

    if not stripped:
        read_player2 = True
        continue

    if read_player2:
        player2.append(stripped)
    else:
        player1.append(stripped)

print(player1)
print(player2)

# Part 1
# print("Starting Play")
# def play():
#     p1card = player1.popleft()
#     p2card = player2.popleft()
#
#     # print("1:{} 2:{}".format(p1card, p2card))
#
#     if int(p1card) > int(p2card):
#         player1.append(p1card)
#         player1.append(p2card)
#     else:
#         player2.append(p2card)
#         player2.append(p1card)
#
# while len(player1) and len(player2):
#     play()
#     # print(player1)
#     # print(player2)
#     # break
#
# winner_score = 0
# winner = player1 if len(player1) > len(player2) else player2
# index = 1
# while len(winner):
#     winner_score += index * int(winner.pop())
#     index += 1
# print(winner_score)

# Part 2
print("Starting Play")


def play_game(p1, p2):
    # Main Recursive Function

    finished_p1 = set()
    finished_p2 = set()

    while len(p1) and len(p2):

        print("Round Started\nP1:{}\nP2:{}\n".format(p1, p2))

        p1s = int(''.join(p1))
        p2s = int(''.join(p2))

        if p1s in finished_p1 and p2s in finished_p2:
            print("Recursion:\nP1:{}\nP2:{}\nP1 Wins".format(p1, p2))
            return 1, p1

        finished_p1.add(p1s)
        finished_p2.add(p2s)

        p1card = p1.popleft()
        p2card = p2.popleft()

        if len(p1) >= int(p1card) and len(p2) >= int(p2card):
            print("Recursion Combat 1:{} 2:{}\nP1:{}\nP2:{}\n".format(p1card, p2card, p1, p2))
            # Copy of that many cards
            p1copy = deque([val for ind, val in enumerate(p1) if ind < int(p1card)])
            p2copy = deque([val for ind, val in enumerate(p2) if ind < int(p2card)])

            player_n, player_cards = play_game(p1copy, p2copy)

            if player_n == 1:
                p1.append(p1card)
                p1.append(p2card)
                print("1 Wins")
            else:
                p2.append(p2card)
                p2.append(p1card)
                print("2 Wins")
        else:

            print("Regular Combat 1:{} 2:{}".format(p1card, p2card))
            if int(p1card) > int(p2card):
                p1.append(p1card)
                p1.append(p2card)
                print("1 Wins")
            else:
                p2.append(p2card)
                p2.append(p1card)
                print("2 Wins")

        print("Round Done\nP1:{}\nP2:{}\n".format(p1, p2))

    return (1, p1) if len(p1) > len(p2) else (2, p2)

player_num, winner = play_game(player1, player2)

winner_score = 0
index = 1
while len(winner):
    winner_score += index * int(winner.pop())
    index += 1
print(winner_score)
