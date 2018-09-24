import React from "react";
import { Button } from "semantic-ui-react"

import "../styles/NotFoundPage.css";


const NotFoundPage = props => {

  return (
    <div className={"not-found-page"}>
      <div className={"not-found-page__container"}>
        <h1> 404: Route Not Found :(</h1>
        <h4> It looks like we couldn't find that page. </h4>
        <Button onClick={() => {window.location.href = "/"}}>
          Back to Main Page
        </Button>
      </div>
    </div>
  );
};


export default NotFoundPage;