import os
import pandas as pd

OUTPUT_PATH = 'output'
INPUT_PATH = 'input'


def load_csv(filename: str, sep=',') -> pd.DataFrame:
    file_path = os.path.join(INPUT_PATH, filename)
    if os.path.exists(file_path):
        return pd.read_csv(file_path, sep=sep)
    else:
        return pd.DataFrame()
    
    
def count_artists(df: pd.DataFrame) -> int:
    return len(df['Artist'].unique())


def songs_per_artist(df: pd.DataFrame):
    songs_per_artist_series = df.groupby('Artist')['Track'].count()  # Return a series
    return songs_per_artist_series.to_dict()
    
    
if __name__ == '__main__':
    df = load_csv('WorldHits.csv')
    # breakpoint()
    
    # df.info()  # No null data!
    
    # print(count_artists(df))
    print(songs_per_artist(df))
        
