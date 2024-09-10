print("grass cutting duration calculator")
lengthyard = float(input("length of the yard (ft): ")) 
widthyard = float(input("width of the yard (ft): "))
lengthhouse = float(input("length of the house (ft): "))
widthhouse = float(input("width of the house (ft): "))

#user input
luashouse = lengthhouse * widthhouse
luasyard = lengthyard* widthyard
luasgrass = luasyard-luashouse
rate = 2 #ft^2/second

time = luasgrass/rate

print (f"the time required to cut the grass on your yard is {time} second")