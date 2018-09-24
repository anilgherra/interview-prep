/* React Base */
import React from "react";

/* Style */
import "../styles/Header.css";


class Header extends React.Component {

  render() {

    return (
      <header className={"header-main"}>

        <div className={"header__container"}>
 
          <div className={"header__logo-container"}>
            Wifi Association Heat Map
          </div>

        </div>
      </header>
    );
  }
}



export default Header;