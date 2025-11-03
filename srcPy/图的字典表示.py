if __name__ == "__main__":
    """" 解刨字段 d = {"A": {"B":5}} """
    n = int(input())

    nodes = set()  # 顶点数
    edges = set()  # 边数
    total = 0  # 边的总长度

    for _ in range(n):

        line = input().strip()
        dicts = eval(line) # {'A': {'B': 5, 'C': 10, 'D': 15}}

        # 获取节点
        frist = dicts.keys()  # dict_keys(['A'])
        frist_list = list(frist)  # ['A']
        node_header = frist_list[0]  # A
        nodes.add(node_header)

        # A:{}
        dicts_nodes_by = dicts[node_header] # {'B': 5, 'C': 10, 'D': 15}

        for dot, length in dicts_nodes_by.items():
            nodes.add(dot)

            # 把两个顶点组成的边变成“无向边”的标准形式
            iterable = sorted([node_header, dot])  # ['A', 'B']
            edge = tuple(iterable)    # ('A', 'B')

            # 添加边
            if edge not in edges:
                edges.add(edge)  # {('A', 'B'), ('A', 'O'), ('A', 'D')}
                total += length

    print(len(nodes), len(edges), total)
