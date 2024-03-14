import stocks_util
import csv
from datetime import datetime
from datetime import timedelta


def add(file, historical, key):
    file.write(str(stocks_util.get_key(key, historical)))
    file.write(",")

file = "phase3.csv"
output_str = "phase3-o.csv"

stocks = set({})

output = open(output_str, 'w')
csv_file = open(file, 'r');
csv_reader = csv.reader(csv_file, delimiter=',')
count = 0
for row in csv_reader:
    historical = stocks_util.get_stock_at(row[0].strip(), datetime.strptime(row[2].strip(), "%Y-%m-%d") - timedelta(days=1))
    historical2 = stocks_util.get_stock_at(row[0].strip(), datetime.strptime(row[2].strip(), "%Y-%m-%d") + timedelta(days=1))
    if stocks_util.not_valid(historical) or stocks_util.not_valid(historical2):
        print("Invalid")
        stocks.add(row[0])
        continue
    output.write(row[0].strip())
    output.write(",")
    output.write(row[1].strip())
    output.write(",")
    output.write(row[2].strip())
    output.write(",")
    add(output, historical, "open")
    add(output, historical, "close")
    add(output, historical, "high")
    add(output, historical, "low")
    add(output, historical2, "open")
    add(output, historical2, "close")
    add(output, historical2, "high")
    add(output, historical2, "low")
    output.write("\n")
    print(row[0])
    print(count)
    count += 1


csv_file.close();
output.close();

print(len(stocks))
# print(stocks_util.get_market_cap())
