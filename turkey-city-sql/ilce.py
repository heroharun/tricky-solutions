import requests

# Make the request to the API
response = requests.get("https://turkiyeapi.herokuapp.com/api/v1/provinces")
data = response.json()

# Extract the required information
cities = []
counties = []
j=1
for province in data["data"]:
    cityCode  = j
    j += 1
    city = {
        "name": province["name"],
        "code": cityCode,
        "isMetropolitan": province["isMetropolitan"],
        "region": province["region"]
    }
    cities.append(city)
    i = 0
    for district in province["districts"]:
        i += 1
     
        if(i < 10 and cityCode < 10):
            cccc = f'0{cityCode}0{i}'
        elif(i < 10 and cityCode >= 10):
            cccc = f'{cityCode}0{i}'
        elif(i >= 10 and cityCode < 10):
            cccc = f'0{cityCode}{i}'
        else:
            cccc =  f'{cityCode}{i}'

        county = {
            "name": district["name"],
            "code": cccc,
            "cityCode": cityCode

        }
        counties.append(county)
       

# Save cities to a text file
with open("cities.txt", "w") as file:
    for city in cities:
        file.write(f"{city['name']}, {city['code']}, {city['isMetropolitan']}, {city['region']}\n")

# Save counties to a text file
with open("counties.txt", "w") as file:
    for county in counties:
        file.write(f"{county['code']}, {county['cityCode']}, {county['name']} \n")