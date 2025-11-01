from datetime  import datetime 

weather = {}

while True :
    city = input(" your city or done to calculate : ")
    if city.lower() == 'done' :
        break 
    temperature = int(input(" your temperature : "))
    w_type = input(" weather type : ")
    weather[city] = {"temperature" : temperature , "type" : w_type}     


if weather :
    max_city = max( weather, key = lambda x : weather[x]["temperature"])  
    min_city = min(weather, key = lambda x : weather[x]["temperature"])  
    total_city = len(weather)
    sum_tp = sum( item["temperature"] for item in weather.values())

now = datetime.now()
timestamp = now.strftime("%Y-%m-%d %H:%M:%S")    # helps to print the time clearly and in readible way !

with open("weather.txt", "a") as f :
    for item,day in weather.items() :
        f.write(f"{item} with temperature : {day['temperature']} and a type of : {day['type']} \n")

    f.write("\n---------------------------\n")
    f.write(" 🌤 WEATHER SUMMARY :\n")                 # stay turned for v 4 that handle more errors
    f.write("\n-------------------------\n")
    f.write(f" the date and time : {timestamp}\n")
    f.write(f" hotest city : {max_city} \n")
    f.write(f" coldest city : {min_city}\n")
    f.write(f" average temperature : {round(sum_tp / total_city,2)} °C \n")
    f.write(f" number of cities : {total_city} \n")
    f.write("\n---------------------------\n\n")
