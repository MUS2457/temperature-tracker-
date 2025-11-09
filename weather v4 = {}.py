from datetime import datetime
import json

weather = {}
weather_type = {}
count = 0

while True :
    
    city = input(" the name of your city and after 'done' to calculate or 'exit' to exit the program : ")
    if city.lower() == 'exit' :
        print(" the program is closed")
        break
    if city.lower() == 'done' :
        break
    if city == "" :
        print("city name can't be empty")
        continue

    while True :  
        try:
            temperature = int(input("Enter temperature : "))
            break   
        except ValueError:
            print("Please enter a valid number!")

    w_type = input(" weather type : ")

    weather[city]= {"temperature" : temperature ,"type" : w_type}

now = datetime.now()
timestamp = now.strftime("%Y-%m-%d %H:%M:%S")    
  

if weather :
    max_city = max(weather, key = lambda w : weather[w]["temperature"])
    min_city = min(weather, key = lambda w : weather[w]["temperature"] )
    tl_city = len(weather)
    sum_tp = sum([tp["temperature"] for tp in weather.values()])
    average = round( sum_tp / tl_city ,2)

for item,info in weather.items() :
    typ = info["type"]
    tem = info["temperature"]
    if typ in weather_type :
        weather_type[typ] += 1
    else :
        weather_type[typ]  = 1    


data = { "hotest city" : max_city , "coldest city" : min_city,
        "total city" : tl_city, "sum of temperature" : sum_tp,
         "average" : average,  "weather type count" : weather_type
}

with open("weather v4.txt", "w") as f :
    for item,day in weather.items() :
        f.write(f"{item} with temperature : {day['temperature']} and a type of : {day['type']} \n")

    f.write("\n---------------------------\n")
    f.write(" 🌤 WEATHER SUMMARY :\n")                 
    f.write("\n-------------------------\n")
    f.write(f" the date and time : {timestamp}\n")
    f.write(f" hotest city : {max_city} \n")
    f.write(f" coldest city : {min_city}\n")
    f.write(f" average temperature : {average} °C \n")
    f.write(f" number of cities : {tl_city} \n")
    for sun, rain in weather_type.items() :
        print(f" {sun} : {rain}  ")
    f.write("\n---------------------------\n\n")

with open("weather v4.json","w") as v :
    json.dump(data,v,indent=4)

print(json.dumps(data,indent=4))    


