import pandas as pd

def filter_movies(df, min_reviews_movie):
    popular_movies = df['title'].value_counts()
    top_movies = popular_movies[popular_movies >= min_reviews_movie].index
    return df[df['title'].isin(top_movies)]

def filter_users(df, min_reviews_user):
    users_with_enough_reviews = df['userId'].value_counts()
    active_users = users_with_enough_reviews[users_with_enough_reviews >= min_reviews_user].index
    return df[df['userId'].isin(active_users)]

def create_pivot_table(df):
    return df.pivot_table(index='userId', columns='title', values='rating')

def find_similar_movies(moviemat_filtered, enteredmovie_title, min_num_ratings):
    enteredmovie_user_ratings = moviemat_filtered[enteredmovie_title]
    similar_to_enteredmovie = moviemat_filtered.corrwith(enteredmovie_user_ratings)
    corr_enteredmovie = pd.DataFrame(similar_to_enteredmovie, columns=['Correlation'])
    corr_enteredmovie.dropna(inplace=True)
    corr_enteredmovie = corr_enteredmovie.join(ratings['num of ratings'])
    return corr_enteredmovie[corr_enteredmovie['num of ratings'] > min_num_ratings].sort_values('Correlation', ascending=False)

def main():
    df = pd.read_csv('./ratings.csv', sep=',', usecols=['userId', 'movieId', 'rating'])
    movie_titles = pd.read_csv("./movies.csv", sep=',', usecols=['movieId', 'title'])
    df = pd.merge(df, movie_titles, on='movieId')

    min_reviews_movie = 5
    df_filtered_movies = filter_movies(df, min_reviews_movie)

    min_reviews_user = 200
    df_filtered_users = filter_users(df_filtered_movies, min_reviews_user)

    moviemat_filtered = create_pivot_table(df_filtered_users)

    enteredmovie_title = 'Rain Man (1988)'
    min_num_ratings = 100
    similar_movies = find_similar_movies(moviemat_filtered, enteredmovie_title, min_num_ratings)
    print(similar_movies.head())

if __name__ == "__main__":
    main()
