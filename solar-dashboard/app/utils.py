import pandas as pd
import plotly.express as px

def load_country_data(file_path):
    return pd.read_csv(file_path)

def boxplot_ghi(df, country):
    fig = px.box(df, y='GHI', title=f"GHI Distribution for {country}")
    return fig

def top_regions_table(df):
    if 'Region' not in df.columns:
        df['Region'] = 'Unknown'
    top_regions = df.groupby('Region')['GHI'].mean().sort_values(ascending=False).head(10)
    return top_regions.reset_index()
