import React, { useState } from "react";
import "./App.css";
import Navbar from "./components/navbar/Navbar";
import SearchAndResults from "./components/searchAndResults/searchAndResults";
import Hero from "./components/hero/hero";
import Footer from "./components/footer/footer";
import DataVisComp from "./components/datavis/datavis";

function App() {
	return (
		<>
			<div className="bg-base-100 min-h-screen relative">
				<Navbar />
				<Hero />

				<div className="flex flex-col w-full md:w-96 mx-auto items-center">
					<br />
					<SearchAndResults />
					<br />
					<DataVisComp />
				</div>

				<Footer />
			</div>
		</>
	);
}

export default App;
