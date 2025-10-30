def average(tem) :
    if len(tem) == 0 :
        return None
    else :
        return round(sum(tem.values()) / len(tem),2)

temperatures = {}

while True :
    temp = input("the day of the week or 'done' to cal : ") 
    if temp.lower() == 'done' :
        break
    number = int(input("your temprature : "))
    temperatures[temp] = number

max_day = max(temperatures, key = temperatures.get)    
min_day = min( temperatures, key = temperatures.get)
avg = average(temperatures)

with open("temperatures.txt", "w") as f :
    for temp, number in temperatures.items():
        f.write(f"{temp}: {number}°C\n")


print(" most hot day : ", max_day)     
print("most cold day : ",min_day) 
print("average tempurature : ",avg)  
print("Data saved to 'temperatures.txt'.")
