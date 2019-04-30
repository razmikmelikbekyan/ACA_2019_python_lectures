from b import parse_string_dict, calculate_dict_stat


def main():
    # print(__name__)
    input_dict = input("Please enter a dict for calculating stat: ")

    dict_object = parse_string_dict(input_dict)
    dict_stat = calculate_dict_stat(dict_object)
    print(f'\nFor given dict: \n{dict_object}, \ncalculates stats are: \n{dict_stat}.')


if __name__ == "__main__":
    main()
