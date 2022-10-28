# Complete the function rectangle below
def rectangle(l,w,h):
    area = l*w
    surface_area = l*w*2+l*h*2+h*w*2
    volume = l*w*h
    return area, surface_area, volume
 
# Complete the function circle below
def circle(r):
    import math
    area = math.pi*r**2
    surface_area = 4*math.pi*r**2
    volume = (4/3)*math.pi*r**3
    return area, surface_area, volume

# Output Generation. You are not allowed to modify the following codes
def main():
    l = float ( input ( "Enter the length of rectangle:" ) )
    w = float ( input ( "Enter the width of rectangle:" ) )
    h = float ( input ( "Enter the height of rectangle:" ) )
    r = float ( input ( "Enter the radius of circle:" ) )
    area_rectangle, surface_area_rectangle, volume_rectangle = rectangle( l, w, h )
    area_circle, surface_area_sphere, volume_sphere = circle( r )
    print ( "Area of rectangle is", area_rectangle )
    print ( "Surface area of rectangle is", surface_area_rectangle )
    print ( "Volume of rectangle is", volume_rectangle )
    print ( "Area of circle is", area_circle )
    print ( "Surface area of sphere is", surface_area_sphere )
    print ( "Volume of sphere is", volume_sphere )

if __name__ == "__main__":
    main()
