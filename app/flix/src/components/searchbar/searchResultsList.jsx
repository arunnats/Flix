import React from "react";
import styles from "./searchResultsList.module.css";
import SearchResult from "./searchResult";

const SearchResultsList = ({ results, onResultClick }) => {
	return (
		<div className={styles.resultsList}>
			{results.map((result, index) => (
				<SearchResult
					result={result.Title}
					key={index}
					onClick={onResultClick}
				/>
			))}
		</div>
	);
};

export default SearchResultsList;
