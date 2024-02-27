import json
with open("todos.json",'r',encoding="utf-8") as file:
    temp = json.load(file)
for i in range(len(temp)):
    td_cell=open(f"todo{i+1}.json",'w',encoding='utf-8')
    json.dump(temp[i],td_cell)
    td_cell.close()
