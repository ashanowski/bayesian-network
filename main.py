from node import Node
from graph import Graph


if __name__ == "__main__":
    graph = Graph()

    # insert nodes to graph

    print("=== Define nodes ===")
    while True:
        node_name = input("-> New node name: ")

        if node_name in graph.named_nodes:
            print("Node named {} already exists in this graph.".format(node_name))
            continue

        if not node_name:
            break

        graph.add_node(node_name)

    print("--- Adding nodes finished. Your graph contains following {} nodes:".format(len(graph)))

    [print(node.name, end=' ') for node in graph.nodes]

    print("\n=== Define nodes' relations ===")

    # define relations to nodes
    for node in graph.nodes:
        decision = input("Does node named '{}' have any childs? [y/n] ".format(node.name))

        if decision.lower() == 'y':

            # add childs to node
            while True:
                child_name = input("-> Child name: ")

                if not child_name:
                    break
                
                # repeat if node doesn't exist
                if child_name not in graph.named_nodes:
                    print("Node named '{}' does not exist!".format(child_name))
                    continue

                # repeat if node has already been added as a child
                if child_name in node.named_childs:
                    print("Node named '{}' has already been added.".format(child_name))
                    continue

                for node_check in graph.nodes:
                    if node_check.name == child_name:
                        node.add_child(node_check)
        else:
            continue


    print("Relations added:")
    for node in graph.nodes:
        print(node.name, "-->", node.childs)
    
    print("=== Define probability table ===")
    print("--- You only need to define chance for node to occur ---")
    print("--- Probability that it won't occur is autocompleted ---")

    probability_dict = graph.probability_count()

    for node in graph.nodes:

        opt = "probability" if probability_dict[node] == 1 else "probabilities"
            
        print("Node '{}' needs {} {} to be defined".format(node.name, probability_dict[node], opt))

        counter = 1
        while node.prob_len() < probability_dict[node]:
            prob = float(input("{}. probability: ".format(counter)))

            if prob < 0 or prob > 1:
                print("Probability has to be in range [0, 1]")
                continue

            node.add_probability(prob)
            counter += 1

    print("=== Probability tables created. ===")

    for node in graph.nodes:
        print(node.probability_table)

            


