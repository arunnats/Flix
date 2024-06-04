import React from "react";
import styles from "./searchResultsList.module.css";
import SearchResult from "./searchResult";

const SearchResultsList = ({ results }) => {
	return (
		<div className={styles.resultsList}>
			{results.map((result, id) => {
				return <SearchResult result={result.name} key={id} />;
			})}
		</div>
	);
};

export default SearchResultsList;
