from dataclasses import replace

x = (input(""))

vocal = ["a","i","u","e","o"]
result = ""

for i in x.lower():
    if i not in vocal:
        result = result + i 

print("Result : ", result)