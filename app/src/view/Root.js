/* React Base */
import React from "react";

/* Components */
import App from "./App";

/* Redux */
// import createStore from "../redux";
// import { Provider } from "react-redux";

//export const store = createStore();

/**
 * The entry point component for React that binds to the 'root' div on the DOM.
 * This wraps the Flow Metrics <App> with the Redux <Provider> component to enable 'connecting'
 * sub components to the store.
 */
const Root = props => (
//   <Provider store={store}>
    <App />
//   </Provider>
);

export default Root;