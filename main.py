import pandas as pd

# Dataframe is a table with an array of individual entities
# Dataframes are not limited to integers
# Declaring new dataframe - a dictionary whose keys are column names and values are entries
# List of row labels in a Dataframe is an index - assign values using an index parameter
# Series - sequence of values - if DF is table, series is list
# Series is essentially a single DF column - you can use index to assign row values the same way
# Just think of a DF as a lot of series glued together
# You can select attributes in a pandas dataframe in the same way you select properties of a class
# Pandas has Loc and iLoc - both are row first, column second ([,])
# iloc selects like normal python - 0:10 picks 0-9, whereas loc indexes exclusively, meaning 0:10 is 0-10

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
    wine_reviews = pd.read_csv('C:\\Users\\ehold\\Desktop\\Folders\\Datasets\\winemag-data-130k-v2.csv', index_col=0)

    # use shape() to check size of df is
    print(wine_reviews.shape)

    # use head() for quick examining of top 5 rows of dataset
    print(wine_reviews.head())

    # saves wine reviews DF to csv
    # wine_reviews.to_csv('csv_name.csv')

    # accessing the country column of the wine reviews data set
    print(wine_reviews.country)

    # an alternative way to access the country column
    # this alternative allows you to use column names with reserved characters in them (like a space)
    print(wine_reviews['country'])

    # access a specific row within the country column
    print(wine_reviews['country'][0])

    # index based selection - selecting data based on its numerical position in the data
    print(wine_reviews.iloc[0])

    # retrieve column zero with iloc
    print(wine_reviews.iloc[:, 0])

    # use : to select everything before row 3
    print(wine_reviews.iloc[:3, 0])

    # can also pass a list to iloc
    print(wine_reviews.iloc[[0, 1, 2], 0])

    # negative numbers start from the back of the dataset
    print(wine_reviews.iloc[-5])

    # loc is label based selection - data index value matters, not position
    print(wine_reviews.loc[0, 'country'])

    # Loc can be easier to use when your dataset has meaningful indices, iloc is conceptually simpler
    print(wine_reviews.loc[:, ['taster_name', 'taster_twitter_handle', 'points']])

    # you can manipulate the index with set_index - you are not stuck with your index
    # wine_reviews.set_index('title')

    # You can do conditional selection based on dataframes - this returns true if the country is italy
    print(wine_reviews.country == 'Italy')

    # now we can use this logic inside loc to only select italy
    print(wine_reviews.loc[wine_reviews.country == 'Italy'])

    # you can expand this with basic python logic to do multiple conditions for a select
    print(wine_reviews.loc[(wine_reviews.country == 'Italy') & (wine_reviews.points >= 90)])
    print(wine_reviews.loc[(wine_reviews.country == 'Italy') | (wine_reviews.points >= 90)])

    # you can also use the isin operator exclusive to pandas to select items that are in a list of values
    print(wine_reviews.loc[wine_reviews.country.isin(['Italy', 'France'])])

    # isnull and notnull let you select / not select values based on if they are null
    print(wine_reviews.loc[wine_reviews.price.notnull()])

    # you can assign values to a df very easily
    # wine_reviews['critic'] = 'everyone'



practice()
