#!/usr/bin/env python3

class BingoCard:
    def __init__(self):
        self.rows = []
        self.marks = []
        self.done = False

    def mark(self, number):
        if self.done:
            return
        for y, row in enumerate(self.rows):
            if number in row:
                x = row.index(number)
                self.marks[y][x] = 1

    def addRow(self, row):
        self.rows.append(row)
        self.marks.append([0]*len(row))

    def check_win(self):
        for row in self.marks:
            if all(i == 1 for i in row):
                self.done = True
                return True
        for x in range(len(self.rows[0])):
            col = []
            for row in self.marks:
                col.append(row[x])
            if all(i == 1 for i in col):
                self.done = True
                return True
        return False

    def get_score(self):
        score = 0
        for y, row in enumerate(self.marks):
            for x, v in enumerate(row):
                if v == 0:
                    score += int(self.rows[y][x])
        return score

    def __str__(self):
        ret = "Card:\n"
        for r in self.rows:
            ret += str(r) + "\n"
        ret += "Marks:\n"
        for r in self.marks:
            ret += str(r) + "\n"
        return ret

def parse_input():
    cards = []

    with open("input") as f:
        rnd_values = f.readline().split(",")

        for line in f:
            if len(line) < 2:
                card = BingoCard()
                cards.append(card)
            else:
                card.addRow(line.split())

    return cards, rnd_values

def draw_winner(rnd_values, cards):
    for n in rnd_values:
        print("Draw ", n)
        for card in cards:
            if card.done:
                continue

            card.mark(n)
            if card.check_win():
                print("Winner:")
                print(card)
                score = card.get_score()
                print("Score", score)
                print("Solution:", score * int(n))


cards, rnd_values = parse_input()

print(f"Got {len(cards)} cards")

draw_winner(rnd_values, cards)
