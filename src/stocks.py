import csv
import matplotlib.pyplot as plt


def get_before_val(row, before_key, row_idx=2):
    if before_key == "open":
        row_idx += 1;
    elif before_key == "close":
        row_idx += 2;
    elif before_key == "high":
        row_idx += 3;
    elif before_key == "low":
        row_idx += 4;
    else:
        print("Invalid key")
    return row[row_idx];

def get_after_val(row, after_key):
    return get_before_val(row, after_key, 6);

def propability_in_range(distribution, percent, above):
    total_prop = 0 

    for key in distribution:
        if above:
            if key < percent:
                continue
            total_prop += distribution[key]
        else:
            if key > percent:
                continue
            total_prop += distribution[key]

    return total_prop

def value_in_range(distribution, percent, above):
    total_val = 0

    for key in distribution:
        if above:
            if key < percent:
                continue
            total_val += key * distribution[key]
        else:
            if key > percent:
                continue
            total_val -= key * distribution[key]

    return abs(total_val)

def calc_graph(phases, before_key, after_key):
    distribution = {}
    file = open("data.csv", "r")
    csv_reader = csv.reader(file, delimiter=',')
    sum = 0

    for row in csv_reader:
        if row[1] in phases:
            low = float(get_before_val(row, "low"))
            close = float(get_before_val(row, "close"))
            if low > close:
                print("low")
                print(low)
                print("close")
                print(close)
            low = float(get_after_val(row, "low"))
            close = float(get_after_val(row, "close"))
            if low > close:
                print("low")
                print(low)
                print("close")
                print(close)
            before_val = float(get_before_val(row, before_key))
            after_val = float(get_after_val(row, after_key))
            if float(before_val) > 10:
                continue

            key = after_val / before_val - 1;
            key *= 100
            key = int(key)

            if key in distribution:
                distribution[key] += 1
            else:
                distribution[key] = 1;
            sum += 1

        
    print(sum)
   
    for key in distribution:
        distribution[key] /= sum;
    
    total = 0
    
    return distribution;

data = calc_graph(['phase3'], 'high', 'low')
print(value_in_range(data, -5, False))
amounts = data.keys()
props = data.values()

plt.bar(amounts, props)
plt.show()


