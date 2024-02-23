import pickle


def load_dict(path):
    with open(path, 'rb') as file:
        loaded_dict = pickle.load(file)
    return loaded_dict

def save_list_to_file(lst, output_file):
    with open(output_file, 'w', encoding='utf-8') as f:
        for item in lst:
            f.write(f"{item}\n")

def fancyList(liste):
    string = ""
    for l in liste:
        print(l)
        string = string + l + ","
    string = string[0:-1]
    return string
Months = {
    "01": "January",
    "02": "February",
    "03": "March",
    "04": "April",
    "05": "May",
    "06": "June",
    "07": "July",
    "08": "August",
    "09": "September",
    "10": "October",
    "11": "November",
    "12": "December"
}
Days = {
    "01": "1st",
    "02": "2nd",
    "03": "3rd",
    "04": "4th",
    "05": "5th",
    "06": "6th",
    "07": "7th",
    "08": "8th",
    "09": "9th",
    "10": "10th",
    "11": "11th",
    "12": "12th",
    "13": "13th",
    "14": "14th",
    "15": "15th",
    "16": "16th",
    "17": "17th",
    "18": "18th",
    "19": "19th",
    "20": "20th",
    "21": "21st",
    "22": "22nd",
    "23": "23rd",
    "24": "24th",
    "25": "25th",
    "26": "26th",
    "27": "27th",
    "28": "28th",
    "29": "29th",
    "30": "30th",
    "31": "31st",
}
    
dict = load_dict("timeline_dict.txt")



print("Timeline of events stored on Wikipedia")
print("Please insert search tags. Each word is one tag")
tags = str(input("Tags: ")).split(" ")
    
liste = []
for element in dict.keys():
    printed = False
    
    for tag in tags:
        for i in range(len(dict[element])):
            if str(dict[element][i]).lower().find(str(tag).lower()) != -1:
                if not printed:
                    E = element.split(" ")
                    print(Months[E[1]] + " " + Days[E[2]] + " " + E[0] + " - " + dict[element][i])
                    liste.append(Months[E[1]] + " " + Days[E[2]] + " " + E[0] + " - " + dict[element][i])
                    printed = True
print("Save to file? (y / n)")
shouldSaveToFile = input()
if shouldSaveToFile.lower() == "y":
    save_list_to_file(liste,"../results/result-"+fancyList(tags)+".txt")
print("Done")