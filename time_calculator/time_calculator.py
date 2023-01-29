def add_time(startTime, durationTime, startDay = None):

    #Split strings and change time to 24 hour format

    splitST = startTime.split()
    startHour = int(splitST[0].split(":")[0])
    startMinutes = int(splitST[0].split(":")[1])

    if startHour == 12 and splitST[1] == "AM":
        startHour = 0
    elif startHour == 12 and splitST[1] == "PM":
        startHour = 12
    elif splitST[1] == "PM":
        startHour += 12
    
    

    durationHour = int(durationTime.split(":")[0])
    durationMinutes = int(durationTime.split(":")[1])

    #Time passed

    finalHour = startHour + durationHour
    finalMinutes = startMinutes + durationMinutes
    
    daysPassed = 0

    while True:
        if finalMinutes > 60:
            finalMinutes = finalMinutes - 60
            finalHour += 1
        else:
            break

    while True:
        if finalHour >= 24:
            finalHour -= 24
            daysPassed += 1
        else:
            break

    finalMinutesOtp = ""
    
    if finalMinutes < 10:
        finalMinutesOtp = "0" + str(finalMinutes)
    else:
        finalMinutesOtp = str(finalMinutes)


    #Amount of days passed output

    daysPassedOtp = ""

    if daysPassed == 0:
        daysPassedOtp = ""
    elif daysPassed == 1:
        daysPassedOtp = " (next day)"
    else:
        daysPassedOtp = " (" + str(daysPassed) + " days later)"


    #Change to 12 hour format again
    
    dayHalf = ""

    if finalHour > 12:
        dayHalf = "PM"
        finalHour -= 12
    elif finalHour == 12:
        dayHalf = "PM"
    elif finalHour == 0:
        finalHour = 12
        dayHalf = "AM"
    else:
        dayHalf = "AM"


    #Days of the week

    weekDays = {
        1: "sunday",
        2: "monday",
        3: "tuesday",
        4: "wednesday",
        5: "thursday",
        6: "friday",
        7: "saturday",
        8: "sunday"
    }
    
    finalDay = ""
    startDay = str(startDay).lower()

    for i in range(7):
        if startDay == None:
            finalDay = ""
            break
        if startDay == weekDays[i + 1]:
            finalDayNum = i + 1 + daysPassed

            while True:
                if finalDayNum > 7:
                    finalDayNum -= 7
                else:
                    break

            finalDay = ", " + weekDays[finalDayNum].capitalize()
            break

    
    
    output = str(finalHour) + ":" + finalMinutesOtp + " " + dayHalf + finalDay + daysPassedOtp
    
    return output