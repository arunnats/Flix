import React from "react";
import Carousel from "../carousel/carousel";

const DataVisComp = () => {
	return (
		<div className="flex flex-col items-center my-5">
			<h1 className="text-5xl my-3 text-accent font-custom " id="data-analysis">
				Data Analysis
			</h1>
			<Carousel />
		</div>
	);
};

export default DataVisComp;
