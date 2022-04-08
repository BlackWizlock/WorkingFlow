def ant_bridge(ants, terrain):
    if terrain.count("."):
        terrain = terrain.count(".") + 2
    else:
        terrain = 0
    list_ants = [_ for _ in ants]
    num_to_start = len(ants) - terrain
    # list_ants.reverse()
    answer_list = [list_ants[_] for _ in range(num_to_start, len(list_ants))]
    for _ in range(0, len(list_ants) - terrain):
        answer_list.append(list_ants[_])
    return "".join(_ for _ in answer_list)


ant_bridge("GFEDCBA", "---------------------------")


