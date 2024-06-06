import React from "react";
import Stat from "../stat/stat";

const Hero = () => {
	return (
		<div
			className="hero min-h-screen bg-cover bg-center"
			style={{
				backgroundImage:
					"url(https://img.pikbest.com/ai/illus_our/20230422/83a8dec832f43af3bc88c44e3223e9b2.jpg!w700wp)",
			}}
		>
			<div className="hero-overlay bg-opacity-85"></div>
			<div className="hero-content text-center text-neutral-content px-4">
				<div className="max-w-md mx-auto">
					<h1 className="mb-5 text-5xl font-bold">FLiX</h1>
					<p className="mb-5 text-xl text-accent">
						Instant movie recommendation model based on:
					</p>
					<div className="my-3">
						<Stat />
					</div>
					<button className="btn btn-primary">Start Watching!</button>
				</div>
			</div>
		</div>
	);
};

export default Hero;
