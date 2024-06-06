import React, { useEffect, useState } from "react";

import movieIcon from "../../assets/icons8-movie-50.png";
import userIcon from "../../assets/icons8-director-48.png";

const CountUpAnimation = ({
	iconComponent,
	initialValue,
	targetValue,
	text,
	duration = 2000,
}) => {
	const [count, setCount] = useState(initialValue);

	useEffect(() => {
		const increment = Math.ceil((targetValue - initialValue) / (duration / 50));
		const interval = setInterval(() => {
			setCount((prevCount) => {
				const newValue = prevCount + increment;
				if (newValue >= targetValue) {
					clearInterval(interval);
					return targetValue;
				}
				return newValue;
			});
		}, 50);

		return () => {
			clearInterval(interval);
		};
	}, [targetValue, initialValue, duration]);

	return (
		<div className="stat">
			<div className="stat-figure text-primary">
				<img className="min-w-10" src={iconComponent} alt="" />
			</div>
			<div className="stat-title">{text}</div>
			<div className="stat-value text-2xl">{count}</div>
		</div>
	);
};

const Stat = () => {
	return (
		<div className="stats stats-vertical lg:stats-horizontal shadow">
			<CountUpAnimation
				iconComponent={movieIcon}
				initialValue={0}
				targetValue={24319}
				text="Total Movies"
			/>

			<CountUpAnimation
				iconComponent={userIcon}
				initialValue={0}
				targetValue={43897}
				text="Total Users"
			/>
		</div>
	);
};

export default Stat;
