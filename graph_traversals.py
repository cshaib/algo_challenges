def main():	

	# graph struct 

	nodes = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

	adjacency_list = {0: [8, 7, 11],
					  1:[10, 8],
					  2:[12, 3],
					  3:[2, 4, 7],
					  4:[3],
					  5:[6],
					  6:[5, 7],
					  7:[3, 6, 0, 11],
					  8:[12, 0, 9, 1],
					  9:[10, 8],
					  10:[1, 9],
					  11:[7, 0],
					  12:[8, 2]
					  }


	""" 

	Depth-first search, should output:
	[10, 1, 8, 12, 2, 3, 4, 7, 6, 5, 0, 11, 9]

	"""
	bfs_results = []
	dfs_results = []

	seen_dfs = [False] * len(nodes)
	seen_bfs = [False] * len(nodes)

	def dfs(node, l):
		idx = nodes.index(node)

		# base case: if the node has been seen, return 
		if seen_dfs[idx]: 
			return None

		# otherwise mark it as seen
		seen_dfs[idx] = True

		# add it to the print list 
		l.append(node)

		# call dfs on the next node in the *list* 
		for next_node in adjacency_list[node]: 
			dfs(next_node, l)

	""" 

	Breadth-first search, should output:
	[10, 1, 9, 8, 12, 0, 2, 7, 11, 3, 6, 4, 5]

	"""
	def bfs(node, l):

		# FIFO queue to track levels
		fifo = [] 

		# append the first node
		fifo.append(node)
		l.append(node)

		# mark the first node as seen
		seen_bfs[nodes.index(node)] = True

		while fifo: 
			# neighbour list to loop over
			search_list = adjacency_list[fifo[0]]

			for neighbour in search_list:
				if not seen_bfs[nodes.index(neighbour)]:
					# mark as seen 
					seen_bfs[nodes.index(neighbour)] = True

					# append to queue, and print that you have traversed
					fifo.append(neighbour)
					l.append(neighbour)

			# at the end of the neighbour list, pop out the first node
			fifo.pop(0)


	##########################################################################################

	dfs(nodes[10], dfs_results)

	bfs(nodes[10], bfs_results)
 
	print(f'Depth-first Traversal:   {dfs_results} \nBreadth-first Traversal: {bfs_results}')

if __name__ == "__main__":
	main()