import React from "react";
import Card from "../card/card";

const Carousel = () => {
	return (
		<div className="carousel carousel-center max-w-md p-4 space-x-4 bg-neutral rounded-box">
			<div className="carousel-item">
				<Card />
			</div>
			<div className="carousel-item">
				<Card />
			</div>
			<div className="carousel-item">
				<Card />
			</div>
			<div className="carousel-item">
				<Card />
			</div>
			<div className="carousel-item">
				<Card />
			</div>
		</div>
	);
};

export default Carousel;
