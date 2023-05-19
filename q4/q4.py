import numpy as np
import pandas as pd
def q4():
    f=pd.read_csv('q4/gender2.csv',delimiter=',',encoding="ANSI",index_col=0,usecols=["행정구역","2022년_계_총인구수","2022년_남_총인구수","2022년_여_총인구수"])
    df=pd.DataFrame(f)
    df.rename(columns={"2022년_계_총인구수":"Total", "2022년_남_총인구수":"Male","2022년_여_총인구수":"Female"},inplace=True)
    print(df)


if __name__=="__main__":
    q4()