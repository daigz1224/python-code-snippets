import os
import multiprocessing

# 多进程中判断一个文件是否存在
def create_folder_if_not_exist(folder):
    isExist = os.path.exists(folder)
    if not isExist:
        try:
            os.makedirs(folder)
        except Exception as ex:
            checkExist = os.path.exists(folder)
            if not checkExist:
                print('Error: ', ex)


# 多进程手机每个进程返回的结果，使用_getvalue()方法转为普通dict
manager = multiprocessing.Manager()
res = manager.dict()
with open('/path/to/xxx.json', 'w') as f:
    f.write(json.dumps(res._getvalue(),indent=2, separators=(',', ':')))
