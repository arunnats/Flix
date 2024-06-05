import React from "react";
import styles from "./searchResult.module.css";

const SearchResult = ({ result, onClick }) => {
	return (
		<div className={styles.searchResult} onClick={() => onClick(result)}>
			{result}
		</div>
	);
};

export default SearchResult;
