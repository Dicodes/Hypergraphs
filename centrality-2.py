from Hypergraph.halp.undirected_hypergraph import UndirectedHypergraph



def creating_hypergraph():
	#global name_nodes
	#global name

	hyperedges = [set1, set2, set3, set4]

	hyperedge_ids =\
	    H.add_hyperedges(hyperedges) # automatically adds any nodes not present in the original node_list to the node list of the hypergraph


	print("Hyperedge ID           Nodes in Hyperedge")

	for i in range(n):
		name[i] = H.get_hyperedge_id(set_list[i])
		name_nodes[i] = H.get_hyperedge_nodes(name[i])
		print(name[i],'                 ', name_nodes[i])



def computing_sv_method_1():
	global vol
	global size

	for i in range(n):
		Ng = 0
		current_set = set_list[i]
		size[i] = len(set_list[i])
		for j in range (n):
			if i != j:
				intersection_set = current_set.intersection(set_list[j])

				current_id = H.get_hyperedge_id(current_set)
				set_id = H.get_hyperedge_id(set_list[j]) 

				if intersection_set != set(): 
					Ng = Ng+1
					vol[i] = vol[i]+len(intersection_set)
                    
        #current_id = H.get_hyperedge_id(current_set)
		print("Size of neighborhood of",current_id,"is",Ng)
		H.add_hyperedge(current_set,{'cardinality':Ng})
"""
    NOT WORKING

    HOW TO GIVE INPUT FOR H.get_hyperedge_attribute() to retrieve the size of the neighborhood?

    attribute = {'cardinality'}

    for i in range(n):
        current_hyperedge = name[i]
        cardinality[i] = H.get_hyperedge_attribute(current_hyperedge,attribute)
        svl[i] = 1/(1+cardinality[i])
        print(current_hyperedge, svl[i])
"""
def computing_sv_method_2():
	sv = [0] * len(set_list)
        
	for i in range (n):
		current_set = set_list[i]
		print("Intersection with the set",H.get_hyperedge_id(current_set))
		print("VOL OF INTERSECTION   SIZE OF THE SET")
		for j in range(n):
			intersection_set = current_set.intersection(set_list[j])

			if i != j: #implies set[j] belongs to neghborhood of i
				if intersection_set != set():

					sv[i] = sv[i] + 1/(vol[j] + size[j])# calculating shapley value based on the formula given in the paper Computing centrality of hyoergraphs

					print(H.get_hyperedge_id(set_list[j]),vol[j],size[j])

				else:
					print(H.get_hyperedge_id(set_list[j]),vol[j],size[j])

		print("SHAPLEY VALUE")
		print(H.get_hyperedge_id(set_list[i]),sv[i])

H=UndirectedHypergraph()
node_list = ["A","B","C","D"] # you can also add individual attributes
attributes = {'label' : "positive"} #common attributes for all the nodes

H.add_nodes(node_list, attributes)

set1 = set(["A","B","D"]) #set of nodes in hyperedge-1
frozen_set1 = frozenset(set1)
set2 = set(["A","C"]) # set of nodes in hyperedge-2
frozen_set2 = frozenset(set2) 
set3 = set(["B","D"])
frozen_set3 = frozenset(set3)
set4 = set(["E","F"])

set_list=[set1,set2,set3,set4]
n = len(set_list)

name = [None] * n
name_nodes = [None] * n

vol = [0] * n
size = [0] * n

creating_hypergraph()
print("METHOD 1 OF SHAPLEY VALUE CALCULATION")
computing_sv_method_1()
print("METHOD 2 OF SHAPLEY VALUE CALCULATION")
computing_sv_method_2()
