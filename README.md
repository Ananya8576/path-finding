# path-finding

Describing the movement of each piece, we are finding the path from the star to goal position for the King considering other pieces are threatening some positions. Also, some positions are blocked by obstacles so the route of the king must avoid these obstacles and threatened positions

We find the neighbors from each position and move to the most optimal one

BFS, DFS don't consider cost here so may not be optimal

UCS considers optimal cost for each movement

A star uses a unique heuristic to discover the optimal path using the minimum number of nodes
