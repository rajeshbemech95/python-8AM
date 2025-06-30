# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt

# df = pd.read_csv("monthly-writing-paper-sales.csv")
# # print(df)
# print(df.head())

# df.set_index('Month', inplace=True)
# df['Sales_MA3'] = df['Sales'].rolling(window=3).mean()
# df['Pct_Change'] = df['Sales'].pct_change() * 100

# print(df.tail())

# plt.figure(figsize=(10, 5))
# plt.plot(df.index, df['Sales'], label='Monthly Sales', marker='o')
# plt.plot(df.index, df['Sales_MA3'], label='3-Month MA', linestyle='--')
# plt.title('Writing Paper Sales')
# plt.xlabel('Month')
# plt.ylabel('Sales Units')
# plt.legend()
# plt.grid(True)
# plt.tight_layout()
# plt.show()

import pandas as pd
import dash
from dash import html, dcc
import plotly.express as px

# Load and process data
df = pd.read_csv("monthly-writing-paper-sales.csv", parse_dates=["Month"])
df.set_index("Month", inplace=True)
df["Sales_MA3"] = df["Sales"].rolling(3).mean()
df["Pct_Change"] = df["Sales"].pct_change() * 100

# Create Plotly figure
fig = px.line(df.reset_index(), x="Month", y=["Sales", "Sales_MA3"],
              labels={"value": "Sales", "variable": "Type"},
              title="Writing Paper Sales & 3-Month Avg")

# Dash app layout
app = dash.Dash(__name__)
app.layout = html.Div([
    html.H1("Sales Dashboard", style={"textAlign": "center"}),
    dcc.Graph(figure=fig)
])

# Run the app
if __name__ == "__main__":
    app.run_server(debug=True)
