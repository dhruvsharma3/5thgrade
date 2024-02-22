def area():
    lenth = input("length please:")
    width = input("width please or type skip if skipped:")
    if width == "skip":
        width = float(10)
        lenth = float(lenth)
    else:
        width = float(width)
        lenth = float(lenth)

    area = width * lenth
    print(area)
    
area()