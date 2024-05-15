# class X(object):
#      """Example class"""
#      def __init__(self):
#          """init function for class X"""
#          self.a = 1
#          self._a = 2
#          self.__a = 3
#
#      def get_the_hidden_attribute(self):
#          return self._X__a
#
# x = X()
# print(x.a)
# print(x._a)
# print(x.get_the_hidden_attribute())


class Point:

    def __init__(self, x=0, y=0):
        self._x = x
        self._y = y

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError("Coordinates must be numbers.")
        self._x = value

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError("Coordinates must be numbers.")
        self._y = value


if __name__ == "__main__":
    p = Point()

    print("Initial coordinates:", p.x, p.y)
    p.x = 3
    p.y = 5
    print("Modified coordinates:", p.x, p.y)

    try:
        p.x = "abc"
    except ValueError as e:
        print("Error:", e)
