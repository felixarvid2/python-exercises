x = 10
y = 5
num = [1, 2, 3, 4, 5]


print(num)


ids = [1, 2, 3]
todo = {"id": 1, "task": "chilla hela dagen"}
task = {"id": 1, "task": "chilla hela dagen"}
todos = [
    {"id": 1, "task": "chilla hela dagen"},
    {"id": 2, "task": "åka tåg"}
    ]

print("saker jag behöver göra:\n")
for todo in todos:
    print(f"{todo["id"]}. {todo["task"]}")