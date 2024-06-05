import React, { createContext, useState, useContext } from "react";

const RecommendationContext = createContext();

export const useRecommendation = () => {
	return useContext(RecommendationContext);
};

export const RecommendationProvider = ({ children }) => {
	const [recommendations, setRecommendations] = useState([]);

	const updateRecommendations = (data) => {
		setRecommendations(data);
	};

	return (
		<RecommendationContext.Provider
			value={{ recommendations, updateRecommendations }}
		>
			{children}
		</RecommendationContext.Provider>
	);
};
