from PIL import Image


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
        r = self.func(xy00[0], xy01[0], xy10[0], xy11[0])
        g = self.func(xy00[1], xy01[1], xy10[1], xy11[1])
        b = self.func(xy00[2], xy01[2], xy10[2], xy11[2])
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
# t.move(20.2, 35.8)
# t.resize(520, 640)
