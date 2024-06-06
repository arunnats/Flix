import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.font_manager import FontProperties

# Load the data
ratings = pd.read_csv('../data/ratings.csv', sep=',', usecols=['userId', 'movieId', 'rating'])
movies = pd.read_csv('../data/movies.csv', sep=',', usecols=['movieId', 'title'])

# Merge the ratings and movies dataframes
merged_df = pd.merge(ratings, movies, on='movieId')

# Calculate ratings statistics
ratings_stats = merged_df.groupby('title')['rating'].agg(['mean', 'count']).rename(columns={'mean': 'rating', 'count': 'num of ratings'})

# Define plot style and colors
sns.set_style("whitegrid")
colors = ["#E30C32", "#070521"]

def apply_plot_style():
    SIZE_DEFAULT = 14
    SIZE_LARGE = 16
    plt.rc("font", family="Roboto-Medium")
    plt.rc("font", weight="normal")
    plt.rc("font", size=SIZE_DEFAULT)
    plt.rc("axes", titlesize=SIZE_LARGE)
    plt.rc("axes", labelsize=SIZE_LARGE)
    plt.rc("xtick", labelsize=SIZE_DEFAULT)
    plt.rc("ytick", labelsize=SIZE_DEFAULT)
    
    prop = FontProperties(fname="Roboto-Medium.ttf")  # Provide the path to your TTF file
    plt.rcParams['font.family'] = prop.get_name()

# Distribution of Number of Ratings
apply_plot_style()
fig, ax = plt.subplots(figsize=(6, 4.8))  # 1.25:1 aspect ratio
ratings_stats['num of ratings'].hist(bins=100, color=colors[0], ax=ax)
ax.set_title('Distribution of Number of Ratings')
ax.set_xlabel('Number of Ratings')
ax.set_ylabel('Frequency')
plt.savefig('number_of_ratings_distribution.png', dpi=300)
plt.close()

# Distribution of Ratings
apply_plot_style()
fig, ax = plt.subplots(figsize=(6, 4.8))  # 1.25:1 aspect ratio
ratings_stats['rating'].hist(bins=70, color=colors[1], ax=ax)
ax.set_title('Distribution of Ratings')
ax.set_xlabel('Rating')
ax.set_ylabel('Frequency')
plt.savefig('ratings_distribution.png', dpi=300)
plt.close()

# Jointplot of Rating vs Number of Ratings
apply_plot_style()
sns.jointplot(x='rating', y='num of ratings', data=ratings_stats, alpha=0.5, kind='scatter', color=colors[0], height=6, ratio=4)
plt.xlabel('Rating')
plt.ylabel('Number of Ratings')
plt.title('Number of Ratings vs Rating')
plt.savefig('rating_vs_num_of_ratings.png', dpi=300)
plt.close()

# Weighted rating calculation
def weighted_rating(x, m, C):
    v = x['num of ratings']
    R = x['rating']
    return (v / (v + m) * R) + (m / (v + m) * C)

# Average rating across all movies
C = ratings_stats['rating'].mean()

# Minimum number of ratings to be listed in top rated
m = ratings_stats['num of ratings'].quantile(0.90)

# Filter out movies with fewer ratings than the threshold
qualified_movies = ratings_stats[ratings_stats['num of ratings'] >= m].copy()

# Calculate the weighted rating
qualified_movies['weighted_rating'] = qualified_movies.apply(lambda x: weighted_rating(x, m, C), axis=1)

# Top 10 Movies by Weighted Rating
top_10_weighted = qualified_movies.sort_values('weighted_rating', ascending=False).head(10)

apply_plot_style()
fig, ax = plt.subplots(figsize=(6, 4.8))  # 1.25:1 aspect ratio
top_10_weighted['weighted_rating'].plot(kind='bar', color=colors[0], ax=ax)
ax.set_title('Top 10 Movies by Weighted Rating')
ax.set_xlabel('Movie Title')
ax.set_ylabel('Weighted Rating')
ax.set_xticks(range(10))
ax.set_xticklabels(top_10_weighted.index, rotation=45)
plt.savefig('top_10_weighted_movies.png', dpi=300)
plt.close()

# User analysis
user_stats = merged_df.groupby('userId')['rating'].agg(['mean', 'count']).rename(columns={'mean': 'average_rating', 'count': 'num_of_ratings'})

# Distribution of Average Rating Given by Users
apply_plot_style()
fig, ax = plt.subplots(figsize=(6, 4.8))  # 1.25:1 aspect ratio
user_stats['average_rating'].hist(bins=100, color=colors[1], ax=ax)
ax.set_title('Distribution of Average Rating Given by Users')
ax.set_xlabel('Average Rating')
ax.set_ylabel('Frequency')
plt.savefig('average_rating_distribution.png', dpi=300)
plt.close()

# Jointplot of Number of Ratings Given by Users vs Average Rating
apply_plot_style()
sns.jointplot(x='average_rating', y='num_of_ratings', data=user_stats, alpha=0.5, kind='scatter', color=colors[1],  height=6, ratio=4)
plt.xlabel('Average Rating')
plt.ylabel('Number of Ratings')
plt.title('Number of Ratings vs Average Rating')
plt.savefig('num_of_ratings_vs_average_rating.png', dpi=300)
plt.close()

# Load genres data
genres = pd.read_csv('./data/movies.csv', sep=',', usecols=['genres'])

# Split genres into separate rows
genres = genres['genres'].str.split('|', expand=True).stack().reset_index(level=1, drop=True)

# Plot genre distribution
plt.figure(figsize=(6, 4.8))  # 1.25:1 aspect ratio
genres.value_counts().plot(kind='bar', color=colors[0])
plt.title('Genre Distribution')
plt.xlabel('Genre')
plt.ylabel('Frequency')
plt.xticks(rotation=45)
plt.savefig('genre_distribution.png', dpi=300)
plt.close()

# Convert timestamp to datetime
ratings['timestamp'] = pd.to_datetime(ratings['timestamp'], unit='s')

# Extract year from timestamp
ratings['year'] = ratings['timestamp'].dt.year

# Plot user ratings over time
plt.figure(figsize=(6, 4.8))  # 1.25:1 aspect ratio
ratings.groupby('year')['rating'].mean().plot(color=colors[1])
plt.title('Average User Ratings Over Time')
plt.xlabel('Year')
plt.ylabel('Average Rating')
plt.savefig('user_ratings_over_time.png', dpi=300)
plt.close()

# Merge ratings with movies including genres
merged_df = pd.merge(ratings, movies, on='movieId')

# Split genres into separate rows
genres_df = merged_df['genres'].str.get_dummies('|')

# Combine genres with ratings
ratings_genres = pd.concat([ratings, genres_df], axis=1)

# Calculate average ratings by genre
average_ratings_by_genre = ratings_genres.groupby('title').agg({'rating': 'mean', 'Action': 'sum', 'Adventure': 'sum', 'Animation': 'sum', 'Children': 'sum', 'Comedy': 'sum', 'Crime': 'sum', 'Documentary': 'sum', 'Drama': 'sum', 'Fantasy': 'sum', 'Film-Noir': 'sum', 'Horror': 'sum', 'IMAX': 'sum', 'Musical': 'sum', 'Mystery': 'sum', 'Romance': 'sum', 'Sci-Fi': 'sum', 'Thriller': 'sum', 'War': 'sum', 'Western': 'sum'}).reset_index()

# Plot average ratings by genre
plt.figure(figsize=(6, 4.8))  # 1.25:1 aspect ratio
average_ratings_by_genre.mean().drop(['rating', 'title']).plot(kind='bar', color=colors[0])
plt.title('Average Ratings by Genre')
plt.xlabel('Genre')
plt.ylabel('Average Rating')
plt.xticks(rotation=45)
plt.savefig('average_ratings_by_genre.png', dpi=300)
plt.close()


# Plot user rating distribution
plt.figure(figsize=(6, 4.8))  # 1.25:1 aspect ratio
ratings['rating'].hist(bins=5, color=colors[1])
plt.title('User Rating Distribution')
plt.xlabel('Rating')
plt.ylabel('Frequency')
plt.savefig('user_rating_distribution.png', dpi=300)
plt.close()

# Load movie length data
movie_lengths = pd.read_csv('./data/movies.csv', sep=',', usecols=['title', 'movieId'])

# Merge with ratings
merged_df = pd.merge(ratings, movie_lengths, on='movieId')

# Plot movie length vs. average rating
plt.figure(figsize=(6, 4.8))  # 1.25:1 aspect ratio
merged_df.groupby('title').agg({'rating': 'mean', 'movieId': 'count'}).plot(kind='scatter', x='movieId', y='rating', color=colors[0])
plt.title('Movie Length vs. Average Rating')
plt.xlabel('Movie Length (Number of Ratings)')
plt.ylabel('Average Rating')
plt.savefig('movie_length_vs_average_rating.png', dpi=300)
plt.close()
