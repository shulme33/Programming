import React, { useEffect, useState } from "react";
import "./App.css";
import { directive } from "@babel/types";

const comic = {
  code: 200,
  status: "Ok",
  copyright: "© 2019 MARVEL",
  attributionText: "Data provided by Marvel. © 2019 MARVEL",
  attributionHTML:
    '<a href="http://marvel.com">Data provided by Marvel. © 2019 MARVEL</a>',
  etag: "5d55f3b593617bd427d632d70506bd93000c9306",
  data: {
    offset: 0,
    limit: 20,
    total: 1,
    count: 1,
    results: [
      {
        id: 60602,
        digitalId: 44277,
        title: "Deadpool (2015) #28",
        issueNumber: 28,
        variantDescription: "",
        description:
          "Deadpool's whirlwind romance with Shiklah was one of the most exciting times of his life. Traveling across the world, fighting all sorts of threats at her side, and finally marrying her as a way to thwart the evil vampire lord, Dracula. But since then, the reality has set in. Shiklah is a demon succubus, and more than that, the Queen of the monster kingdom hidden beneath Manhattan...and the problems between them continue to pile up.\nNow, when an affront to Shiklah's people demands justice, a line is crossed. As the Monster Metropolis declares war on the surface world, Deadpool must choose between the wife to whom he's pledged himself and the role he's been crafting for himself as a hero. Also featuring Spider-Man and the Mercs for Money, this is one domestic dispute that's really going to break some things up.",
        modified: "2017-03-16T09:16:59-0400",
        isbn: "",
        upc: "75960608332902811",
        diamondCode: "JAN171058",
        ean: "",
        issn: "1946-9292",
        format: "Comic",
        pageCount: 32,
        textObjects: [
          {
            type: "issue_solicit_text",
            language: "en-us",
            text:
              "Deadpool's whirlwind romance with Shiklah was one of the most exciting times of his life. Traveling across the world, fighting all sorts of threats at her side, and finally marrying her as a way to thwart the evil vampire lord, Dracula. But since then, the reality has set in. Shiklah is a demon succubus, and more than that, the Queen of the monster kingdom hidden beneath Manhattan...and the problems between them continue to pile up.\nNow, when an affront to Shiklah's people demands justice, a line is crossed. As the Monster Metropolis declares war on the surface world, Deadpool must choose between the wife to whom he's pledged himself and the role he's been crafting for himself as a hero. Also featuring Spider-Man and the Mercs for Money, this is one domestic dispute that's really going to break some things up."
          }
        ],
        resourceURI: "http://gateway.marvel.com/v1/public/comics/60602",
        thumbnail: {
          path: "http://i.annihil.us/u/prod/marvel/i/mg/5/70/58b0a1463b05a",
          extension: "jpg"
        }
      }
    ]
  }
};

const getDeadpoolComic = async () => {
  console.log("Making Marvel API Call...");
  const response = await fetch(
    `https://gateway.marvel.com:443/v1/public/comics/60602?apikey=f9574ec15ecaab11349d2a1bdbd17619`
  );
  const data = await response.json();
  console.log("Comics Loaded.");
  console.log(data.data.results[0]);
};

getDeadpoolComic();

const App = () => {
  const { thumbnail } = comic.data.results[0]; //Destructuring
  return (
    <div className="App">
      <h1> {comic.data.results[0].title} </h1>
      <img
        className="comic-thumbnail"
        src={thumbnail.path + "." + thumbnail.extension}
        alt="Deadpool Image"
      />
    </div>
  );
};

export default App;
