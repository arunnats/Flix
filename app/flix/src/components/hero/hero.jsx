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

					<h1 className="mb-6 mt-9 text-8xl font-bold font-custom">flix</h1>
					<p className="mb-3 mt-9 text-l md:text-xl text-accent font-custom">
						Instant movie recommendation model based on:
					</p>
					<div className="my-3">
						<Stat />
					</div>
				</div>
				<br />
				<h1 className=" my-5 text-3xl md:text-5xl text-accent font-custom ">
					Get Recommendations
				</h1>
				<h2 className=" mb-1 text-2xl md:text-3xl text-accent font-custom ">
					Enter a Movie Title{""}
				</h2>
				<SearchAndResults />
			</div>
			<div className="absolute bottom-0 w-full h-96 bg-gradient-to-b from-transparent to-base-100">
				{" "}
			</div>
		</div>
	);
};

export default Hero;
