import pandas as pd
import os


def dump_to_xlsx(results, file='./output.xlsx'):
    """
    Function to dump output to file
    """
    f = open(file, 'w')
    f.close()
    df = pd.DataFrame(results)
    _, ext = os.path.splitext(file)
    if str(ext) == '.csv':
        df.to_csv(file)
    else:
        df.to_excel(file)
    print(f'Output dumped to {file}')
