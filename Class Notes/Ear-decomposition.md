# Ear Decomposition

## Jen Schmidt

1). Take rooted DFS Tree.
2). Direct Tree towards the root.
3). Direct Non tree edges away from the root.
4). Take a lowest non tree edge(by dfs number) and trace the fundamental cycle until reaching a previsited node, that path traced is a ear decomposition.

## Ramachandran

1). Take a spanning tree
2). Give preorder numbering
3). Mark the non tree edges with the preorder number of its lca
4). Sort them, give duplicates new numbers( but order should remain same)
5). For all tree edges, find in which and all fundamental cyles of non tree edges the exist, choose the least marked non tree edges cycle as its cycle.
