# area of triangle with breadth and height

"""breadth=int(input("enter the breadth value:"))
height=int(input("enter the height value:"))
area = 1/2 * breadth*height

print(int(area))"""

#area of triangle with given sides
# if given sides are a,b,c  then,
# semi perimeter s=(a+b+c)/2
# and area of triangle is area =  sqare root of (s*(s-a)*(s-b)*(s-c))

a= int(input("enter the side1:"))
b= int(input("enter the side2:"))
c= int(input("enter the side3:"))

s = (a+b+c)/2

area= ((s*(s-a)*(s-b)*(s-c))) ** 0.5

print(float(round(area,2)))

