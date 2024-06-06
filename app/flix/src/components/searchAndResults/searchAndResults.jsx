import React from "react";

import SearchBar from "../searchbar/searchBar";
import SearchResultsList from "../searchbar/searchResultsList";
import Results from "../results/results";
import axios from "axios";
import { useState } from "react";

const SearchAndResults = () => {
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
		<div className="search-bar-container w-full flex flex-col justify-center items-center ">
			<SearchBar setResults={setResults} />
			{results && results.length > 0 && (
				<SearchResultsList
					results={results}
					onResultClick={getRecommendations}
					className="bg-white shadow-lg rounded-lg overflow-hidden absolute z-9999"
				/>
			)}
			<br />
			<Results className="relative z-40" recommendations={recommendations} />
		</div>
	);
};

export default SearchAndResults;
