require([ "esri/Map", "esri/views/MapView" ], function(Map, MapView) {
    var cumulative_map = new Map({
        basemap: "dark-gray"
    });

    var cumulative_view = new MapView({
        container: "cumulative-map", // Reference to the DOM node that will contain the view
        map: cumulative_map // References the map object created in step 3
    });

    var current_map = new Map({
        basemap: "dark-gray"
    });

    var current_view = new MapView({
        container: "current-map", // Reference to the DOM node that will contain the view
        map: current_map // References the map object created in step 3
    });
});