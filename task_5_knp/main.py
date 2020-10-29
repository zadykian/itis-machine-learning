from graph_edge import GraphEdge
from point import Point



def main():
	first_node = Point(1, 1)
	second_node = Point(2, 2)
	edge = GraphEdge(first_node, second_node)
	print(edge)


if __name__ == "__main__":
	main()