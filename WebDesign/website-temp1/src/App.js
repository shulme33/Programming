import React from "react";
import logo from "./logo.svg";
import "./App.css";
import NavBar from "./components/NavBar.jsx";
import Banner from "./components/Banner.jsx";
import MenuBar from "./components/MenuBar";
import MenuHeader from "./components/MenuHeader";
import Menu from "./components/Menu";
import Footer from "./components/Footer.jsx";

const App = () => {
  /*
    Comments

    Main Colors:
      Cherry Red: #EA212D
      Dark Red:   #D41E29
      Grey:       #353535
      Off-White:  #F6F6F6

    React Elements:
      1.) NavBar (Element)
      2.) Picture Section (HTML in App)
      3.) Menu (Element)
          3a.) Each Menu (Element)
      4.) Menu Section (Element)
          4a.) SubMenus (Element)
      5.) Footer
  */

  return (
    <div className="App">
      <NavBar />
      <Banner />
      <MenuBar />
      <Menu />
      <Footer />
    </div>
  );
};

export default App;
