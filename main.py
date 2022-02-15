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


# load practice dataset
# can use index_col in read_csv to specify a column in the csv that is an index
# windows
wine_reviews = pd.read_csv('C:\\Users\\ehold\\Desktop\\Folders\\Datasets\\winemag-data-130k-v2.csv', index_col=0)
# mac
# wine_reviews = pd.read_csv(r"/Users/eric/Desktop/winemag-data-130k-v2.csv", index_col=0)

def createReadWrite(wine_reviews):
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

    # use shape() to check size of df is
    print(wine_reviews.shape)

    # use head() for quick examining of top 5 rows of dataset
    print(wine_reviews.head())

    # saves wine reviews DF to csv
    # wine_reviews.to_csv('csv_name.csv')


def indexSelectAssign(wine_reviews):
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

    # generates a high level summary of the attributes in a column - only makes sense for numeric columns
    print(wine_reviews.points.describe())

    # other good functions to see some summary stats are - unique, mean, value_counts


def summaryFunctionMaps(wine_reviews):
    # map is a function that takes one set of values and "maps" them to another set of values
    # map() should expect a single value from the series (a point value, in the below example), and returns a transformed version of the value
    # in the below, we remapped each point to remean the scores to 0
    # review_points_mean = wine_reviews.points.mean()
    # print('Map() function')
    # print(wine_reviews.points.map(lambda p: p - review_points_mean))

    # apply is an equivalent method to transform a whole DF by calling a custom method on each row
    # if we called apply() with axis='index' then we would need a function to transform each column, not row
    # def remean_points(row):
    #     row.points = row.points - review_points_mean
    #     return row
    #
    # print('Apply() function')
    # print(wine_reviews.apply(remean_points, axis='columns'))

    # map and apply return new, transformed series and dfs - they dont modify the original data they're called on

    # pandas has mapping operations build in
    # this is a faster way to remean the points column
    # pandas understands how to interpret a lot of values on one side and a single value
    review_points_mean = wine_reviews.points.mean()
    # lot of values - points vs single value - mean. Mean gets applied to every value
    print(wine_reviews.points - review_points_mean)
    # pandas can also do series of equal length
    # country and region 1 are the same length
    print(wine_reviews.country + ' - ' + wine_reviews.region_1)
    # these quick operations are faster than map or apply but cant do as advanced of things as map and apply

    # creating a series of star_ratings to apply to each row based on score or being in canada
    # def stars(row):
    #     if row.country == 'Canada':
    #         return 3
    #     elif row.points >= 95:
    #         return 3
    #     elif row.points >= 85:
    #         return 2
    #     else:
    #         return 1
    #
    # star_ratings = wine_reviews.apply(stars, axis='columns')


def groupSort(wine_reviews):
    # if we want to group data and operate on the group, we use groupby(), instead of map and apply which iterates over every row
    # replacing value counts by a groupby - value counts is just a shortcut to groupby
    # created a group of reviews which had the same point values for a wine, then we grabbed the points column in the group and counted how many times it appeared
    print(wine_reviews.groupby('points').points.count())
    # any summary functions can be replaced by using groupbys

    # each group can be thought of as a slice of the dataframe containing only data with values that match. You can access this sliced dataframe by using apply, and can manipulate from there however we want
    print(wine_reviews.groupby('winery').apply(lambda df: df.title.iloc[0]))

    # if you want even more control you can group by multiple columns
    print(wine_reviews.groupby(['country', 'province']).apply(lambda df: df.loc[df.points.idxmax()]))

    # agg() lets you run different functions on your groupby df simultaneously
    print(wine_reviews.groupby(['country']).price.agg([len, min, max]))

    # multi indexes can occur from groupbys - a df with more than one index
    # kind of looks like a multi row pivot table
    countries_reviewed = wine_reviews.groupby(['country', 'province']).description.agg([len])
    print(countries_reviewed)
    # check index type
    mi = countries_reviewed.index
    print(type(mi))

    # the most common multi index method to use is just reverting back to a single index
    countries_reviewed = countries_reviewed.reset_index()
    print(countries_reviewed)
    # check index type
    mi = countries_reviewed.index
    print(type(mi))

    # groupyby returns in index order, if we want to sort any other way we call sort_values()
    print(countries_reviewed.sort_values(by='len'))

    # sort_values defaults to ascending, set ascendign to false for descending
    print(countries_reviewed.sort_values(by='len', ascending=False))

    # sorting on index values
    print(countries_reviewed.sort_index())

    # sort by multiple values by passing a list to sort_values()
    print(countries_reviewed.sort_values(by=['country', 'len']))


def dtypesMissingValues(wine_reviews):
    # use dtype to grab the typ eof a specific column
    print(wine_reviews.price.dtype)

    # or you can grab dtype on every column
    print(wine_reviews.dtypes)

    # can convert datatypes using astype
    wine_reviews.points.astype('float64')

    # access dtype of the entire df
    print(wine_reviews.index.dtype)

    # select null values with is null
    print(wine_reviews[pd.isnull(wine_reviews.country)])

    # replacing missing values is a common operation
    # use fillna()
    wine_reviews.region_2.fillna('Unknown')

    # can also replace non null values with replace()
    wine_reviews.taster_twitter_handle.replace('@kerinokeefe', '@kerino')


def renameCombine(wine_reviews):
    # rename lets you change index or column names
    wine_reviews.rename(columns={'points': 'score'})

    # renaming indexes using dictionary {index1: name1 , index2: name2}
    # set_index() is usually more convenient, as renaming indexes is rare
    wine_reviews.rename(index={0: 'firstEntry', 1: 'secondEntry'})

    # you can name the row index and the column indexes with rename axis
    wine_reviews.rename_axis('wines', axis='rows').rename_axis('fields', axis='columns')

    # you can combine dfs with concat() join() and merge()
    canadian_youtube = pd.read_csv('C:\\Users\\ehold\\Desktop\\Folders\\Datasets\\CAvideos.csv', index_col=0)

    british_youtube = pd.read_csv('C:\\Users\\ehold\\Desktop\\Folders\\Datasets\\GBvideos.csv', index_col=0)

    # given a list of elements, concat will just push these elements together along an axis
    print(pd.concat([canadian_youtube, british_youtube]))

    # join lets you combine different df with an index in common
    # similar to an sql join with left right etc
    left = canadian_youtube.set_index(['title', 'trending_date'])
    right = british_youtube.set_index(['title', 'trending_date'])

    left.join(right, lsuffix='_CAN', rsuffix='_UK')
