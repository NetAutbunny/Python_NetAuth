# f = open("show_version.txt")
# data = f.readline()
# print(data)
# print(type(data))
# f.close()

with open("show_version.txt") as f:
    data = f.readline()
    print(data)
    print(type(data))