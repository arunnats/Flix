import React, { useState } from "react";
import "./App.css";
import Navbar from "./components/navbar/Navbar";
import SearchBar from "./components/searchbar/searchBar";
import SearchResultsList from "./components/searchbar/searchResultsList";

function App() {
	const [results, setResults] = useState([]);

	return (
		<>
			<Navbar />
			<div className="flex flex-col w-96 mx-auto items-center">
				<h1 className="text-4xl font-bold mt-10">Hello, world!</h1>
				<br />
				<div className="search-bar-container">
					<SearchBar setResults={setResults} />
					{results && results.length > 0 && (
						<SearchResultsList results={results} />
					)}
				</div>
			</div>
		</>
	);
}

export default App;
