# 写函数，检查传入字典的每一个value的长度，如果大于2，那么仅保留前2个长度的内容，并将新内容返回给调用者。PS：字典中的value只能是字符串或列表
def length(**kwargs):
    '''
    处理字典类型的数据
    :param kwargs:字典
    :return:处理完成的字典
    '''
    for key, value in kwargs.items():
        if len(kwargs.values()) > 2:
            kwargs[key] = value[:2]
            pass
    return kwargs
dictA = {"name": "00", "age": '23', "height": "1.67", "other": "234234234232"}
opt = length(**dictA)
print(opt)