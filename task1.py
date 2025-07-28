dict={
    "alice": 30,
    "yash": 40,
}
name=input("enter the name of student you want to know marks ")
if name in dict:
    print(f"{name}'s marks is : {dict[name]}")
else:
    print("student not found")




