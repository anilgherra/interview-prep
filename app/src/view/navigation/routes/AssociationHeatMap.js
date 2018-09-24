/* React Base */
import React from 'react';

/* Styling */
import '../../App.css';

/* Modules */
import * as esriLoader from 'esri-loader';

const options = {
  url: "https://js.arcgis.com/4.8/esri/css/main.css"
}

const styles =  {
  container: {
    height: '100vh',
    width: '100vw'
  },
  mapDiv: {
    padding: 0,
    margin: 0,
    height: '100%',
    width: '100%'
  },
}

class AssociationHeatMap extends React.Component {

    constructor(props) {
      super(props);
      this.state = {
        status: 'loading',
        map: null,
        view: null,
      }
    }
  
    updateMap = (update) => {
      this.setState({update})
    }
  
    componentDidMount() {
  
      esriLoader.loadModules(
        ['esri/Map', 'esri/views/MapView', "esri/layers/MapImageLayer", "esri/layers/FeatureLayer"], 
        options
      )
        .then(([Map, MapView, MapImageLayer, FeatureLayer]) => {
  
          var interiorBaseLyr = new MapImageLayer({
              url: "https://stg-dcgis01.flysfo.com/arcgis/rest/services/" +
                  "Interior_Base/Terminal_Floorplans_Performance/MapServer",
              id: "interior-layer",
              visible: true
          });
  
          var sfoBaseLayer = new MapImageLayer({
              url: "https://stg-dcgis01.flysfo.com/arcgis/rest/services/" +
                  "Exterior_Base/SFO_Base_Dark/MapServer",
              id: "exterior-layer",
              visible: true
          });
  
          // var apLayer = new FeatureLayer({
            //   url: "https://services.arcgis.com/Zs2aNLFN00jrS4gG/arcgis/" +
            //       "rest/services/ITT_AP_COLLECTION/FeatureServer/0",
            //   id: "AP-layer",
            //   visible: false
          // });
  
          var map = new Map({
              basemap: "dark-gray",
              layers: [sfoBaseLayer]
          });
  
          map.add(interiorBaseLyr);
          //map.add(apLayer);
  
          new MapView({
            container: "viewDiv",
            map: map,
            zoom: 18,
            center: [-122.381727, 37.617637]
          });
  
          this.updateMap({status:'loaded'});
  
        })
        .catch(err => {
          console.error(err)
        })
  
    }
  
  
    render() {
      return (
 
        <div style={styles.container}>
            <div id='viewDiv' style={ styles.mapDiv }></div>
        </div>
         
      );
    }
  }
  
  export default AssociationHeatMap;