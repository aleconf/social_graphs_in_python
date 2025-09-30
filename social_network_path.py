#!/usr/bin/env python


def graph_creation(input_data="SocialNetwork.txt"):
    """Creation of the graph from the text file.

    The graph is encoded as a dictionary: the keys are the vertices and the
    values are the lists of neighbour vertices, i.e. the value is the list of
    all friends of that vertex / key.
    """

    # input_file = open(input_data)
    with open(input_data, "r") as file:
        input_file = file.readlines()
    graph = dict()
    for line in input_file:
        working_line = list(line)
        comma_position = 0
        assert working_line[len(working_line) - 1] == "\n"
        for index in range(len(working_line) - 1):
            if working_line[index] == ",":
                comma_position = index
        person1_list = working_line[0:comma_position]
        person2_list = working_line[comma_position + 1 : len(working_line) - 1]
        person1 = "".join(person1_list)
        person2 = "".join(person2_list)
        if person1 in graph:
            graph[person1].append(person2)
        else:
            graph[person1] = [person2]
        if person2 in graph:
            graph[person2].append(person1)
        else:
            graph[person2] = [person1]
    return graph


def compute_distance(a, b, graph):
    """A variation of the BFS algorithm is used."""
    search_list = [a]
    predecessor = {a: "ROOT"}
    flag = False
    for element in search_list:
        for neighbour in graph[element]:
            if neighbour == b:
                predecessor[neighbour] = element
                flag = True
            else:
                if neighbour not in predecessor:
                    search_list.append(neighbour)
                    predecessor[neighbour] = element
            if flag:
                break
        if flag:
            break
    path = [b]
    if flag:
        runner = predecessor[b]
        while runner != a:
            path.append(runner)
            runner = predecessor[runner]
        path.append(a)
        path.reverse()
    return path


def main():
    graph = graph_creation()
    print("There are", len(graph), "persons in the social network.")
    assert compute_distance("STACEY_STRIMPLE", "RICH_OMLI", graph) == [
        "STACEY_STRIMPLE",
        "KORY_NICKOLAS",
        "LUCIANO_KEBA",
        "RIGOBERTO_RACCA",
        "FRITZ_RYBCZYK",
        "RICH_OMLI",
    ]
    a = input("Please enter the first name: ")
    b = input("Please enter the second name: ")
    if a not in graph or b not in graph:
        print("At least one of the two persons is not in the social network.")
    elif a == b:
        print("The two names are identical, hence the distance is 0.")
    else:
        path = compute_distance(a, b, graph)
        if len(path) > 1:
            print("The distance between", a, "and", b, "is", len(path) - 1, "\b.")
            print("One instance of a minimal path between", a, "and", b, "is", path)
        else:
            print(
                a,
                "and",
                b,
                "are not connected in the social network,",
                "they must belong to two different connected components.",
            )


if __name__ == "__main__":
    main()
