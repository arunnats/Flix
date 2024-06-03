import numpy as np
import pandas as pd

df = pd.read_csv('./ratings.csv', sep=',', usecols=['userId', 'movieId', 'rating'])
movie_titles = pd.read_csv("./movies.csv", sep=',', usecols=['movieId', 'title'])
df = pd.merge(df,movie_titles,on='movieId')

min_reviews_movie = 5
popular_movies = df['title'].value_counts()
top_movies = popular_movies[popular_movies >= min_reviews_movie].index
df_filtered_movies = df[df['title'].isin(top_movies)]

min_reviews_user = 200
users_with_enough_reviews = df_filtered_movies['userId'].value_counts()
active_users = users_with_enough_reviews[users_with_enough_reviews >= min_reviews_user].index
df_filtered_users = df_filtered_movies[df_filtered_movies['userId'].isin(active_users)]

moviemat_filtered = df_filtered_users.pivot_table(index='userId', columns='title', values='rating')

enteredmovie_user_ratings = moviemat_filtered['user input']
similar_to_enteredmovie = moviemat_filtered.corrwith(enteredmovie_user_ratings)
corr_enteredmovie = pd.DataFrame(similar_to_enteredmovie,columns=['Correlation'])
corr_enteredmovie.dropna(inplace=True)
corr_enteredmovie.head()
corr_enteredmovie[corr_enteredmovie['num of ratings']>100].sort_values('Correlation',ascending=False).head()