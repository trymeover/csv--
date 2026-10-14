import csv
header=["姓名","语文","数学","英语"]
data=[["小明","88","92","76"],
      ["小红","","92","76"],
      ["小纲","77","","82"],
      ["小李","91","89",""],
      ["小强","65","78","70"]]
with open("stu.csv",mode="w",encoding="utf-8",newline="")as f:
    writer=csv.writer(f)
    writer.writerow(header)
    writer.writerows(data)
