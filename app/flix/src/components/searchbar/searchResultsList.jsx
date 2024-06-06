import React from "react";
import SearchResult from "./searchResult";

const SearchResultsList = ({ results, onResultClick }) => {
	return (
		<div className="w-[22rem] text-accent flex flex-col rounded-box border-2 shadow-xl border-accent px-4 bg-neutral mt-4 max-h-72 overflow-y-auto z-50 absolute">
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
