#import os
import sys
from pathlib import Path
import pandas as pd


def convert_to_muselsl(fname, outdir):
    # Extract EEG data from file
    df = pd.read_csv(fname)
    # Rename columns, Remove null values
    filtered = df.rename(columns = {'eeg_1':'TP9',
                       'eeg_2':'AF7',
                       'eeg_3':'AF8',
                       'eeg_4':'TP10'})[['timestamps', 'TP9', 'AF7', 'AF8', 'TP10']].dropna()
    filtered['Right AUX'] = 0.0
    print(filtered.head(), len(df), len(filtered))
    # TODO : Support ACC, PPG

    # Get absolute filename
    outname = f'{outdir}/{str(Path(fname).name)}'
    filtered.to_csv(outname)

if __name__=="__main__":
    if len(sys.argv) > 1:
        path = Path(sys.argv[1])
    else:
        path = Path("/Users/ganois/muselab/recordings")

    csv_files = []
    if path.exists():
        if path.is_dir():
            csv_files = [str(filepath.absolute()) for filepath in path.rglob('*.csv')]
        elif path.is_file() and path.suffix == ".csv":
            csv_files = [str(path.absolute())]
            
    for f in csv_files:
        convert_to_muselsl(f, './converted')

