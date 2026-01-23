import matplotlib.pyplot as plt
import pandas as pd
import sys


# def std():


def mean(marks):
    means_per_house = []

    for house in marks:
        means_courses = []
        for course in house:
            mean = sum(course) / len(course)
            means_courses.append(mean)
        means_per_house.append(means_courses)
    
    return means_per_house


def retrieve_marks(df, houses, courses):
    gryffindor_marks = []
    slytherin_marks = []
    hufflepuff_marks = []
    ravenclaw_marks = []

    for course in courses:
        gryffindor_course_marks = []
        slytherin_course_marks = []
        hufflepuff_course_marks = []
        ravenclaw_course_marks = []
        i = 0

        for mark in df[course]:
            if pd.isna(mark):
                continue
            mark = float(mark)
            house = houses[i]
            if house == "Gryffindor":
                gryffindor_course_marks.append(mark)
            elif house == "Slytherin":
                slytherin_course_marks.append(mark)
            elif house == "Hufflepuff":
                hufflepuff_course_marks.append(mark)
            elif house == "Ravenclaw":
                ravenclaw_course_marks.append(mark)
            i += 1
        gryffindor_marks.append(gryffindor_course_marks)
        slytherin_marks.append(slytherin_course_marks)
        hufflepuff_marks.append(hufflepuff_course_marks)
        ravenclaw_marks.append(ravenclaw_course_marks)
    
    return [gryffindor_marks, slytherin_marks, hufflepuff_marks, ravenclaw_marks]


def main():
    try:
        if not len(sys.argv) == 1:
            raise SystemExit("Wrong number of arguments.")
        df = pd.read_csv("dataset_train.csv")

        marks = retrieve_marks(df, df.iloc[:, 1], df.iloc[:, 6:].columns)
        mean_per_house = mean(marks)
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
