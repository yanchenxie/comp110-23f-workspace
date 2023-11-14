"""CQ07 Making Points."""

from lessons.CQ07.point import Point

my_point: Point = Point(2.3, 4.6)
print(my_point.x)

my_point.scale_by(3)
print(my_point.x)

my_new_point: Point = my_point.scale(3)
print(my_new_point.x)