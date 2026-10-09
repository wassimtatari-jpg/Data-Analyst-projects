import pandas as pd
import matplotlib.pyplot as plt

commerce_dt=pd.read_csv("ecommerce_sales.csv")
print(commerce_dt.columns)

print(commerce_dt.head(50))

regular_order=commerce_dt[
    (commerce_dt["year"]>=2020)&
    (commerce_dt["year"]<=2022)&
    (commerce_dt["order_type"]=="Regular")
]
plt.bar(regular_order["order_id"],regular_order["price"])
plt.xlabel("Order ID")
plt.ylabel("Prices")
plt.title("Regular Order Situation")
plt.show()
most_commen_price=regular_order["price"].value_counts().index[0]
print(f"Most common price is {most_commen_price}")
high_price_order=len(regular_order[regular_order["price"]>100])
plt.bar("High Price Order",high_price_order)
plt.show()
print(high_price_order)
count_order=commerce_dt["category"].value_counts()
plt.bar(count_order.index,count_order.values)
plt.ylabel("Count")
plt.xlabel("Category")
plt.title("Number of ordres by Category")
plt.show()
order_year=commerce_dt["year"].value_counts()
plt.bar(order_year.index,order_year.values)
plt.title("Numbers of ordres by Year")
plt.xlabel("Years")
plt.ylabel("count")
plt.show()
mid_sales=commerce_dt.groupby("category")["price"].mean()
plt.bar(mid_sales.index,mid_sales.values)
plt.xlabel("Category")
plt.ylabel("Average")
plt.title("Mean prices by Category")
plt.show()
price_order=commerce_dt[["order_id","price"]]
plt.bar(price_order["order_id"],price_order["price"])
plt.xlabel("Order Id")
plt.ylabel("Price")
plt.title("Price of each order")
plt.show()
order_count_type=commerce_dt["order_type"].value_counts()
plt.bar(order_count_type.index,order_count_type.values)
plt.title("Numbers of order By Type")
plt.ylabel("Count")
plt.xlabel("Type")
plt.show()
order_result=commerce_dt["result"].value_counts()
plt.bar(order_result.index,order_result.values)
plt.title("Numbers of order by Result")
plt.ylabel("Count")
plt.xlabel("Result")
plt.show()




