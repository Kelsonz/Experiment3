from PIL import Image
import math


class exp:
    def __init__(self, filename):
        # 载入图像
        self.filename = filename
        self.im = Image.open(filename)
        # 获得图片属性
        self.xsize, self.ysize = self.im.size
        self.rgb = list(self.im.getdata())

    def set_data(self, x, y, data):
        index = x * self.new_xsize + y
        self.new_rgb[index] = data

    def get_data(self, x, y):
        index = x * self.xsize + y
        return self.rgb[index]

    def save(self, item):
        self.new_im.putdata(self.new_rgb)
        self.new_im.save(item + self.filename)
        self.new_im.show()

    def new_image(self, xsize, ysize):
        self.new_xsize = xsize
        self.new_ysize = ysize
        self.new_im = Image.new('RGB', (xsize, ysize))
        self.new_rgb = [(0, 0, 0)] * (xsize * ysize)

    def rotate(self, degree):
        cos = math.cos(math.radians(degree))
        sin = math.sin(math.radians(degree))
        d = int(math.sqrt(math.pow(self.xsize, 2) + math.pow(self.ysize, 2)))
        x = y = d
        self.new_image(x, y)
        for j in range(self.ysize):
            for i in range(self.xsize):
                X = int((i - self.xsize / 2) * cos + (j - self.ysize / 2) * sin + x / 2)
                Y = int(-(i - self.xsize / 2) * sin + (j - self.ysize / 2) * cos + y / 2)
                self.set_data(X, Y, self.get_data(j, i))
        for j in range(y):
            for i in range(x):
                if self.new_rgb[j * x + i] == (0, 0, 0):
                    cos = math.cos(math.radians(-degree))
                    sin = math.sin(math.radians(-degree))
                    X = (i - x / 2) * cos + (j - y / 2) * sin + self.xsize / 2
                    Y = -(i - x / 2) * sin + (j - y / 2) * cos + self.ysize / 2
                    if X >= self.xsize or Y >= self.ysize:
                        pass
                    elif X < 0 or Y < 0:
                        pass
                    else:
                        self.deltax = X - int(X)
                        self.deltay = Y - int(Y)
                        if int(X) + 1 == self.xsize - 1:
                            xx = self.xsize - 1
                        else:
                            xx = int(X) + 1
                        if int(Y) + 1 == self.ysize - 1:
                            yy = self.ysize - 1
                        else:
                            yy = int(Y) + 1
                        xy00 = self.get_data(yy , int(X))
                        xy01 = self.get_data(int(Y), int(X))
                        xy10 = self.get_data(yy, xx)
                        xy11 = self.get_data(int(Y), xx)
                        self.set_data(i, j, self.rgb_double_interpolating(xy00, xy01, xy10, xy11))

        self.save('rotate_' + str(degree) + '_')

    def flip(self):
        self.new_image(self.xsize, self.ysize)
        for i in range(self.ysize):
            for j in range(self.xsize):
                self.set_data(i, j, self.get_data(i, self.xsize - j - 1))
        self.save('flip_')

    def resize(self, new_x, new_y):
        cx = self.xsize / new_x
        cy = self.ysize / new_y
        self.new_image(new_x, new_y)
        for i in range(new_y):
            for j in range(new_x):
                self.set_data(i, j, self.get_data(int(cy * i), int(cx * j)))
        self.save('resize_')

    def move(self, x, y):
        x = int(x)
        y = int(y)
        self.new_image(x + self.xsize, y + self.ysize)
        for i in range(self.ysize):
            for j in range(self.xsize):
                self.set_data(i + y, j + x, self.get_data(i, j))
        self.save('move_')

    def rgb_double_interpolating(self, xy00, xy01, xy10, xy11):
        r = int(self.func(xy00[0], xy01[0], xy10[0], xy11[0]))
        g = int(self.func(xy00[1], xy01[1], xy10[1], xy11[1]))
        b = int(self.func(xy00[2], xy01[2], xy10[2], xy11[2]))
        return (r, g, b)

    def func(self, xy00, xy01, xy10, xy11):
        a = (1 - self.deltax) * xy00 + self.deltax * xy01
        b = (1 - self.deltax) * xy10 + self.deltax * xy11
        return (1 - self.deltay) * a + self.deltay * b


def matrix(matrix, xsize, ysize):
    for j in range(ysize):
        t = list()
        for i in range(xsize):
            t.append(matrix[j * ysize + i])
        print(t)


# t = exp('color.jpg')
t = exp('002.jpg')
t.rotate(404)
# t.flip()
# t.move(20.2, 35.8)
# t.resize(520, 640)
