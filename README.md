# Flix

Flix is a movie recommender app which utilizes the MovieLens database to provide personalized movie recommendations based on user preferences. The app employs a collaborative filtering technique, leveraging a correlation matrix derived from user ratings. It selects the top-rated movies and those with a substantial number of reviews to build a correlation matrix, which forms the backbone of the recommendation engine.

## Features

- **Recommendation Engine**: Generates movie recommendations based on user preferences and ratings.
- **Live Search**: Allows users to search for movies in real-time using a live search feature.
- **Data Visualization**: Visualizes movie data using various graphs and charts to provide insights into movie ratings, genres, and other relevant information.
- **Database Integration**: Utilizes MySQL for storing movie names and facilitating live querying and seamless integration with the recommendation engine.

## Technologies Used

- **Frontend**: React, Tailwind CSS.
- **Backend**: Vite, Node, FastAPI.
- **Database**: MySQL.
- **Data Analysis and Machine Learning Model**: Python, numPy, MathPlotLib, Seaborn, SciKit-Learn.

## How It Works

1. **Data Collection**: The app retrieves movie data from the MovieLens database, including user ratings and movie information.
2. **Correlation Matrix Generation**: It constructs a correlation matrix based on user ratings, focusing on highly-rated movies and those with a significant number of reviews.
3. **Recommendation Generation**: Using the correlation matrix, the app generates movie recommendations tailored to each user's preferences.
4. **Live Search**: Users can search for movies in real-time using the live search feature, which fetches results dynamically as the user types.
5. **Data Visualization**: The app visualizes movie data using various graphs and charts, providing users with insights into movie ratings, genres, and other relevant metrics.

## Machine Learning and Python Usage

The recommendation engine's machine learning model is implemented using Python, leveraging libraries such as numPy, MathPlotLib, Seaborn, and SciKit-Learn. Python is also used for data analysis tasks, including building correlation matrices and exporting them for further processing.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
