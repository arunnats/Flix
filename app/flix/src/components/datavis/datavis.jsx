import React from "react";
import Carousel from "../carousel/carousel";
import AveRating from "../../assets/graphs/average_rating_distribution.png";
import GenreDist from "../../assets/graphs/genre_distribution.png";
import MovieLenVAverage from "../../assets/graphs/movie_length_vs_average_rating.png";
import NumRatingVAverage from "../../assets/graphs/num_of_ratings_vs_average_rating.png";
import NumRatingDist from "../../assets/graphs/number_of_ratings_distribution.png";
import RatingVNumrating from "../../assets/graphs/rating_vs_num_of_ratings.png";
import RatingDist from "../../assets/graphs/ratings_distribution.png";
import TopMovieDisk from "../../assets/graphs/top_10_weighted_movies.png";
import UserRatingDist from "../../assets/graphs/average_rating_distribution.png";

const DataVisComp = () => {
	return (
		<div className="flex flex-col my-2">
			<h1 text-xl my-1>
				Data Analysis
			</h1>
			<Carousel />
		</div>
	);
};

export default DataVisComp;
