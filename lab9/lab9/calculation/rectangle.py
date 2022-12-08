def rectangle( length, width, height ):
    area = length * width
    surface_area = ( length * width + length * height + width * height ) * 2
    volume = length * width * height
    return area, surface_area, volume
 
if __name__ == "__main__":
    print ("The following codes are used to test the rectangle library")
    area, surface_area, volume = rectangle(2,4,6)
    print ("Area of rectangle (length * width) is", area)
    print ("Surface area of rectangle is", surface_area)
    print ("Volume of rectangle is", volume)
