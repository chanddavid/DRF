import json
import requests




def Get(id=None):
    URL='http://127.0.0.1:8000/get_api/'
    data={}
    if id is not None:
        data={'id':id}
    json_data=json.dumps(data)
    r=requests.get(url=URL,data=json_data,headers={'content-type':'application/json'})
    final=r.json()
    print(final)

Get(30)

def Post():
    URL='http://127.0.0.1:8000/get_api/'
    data={
        'name':'hari',
        'roll':223,
        'city':'tkp'
    }
    json_data=json.dumps(data)
    r=requests.post(url=URL,data=json_data,headers={'content-type':'application/json'})
    final=r.json()
    print(final['value'])

# Post()


def Put(id):
    URL='http://127.0.0.1:8000/get_api/'
    data={
        'id':id,
        'name':'harihari',
        'roll':111,
        'city':'ktm'
    }
    json_data=json.dumps(data)
    r=requests.put(url=URL,data=json_data,headers={'content-type':'application/json'})
    final=r.json()
    print(final)

# Put(31)


def Patch(id):
    URL='http://127.0.0.1:8000/get_api/'
    data={
        'id':id,
        'name':'hari',
        'roll':111,
        'city':'ktm'
    }
    json_data=json.dumps(data)
    r=requests.patch(url=URL,data=json_data,headers={'content-type':'application/json'})
    final=r.json()
    print(final)

# Patch(31)

def Delete(id):
    URL='http://127.0.0.1:8000/get_api/{id}'
    data={'id':id}
    json_data=json.dumps(data)
    r=requests.delete(url=URL,data=json_data,headers={'content-type':'application/json'})
    final=r.json()
    print(final)

# Delete(31)