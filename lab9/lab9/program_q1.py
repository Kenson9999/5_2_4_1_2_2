import calculation.circle
import calculation.rectangle
while True:
    try:
        l = float ( input ( "Enter the length of rectangle: " ) )
        break
    except ValueError:
        print("Input a numeric value again")
        
while True:
    try:
        w = float ( input ( "Enter the width of rectangle: " ) )
        break
    except ValueError:
        print("Input a numeric value again")
        
while True:
    try:
        h = float ( input ( "Enter the height of rectangle: " ) )
        break
    except ValueError:
        print("Input a numeric value again")
        
while True:
    try:
        r = float ( input ( "Enter the radius of circle: " ) )
        break
    except ValueError:
        print("Input a numeric value again")

area_rectangle, surface_area_rectangle, volume_rectangle = calculation.rectangle.rectangle( l, w, h )
area, surface_area, volume = calculation.circle.circle(r)
print("Area of rectangle (length * width) is",area_rectangle)
print("Surface area of rectangle is ",surface_area_rectangle)
print("Volume of rectangle is ",volume_rectangle)
print ("Area of circle is", area)
print ("Surface area of sphere is", surface_area)
print ("Volume of sphere is", volume)