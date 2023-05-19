import numpy as np
import pandas as pd

def q3():
    df = pd.DataFrame([[1000,25],[280,120],[900,30]],index=['store1','store2','store3'],columns=['unit price','number'])
    print(df)
    df['total price']=df.prod(axis=1)
    print(df)
    df=df.sort_values(by='total price',ascending=False)
    print(df[0:2])
    

if __name__=="__main__":
    q3()