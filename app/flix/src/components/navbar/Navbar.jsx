// Navbar.jsx
import React from "react";
import logo from "../../assets/Logo.png";
import githubLogo from "../../assets/icons8-github.svg";

const Navbar = () => {
	return (
		<div className="navbar bg-neutral	">
			<div className="navbar-start">
				<a href="https://www.arunnats.com/" className="btn btn-ghost text-xl">
					<img className="h-9 max-w-lg" src={logo} alt="Logo" />
				</a>
			</div>

			<div className="navbar-end">
				<a href="https://www.arunnats.com/" className="btn btn-ghost text-m">
					Recommendations
				</a>
				<a href="https://www.arunnats.com/" className="btn btn-ghost text-m">
					Data Analysis
				</a>
				<a
					href="https://github.com/arunnats/Flix/"
					className="btn btn-ghost text-xl"
				>
					<img className="mx-1 h-8 max-w-lg" src={githubLogo} alt="Logo" />
				</a>

				{/* <label className="flex cursor-pointer gap-2">
					<svg
						xmlns="http://www.w3.org/2000/svg"
						width="20"
						height="20"
						viewBox="0 0 24 24"
						fill="none"
						stroke="currentColor"
						strokeWidth="2"
						strokeLinecap="round"
						strokeLinejoin="round"
					>
						<circle cx="12" cy="12" r="5" />
						<path d="M12 1v2M12 21v2M4.2 4.2l1.4 1.4M18.4 18.4l1.4 1.4M1 12h2M21 12h2M4.2 19.8l1.4-1.4M18.4 5.6l1.4-1.4" />
					</svg>
					<input
						type="checkbox"
						value="dark"
						className="toggle theme-controller"
					/>
					<svg
						xmlns="http://www.w3.org/2000/svg"
						width="20"
						height="20"
						viewBox="0 0 24 24"
						fill="none"
						stroke="currentColor"
						strokeWidth="2"
						strokeLinecap="round"
						strokeLinejoin="round"
					>
						<path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"></path>
					</svg>
				</label> */}
			</div>
		</div>
	);
};

export default Navbar;
