import React, { useEffect, useState } from "react";
import Recipe from "./Recipe";
import "./App.css";

const App = () => {
  const APP_ID = "70ccc971";
  const APP_KEY = "70775172cf795ed7d575d139e5afd843";

  const [recipes, setRecipes] = useState([]); //Holds all the recipes returned from the API
  const [search, setSearch] = useState(""); //Holds the value of what is in the search bar
  const [query, setQuery] = useState("chicken");

  useEffect(() => {
    const getRecipes = async () => {
      console.log("Loading Recipes from Edamam...");
      const response = await fetch(
        `https://api.edamam.com/search?q=${query}&app_id=${APP_ID}&app_key=${APP_KEY}`
      );
      const data = await response.json();
      setRecipes(data.hits);
      console.log("Recipes Loaded.");
      console.log(data.hits);
    };
    //Runs when the program is built (mounted)
    getRecipes();
  }, [query]);

  const updateSearch = e => {
    setSearch(e.target.value);
    console.log(search);
  };

  const getSearch = e => {
    e.preventDefault(); //Stops the refresh??
    setQuery(search);
    setSearch("");
  };

  return (
    <div className="App">
      <h1>Edamam Recipes</h1>
      <form className="search-form" onSubmit={getSearch}>
        <input
          className="search-bar"
          type="text"
          value={search}
          onChange={updateSearch}
        />
        <br></br>
        <button className="search-button" type="submit">
          Search
        </button>
      </form>
      <div className="recipes">
        {recipes.map(recipe => (
          <Recipe
            key={recipes.indexOf(recipe)}
            title={recipe.recipe.label + " >> " + recipes.indexOf(recipe)}
            calories={recipe.recipe.calories}
            image={recipe.recipe.image}
            ingredients={recipe.recipe.ingredients}
          />
        ))}
      </div>
    </div>
  );
};

export default App;
