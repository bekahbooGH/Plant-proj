// let map;
// let marker

// function initMap() {
//     map = new google.maps.Map(
//         document.getElementById("map"),
//         {center:{lat: 34.0872647, lng: -118.3871645},
//         zoom: 13,
//         fullscreenControl:false});
//     }
let marker;

function initMap() {
    const map = new google.maps.Map(document.getElementById("map"), {
    zoom: 14,
    center: {lat: 34.07462850125127, lng: -118.36057025355362},
    });
    marker = new google.maps.Marker({
    map,
    draggable: true,
    animation: google.maps.Animation.DROP,
    position: {lat: 34.08510905153518, lng: -118.37676935991092},
    title: "La Cienega Nursery"
    });
    marker = new google.maps.Marker({
        map,
        draggable: true,
        animation: google.maps.Animation.DROP,
        position: {lat: 34.07662507925801, lng: -118.35368808874652},
        title: "Rolling Greens Los Angeles"
        });
        marker = new google.maps.Marker({
            map,
            draggable: true,
            animation: google.maps.Animation.DROP,
            position: {lat: 34.090732152843245, lng: -118.34310913107532},
            title: "Tropics Inc"
            });
            marker = new google.maps.Marker({
                map,
                draggable: true,
                animation: google.maps.Animation.DROP,
                position: {lat: 34.09432655980319, lng: -118.34311081573361},
                title: "Mickey Hargitay Plants"
                });
                marker = new google.maps.Marker({
                    map,
                    draggable: true,
                    animation: google.maps.Animation.DROP,
                    position: {lat: 34.05227247096256, lng: -118.38360510420672},
                    title: "Xotx-Tropico"
                    });
}

// function initMap() {
//     const map = new google.maps.Map(document.getElementById("map"), {
//     zoom: 13,
//     center: {lat: 34.0872647, lng: -118.3871645},
//     });
//     marker = new google.maps.Marker({
//     map,
//     draggable: true,
//     animation: google.maps.Animation.DROP,
//     position: {lat: 34.0731172, lng: -118.3911652},
//     });

// }
    // const marker1 = new google.maps.Marker(
    //     {
    //         position: {lat: 34.0731172, lng: -118.3911652},
    //         title: "La Cienega Nursery",
    //         map: map
    //     }
    // )
    // map.setCenter({lat:34.0731172, lng:-118.3911652})

    // const marker2 = new google.maps.Marker(
    //     {
    //         position: {lat: 34.0742529, lng: -118.392529},
    //         title: "Rolling Greens Los Angeles",
    //         map: map
    //     }
    // )

    // const marker3 = new google.maps.Marker(
    //     {
    //         position: {lat: 34.0742529, lng: -118.392529},
    //         title: "Tropics Inc",
    //         map: map
    //     }
    // )

    // const marker4 = new google.maps.Marker(
    //     {
    //         position: {lat: 34.0742529, lng: -118.392529},
    //         title: "Mickey Hargitay Plants",
    //         map: map
    //     }
    // )



    // const locations = 
    //   {
    //     name: 'Nursery 1',
    //     coords: {
    //       lat: 34.0731172,
    //       lng: -118.3911652
    //     }}

    //   },
    //   {
    //     name: 'Nursery 2',
    //     coords: {
    //       lat: 
    //       lng: 
    //     }
    //   },
    //   {
    //     name: 'Nursery 3',
    //     coords: {
    //       lat: 
    //       lng: 
    //     }
      
    // ];

//     const markers = [];
//     for (const location of locations) {
//       markers.push(new google.maps.Marker({
//         position: location.coords,
//         title: location.name,
//         map: basicMap,
//         // icon: {  // custom icon
//         // //   url: '/static/img/marker.svg',
//         //   scaledSize: {
//         //     width: 30,
//         //     height: 30
//         //   }
//         // }
//       }));
//     }
  
//     for (const marker of markers) {
//       const markerInfo = (`
//         <h1>${marker.title}</h1>
//         <p>
//           Located at: <code>${marker.position.lat()}</code>,
//           <code>${marker.position.lng()}</code>
//         </p>
//       `);
  
//       const infoWindow = new google.maps.InfoWindow({
//         content: markerInfo,
//         maxWidth: 200
//       });
  
//       marker.addListener('click', () => {
//         infoWindow.open(basicMap, marker);
//       });
//     }
//   }

// const laHWood = {
//     lat:
//     lng:
// };

// const basicMap = new google.maps.Map(
//     document.querySelector('#map'),
//     {
//         center: laHWood,
//         zoom: 13
//     }
// );
    
// const laMarker = new google.maps.Marker({
//     position: laHWood,
//     title: 'Hollywood',
//     map: basicMap
// })