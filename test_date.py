import json

with open(r"C:\Users\HP\Desktop\test.json", "r") as read_file:
    data = json.load(read_file)
    print(data)

cast_query='INSERT INTO TABLE1 SELECT '
ddl_query='CREATE TABLE TABLE_NAME ('

for i in data:
    ddl_query = ddl_query + str(i['name']).upper() + ' ' + str(i['type']).upper() + ', '
    cast_query = cast_query + '(CAST ' + str(i['name']).upper() + ' AS ' + str(i['type']).upper() + ') AS ' + str(i['name']).upper() + ', '

ddl_query=ddl_query[:len(ddl_query)-2] + ');'
cast_query=cast_query[:len(cast_query)-2] + ' FROM TABLE2;'

print(cast_query)
print(ddl_query)