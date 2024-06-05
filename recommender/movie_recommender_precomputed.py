from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
import random

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def load_precomputed_data():
    global app
    print("Loading precomputed correlation matrix and ratings...")
    app.state.corr_matrix = pd.read_pickle('./pickles/correlation_matrix.pkl')
    app.state.ratings = pd.read_pickle('./pickles/ratings.pkl')
    print("Precomputed data loaded.")

@asynccontextmanager
async def lifespan(app: FastAPI):
    load_precomputed_data()
    yield

app.router.lifespan_context = lifespan

@app.get("/recommend/")
async def get_usage(movie_title: str):
    if movie_title not in app.state.corr_matrix.index:
        print(f"Movie '{movie_title}' not found in correlation matrix.")
        return {"error": "Movie not found"}
    
    # Select the correlation data for the specified movie title
    corr_movie = app.state.corr_matrix.loc[movie_title]
    print(f"Correlation data for '{movie_title}':\n{corr_movie.head()}")  # Log the correlation data

    # Drop NaN values in the correlation data
    corr_movie.dropna(inplace=True)
    print(f"Correlation data after dropping NaNs:\n{corr_movie.head()}")  # Log after dropping NaNs
    
    # Create a DataFrame from the correlation data
    corr_movie_df = pd.DataFrame({'Correlation': corr_movie})
    print(f"Correlation data in DataFrame format:\n{corr_movie_df.head()}") 
    
    # Join with the ratings DataFrame
    corr_movie_df = corr_movie_df.join(app.state.ratings['num of ratings'])
    print(f"Correlation data after joining ratings:\n{corr_movie_df.head()}")  # Log after joining ratings
    
    # Filter movies with enough ratings
    corr_movie_df = corr_movie_df[corr_movie_df['num of ratings'] > 700]
    
    # Sort by correlation in descending order
    corr_movie_df = corr_movie_df.sort_values(by='Correlation', ascending=False)
    print(f"Final recommendation result:\n{corr_movie_df.head()}")
    
    return corr_movie_df.head().to_dict()

@app.get("/random-movies/")
async def get_random_movies():
    random_movies = random.sample(list(app.state.corr_matrix.columns), 5)
    return {"random_movies": random_movies}
