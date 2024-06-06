import React from "react";

const Card = ({ title, text, imageUrl }) => {
	return (
		<div className="card card-compact max-w-xs bg-base-100 shadow-xl">
			<figure className="overflow-hidden">
				<img
					className="w-full h-full object-cover"
					src={imageUrl}
					alt={title}
				/>
			</figure>
			<div className="card-body flex flex-col justify-between">
				<h2 className="card-title">{title}</h2>
				<p>{text}</p>
			</div>
		</div>
	);
};

export default Card;
