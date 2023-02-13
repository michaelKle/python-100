row1 = ["□","□", "□"]
row2 = ["□","□", "□"]
row3 = ["□","□", "□"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the reasure? ")
coord = position.split(" ")

map[int(coord[1])-1][int(coord[0])-1] = "x"
print(f"{row1}\n{row2}\n{row3}")