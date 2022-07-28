import pandas as pd
import os
import traceback


class ReadData:
    dir_str = ''

    def __init__(self, dir_str):
        self.dir_str = dir_str

    # 读取文件夹，获取文件路径
    def read_file_list(self):
        return os.listdir(self.dir_str)

    def read_data(self, file_path):
        try:
            datas = pd.read_table(self.dir_str + file_path, header=1, encoding="gbk", sep='\t')
            datas.drop(datas.tail(1).index, inplace=True)
            datas.columns = datas.columns.str.strip()
            datas['temp'] = datas['收盘']
            datas['temp'] = datas['temp'].shift(1)
        except Exception as e:
            print("文件：{}异常，{}", file_path, e)
            traceback.print_exc()
            raise Exception(e)
        return datas
