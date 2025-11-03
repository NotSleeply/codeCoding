def get_sort_key(item):
    """
    排序键函数
    规则：
      - 若 key 为 int，返回 (0, key) -> 数字键排前，按数值升序；
      - 若 key 为 str，返回 (1, key) -> 字符串键排后，按字典序（ASCII）升序。
    参数：
      item: 来自 dict.items() 的二元组 (key, value)
    返回：
      用于比较的元组 (type_flag, key)
    例子： 
      (0, 1)   # for key 1
      (1, '2') # for key '2'
      (0, 3)   # for key 3
      (1, '3') # for key '3'
      (1, 'b') # for key 'b'
      最终排序顺序是：
      (0, 1) → key 1  
      (0, 3) → key 3  
      (1, '2') → key '2'  
      (1, '3') → key '3'  
      (1, 'b') → key 'b'
      所以输出结果是: {1: 8, 3: 10, '2': 5, '3': 7, 'b': 9}
    """
    key, _ = item
    if isinstance(key, int):
        return (0, key)  # 数字键：type_flag = 0，保证数字排在前面
    return (1, key)  # 非数字键（此处为字符串）：type_flag = 1，保证字符串排在数字之后


if __name__ == "__main__":
    dict1 = eval(input())  # {1:3,"2":5, 3: 10}
    dict2 = eval(input())  # {1:5,"3":7, "b":9}
    result = {}

    # 合并键值对
    for key in dict1:
        if key in dict2:
            result[key] = dict1[key] + dict2[key]
        else:
            result[key] = dict1[key]  
    # {1: 8, '2': 5, 3: 10}
    
    for key in dict2:
        if key not in dict1:
            result[key] = dict2[key]
    # {1: 8, '2': 5, 3: 10, '3': 7, 'b': 9}

    # 排序
    sorted_dict = dict(sorted(result.items(), key=get_sort_key))
    print(sorted_dict)
