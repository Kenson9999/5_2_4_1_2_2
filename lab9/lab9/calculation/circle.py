import math

def circle( radius ):
    area = radius ** 2 * math.pi
    surface_area = 4 * math.pi * radius ** 2
    volume = 4 / 3 * math.pi * radius ** 3
    return area, surface_area, volume
if __name__ == "__main__":
    print ("The following codes are used to test the circle library")
    area, surface_area, volume = circle(5)
    print ("Area of circle is", area)
    print ("Surface area of sphere is", surface_area)
    print ("Volume of sphere is", volume)
