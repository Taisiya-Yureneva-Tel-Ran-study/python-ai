from typing import Iterable
from pandas import DataFrame

def enumerator(values: Iterable[str]) -> dict[str, int]:
    return {value: index for (index, value) in enumerate({a for a in values})}

def columnsMapper(columnsStr: list[str], df: DataFrame)->dict[str, dict[str, int]]:
    return {colName: enumerator(df[colName]) for colName in columnsStr}   
    
def convertX(df: DataFrame, mapper: dict[str, dict[str, int]])-> DataFrame:
    res = {colName: [mapper[colName][value] for value in df[colName]] for colName in df.columns}
    return DataFrame(res)

if __name__ == "__main__":
    df = DataFrame(({
            "Company":['Toyota','Toyota','Hundai', 'Hundai', 'Hundai' ],
            "Model": ['Camry', 'Corolla', 'i10', 'Elantra', 'Kona']
            }))
    mapper = columnsMapper(["Company","Model"], df) 
    print(mapper)
    print(df)
    print(convertX(df, mapper))