def is_valid_walk(walk):
    if len(walk) != 10:
        return False
    else:
        walking_dict = {
            "n": 0,
            "s": 0,
            "w": 0,
            "e": 0,
        }
        for way in walk:
            # if walking_dict[way] == 0:
            walking_dict[way] += 1
            # else:
            #     walking_dict[way] -= 1
        if (walking_dict["n"] == walking_dict["s"]) and (walking_dict["w"] == walking_dict["e"]):
            return True
        else:
            return False


print(is_valid_walk(['n', 'n', 'n', 's', 's', 's', 'n', 's', 'n', 's']))
