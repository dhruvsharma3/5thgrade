def string_makefat(*smallstring):
    fat_string = ""
    for smallstring in smallstring:
        fat_string += smallstring
    print(fat_string)

string_makefat("Very","", "fat", "", "string") 