if __name__ == "__main__":
    """" 解刨字段 d = {"A": {"B":5}} """
    n = int(input())

    nodes = set()  # 顶点数
    edges = set()  # 边数
    total = 0  # 边的总长度

    for _ in range(n):

        strLine = input().strip()
        dictLine = eval(strLine)  # {'A': {'B': 5, 'C': 10, 'D': 15}}

        # 获取节点 A
        frist = dictLine.keys()  # dict_keys(['A'])
        frist_list = list(frist)  # ['A']
        node = frist_list[0]  # A
        nodes.add(node)

        # 获取被链接的节点 A:{}
        dicts_nodes_by = dictLine[node]  # {'B': 5, 'C': 10, 'D': 15}

        for dot, length in dicts_nodes_by.items():
            nodes.add(dot)

            # 把两个顶点组成的边变成“无向边”的标准形式
            listOrder = sorted([node, dot])  # ['A', 'B']
            edge = tuple(listOrder)    # ('A', 'B')

            # 添加边
            if edge not in edges:
                edges.add(edge)  # {('A', 'B'), ('A', 'O'), ('A', 'D')}
                total += length

    print(len(nodes), len(edges), total)
