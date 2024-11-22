sample_dictionary={
    "name":"Henry",
    "age":10,
    "location":"england"
    }
print(sample_dictionary)
print(sample_dictionary["age"])
print(sample_dictionary.keys())
print(sample_dictionary.values())
for key in sample_dictionary.keys():
    print(key,sample_dictionary[key])
if "location" in sample_dictionary:
    print(sample_dictionary["location"])
else:
    print("key doesn't exist")
sample_dictionary["profession"]="gaming"
print(sample_dictionary)
sample_dictionary["marks"]=["maths:99.99999999999","french:5","english:80","science:90","computing:99999999999999999999999999999999999999999999999999999999999999999999999999999999999"]
print(sample_dictionary)
classroom={
    "Frankie":{
    "age":11,
    "marks":["english:70","french:70","computing:70"]
    },
    "henry":{
        "age":10,
        "marks":["maths:99.99999999999","french:5","english:80","science:90","computing:99999999999999999999999999999999999999999999999999999999999999999999999999999999999"]
    }
    }
print(classroom.keys())
print(classroom.values())