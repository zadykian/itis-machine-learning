from graph_edge import GraphEdge
from graph_node import GraphNode



def main():
	first_node = GraphNode(1, 1)
	second_node = GraphNode(2, 2)
	edge = GraphEdge(first_node, second_node)
	print(edge)


if __name__ == "__main__":
	main()