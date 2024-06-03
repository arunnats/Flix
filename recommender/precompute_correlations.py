import pandas as pd

def precompute_and_save():
    print("Reading ratings and movie titles data...")
    df_ratings = pd.read_csv('./data/ratings.csv', sep=',', usecols=['userId', 'movieId', 'rating'])
    df_titles = pd.read_csv("./data/movies.csv", sep=',', usecols=['movieId', 'title'])
    print("Done reading.")

    print("Merging dataframes...")
    df = pd.merge(df_ratings, df_titles, on='movieId')

    # Calculate number of ratings per movie
    print("Calculating ratings per movie...")
    ratings = pd.DataFrame(df.groupby('title')['rating'].mean())
    ratings['num of ratings'] = pd.DataFrame(df.groupby('title')['rating'].count())

    min_reviews_movie = 15
    min_reviews_user = 150

    # Filter movies with at least 'x' reviews
    print("Filtering movies...")
    popular_movies = df['title'].value_counts()
    top_movies = popular_movies[popular_movies >= min_reviews_movie].index
    df_filtered_movies = df[df['title'].isin(top_movies)]

    # Filter users with at least 'x' reviews
    print("Filtering users...")
    users_with_enough_reviews = df_filtered_movies['userId'].value_counts()
    active_users = users_with_enough_reviews[users_with_enough_reviews >= min_reviews_user].index
    df_filtered_users = df_filtered_movies[df_filtered_movies['userId'].isin(active_users)]

    # Create the pivot table
    print("Creating pivot table...")
    moviemat_filtered = df_filtered_users.pivot_table(index='userId', columns='title', values='rating')
    print("Setup complete.")

    # Calculate the correlation matrix between movies
    print("Calculating correlation matrix...")
    corr_matrix = moviemat_filtered.corr(method='pearson')
    print("Correlation matrix calculation complete.")

    # Save the correlation matrix and ratings DataFrame to disk
    corr_matrix.to_pickle('correlation_matrix.pkl')
    ratings.to_pickle('ratings.pkl')
    print("Correlation matrix and ratings saved to disk.")

if __name__ == "__main__":
    precompute_and_save()
