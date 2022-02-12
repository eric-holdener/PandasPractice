import pandas as pd

# Dataframe is a table with an array of individual entities
# Dataframes are not limited to integers
# Declaring new dataframe - a dictionary whose keys are column names and values are entries
# List of row labels in a Dataframe is an index - assign values using an index parameter
# Series - sequence of values - if DF is table, series is list
# Series is essentially a single DF column - you can use index to assign row values the same way
# Just think of a DF as a lot of series glued together

def practice():
    # smple dataframe declaration
    exDF = pd.DataFrame({'Yes': [50, 21], 'No': [131, 2]})
    print(exDF)

    # using index parameter to assign rows
    exDF = pd.DataFrame({'Bob': ['I liked it.', 'It was awful.'],
              'Sue': ['Pretty good.', 'Bland.']},
             index=['Product A', 'Product B'])
    print(exDF)

    # simple series declaration
    exSeries = pd.Series([1, 2, 3, 4, 5])
    print(exSeries)

    # series with row names in the index - instead of column names, a series has one overall name, ex. product a
    exSeries = pd.Series([30, 35, 40], index=['2015 Sales', '2016 Sales', '2017 Sales'], name='Product A')
    print(exSeries)

    # load practice dataset
    # can use index_col in read_csv to specify a column in the csv that is an index
    wine_reviews = pd.read_csv('C:\\Users\\ehold\\Desktop\\Folders\\Datasets\\winemag-data-130k-v2.csv')

    # use shape() to check size of df is
    print(wine_reviews.shape)

    # use head() for quick examining of top 5 rows of dataset
    print(wine_reviews.head())

    # saves wine reviews DF to csv
    # wine_reviews.to_csv('csv_name.csv')


practice()
