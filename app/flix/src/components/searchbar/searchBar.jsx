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
		<div className={styles.inputWrapper}>
			<FaSearch id={styles.searchIcon} />
			<input
				placeholder="Type to search..."
				value={input}
				onChange={(e) => handleChange(e.target.value)}
			/>
		</div>
	);
};

export default SearchBar;
