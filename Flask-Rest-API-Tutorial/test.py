import requests

BASE = "http://127.0.0.1:5000/"

data = [{"likes":10, "name":"Kevin","views":4211},
        {"likes":42, "name":"Matt","views":55134},
        {"likes":51, "name":"Henry","views":150}]

#### PUT
# for i in range(len(data)):
#     response = requests.put(BASE + "/video/" + str(i), data[i])
#     print("PERFORMING PUT: ", response.json())    

#### DELETE
# input()
# response = requests.delete(BASE + "/video/0")
# print("PERFOMING DELETE: ", response) #delete isnt returning anything except a status code


#### GET
# response = requests.get(BASE + "video/5")
# print("PERFORMING GET: ", response.json())

# response = requests.get(BASE + "helloworld/kevin")
# response = requests.put(BASE + "/video/2", {"likes":10, "name":"Kevin","views":1000}) # how to send additional data or a form
# print("PERFORMING DELETE: ", response.json())

#### UPDATE
response = requests.patch(BASE + "video/2", {"views":9999})
print("PERFORMING UPDATE: ", response.json())

