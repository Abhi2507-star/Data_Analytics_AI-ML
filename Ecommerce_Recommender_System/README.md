🛒 Ecommerce_Recommender_System

A content-based recommender system
built for e-commerce platforms using genre-based movie data. 
This project recommends similar items (movies in this case) based on Jaccard similarity.
---

 ✅ Features

- 🔍 Recommends products/movies based on content (genres)
- 🧠 Uses **Jaccard Similarity** instead of cosine
- 🚀 Lightweight and easy to understand

---

📁 Dataset

The project uses a `movies.csv` file with at least the following columns:

- `title` – Name of the product/movie (e.g., *We (2018)*)
- `genres` – Genre or category list, pipe- or comma-separated (e.g., *Drama|Romance*)

Sample Rows--

movieId	  title	                              genres
0	        Toy Story (1995)      	           Adventure|Animation|Children|Comedy|Fantasy
1	      	Jumanji (1995)         	            Adventure|Children|Fantasy
2	      	Grumpier Old Men (1995)	            Comedy|Romance
3	      	Waiting to Exhale (1995)	          Comedy|Drama|Romance
4	      	Father of the Bride Part II (1995)	Comedy
