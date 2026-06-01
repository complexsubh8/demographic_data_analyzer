import pandas as pd

def calculate_demographic_data(print_data=True):

    # Read data
    column_names = [
    'age', 'workclass', 'fnlwgt', 'education',
    'education-num', 'marital-status', 'occupation',
    'relationship', 'race', 'sex',
    'capital-gain', 'capital-loss',
    'hours-per-week', 'native-country', 'salary'
    ]

    df = pd.read_csv(
    r"D:\\College Coding\\Python Projects\\Demographic_Data_Analyzer\\adult.data.csv",
    names=column_names,
    skipinitialspace=True
    )

    # Number of each race
    race_count = df["race"].value_counts()

    # Average age of men
    average_age_men = round(
        df[df["sex"] == "Male"]["age"].mean(), 1
    )

    # Percentage with Bachelor's degree
    percentage_bachelors = round(
        (df["education"] == "Bachelors").mean() * 100, 1
    )

    higher_education = df["education"].isin(
        ["Bachelors", "Masters", "Doctorate"]
    )

    # Percentage with salary >50K
    higher_education_rich = round(
        (
            df[higher_education]["salary"] == ">50K"
        ).mean() * 100,
        1,
    )

    lower_education_rich = round(
        (
            df[~higher_education]["salary"] == ">50K"
        ).mean() * 100,
        1,
    )

    # Minimum work hours
    min_work_hours = df["hours-per-week"].min()

    # Rich among minimum workers
    num_min_workers = df[
        df["hours-per-week"] == min_work_hours
    ]

    rich_percentage = round(
        (
            num_min_workers["salary"] == ">50K"
        ).mean() * 100,
        1,
    )

    # Country with highest percentage >50K
    country_percentages = (
        df.groupby("native-country")["salary"]
        .apply(lambda x: (x == ">50K").mean() * 100)
    )

    highest_earning_country = country_percentages.idxmax()

    highest_earning_country_percentage = round(
        country_percentages.max(),
        1,
    )

    # Most popular occupation in India for >50K
    top_IN_occupation = (
        df[
            (df["native-country"] == "India")
            & (df["salary"] == ">50K")
        ]["occupation"]
        .value_counts()
        .idxmax()
    )

    if print_data:
        print("Number of each race:\n", race_count)
        print("Average age of men:", average_age_men)
        print("% with Bachelors degrees:", percentage_bachelors)
        print(
            "% with higher education that earn >50K:",
            higher_education_rich,
        )
        print(
            "% without higher education that earn >50K:",
            lower_education_rich,
        )
        print("Min work time:", min_work_hours)
        print(
            "% of rich among those who work fewest hours:",
            rich_percentage,
        )
        print(
            "Country with highest percentage of rich:",
            highest_earning_country,
        )
        print(
            "Highest percentage of rich people in country:",
            highest_earning_country_percentage,
        )
        print(
            "Top occupations in India:",
            top_IN_occupation,
        )

    return {
    'race_count': race_count,
    'average_age_men': float(average_age_men),
    'percentage_bachelors': float(percentage_bachelors),
    'higher_education_rich': float(higher_education_rich),
    'lower_education_rich': float(lower_education_rich),
    'min_work_hours': int(min_work_hours),
    'rich_percentage': float(rich_percentage),
    'highest_earning_country': highest_earning_country,
    'highest_earning_country_percentage': float(highest_earning_country_percentage),
    'top_IN_occupation': top_IN_occupation
}