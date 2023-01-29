def arithmetic_arranger(operations: list, showResult: bool = False) -> str:
  
    if len(operations) > 5:
      return "Error: Too many problems."

    firstLine = []
    secondLine = []
    thirdLine = []
    result = []


    #Formatting each line with values given

    for item in range(len(operations)):

        entry = operations[item].split()

        if len(entry[0]) > 4 or len(entry[2]) > 4:
          return "Error: Numbers cannot be more than four digits."
      
        if len(entry[2]) > len(entry[0]):
            secondLine.append("{:<1}{:>{}}".format(entry[1], entry[2], len(entry[2]) + 1))

            firstLine.append("{:>{}}".format(entry[0], len(secondLine[item])))
        else:
            secondLine.append("{:<2}{:>{}}".format(entry[1], entry[2], len(entry[0])))

            firstLine.append("{:>{}}".format(entry[0], len(entry[0]) + 2))

        try:
          if entry[1] == "+":
              operation = int(entry[0]) + int(entry[2])
          elif entry[1] == "-":
              operation = int(entry[0]) - int(entry[2])
          else:
            return "Error: Operator must be '+' or '-'."
        except ValueError:
          return "Error: Numbers must only contain digits."
      
        result.append("{:>{}}".format(str(operation), len(secondLine[item])))



    #Dashes with same length as the biggest line

    for i in range(len(firstLine)):
        if firstLine[i] > secondLine[i]:
            dashes = ""
            for k in range(len(firstLine[i])):
                dashes = dashes + "-"
            thirdLine.append(dashes)
        else:
            dashes = ""
            for k in range(len(secondLine[i])):
                dashes = dashes + "-"
            thirdLine.append(dashes)


    #Output lines

    firstLineOutput = ""

    for k in range(len(firstLine)):
        if k == len(firstLine) - 1:
            firstLineOutput = firstLineOutput + firstLine[k]
        else:
            firstLineOutput = firstLineOutput + firstLine[k] + "    "
    



    secondLineOutput = ""

    for k in range(len(secondLine)):
        if k == len(secondLine) - 1:
            secondLineOutput = secondLineOutput + secondLine[k]
        else:
            secondLineOutput = secondLineOutput + secondLine[k] + "    "



    thirdLineOutput = ""

    for k in range(len(thirdLine)):
        if k == len(thirdLine) - 1:
            thirdLineOutput = thirdLineOutput + thirdLine[k]
        else:
            thirdLineOutput = thirdLineOutput + thirdLine[k] + "    "


      
    #Output without result
  
    arranged_problems = firstLineOutput + "\n" + secondLineOutput + "\n" + thirdLineOutput
    

      
    #Show result if second argument is True

    resultOutput = ""
    
    if showResult == True:
        for k in range(len(result)):
            if k == len(result) - 1:
                resultOutput = resultOutput + result[k]
            else:
                resultOutput = resultOutput + result[k] + "    "

        arranged_problems = arranged_problems + "\n" + resultOutput



    return arranged_problems