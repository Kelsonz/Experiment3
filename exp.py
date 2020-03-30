from PIL import Image


class exp:
    def __init__(self, filename):
        # 载入图像
        self.filename = filename
        self.img = Image.open(filename)
        self.im = self.img.copy()
        # 获得图片属性
        self.xsize, self.ysize = self.im.size
        self.r = list(self.im.split()[0].getdata())
        self.g = list(self.im.split()[1].getdata())
        self.b = list(self.im.split()[2].getdata())
        self.new_r = self.r.copy()
        self.new_g = self.g.copy()
        self.new_b = self.b.copy()

    def set_data(self, x, y, data):
        index = x * self.ysize + y
        self.new_r[index] = data[0]
        self.new_g[index] = data[1]
        self.new_b[index] = data[2]

    def get_data(self, x, y):
        index = x * self.xsize + y
        return (self.r[index], self.g[index], self.b[index])

    def out_of_range(self, i, j, x, y):
        i = i + y
        j = j + x
        index = i * self.ysize + j
        if index > self.ysize * self.xsize:
            return True
        else:
            return False

    def save(self):
        self.im.putdata([self.new_r, self.g, self.b])
        self.im.save('test.jpg')

    def move(self, x, y):
        zero = (0, 0, 0)
        for i in range(self.ysize):
            for j in range(self.xsize):
                self.set_data(i, j, zero)
                if self.out_of_range(i, j, x, y) is False:
                    self.set_data(i + y, j + x, self.get_data(i, j))
        self.save()


t = exp('color.jpg')
t.move(3, 5)
