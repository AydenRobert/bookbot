def get_num_words(contents):
    return len(contents.split())


def get_char_dict(contents):
    char_list = list(contents.lower())
    alpha_list = list(filter(lambda x: x.isalpha(), char_list))
    alpha_dict = {}
    for char in alpha_list:
        if char not in alpha_dict:
            alpha_dict[char] = 0
        alpha_dict[char] += 1
    return alpha_dict


def get_sorted_dict(inp_dict):
    out_list = list()
    for key in inp_dict:
        out_list.append({"char": key, "num": inp_dict[key]})
    out_list.sort(key=lambda item: item["num"])
    out_list.reverse()
    return out_list
