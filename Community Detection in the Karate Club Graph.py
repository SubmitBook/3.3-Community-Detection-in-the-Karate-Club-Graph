import networkx as nx
import matplotlib.pyplot as plt
from networkx.algorithms import community

# 载入 Zachary 空手道俱乐部图
G = nx.karate_club_graph()

import community as community_louvain

# 计算 Louvain 社区
partition = community_louvain.best_partition(G)

# 获取所有社区
communities = {}
for node, comm in partition.items():
    if comm not in communities:
        communities[comm] = []
    communities[comm].append(node)

# 打印检测出的社区
for comm, nodes in communities.items():
    print(f"社区 {comm}: {nodes}")

from networkx.algorithms.community import girvan_newman

# 计算 Girvan-Newman 社区
comp = girvan_newman(G)
top_level_communities = next(comp)  # 获取第一层划分
girvan_communities = [list(c) for c in top_level_communities]

# 打印社区
for i, comm in enumerate(girvan_communities):
    print(f"社区 {i}: {comm}")

import matplotlib.cm as cm
import numpy as np

# 为每个社区分配颜色
colors = cm.rainbow(np.linspace(0, 1, len(set(partition.values()))))
node_colors = [colors[partition[node]] for node in G.nodes()]

# 绘制网络图
plt.figure(figsize=(10, 7))
nx.draw(
    G, with_labels=True, node_color=node_colors,
    edge_color="gray", node_size=500, cmap=plt.cm.rainbow
)
plt.show()
