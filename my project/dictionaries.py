student_info= {
    "student1": {
        "name" : "Rashik",
        "roll" : "33",
        "class" : "12",
        "section" : "science",
        "number" : "01921856093"
    },
    "student2": {
        "name" : "Tahi",
        "roll" : "23",
        "class" : "10",
        "section" : "science",
        "number" : "01772889734"
    }
}
print(student_info)
print(student_info["student1"])
print(student_info["student1"]["name"])
print(student_info["student2"])
print(student_info["student2"]["name"])

student_info["student2"]["number"]= "123456789"
print(student_info["student2"])
student_info["student2"].update({"section": "arts"})
print(student_info["student2"])
x= student_info["student1"].get("number")
print(x)
print(student_info.values())