with open("E:\\cities.txt", "a+") as city_file:
    for i in range(0, 13):
        print("{0:>2} times 2 is {1:<2}".format(i, (i*2)), file=city_file)
        #cities.append(city.strip('\n'))