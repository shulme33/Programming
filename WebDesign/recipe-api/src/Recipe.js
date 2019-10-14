import React from "react";
import recipeStyle from "./recipe.module.css";

const Recipe = ({ title, calories, image, ingredients }) => {
  return (
    <div className={recipeStyle.recipe}>
      <h1>{title}</h1>
      <ol>
        {ingredients.map(ing => (
          <li key={ingredients.indexOf(ing)}>{ing.text}</li>
        ))}
      </ol>
      <p>{Math.round(calories)} cal.</p>
      <img src={image} alt="" />
    </div>
  );
};

export default Recipe;
