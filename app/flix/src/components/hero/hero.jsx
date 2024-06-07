import React from "react";
import Stat from "../stat/stat";
import heroBg from "../../assets/hero-bg.jpg";
import SearchAndResults from "../searchAndResults/searchAndResults";

const Hero = () => {
	return (
		<div
			className="relative min-h-screen bg-cover bg-center"
			style={{
				backgroundImage: `url(${heroBg})`,
			}}
		>
			<div className="absolute inset-0 bg-base-100 bg-opacity-50"></div>
			<div className="relative z-10 text-center text-neutral-content px-4">
				<div className="max-w-md mx-auto">
					<br />

					<h1 className="mb-5 text-5xl font-bold">FLiX</h1>
					<p className="mb-5 text-xl text-accent">
						Instant movie recommendation model based on:
					</p>
					<div className="my-3">
						<Stat />
					</div>
					<button className="btn btn-primary">Start Watching!</button>
				</div>
				<h1 className=" mb-5 text-6xl text-accent">Enter a Movie Title </h1>
				<SearchAndResults />
			</div>
			<div className="absolute bottom-0 w-full h-96 bg-gradient-to-b from-transparent to-base-100">
				{" "}
			</div>
		</div>
	);
};

export default Hero;
