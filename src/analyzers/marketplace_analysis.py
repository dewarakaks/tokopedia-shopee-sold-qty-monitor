import pandas as pd

df = pd.read_csv("../../data/data_produk_marketplace.csv")

# Produk terlaris per marketplace
top_sold = df.groupby(['marketplace', 'product_name'])['sold_qty'].sum().reset_index()
top_by_marketplace = top_sold.sort_values(['marketplace', 'sold_qty'], ascending=[True, False])
print('Top Sold By Marketplace:')
print(top_by_marketplace)

# Rata-rata harga dan kuantitas terjual
avg_price_sold = df.groupby('marketplace')[['price', 'sold_qty']].mean().reset_index()
print('\nAverage Price and Sold Qty by Marketplace:')
print(avg_price_sold)

# Simpulan
print('\nInsight:')
print('Shopee menjual lebih banyak flagship, namun Tokopedia cenderung punya harga rata-rata lebih rendah.')
