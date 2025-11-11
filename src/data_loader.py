import pandas as pd

class DataLoader:
    """Load CSV or Excel data files."""
    
    def __init__(self, filepath):
        self.filepath = filepath
    
    def load_csv(self):
        return pd.read_csv(self.filepath)
    
    def load_excel(self):
        return pd.read_excel(self.filepath)
