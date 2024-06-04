const express = require("express");
const mysql = require("mysql2/promise");

const app = express();
app.use(express.json());

// MySQL connection pool
const pool = mysql.createPool({
	host: "localhost",
	user: "root",
	password: "nats",
	database: "flix",
	waitForConnections: true,
	connectionLimit: 100,
	queueLimit: 0,
});

// Simple in-memory cache
const cache = new Map();

app.get("/search", async (req, res) => {
	const query = req.query.q;
	if (!query) {
		return res.status(400).json({ error: "Query parameter 'q' is required" });
	}

	// Check cache first
	if (cache.has(query)) {
		console.log("Using cache for query:", query);
		return res.json(cache.get(query));
	}

	try {
		// const [results] = await pool.query(
		// 	`SELECT Title, MovieId FROM movie WHERE MATCH(Title) AGAINST(? IN NATURAL LANGUAGE MODE) LIMIT 10`,
		// 	[`${query}%`]
		// );

		const [results] = await pool.query(
			`SELECT Title, MovieId FROM movie WHERE Title LIKE ? LIMIT 10`,
			[`${query}%`]
		);

		// Update cache
		cache.set(query, results);

		res.json(results);
	} catch (error) {
		console.error("Error executing query", error);
		res.status(500).json({ error: "Internal server error" });
	}
});

// Clear cache periodically
setInterval(() => {
	cache.clear();
	console.log("Cache cleared");
}, 1000 * 60 * 60); // clear cache every hour

const PORT = 5000;
app.listen(PORT, () => {
	console.log(`Server running on port ${PORT}`);
});
