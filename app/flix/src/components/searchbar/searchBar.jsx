import React, { useState } from "react";
import { FaSearch } from "react-icons/fa";
import axios from "axios";

const SearchBar = ({ setResults }) => {
	const [input, setInput] = useState("");

	const fetchData = async (value) => {
		console.log(value);
		try {
			const response = await axios.get(
				`http://localhost:5000/search?q=${value}`
			);
			console.log(response.data);
			setResults(response.data);
		} catch (error) {
			console.error("Error fetching data:", error);
		}
	};

	const handleChange = (value) => {
		setInput(value);
		if (value === "") {
			setResults([]);
		} else {
			fetchData(value);
		}
	};
	return (
		<div className="flex flex-col mx-auto items-center w-80">
			<h1 className="mb-5">Enter a Movie Title!</h1>
			<div className="w-full h-10 rounded-lg border-2 shadow-xl border-accent px-4 bg-neutral flex items-center">
				<FaSearch className="text-primary" />
				<input
					placeholder="Type to search..."
					value={input}
					onChange={(e) => handleChange(e.target.value)}
					className="bg-transparent border-none h-full text-lg w-full ml-2 focus:outline-none"
				/>
			</div>
		</div>
	);
};

export default SearchBar;
