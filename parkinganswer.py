vehicle = input("What kind of vehicle?")
timein = input("Time in:")
timeout = input("Time out:")

time_in_ans = int(timein)
time_out_ans = int(timeout)

if(time_in_ans > 0 and time_in_ans < 25 and time_out_ans > 0 and time_out_ans < 25):
    if(time_in_ans < time_out_ans):
        total_time = time_out_ans - time_in_ans
        if(vehicle == "Car"):
            if(total_time <= 3):
                total = 30
            elif(total_time > 3):
                total = (total_time - 3)*5
                total += 30
        elif(vehicle == "Motorcycle"):
            if(total_time <= 3):
                total = 20
            elif(total_time > 3):
                total = (total_time - 3)*5
                total += 20
        elif(vehicle == "Trucks"):
            if(total_time <= 2):
                total = 40
            elif(total_time > 2):
                total = (total_time - 2)*10
                total += 40
        
        print("The total nummber of hours you spent is {} and the amount you need to pay is {}".format(total_time, total))

    else:
        print("Invalid Time!!")
else:
    print("Invalid Time!!")