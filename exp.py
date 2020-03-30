from PIL import Image


class exp:
    def __init__(self, filename):
        # 载入图像
        self.filename = filename
        self.img = Image.open(filename)
        self.im = self.img.copy()
        # 获得图片属性
        self.xsize, self.ysize = self.im.size
        self.rgb = list(self.im.getdata())
        self.new_rgb = self.rgb.copy()

    def set_data(self, x, y, data):
        index = x * self.xsize + y
        self.new_rgb[index] = data

    def get_data(self, x, y):
        index = x * self.xsize + y
        return self.rgb[index]

    def out_of_range(self, i, j, x, y):
        i = i + y
        j = j + x
        if i >= self.ysize or j >= self.xsize:
            return True
        else:
            return False

    def save(self):
        self.im.putdata(self.new_rgb)
        self.im.save('test.jpg')
        self.im.show()

    def not_in_pic(self, i, j, x, y):
        if i < y or j < x:
            return True
        else:
            return False

    def move(self, x, y):
        zero = (0, 0, 0)
        for i in range(self.ysize):
            for j in range(self.xsize):
                if not self.out_of_range(i, j, x, y):
                    self.set_data(i + y, j + x, self.get_data(i, j))
                if self.not_in_pic(i, j, x, y):
                    self.set_data(i, j, zero)
                # matrix(self.new_rgb, self.xsize, self.ysize)
        self.save()


def matrix(matrix, xsize, ysize):
    for j in range(ysize):
        t = list()
        for i in range(xsize):
            t.append(matrix[j * ysize + i])
        print(t)


t = exp('color.jpg')
t.move(10, 50)
