import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.font_manager import FontProperties

# Load the data
ratings = pd.read_csv('../data/ratings.csv', sep=',', usecols=['userId', 'movieId', 'rating'])
movies = pd.read_csv('../data/movies.csv', sep=',', usecols=['movieId', 'title', 'genres'])

# Merge the ratings and movies dataframes
merged_df = pd.merge(ratings, movies, on='movieId')

# Calculate ratings statistics
ratings_stats = merged_df.groupby('title')['rating'].agg(['mean', 'count']).rename(columns={'mean': 'rating', 'count': 'num of ratings'})

sns.set_style("white")
plt.rcParams.update({
    'axes.facecolor': '#FFFFF0',
    'axes.edgecolor': '#FFFFF0',
    'axes.labelcolor': '#FFFFF0',
    'xtick.color': '#FFFFF0',
    'ytick.color': '#FFFFF0',
    
    'text.color': '#FFFFF0',
    'figure.facecolor': '#25233D',
    'grid.color': '#25233D'
})
colors = ["#E30C32", "#E30C32"]

def apply_plot_style():
    SIZE_DEFAULT = 10
    SIZE_LARGE = 12
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
ax.set_facecolor('#25233D')
ax.grid(False)
plt.tight_layout()
plt.savefig('number_of_ratings_distribution.png', dpi=300)
plt.close()

# Distribution of Ratings
apply_plot_style()
fig, ax = plt.subplots(figsize=(6, 4.8))  # 1.25:1 aspect ratio
ratings_stats['rating'].hist(bins=70, color=colors[1], ax=ax)
ax.set_title('Distribution of Ratings')
ax.set_xlabel('Rating')
ax.set_ylabel('Frequency')
ax.set_facecolor('#25233D')
ax.grid(False)
plt.tight_layout()
plt.savefig('ratings_distribution.png', dpi=300)
plt.close()

# Jointplot of Rating vs Number of Ratings
apply_plot_style()
g = sns.jointplot(x='rating', y='num of ratings', data=ratings_stats, alpha=0.5, kind='scatter', color=colors[0], height=6, ratio=4, marginal_kws={'bins': 20, 'fill': True})
g.fig.suptitle('Number of Ratings vs Rating', y=1.03)
g.set_axis_labels('Rating', 'Number of Ratings')
g.ax_joint.set_facecolor('#25233D')
g.ax_marg_x.set_facecolor('#25233D')
g.ax_marg_y.set_facecolor('#25233D')
g.ax_joint.grid(False)
plt.tight_layout()
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
ax.set_xticklabels(top_10_weighted.index, rotation=70, fontsize=6)
ax.set_facecolor('#25233D')
ax.grid(False)
plt.tight_layout()
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
ax.set_facecolor('#25233D')
ax.grid(False)
plt.tight_layout()
plt.savefig('average_rating_distribution.png', dpi=300)
plt.close()

# Jointplot of Number of Ratings Given by Users vs Average Rating
apply_plot_style()
g = sns.jointplot(x='average_rating', y='num_of_ratings', data=user_stats, alpha=0.5, kind='scatter', color=colors[1], height=6, ratio=4, marginal_kws={'bins': 20, 'fill': True})
g.fig.suptitle('Number of Ratings vs Average Rating', y=1.03)
g.set_axis_labels('Average Rating', 'Number of Ratings')
g.ax_joint.set_facecolor('#25233D')
g.ax_marg_x.set_facecolor('#25233D')
g.ax_marg_y.set_facecolor('#25233D')
g.ax_joint.grid(False)
plt.tight_layout()
plt.savefig('num_of_ratings_vs_average_rating.png', dpi=300)
plt.close()

# Load genres data
genres = pd.read_csv('../data/movies.csv', sep=',', usecols=['genres'])

# Split genres into separate rows
genres = genres['genres'].str.split('|', expand=True).stack().reset_index(level=1, drop=True)

# Plot genre distribution
plt.figure(figsize=(6, 4.8))  # 1.25:1 aspect ratio
ax = genres.value_counts().plot(kind='bar', color=colors[0])
ax.set_facecolor('#25233D')
ax.set_title('Genre Distribution')
ax.set_xlabel('Genre')
ax.set_ylabel('Frequency')
ax.grid(False)
plt.xticks(rotation=45, fontsize=6)
plt.tight_layout()
plt.savefig('genre_distribution.png', dpi=300)
plt.close()

# Merge ratings with movies including genres
merged_df = pd.merge(ratings, movies, on='movieId')

# Split genres into separate rows
genres_df = merged_df['genres'].str.get_dummies('|')

# Combine genres with ratings
ratings_genres = pd.concat([merged_df[['title', 'rating']], genres_df], axis=1)

# Calculate average ratings by genre
# average_ratings_by_genre = ratings_genres.groupby('title').agg({'rating': 'mean', 'Action': 'sum', 'Adventure': 'sum', 'Animation': 'sum', 'Children': 'sum', 'Comedy': 'sum', 'Crime': 'sum', 'Documentary': 'sum', 'Drama': 'sum', 'Fantasy': 'sum', 'Film-Noir': 'sum', 'Horror': 'sum', 'IMAX': 'sum', 'Musical': 'sum', 'Mystery': 'sum', 'Romance': 'sum', 'Sci-Fi': 'sum', 'Thriller': 'sum', 'War': 'sum', 'Western': 'sum'}).reset_index()

# Plot average ratings by genre
# plt.figure(figsize=(6, 4.8))  # 1.25:1 aspect ratio
# ax = average_ratings_by_genre.mean().drop(['rating', 'title']).plot(kind='bar', color=colors[0])
# ax.set_facecolor('#25233D')
# ax.set_title('Average Ratings by Genre')
# ax.set_xlabel('Genre')
# ax.set_ylabel('Average Rating')
# ax.grid(False)
# plt.xticks(rotation=45, fontsize=6)
# plt.tight_layout()
# plt.savefig('average_ratings_by_genre.png', dpi=300)
# plt.close()

# Plot user rating distribution
plt.figure(figsize=(6, 4.8))  # 1.25:1 aspect ratio
ax = ratings['rating'].hist(bins=5, color=colors[1])
ax.set_facecolor('#25233D')
ax.set_title('User Rating Distribution')
ax.set_xlabel('Rating')
ax.set_ylabel('Frequency')
ax.grid(False)
plt.tight_layout()
plt.savefig('user_rating_distribution.png', dpi=300)
plt.close()

# Load movie length data
movie_lengths = pd.read_csv('../data/movies.csv', sep=',', usecols=['title', 'movieId'])

# Merge with ratings
merged_df = pd.merge(ratings, movie_lengths, on='movieId')

# Plot movie length vs. average rating
plt.figure(figsize=(6, 4.8))  # 1.25:1 aspect ratio
ax = merged_df.groupby('title').agg({'rating': 'mean', 'movieId': 'count'}).plot(kind='scatter', x='movieId', y='rating', color=colors[0])
ax.set_facecolor('#25233D')
ax.set_title('Movie Length vs. Average Rating')
ax.set_xlabel('Movie Length (Number of Ratings)')
ax.set_ylabel('Average Rating')
ax.grid(False)
plt.tight_layout()
plt.savefig('movie_length_vs_average_rating.png', dpi=300)
plt.close()
