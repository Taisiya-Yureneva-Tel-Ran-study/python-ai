# HW#29 
## Module (Python file 'converter.py') containing the following functions
### def enumerator(values: Iterable[str]) -> dict[str, int]
takes Iterable of strings<br>
returns dictionary with initial string as key and sequentianal number as value<br>
### def columnsMapper(columnsStr: list[str], df: DataFrame)->dict[str, dict[str, int]]
takes list of the column names DataFrame (type from pandas; if there is 'import pandas as pd' this type may be defined like pd.DataFrame)<br>
returns dictionary with name of column as key and dictionary (see description of returning type in previous function) as value<br>
this function is intended for getting enumerated values for the specified columns
### def convertX(df:pd.DataFrame, mapper: dict[str, dict[str, int]])-> pd.DataFrame
takes DataFrame and mapper (result of the previous function)<br>
returns DataFrame with columns containing sequentianal numbers as the values<br>
this function is intended for converting DataFrame containing strings as the values to a DataFrame containing the numbers as the values
