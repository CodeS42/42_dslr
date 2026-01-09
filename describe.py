import pandas as pd
import sys


def ft_count(df, cols):
    count_lst = []
    for col in range(cols):
        count = 0
        for nb in df.iloc[:, col]:
            if not pd.isna(nb):
                count += 1
        count_lst.append(float(count)) #.6f
    return count_lst


def ft_mean(df, count_lst, cols):
    mean_lst = []
    for col, nb_values in zip(range(cols), count_lst):
        result = sum(nb for nb in df.iloc[:, col] if not pd.isna(nb)) / nb_values
        mean_lst.append(result)
    return mean_lst

# def ft_std():



# def ft_min():



# def ft_q25():



# def ft_q50():



# def ft_q75():



# def ft_max(df):




def analyze_csv(df):
    csv_part = df.iloc[:, 6:]
    count_lst = ft_count(csv_part, csv_part.shape[1])
    mean_lst = ft_mean(csv_part, count_lst, csv_part.shape[1])
    # std_lst = ft_std(csv_part, csv_part.shape[1])
    # min_lst = ft_min(csv_part, csv_part.shape[1])
    # q25_lst = ft_q25(csv_part, csv_part.shape[1])
    # q50_lst = ft_q50(csv_part, csv_part.shape[1])
    # q75_lst = ft_q75(csv_part, csv_part.shape[1])
    # max_lst = ft_max(csv_part, csv_part.shape[1])

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
