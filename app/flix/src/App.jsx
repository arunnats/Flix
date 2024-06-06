import React, { useState } from "react";
import "./App.css";
import Navbar from "./components/navbar/Navbar";
import SearchBar from "./components/searchbar/searchBar";
import SearchResultsList from "./components/searchbar/searchResultsList";
import Results from "./components/results/results";
import Hero from "./components/hero/hero";
import dataVisComp from "./components/stat/stat";
import axios from "axios";

function App() {
	const [results, setResults] = useState([]);
	const [recommendations, setRecommendations] = useState([]);

	const getRecommendations = async (result) => {
		try {
			const response = await axios.get(
				`http://127.0.0.1:8000/recommend/?movie_title=${result}`
			);
			const recommendationTitles = Object.keys(response.data.Correlation);
			setRecommendations(recommendationTitles);
		} catch (error) {
			console.error("Error fetching recommendations:", error);
		}
	};

	return (
		<>
			<div className="bg-base-100 min-h-screen">
				<Navbar />
				<Hero />
				<div className="flex flex-col w-96 mx-auto items-center">
					<br />
					{recommendations && recommendations.length > 0 && (
						<Results recommendations={recommendations} />
					)}
					<br />
					<dataVisComp />
					<br />
					<div className="search-bar-container">
						<SearchBar setResults={setResults} />
						{results && results.length > 0 && (
							<SearchResultsList
								results={results}
								onResultClick={getRecommendations}
							/>
						)}
					</div>
				</div>
			</div>
		</>
	);
}

export default App;
