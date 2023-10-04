list = [80, 25, 80, 95, 6, 4, 98, 0]
unique_list = []
for number in list:
    if number not in unique_list:
        unique_list.append(number)
print(unique_list)
#Dictionaries
customer = {
    "name": "Pavan Balusu",
    "age": 30,
    "is verified": True
}
#to add any thing on dictionaries

output = ""
for x in input:
    output += translate_word.get(x,"!") + ""
print(output)