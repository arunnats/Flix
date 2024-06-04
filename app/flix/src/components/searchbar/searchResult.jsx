import React from "react";
import styles from "./searchResult.module.css";

const SearchResult = ({ result }) => {
	return (
		<div
			className={styles.searchResult}
			onClick={() => alert(`You selected ${result}!`)}
		>
			{result}
		</div>
	);
};

export default SearchResult;
