from question1 import mat_to_list
from question2 import reachable

def main():
    adj_mat = [[0, 1, 0, 0, 0, 0],
               [1, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 1, 0],
               [0, 0, 0, 1, 0, 0],
               [0, 0, 0, 0, 0, 0]]
    adj_list = mat_to_list(adj_mat)
    print(f"Adjacency list: {adj_list}")

    start_node = 0
    reachable_nodes = reachable(adj_list, start_node)
    print(f"Nodes reachable from node {start_node}: {reachable_nodes}")

if __name__ == '__main__':
    main() 