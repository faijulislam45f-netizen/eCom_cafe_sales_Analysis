import pandas as pd
import plotly.express as px

df = pd.read_csv('cafe_sales1.csv')
df['Transaction Date'] = pd.to_datetime(df['Transaction Date'], format='%y-%m-%d')
df['Month'] = df['Transaction Date'].dt.to_period('M').astype(str)

# Item wise total revenue
fig1 = px.bar(df.groupby('Item')['Total Spent'].sum().reset_index(), 
              x='Item', y='Total Spent', title='Item Wise Total Revenue')
fig1.write_html('chart1_revenue.html')

# Payment method distribution
fig2 = px.pie(df, names='Payment Method', title='Payment Method Distribution')
fig2.write_html('chart2_payment.html')

# Location wise sales
fig3 = px.bar(df.groupby('Location')['Total Spent'].sum().reset_index(), 
              x='Location', y='Total Spent', title='Location wise Total Sales')
fig3.write_html('chart3_location.html')

# Monthly revenue trend
fig4 = px.line(df.groupby('Month')['Total Spent'].sum().reset_index(), 
               x='Month', y='Total Spent', title='Monthly Revenue Trend')
fig4.write_html('chart4_monthly.html')
print("All Charts Done")
