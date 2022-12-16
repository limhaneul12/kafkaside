import pandas as pd 

import os
import pathlib
import create_log


burket: int = 0
for i in (pathlib.Path(f"{os.getcwd()}/data/{i}") for i in range(1, 13)):
    for j in (i for i in list(pathlib.Path(i).iterdir())):
        data: int = pd.read_parquet(j).shape[0]
        burket += data


create_log.log().info(f"총 데이터는 : {burket}개 입니다")