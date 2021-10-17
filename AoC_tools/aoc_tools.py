def display_grid(positions, lookup_table=None):
    """takes two dictionaries as input: positions with their values, and a lookup table that specifies
    how each value should be visualized. If value should simply be visualized as itself, no lookup table is needed."""
    x_range = [p[0] for p in positions]
    y_range = [p[1] for p in positions]

#    print(min(x_range), max(x_range))
#    print(min(y_range), max(y_range))

    dim_x = max(x_range) + abs(min(x_range))
    dim_y = max(y_range) + abs(min(y_range))
    #print(dim_x, dim_y)

    cols = [i for i in range(min(x_range), max(x_range)+1)]
    index = [i for i in range(max(y_range), min(y_range)-1, -1)]

#    print(cols)
#    print(index)

    import pandas as pd
    #
    grid = pd.DataFrame(columns=cols, index=index)
    for col in grid.columns:
        grid[col].values[:] = ' '

    if lookup_table is None:
        for key, value in positions.items():
            grid.loc[key[1], key[0]] = value

    elif lookup_table is not None:
        for p in positions:
            for key, value in lookup_table.items():
                if positions[p] == key:
                    grid.loc[p[1], p[0]] = value

    lol = grid.values.tolist()
    for l in lol:
        print(" ".join(l))