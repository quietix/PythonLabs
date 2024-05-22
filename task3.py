def modify_fuel_data(fuel_levels, target_value=0, in_place=False):
    if in_place:
        for i in range(len(fuel_levels)):
            if fuel_levels[i] % 2 == 0:
                fuel_levels[i] = target_value
        return fuel_levels
    else:
        fuel_levels_dump = fuel_levels[:]
        for i in range(len(fuel_levels_dump)):
            if fuel_levels_dump[i] % 2 == 0:
                fuel_levels_dump[i] = target_value
        return fuel_levels_dump


if __name__ == "__main__":
    fuel_levels = [i for i in range(1, 11)]
    print("Original array:", fuel_levels)

    result = modify_fuel_data(fuel_levels, target_value=0, in_place=False)
    print("Modified array (not in place):", result)
    print("Original array after function call:", fuel_levels)

    result_in_place = modify_fuel_data(fuel_levels, target_value=0, in_place=True)
    print("Modified array (in place):", result_in_place)
    print("Original array after function call (in place):", fuel_levels)
