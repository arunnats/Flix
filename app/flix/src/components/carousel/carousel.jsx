import React from "react";
import Card from "../card/card";
import AveRating from "../../assets/graphs/average_rating_distribution.png";
import GenreDist from "../../assets/graphs/genre_distribution.png";
import MovieLenVAverage from "../../assets/graphs/movie_length_vs_average_rating.png";
import NumRatingVAverage from "../../assets/graphs/num_of_ratings_vs_average_rating.png";
import NumRatingDist from "../../assets/graphs/number_of_ratings_distribution.png";
import RatingVNumrating from "../../assets/graphs/rating_vs_num_of_ratings.png";
import RatingDist from "../../assets/graphs/ratings_distribution.png";
import TopMovieDisk from "../../assets/graphs/top_10_weighted_movies.png";
import UserRatingDist from "../../assets/graphs/average_rating_distribution.png";

const Carousel = () => {
	const cardsData = [
		{
			title: "Average Rating Distribution",
			text: "Distribution of average ratings given by users.",
			imageUrl: AveRating,
		},
		{
			title: "Genre Distribution",
			text: "Distribution of genres among movies.",
			imageUrl: GenreDist,
		},
		{
			title: "Movie Length vs. Average Rating",
			text: "Relation between movie length and average rating.",
			imageUrl: MovieLenVAverage,
		},
		{
			title: "Ratings Distribution",
			text: "Distribution of ratings.",
			imageUrl: RatingDist,
		},
		{
			title: "Top 10 Weighted Movies",
			text: "Top 10 movies by weighted rating.",
			imageUrl: TopMovieDisk,
		},
		{
			title: "User Rating Distribution",
			text: "Distribution of average ratings given by users.",
			imageUrl: UserRatingDist,
		},
		{
			title: "Number of Ratings Distribution",
			text: "Distribution of the number of ratings.",
			imageUrl: NumRatingDist,
		},
		{
			title: "Number of Ratings vs. Average Rating",
			text: "Relation between number of ratings and average rating.",
			imageUrl: NumRatingVAverage,
		},
		{
			title: "Rating vs. Number of Ratings",
			text: "Relation between ratings and number of ratings.",
			imageUrl: RatingVNumrating,
		},
	];

	return (
		<div className="carousel carousel-center max-w-[22rem] p-4 space-x-4 bg-neutral rounded-box border-2 shadow-xl border-accent">
			{cardsData.map((card, index) => (
				<div className="carousel-item max-w-xs" key={index}>
					<Card title={card.title} text={card.text} imageUrl={card.imageUrl} />
				</div>
			))}
		</div>
	);
};

export default Carousel;
