import React from "react";

const Results = ({ recommendations }) => {
	return (
		<div>
			<h2>Recommendations</h2>
			<ul>
				{recommendations.map((recommendation, index) => (
					<li key={index}>{recommendation}</li>
				))}
			</ul>
		</div>
	);
};

export default Results;
