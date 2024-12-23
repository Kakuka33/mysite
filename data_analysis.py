import pandas as pd
import matplotlib.pyplot as plt

# ExcelファイルをExcelFileオブジェクトとして読み込む
excel_data = pd.ExcelFile('coffee Orders.xlsx')

# シート名一覧を取得
print(excel_data.sheet_names)

# 必要なシートをデータフレームとして読み込む
orders_df = excel_data.parse('orders')
products_df = excel_data.parse('products')

# OrdersとProductsデータを結合する
merged_df = pd.merge(orders_df, products_df, on="Product ID")

# 日付をdatetime型に変換
merged_df['Ordear Date'] = pd.to_datetime(merged_df['Order Date'])

# 月ごとの売上集計
monthly_sales = merged_df.groupby(merged_df['Order Date'].dt.to_period('M')).sum(numeric_only=True)['Sales']

# 時系列グラフ
plt.figure(figsize=(10,6))
monthly_sales.plot(kind='line', marker='o', title="Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Sales(USD)")
plt.grid()
plt.show()

# コーヒーのタイプ別の売上
coffee_type_sales = merged_df.groupby("Coffee Type_x").sum(numeric_only=True)['Sales']

# 棒グラフ
plt.figure(figsize=(10,6))
coffee_type_sales.sort_values().plot(kind='bar', color='brown', title="Coffee Type Sales")
plt.xlabel("Coffee Type")
plt.ylabel("Sales(USD)")
plt.xticks(rotation=0)
plt.grid(axis='y')
plt.show()

#Month列を作成
merged_df['Month'] = merged_df['Order Date'].dt.to_period('M')

# タイプ別の月次売上
monthly_sales_by_type = merged_df.groupby(['Month','Coffee Type_x']).sum(numeric_only=True)['Sales'].unstack()
plt.figure(figsize=(12,6))
monthly_sales_by_type.plot(kind='line', marker='o', title="Coffee Type Sales by Month")
plt.xlabel("Month")
plt.ylabel("Sales(USD)")
plt.legend(title='Coffee Type', bbox_to_anchor=(1.05,1), loc='upper left')
plt.grid()
plt.tight_layout()
plt.show()

# 国別の売上集計
country_sales = merged_df.groupby('Country').sum(numeric_only=True)['Sales']
# 棒グラフ
plt.figure(figsize=(10,6))
country_sales.sort_values().plot(kind='bar', color='orange', title="Sales by Country")
plt.xlabel('Country')
plt.ylabel('Sales(USD)')
plt.xticks(rotation=45)
plt.grid(axis='y')
plt.show()

# The most profitable coffee
# 利益率の高い商品
top_profit_products = merged_df.groupby('Product ID').mean(numeric_only=True)['Profit'].sort_values(ascending=False).head(10)
plt.figure(figsize=(10,6))
top_profit_products.plot(kind='bar', color='green', title='Ranking of most profitable products')
plt.xlabel('Product ID')
plt.ylabel('Profit(USD)')
plt.xticks(rotation=45)
plt.grid(axis='y')
plt.show()

