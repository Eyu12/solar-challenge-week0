class DataCleaner:
    """Perform basic cleaning like missing value handling."""
    
    def __init__(self, df):
        self.df = df
    
    def drop_missing(self):
        self.df = self.df.dropna()
        return self.df
    
    def fill_missing(self, column, value):
        self.df[column] = self.df[column].fillna(value)
        return self.df
