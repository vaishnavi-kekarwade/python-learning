#key : value
#simple example
student ={
    "name": "navi",
    "age" :21,
    "course" : "python"
}
print(student)

# to creating dictionary
student ={"name":"navi","age": 21}
print(student)

# Accessing values
print(student["name"])

#adding andupdating values

student["age"] = 21 #update
student["city"] = "Nagpur" #add new one
print(student)

# removing items
student.pop("city")
print(student)


info ={
    "key" :"value",
    "name":"vaishnavi",
    "learning":"coding",
    "age" :21,
    "is_adult":True,
    "marks" :98.1

}
print(info)

dict ={
    "name": "vaishnavi",
    "subjects":["python","C","java"],
    "topics" :("dictonary","set"),
    "age" :21,
    "is_adult" :True,
    "marks": 65.3

}
print(type(dict)) 
#dictionary is mutable , unordered, do not allow duplicate keys

null_dict ={}
print(null_dict)
#nested dictionary
student = {
    "name" : "vaishnavi kekarwade",
    "subjects" :{
        "problem solving":50,
        "story telling" : 60,
        "communication":70
    }
}
print(student["subjects"]["problem solving"])
print(len(student.keys()))
print(list(student.values()))
print(student.items()) # in tupleform
print(list(student.items()))
pairs=list(student.items())
print(pairs[0])
print(student["name"])
print(student.get("name"))
#passing new dict

new_dict = {"city" : "nagpur", "age":21,"name": "navi"}
student.update(new_dict)
print(student)

#dictionry methods
#student.key() # all keys
#student.values()#all values
#student.items()#key  value pairs

collection ={1,2,3,3,3,4,"vaishnavi", "work"} # set is collection of the unorderd itms each elemnent is the set must be unique and immutable


print(collection)
print(type(collection))
print(len(collection)) #total number of items 
collection ={}#empty dictionary
print(type(collection))

collection = set() #empty set; syntax
print(type(collection))

#set methods sets is mutable; and set elements is immuatable
collection.add(1)
collection.add(2)
collection.remove(1)
collection.add("vaishnavikekarwade")
collection.add((1,2,3))
collection.clear()
#collection.pop()
print(len(collection))

set1 ={1,2,3}
set2 = {2,3,4}
print(set1.union(set2)) #{1,2,3,4}
print(set1)
print(set2)

#intersction commonsets
print(set.intersection(set2)) #3
print(set1)
print(set2)
subjects ={
    "python","java","c++","python","javascript","java",
    "python","java","c++","c"
}
print(subjects)

marks={}

x=int(input("enter phy:"))
marks.update({"phy" :x})

x=int(input("enter math:"))
marks.update({"maths" :x})

x=int(input("enter phy:"))
marks.update({"chem":x})

print(marks)

values ={9,9.25}
print(values)

