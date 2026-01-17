import pandas as pd
import sys


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


# def ft_std():



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


def valid_numbers(df, col):
    nb_lst = []
    for nb in df.iloc[:, col]:
        if not pd.isna(nb):
            nb_lst.append(nb) 
    return nb_lst


def ft_q25(df, count_lst, cols):
    q25_lst = []
    for col, nb_values in zip(range(cols), count_lst):
        nb_lst = valid_numbers(df, col)
        sorted_nb = sorted(nb_lst)
        i_q25 = int(nb_values) // 4
        if i_q25 % 4 == 0:
            q25 = (sorted_nb[i_q25 - 1] + sorted_nb[i_q25]) / 2
        else:
            q25 = sorted_nb[i_q25]
        q25_lst.append(round(q25, 6))
    return q25_lst


def ft_q50(df, count_lst, cols):



def ft_q75(df, count_lst, cols):
    q75_lst = []
    for col, nb_values in zip(range(cols), count_lst):
        nb_lst = valid_numbers(df, col)
        sorted_nb = sorted(nb_lst)
        i_q75 = int(nb_values) * 3 // 4
        if i_q75 % 4 == 0:
            q75 = (sorted_nb[i_q75 - 1] + sorted_nb[i_q75]) / 2
        else:
            q75 = sorted_nb[i_q75]
        q75_lst.append(round(q75, 6))
    return q75_lst

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
    # std_lst = ft_std(csv_part, csv_part.shape[1])
    min_lst = ft_min(csv_part, csv_part.shape[1])
    q25_lst = ft_q25(csv_part, count_lst, csv_part.shape[1])
    q50_lst = ft_q50(csv_part, count_lst, csv_part.shape[1])
    print(q50_lst)
    q75_lst = ft_q75(csv_part, count_lst, csv_part.shape[1])
    max_lst = ft_max(csv_part, csv_part.shape[1])

    # return [count_lst, mean_lst, std_lst, min_lst, q25_lst, q50_lst, q75_lst, max_lst]

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
