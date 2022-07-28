import time

from read_data import ReadData
from Alg import Alg
import os
import traceback

dir_str = r'C:/Users/xshell/Desktop/demo/cfmm/export/'

if __name__ == '__main__':
    code = []
    rd = ReadData(dir_str)
    alg = Alg()
    file_list = rd.read_file_list();
    # datas = rd.read_data("SH#600938.txt")
    # alg.cfmm(datas, "SH#600938.txt")
    print("开始选股：===============================")
    for x in file_list:
        try:
            if os.path.splitext(x)[1] == '.txt':
                datas = rd.read_data(x)
                result = alg.cfmm(datas, x)
                if result:
                    code.append(os.path.splitext(x)[0])
        except Exception as e:
            print("系统处理异常，{}",  e)
            traceback.print_exc()

    print("选股结束：===============================")
    print("选股结果：", code)
    # 写入结果到文件
    date_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
    file_path = 'result_data' + date_time + '.txt'
    with open(file_path, mode='w', encoding='utf-8') as file_obj:
        file_obj.write(str(code))





