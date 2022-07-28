import pandas as pd
import traceback


# 第一步：观察近check_day天有无涨停,如果有则继续，没有则返回
# 第二步：观察涨停后几天有无天量股票
# 第三步：观察天量后有无缩量到天量一半一下，则为待观察股票
class Alg:
    check_day = 5
    rise_const = 9
    result = False
    file_name = ''
    num = 1.5

    def cfmm(self, datas, file_name):
        try:
            self.file_name = file_name
            datas = datas.tail(self.check_day)
            datas = self.cal_zhang_ting(datas)
            rise_list = datas['rise'].loc[datas['rise'] >= self.rise_const]
            if rise_list.values.size == 0:
                return self.result
            index = rise_list.tail(1).index
            print("涨停数据：{}", datas)
            datas = self.select_data(datas, index)
            if datas.values.size == 0:
                return self.result
            avg = datas["成交量"].mean()
            max = datas["成交量"].max()
            if max < avg * self.num:
                return self.result
            rise_list = datas[datas['成交量'] == datas['成交量'].max()]
            if rise_list.values.size == 0:
                return self.result
            index = rise_list.tail(1).index
            print("天量数据：{}", datas)
            datas = self.select_data(datas, index)
            max1 = datas["成交量"].max()
            if datas.values.size == 0 or max1 == 0:
                return self.result
            rise_list = datas['成交量'].loc[datas['成交量'] <= (max / 2)]
            if rise_list.values.size == 0:
                return self.result
            print("缩量数据：{}", datas)
        except Exception as e:
            print("文件：{}异常".format(file_name, e))
            traceback.print_exc()
            return self.result
        return True

    def cal_zhang_ting(self, datas):
        print(datas)
        kai_pan = datas['开盘']
        shou_pan = datas['temp']
        temp = shou_pan - kai_pan
        zhang_ting = (temp / shou_pan) * 100
        datas['rise'] = zhang_ting
        return datas

    def select_data(self, datas, index):
        df = pd.DataFrame()
        row_list = []
        for idx, row in datas.iterrows():
            if idx > index:
                df = df.append(row, ignore_index=True)
        return df
