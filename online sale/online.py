import pandas as pd

import matplotlib.pyplot as plt


sales=pd.read_csv("online_sales.csv",sep=";")

print(sales.head(5))
print(sales.columns)
sales.info()

sales_2021_2022=sales[
    (sales['year']>=2021)&
    (sales["year"]<=2022)
]
print("Total sales 2021-2022")
print(sales_2021_2022)
print("-"*30)
electronics_sales=sales[sales["category"]=='Electronics']
print("Electronics sales")
print(electronics_sales)
print("-"*30)
order_price=sales[sales['price']>150]
print("order biger than 150")
print(order_price)
print("-"*30)
sales_2021=sales[
    (sales["year"]==2021)&
    (sales["price"]>100)
]
print("Sales 2021 and biger than 100")
print(sales_2021)
print("-"*30)

sales["total_sales"]=sales['quantity']*sales["price"]
print("Total sales")

print(sales["total_sales"].sum())
print("-"*30)

total_sales_cat=sales.groupby("category")['total_sales'].sum()
print("Total sales by category")
print(total_sales_cat)
print("-"*30)

mean_sales=sales.groupby("category")["total_sales"].mean()
print("Mean sales")
print(mean_sales)
print("-"*30)
mean_sales_pro=sales["price"].mean()
print("Mean product price")
print(mean_sales_pro)
print("-"*30)
category_order_count=sales['category'].value_counts()
print("Sales Details category ")
print(category_order_count)
print("-"*30)
high_price=sales['price'].max()
high_product=sales.loc[sales['price']==high_price,"product"]
print("High product price")
print(high_product)
print("-"*30)
sales_category=sales["category"].value_counts()
plt.bar(sales_category.index,sales_category.values)
plt.title("Total sales by category")
plt.xlabel("Category")
plt.ylabel("Count")
plt.show()
print(sales_category)
print(sales_category.index)
print(sales_category.values)
plt.bar(total_sales_cat.index,total_sales_cat.values)
plt.title("Total sales")
plt.xlabel("Category")
plt.ylabel("Total")
plt.show()
total_sales_year=sales.groupby("year")['total_sales'].sum()
plt.bar(total_sales_year.index,total_sales_year.values)
plt.xticks(total_sales_year.index)
plt.title("Total sales by year")
plt.ylabel("total sales")
plt.xlabel("Year")
plt.show()