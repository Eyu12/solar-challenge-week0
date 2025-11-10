import pandas as pd

class CrossCountryAnalyzer:
    """Combine and analyze cleaned datasets from multiple countries."""
    
    def __init__(self, data_files):
        """
        data_files: dict of {country_name: file_path}
        Example: {'Benin':'benin_cleaned.csv', 'Togo':'togo_cleaned.csv'}
        """
        self.data_files = data_files
        self.combined_df = None

    def load_and_combine(self):
        frames = []
        for country, path in self.data_files.items():
            df = pd.read_csv(path)
            df['Country'] = country
            frames.append(df)
        self.combined_df = pd.concat(frames, ignore_index=True)
        return self.combined_df

    def summarize_metrics(self, columns=['GHI','DNI','DHI']):
        if self.combined_df is None:
            raise ValueError("Data not loaded. Run load_and_combine() first.")
        summary = self.combined_df.groupby('Country')[columns].agg(['mean','std','min','max'])
        return summary
