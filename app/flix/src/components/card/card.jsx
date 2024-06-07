import React from "react";

const Card = ({ title, text, imageUrl }) => {
	return (
		<div className="card card-compact max-w-xs bg-base-100 border-2 shadow-xl border-accent">
			<figure className="overflow-hidden">
				<img
					className="w-full h-full object-cover"
					src={imageUrl}
					alt={title}
				/>
			</figure>
			<div className="card-body flex flex-col justify-between">
				<h2 className="text-2xl text-center card-title text-accent font-customRoboto">
					{title}
				</h2>
				<p className="text-l text-justify font-customRoboto">{text}</p>
			</div>
		</div>
	);
};

export default Card;
