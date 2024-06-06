import React, { useState } from "react";
import { FaSearch } from "react-icons/fa";
import axios from "axios";
import styles from "./searchBar.module.css";

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
		<div className="flex flex-col mx-auto items-center min-w-80">
			<h1 className="mb-5">Enter a Movie Title!</h1>
			<div className={styles.inputWrapper}>
				<FaSearch id={styles.searchIcon} />

				<input
					placeholder="Type to search..."
					value={input}
					onChange={(e) => handleChange(e.target.value)}
				/>
			</div>
		</div>
	);
};

export default SearchBar;
