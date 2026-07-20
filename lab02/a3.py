# mean, variance
import pandas as pan
import numpy as num
import time as t

def find_mean(given_list):
    sum=0
    for i in given_list:
        sum+= i
    return sum / len(given_list)

def find_variance(given_list):
    mean = find_mean(given_list)
    sum = 0
    for i in given_list:
        sum += (i-mean) ** 2
    return sum/len(given_list)

def calc_time(fn, parameter):
    total = 0

    for i in range(10):
        start = t.perf_counter()
        fn(parameter)
        end = t.perf_counter()
        total += (end - start)
    
    return total / 10

def loss(value):
    if value < 0:
        return True
    elif value > 0:
        return False
    
def probability_loss(given_list):
    count_loss = 0
    for i in given_list:
        if loss(i) == True:
            count_loss += 1
    
    return count_loss/len(given_list)
        
def probability_profit(given_list):
    count_profit = 0
    for i in given_list:
        if loss(i) == False:
            count_profit+=1
    return count_profit/len(given_list)


def main():
    stock_price = pan.read_excel("Lab_Session_Data.xlsx", sheet_name = "IRCTC Stock Price")
    price = stock_price["Price"]
    data_wednesday = stock_price[stock_price["Day"]=="Wed"]
    numpy_mean_Wednesday = num.mean(data_wednesday["Price"])
    data_April = stock_price[stock_price["Month"]=="Apr"]
    numpy_mean_April = num.mean(data_April["Price"])

    chg = stock_price["Chg%"]
    wed_profit = probability_profit(data_wednesday["Chg%"]) * len(data_wednesday) / len(stock_price)

    numpy_mean = num.mean(price)
    normal_mean = find_mean(price)
    numpy_variance = num.var(price)
    normal_variance = find_variance(price)

    print("Time taken by numpy to calculate mean: ", calc_time(num.mean, price))
    print("Time taken by function to calculate mean: ", calc_time(find_mean, price))
    print("Time taken by numpy to calculate variance: ", calc_time(num.var, price))
    print("Time taken by function to calculate variance: ",calc_time(find_variance, price))

    print("Wednesday mean: ", numpy_mean_Wednesday, "; Population mean: ", numpy_mean)
    print("April mean: ", numpy_mean_April, "; Population mean: ", numpy_mean)
    print("Prob of loss of chg: ", probability_loss(chg))
    print("Prob of making profit on wednesday: ", wed_profit)
    print("Conditional prob of profit given it is on Wednesday: ", probability_profit(data_wednesday["Chg%"]))

main()