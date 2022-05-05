class Drawing:
    def __init__(self, length, height, symbol):
        self.image = [[symbol] * length for i in range (height)]
        print (self.image)

    def print(self):
        for row in self.image:
            for elem in row:
                print(elem, end=' ')
            print()

    def setPoint(self, x, y, symb):
        self.image[y-1][x-1] = symb
        return

    def drawVerticalLine(self, x, y1, y2, symb):
        for y in range (y1-1, y2):
            self.image[y][x-1] = symb

    def drawHorizontalLine(self, y, x1, x2, symb):
        for x in range(x1-1, x2):
            self.image[y-1][x] = symb

    def drawRectangle(self, length, height, symb):
        self.drawVerticalLine(1, 1, height, symb)
        self.drawVerticalLine(length, 1, height, symb)
        self.drawHorizontalLine(1, 1, length, symb)
        self.drawHorizontalLine(height, 1, length, symb)

img = Drawing(10, 9, '.')

img.drawHorizontalLine(2, 5, 7, 'x')
img.drawVerticalLine(2, 5, 7, 'x')
img.print()
