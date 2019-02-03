from random import choice, randint


class Game2048:
    def __init__(self, n=4):
        self.field = [['' for i in range(n)] for k in range(n)]
        self.free_field = [[i, j] for i in range(n) for j in range(n)]
        self.n = n
        self.add_tile()
        self.add_tile()
        self.scorebar = 0

    def __getitem__(self, index):
        return self.field[index]

    def __str__(self):
        output = '\n'
        for i in range(self.n):
            output += '-' * (self.n * 11) + '\n'
            output += '|'
            for j in range(self.n):
                output += '{:^10}|'.format(self[i][j])
            output += '\n'
        output += '-' * (self.n * 11) + '\n'
        return output

    def left(self):
        change = False
        for i in range(self.n):
            for k in range(self.n):
                ctr = 1
                while k+ctr < self.n and not self[i][k+ctr]:
                    ctr += 1
                if k+ctr < self.n and self[i][k] == self[i][k+ctr] != '':
                    self[i][k] *= 2
                    self[i][k+ctr] = ''
                    self.scorebar += self[i][k]
                    change = True

            for k in range(self.n):
                if not self[i][k]:
                    ctr = 1
                    while k+ctr < self.n and not self[i][k+ctr]:
                        ctr += 1
                    if k+ctr < self.n:
                        self[i][k] = self[i][k+ctr]
                        self[i][k+ctr] = ''
                        change = True

        if change:
            self.add_tile()

    def right(self):
        change = False
        for i in range(self.n):
            for k in range(self.n-1, -1, -1):
                ctr = 1
                while k-ctr >= 0 and not self[i][k-ctr]:
                    ctr += 1
                if k-ctr >= 0 and self[i][k] == self[i][k-ctr] != '':
                    self[i][k] *= 2
                    self[i][k-ctr] = ''
                    self.scorebar += self[i][k]
                    change = True

            for k in range(self.n-1, -1, -1):
                if not self[i][k]:
                    ctr = 1
                    while k-ctr >= 0 and not self[i][k-ctr]:
                        ctr += 1
                    if k-ctr >= 0:
                        self[i][k] = self[i][k-ctr]
                        self[i][k-ctr] = ''
                        change = True

        if change:
            self.add_tile()

    def up(self):
        change = False
        for i in range(self.n):
            for k in range(self.n):
                ctr = 1
                while k+ctr < self.n and not self[k+ctr][i]:
                    ctr += 1
                if k+ctr < self.n and self[k][i] == self[k+ctr][i] != '':
                    self[k][i] *= 2
                    self[k+ctr][i] = ''
                    self.scorebar += self[k][i]
                    change = True

            for k in range(self.n):
                if not self[k][i]:
                    ctr = 1
                    while k+ctr < self.n and not self[k+ctr][i]:
                        ctr += 1
                    if k+ctr < self.n:
                        self[k][i] = self[k+ctr][i]
                        self[k+ctr][i] = ''
                        change = True

        if change:
            self.add_tile()

    def down(self):
        change = False
        for i in range(self.n):
            for k in range(self.n-1, -1, -1):
                ctr = 1
                while k-ctr >= 0 and not self[k-ctr][i]:
                    ctr += 1
                if k-ctr >= 0 and self[k][i] == self[k-ctr][i] != '':
                    self[k][i] *= 2
                    self[k-ctr][i] = ''
                    self.scorebar += self[k][i]
                    change = True

            for k in range(self.n-1, -1, -1):
                if not self[k][i]:
                    ctr = 1
                    while k-ctr >= 0 and not self[k-ctr][i]:
                        ctr += 1
                    if k-ctr >= 0:
                        self[k][i] = self[k-ctr][i]
                        self[k-ctr][i] = ''
                        change = True

        if change:
            self.add_tile()

    def add_tile(self):
        free_field = []
        for i in range(self.n):
            for k in range(self.n):
                if self[i][k] == '':
                    free_field.append([i, k])
        i, k = choice(free_field)
        self[i][k] = 4 if randint(0, 9) == 9 else 2

    def get_scorebar(self):
        return str('Score: ' + str(self.scorebar))


if __name__ == '__main__':
    game = Game2048()
    print('Score: ' + str(game.scorebar))
    print(game)
    while True:
        action = input()
        if action == 'w':
            game.up()
        elif action == 'a':
            game.left()
        elif action == 's':
            game.down()
        elif action == 'd':
            game.right()

        print('Score: ' + str(game.scorebar))
        print(game)
