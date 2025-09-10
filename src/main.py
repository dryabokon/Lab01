import os
import pandas as pd
import matplotlib.pyplot as plt
filename_in = "../data/dataset_titanic.csv"
folder_out = "../output"
# ----------------------------------------------------------------------------------------------------------------------
def EDA_histo(df):
    columns = df.select_dtypes(include=['int64', 'float64']).columns.tolist()
    columns = [c for c in columns if c != 'survived']

    os.makedirs(folder_out, exist_ok=True)
    for c1 in range(len(columns)):
        for c2 in range(c1 + 1, len(columns)):
            X = df[columns[c1]]
            Y = df[columns[c2]]

            plt.scatter(X,Y)
            plt.xlabel(columns[c1])
            plt.ylabel(columns[c2])
            plt.title(f'{columns[c1]} vs {columns[c2]}')
            plt.savefig(os.path.join(folder_out, f'plot_{columns[c1]}_{columns[c2]}.png'))
            plt.close()
    return
# ----------------------------------------------------------------------------------------------------------------------
def EDA_Columns(df):
    os.makedirs(folder_out, exist_ok=True)

    for column in df.columns:
        plt.figure(figsize=(10, 6))

        if df[column].dtype in ['int64', 'float64']:
            plt.hist(df[column].dropna(), bins=30)
            plt.xlabel(column)
            plt.ylabel('Frequency')
            plt.title(f'Histogram of {column}')
        else:
            value_counts = df[column].value_counts()
            plt.bar(value_counts.index, value_counts.values)
            plt.xticks(rotation=45)
            plt.xlabel(column)
            plt.ylabel('Count')
            plt.title(f'Bar plot of {column}')

        plt.tight_layout()
        plt.savefig(os.path.join(folder_out, f'column_{column}.png'))
        plt.close()
    return
# ----------------------------------------------------------------------------------------------------------------------
if __name__ == '__main__':
    df = pd.read_csv(filename_in,sep='\t')
    EDA_histo(df)
    EDA_Columns(df)
