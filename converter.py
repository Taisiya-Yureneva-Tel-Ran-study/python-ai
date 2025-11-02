from typing import Iterable
from pandas import DataFrame

def enumerator(values: Iterable[str]) -> dict[str, int]:
    return {value: index for (index, value) in enumerate(values)}

def columnsMapper(columnsStr: list[str], df: DataFrame)->dict[str, dict[str, int]]:
#    return {colName: enumerator(df[colName].unique()) for colName in columnsStr}   
    res: dict[str, dict[str, int]] = {}
    for column in columnsStr:
        res[column] = enumerator(df[column].unique())
    return res
    
def convertX(df: DataFrame, mapper: dict[str, dict[str, int]])-> DataFrame:
    res = {colName: [mapper[colName][value] for value in df[colName]] for colName in mapper.keys()}
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