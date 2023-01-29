class Category:

  def __init__(self, name):
    self.name = name
    self.ledger = []
    self.total = 0
    self.totalWithdraws = 0

  def __str__(self):
    output = self.name.center(30, "*")

    for i in range(len(self.ledger)):
      if len(self.ledger[i]["description"]) > 23:
        rlen = 7
      else:
        rlen = 30 - len(self.ledger[i]["description"])

      output += "\n{:.23}{:>{}}".format(self.ledger[i]["description"], "{:.2f}".format(self.ledger[i]["amount"]), rlen)

    output += "\n" + "Total: " + "{:.2f}".format(self.total)
      
    

    return output

  def deposit(self, amount, description = ""):
    listobj = {"amount": float(amount), "description": description}
    self.ledger.append(listobj)

    self.total += listobj["amount"]



  def withdraw(self, amount, description = ""):
    listobj = {"amount": float(amount * -1), "description": description}

    if self.check_funds(amount) == True:
      self.ledger.append(listobj)
      self.total += listobj["amount"]

      self.totalWithdraws += amount

      return True
    else:
      return False



  def get_balance(self):
    return self.total



  def transfer(self, amount, category):
    withdraw = self.withdraw(amount, "Transfer to " + category.name)

    category.deposit(amount, "Transfer from " + self.name)
    
    if withdraw == True:
      return True
    else:
      return False


  def check_funds(self, amount):
    if amount > self.total:
      return False
    else:
      return True
    




def create_spend_chart(categories):
  
  itemsPercen = []
  totalValue = 0

  for item in categories:
    totalValue += item.totalWithdraws
  for item in categories:
    percen = (100 * item.totalWithdraws) / totalValue

    if percen >= 0 and percen < 10:
      percen = 0
    elif percen >= 10 and percen < 20:
      percen = 10
    elif percen >= 20 and percen < 30:
      percen = 20
    elif percen >= 30 and percen < 40:
      percen = 30
    elif percen >= 40 and percen < 50:
      percen = 40
    elif percen >= 50 and percen < 60:
      percen = 50
    elif percen >= 60 and percen < 70:
      percen = 60
    elif percen >= 70 and percen < 80:
      percen = 70
    elif percen >= 80 and percen < 90:
      percen = 80
    elif percen >= 90 and percen < 100:
      percen = 90
    else:
      percen = 100

    itemsPercen.append(percen)
    

  line1 = "100|"
  line2 = " 90|"
  line3 = " 80|"
  line4 = " 70|"
  line5 = " 60|"
  line6 = " 50|"
  line7 = " 40|"
  line8 = " 30|"
  line9 = " 20|"
  line10 = " 10|"
  line11 = "  0|"
  
  dashes = "    "

  for i in range(len(categories)):
    if itemsPercen[i] == 100:
      line1 += " o "
      line2 += " o "
      line3 += " o "
      line4 += " o "
      line5 += " o "
      line6 += " o "
      line7 += " o "
      line8 += " o "
      line9 += " o "
      line10 += " o "
      line11 += " o "
      
      dashes += "---"

      continue
    else:
      line1 += "   "
    
    if itemsPercen[i] == 90:
      line2 += " o "
      line3 += " o "
      line4 += " o "
      line5 += " o "
      line6 += " o "
      line7 += " o "
      line8 += " o "
      line9 += " o "
      line10 += " o "
      line11 += " o "
      
      dashes += "---"

      continue
    else:
      line2 += "   "

    if itemsPercen[i] == 80:
      line3 += " o "
      line4 += " o "
      line5 += " o "
      line6 += " o "
      line7 += " o "
      line8 += " o "
      line9 += " o "
      line10 += " o "
      line11 += " o "
      
      dashes += "---"

      continue
    else:
      line3 += "   "

    if itemsPercen[i] == 70:
      line4 += " o "
      line5 += " o "
      line6 += " o "
      line7 += " o "
      line8 += " o "
      line9 += " o "
      line10 += " o "
      line11 += " o "
      
      dashes += "---"

      continue
    else:
      line4 += "   "

    if itemsPercen[i] == 60:
      line5 += " o "
      line6 += " o "
      line7 += " o "
      line8 += " o "
      line9 += " o "
      line10 += " o "
      line11 += " o "
      
      dashes += "---"

      continue
    else:
      line5 += "   "

    if itemsPercen[i] == 50:
      line6 += " o "
      line7 += " o "
      line8 += " o "
      line9 += " o "
      line10 += " o "
      line11 += " o "
      
      dashes += "---"

      continue
    else:
      line6 += "   "

    if itemsPercen[i] == 40:
      line7 += " o "
      line8 += " o "
      line9 += " o "
      line10 += " o "
      line11 += " o "
      
      dashes += "---"

      continue
    else:
      line7 += "   "

    if itemsPercen[i] == 30:
      line8 += " o "
      line9 += " o "
      line10 += " o "
      line11 += " o "
      
      dashes += "---"

      continue
    else:
      line8 += "   "

    if itemsPercen[i] == 20:
      line9 += " o "
      line10 += " o "
      line11 += " o "
      
      dashes += "---"

      continue
    else:
      line9 += "   "

    if itemsPercen[i] == 10:
      line10 += " o "
      line11 += " o "
      
      dashes += "---"

      continue
    else:
      line10 += "   "

    if itemsPercen[i] == 0:
      line11 += " o "
      
      dashes += "---"

      continue
    else:
      line11 += "   "



  chart = "Percentage spent by category" + "\n" + line1 + " \n" + line2 + " \n" + line3 + " \n" + line4 + " \n" + line5 + " \n" + line6 + " \n" + line7 + " \n" + line8 + " \n" + line9 + " \n" + line10 + " \n" + line11 + " \n" + dashes + "-"

  biggest = 0
  finalLines = []

  for item in categories:
    if len(item.name) > biggest:
      biggest = len(item.name)
  
  for i in range(biggest):
    finalLines.append("\n    ")

    for item in categories:
      try:
        finalLines[i] += " " + item.name[i] + " "
      except:
        finalLines[i] += "   "

    chart += finalLines[i] + " "

  return chart