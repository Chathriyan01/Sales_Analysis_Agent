import plotly.express as px

def sales_over_time(df):
    return px.line(df, x="date", y="sales", title="Sales Over Time", markers=True)

def sales_by_region(df):
    return px.bar(df, x="region", y="sales", title="Sales by Region", color="region")

def category_distribution(df):
    return px.pie(df, names="category", title="Category Contribution")