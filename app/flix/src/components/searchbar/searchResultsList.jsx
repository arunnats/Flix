import React from "react";
import SearchResult from "./searchResult";

const SearchResultsList = ({ results, onResultClick }) => {
	return (
		<div className="w-80 bg-gray-800 text-white flex flex-col shadow-lg rounded-lg mt-4 max-h-72 overflow-y-auto z-50 absolute">
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
