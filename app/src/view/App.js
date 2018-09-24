/* React Base */
import React from 'react';

/* Styling */
import './App.css';

/* Top Level Components */
import Header from "./navigation/components/Header";

/* Routes */
import AssociationHeatMap from "./navigation/routes/AssociationHeatMap";
import NotFoundPage from "./navigation/routes/NotFoundPage";

/* React Router */
import { BrowserRouter as Router, Route, Switch } from "react-router-dom";

class App extends React.Component {

  render() {
    return (
      <Router>
        <div>

          {/* Header */}
          <div className={"App__header-container"}>
            <Header/>
          </div>
          

          {/* Content */}
          <div className={"App__route-container"}>
            <Switch>
              <Route exact path="/" component={AssociationHeatMap} />
              <Route component={NotFoundPage} />
            </Switch>
          </div>


        </div>
        
      </Router>

    );
  }
}

export default App;
