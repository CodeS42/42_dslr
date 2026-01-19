import pandas as pd
import sys

Q1 = 1
Q2 = 2
Q3 = 3

def ft_count(df, cols):
    count_lst = []
    for col in range(cols):
        count = 0
        for nb in df.iloc[:, col]:
            if not pd.isna(nb):
                count += 1
        count_lst.append(round(float(count), 6))
    return count_lst


def ft_mean(df, count_lst, cols):
    mean_lst = []
    for col, nb_values in zip(range(cols), count_lst):
        result = sum(nb for nb in df.iloc[:, col] if not pd.isna(nb)) / nb_values
        mean_lst.append(round(result, 6))
    return mean_lst


def valid_numbers(df, col):
    nb_lst = []
    for nb in df.iloc[:, col]:
        if not pd.isna(nb):
            nb_lst.append(nb)
    return nb_lst


def variance(df, mean_lst, cols):
    var_lst = []
    for col, mean in zip(range(cols), mean_lst):
        nb_lst = valid_numbers(df, col)
        
        var = sum([() ** 2 ]) / len(nb_lst)
    return var_lst


def ft_std(df, mean_lst, count_lst, cols):
    var = variance(df, mean_lst)
    return [v ** 0.5 for v in var]


def ft_min(df, cols):
    min_lst = []
    for col in range(cols):
        i = 0
        while pd.isna(df.iloc[i, col]):
            i += 1
        min_nb = df.iloc[i, col]
        for nb in df.iloc[i + 1:, col]:
            if not pd.isna(nb):
                if nb < min_nb:
                    min_nb = nb
        min_lst.append(round(min_nb, 6))
    return min_lst


def ft_quartile(df, count_lst, cols, q):
    quartile_lst = []
    for col, nb_values in zip(range(cols), count_lst):
        nb_lst = valid_numbers(df, col)
        sorted_nb = sorted(nb_lst)
        if q == Q1:
            i_quartile = int(nb_values) // 4
        elif q == Q2:
            i_quartile = int(nb_values) * 2 // 4
        elif q == Q3:
            i_quartile = int(nb_values) * 3 // 4
        if i_quartile % 4 == 0:
            quartile = (sorted_nb[i_quartile - 1] + sorted_nb[i_quartile]) / 2
        else:
            quartile = sorted_nb[i_quartile]
        quartile_lst.append(round(quartile, 6))
    return quartile_lst


def ft_max(df, cols):
    max_lst = []
    for col in range(cols):
        i = 0
        while pd.isna(df.iloc[i, col]):
            i += 1
        max_nb = df.iloc[i, col]
        for nb in df.iloc[i + 1:, col]:
            if not pd.isna(nb):
                if nb > max_nb:
                    max_nb = nb
        max_lst.append(round(max_nb, 6))
    return max_lst


def analyze_csv(df):
    csv_part = df.iloc[:, 6:]
    count_lst = ft_count(csv_part, csv_part.shape[1])
    mean_lst = ft_mean(csv_part, count_lst, csv_part.shape[1])
    print(mean_lst)
    std_lst = ft_std(csv_part, mean_lst, count_lst, csv_part.shape[1])
    min_lst = ft_min(csv_part, csv_part.shape[1])
    q25_lst = ft_quartile(csv_part, count_lst, csv_part.shape[1], Q1)
    q50_lst = ft_quartile(csv_part, count_lst, csv_part.shape[1], Q2)
    q75_lst = ft_quartile(csv_part, count_lst, csv_part.shape[1], Q3)
    max_lst = ft_max(csv_part, csv_part.shape[1])

    return [count_lst, mean_lst, std_lst, min_lst, q25_lst, q50_lst, q75_lst, max_lst]

def main():
    try:
        av = sys.argv
        if not len(av) == 2:
            raise SystemExit("Wrong number of arguments.")

        df = pd.read_csv(av[1])

        analyze_csv(df)
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
