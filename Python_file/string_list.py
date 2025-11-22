# print("hii priya")

# data = ["INDIA","USA","UK"]

# OUT = ''.join(data)
# print(OUT)

# data1 = "ABCDEFGH"
# print(len(data1))

# print(data1[2:-1])
# print(data1[::])
# print(data1[::2])
# print(data1[:2])
# print(data1[:])
# print(data1[::-1])  # reverse a string


# palindrom
# palindrome = data1 == data1[::-1]
# palindrome = data1 == data1[::-2]
# print(palindrome)

# out = list(reversed(data1))
# print(out)

# out = ''.join(out)
# print(out)

# out = ''.split(data1)
# print(out)

# print(id(data1))



# lists #

# virat_status = [300,"virat","kohli",36,200,5.8,["batting","bowling","fielding"],None,True,{"spouse":"Anushka","children":2}]

# print(virat_status)

# data = []
# data2 = list("india")
# data3 = "india".split()

# print(data,data2,data3)


# data4 = ["a"]*3
# print(data4)

# countries1 = ["IND","UAE","SL","BAN"]
# countries2 = ["US","UK","AUS","SA"]

# countries1.extend(countries2)
# print(countries1)

# out = countries1 + countries2
# print(out)


# countries1.append("Pak")
# print(countries1)


# countries1 = ["IND","UAE","SL","BAN"]
# print(id(countries1))
# countries1.append("PAK")
# print(id(countries1))

# countries1 = ["IND","UAE","SL","BAN","PAK"]
# print(id(countries1))



# countries1 = ["IND","UAE","SL","BAN"]
# countries2 =countries1
# countries1.append("CHINA")

# print(countries1)
# print(countries2)

# print(id(countries1))
# print(id(countries2))



# countries1 = ["IND","UAE","SL","BAN"]
# countries1.insert(1,"BHU")
# countries1.insert(2,"UK")
# print(countries1)


# modify
# countries1 = ["IND","UAE","CHINA","BAN"]
# countries1[2] = "CHN"
# print(countries1)



countries1 = ['IND', 'UAE', 'SL', 'BAN', 'US', 'UK', 'AUS', 'SA']
countries3 = countries1[:2] + countries1[-2:]
print(countries3)