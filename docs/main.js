const label_day = {
    0 : "Sunday",
    1 : "Monday",
    2 : "Tuesday",
    3 : "Wednesday",
    4 : "Thursday",
    5 : "Friday",
    6 : "Saturday"
};

const label_week = {
    1 : "Week 1",
    2 : "Week 2",
    3 : "Week 3",
    4 : "Week 4",
    5 : "Week 5",
};

//vibgyor in rgb
const color = {
    0 : 'rgba(255,0,0,1)',
    1 : 'rgba(255,127,0,1)',
    2 : 'rgba(255,255,0,1)',
    3 : 'rgba(0,255,0,1)',
    4 : 'rgba(0,0,255,1)',
    5 : 'rgba(75,0,130,1)',
    6 : 'rgba(148,0,211,1)' 
}

const url = 'https://travelverse.pagekite.me';

async function getPrediction(params) {
    const response = await fetch(url+'/predict',{
        body: JSON.stringify( params )  ,
        method: 'POST',
        headers: {
        'Content-Type': 'application/json'
        },
    });
    const data = await response.json();
    let graphData = {}
    data.forEach(item =>{
        if(!graphData[`${item.day}_${item.week}`]){
            graphData[`${item.day}_${item.week}`] = {
                label: label_day[item.day],
                stack: label_week[item.week],
                data:[...Array(12).fill(0)],
                backgroundColor: color[item.day],
                borderWidth: 1
            };
        }
        graphData[`${item.day}_${item.week}`]['data'][item.month] = item.pred;
    });
    graphData = Object.values(graphData);
    myChart.data.datasets = graphData;
    myChart.update();

}

// /////////////////////////////////////////////////////////////////////////////////////
// Step 4: create SVG Dom Marker and add it to the map
const svg = `<svg xmlns="http://www.w3.org/2000/svg" class="svg-icon" viewBox="0 0 100 100">
<circle cx="50" cy="50" r="50" fill="rgb(30, 200, 200)" opacity=".8"/>
<circle cx="50" cy="50" r="4" fill="black"/>
</svg>`;
let clickCounter = 0;
let orgin = {lat:28.5, lng:77.1}; 
let dest = {lat:8.47, lng:26.9};
let orginMarker = new H.map.Marker(orgin,{icon: new H.map.Icon('./icons/start.png',{size: {w: 50, h: 50}})});
let destMarker = new H.map.Marker(dest,{icon: new H.map.Icon('./icons/end.png',{size: {w: 50, h: 50}})});
let lineString = new H.geo.LineString();
lineString.pushPoint(dest);
lineString.pushPoint(orgin);

let line =new H.map.Polyline(lineString, 
    { 
        style: {
            
        lineWidth: 5,
        strokeColor: 'rgba(0, 0, 0, 1)',
        arrows : true,
        lineHeadCap: 'arrow-head'

        }
    }
)


function initMarker(map){
    map.setCenter({lat:15, lng:30});
    map.setZoom(2.5);
    map.addObject(orginMarker);
    map.addObject(destMarker);;
    map.addObject(line);
  }

function setUpClickListener(map) {

    map.addEventListener('tap', function (evt) {
      const coord = map.screenToGeo(evt.currentPointer.viewportX, evt.currentPointer.viewportY);
      lineString.removePoint(orgin);
      lineString.removePoint(dest);
      if(clickCounter == 0){
        orgin = coord;
        clickCounter = 1;
        orginMarker.setGeometry(orgin);
        lineString.pushPoint(orgin);
        lineString.pushPoint(dest);
        line.setGeometry(lineString);
        updateChart();
      }
    else if(clickCounter == 1){
        dest = coord;
        clickCounter = 0;
        destMarker.setGeometry(dest);
        lineString.pushPoint(orgin);
        lineString.pushPoint(dest);
        line.setGeometry(lineString);
        updateChart();
    }
    });
    
  }


  var platform = new H.service.Platform({
    apikey: 'JP1jNJMt6pMack2_WYjaOAyAp0ksxo9EJw_bqgmURqs'
  });
  var defaultLayers = platform.createDefaultLayers();
  
  var map = new H.Map(document.getElementById('map'),
    defaultLayers.vector.normal.map,{
    center: {lat:10, lng:5},
    zoom: 10,
    pixelRatio: window.devicePixelRatio || 1
  });

  window.addEventListener('resize', () => map.getViewPort().resize());
  var behavior = new H.mapevents.Behavior(new H.mapevents.MapEvents(map));
  

  var ui = H.ui.UI.createDefault(map, defaultLayers);
  
  

  window.onload = function () {
    initMarker(map);
    setUpClickListener(map);
    updateChart();
  }

  //////////////////////////////////////////////////////////////////////////////

function updateChart() {
    const cabin = document.getElementById("cabin").value;
    const trip = document.getElementById("trip").value;
    const origin_lat = orgin.lat;
    const origin_lon = orgin.lng;
    const dest_lat = dest.lat;
    const dest_lon = dest.lng;
    const params = [];
    [...Array(12).keys()].forEach(month => {
        [...Array(5).keys()].forEach(week => {
            [...Array(7).keys()].forEach(day => {
                params.push({
                    month : month,
                    day : day,
                    week : week+1,
                    cabin : parseInt(cabin),
                    trip : parseInt(trip),
                    origin_lat : origin_lat,
                    origin_lon : origin_lon,
                    dest_lat : dest_lat,
                    dest_lon : dest_lon
                });
            });
        });
        
    });
    getPrediction(params);
}

const ctx = document.getElementById('myChart').getContext('2d');
const myChart = new Chart(ctx, {
    type: 'bar',
    data: {
        labels: ['JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN','JUL','AUG','SEP','OCT','NOV','DEC'],
        datasets: []
    },
    options: {
        plugins: {
            legend: {
              display: false
            }
          },
        responsive: true,
        maintainAspectRatio: false,
        scales: {
            xAxes: {
                title: {
                    display: true,
                    text: 'Departure Date',
                    font: {
                        size: 12
                    }
                }
            },
            yAxes: {
                title: {
                    display: true,
                    text: 'Days from Ticket issue',
                    font: {
                        size: 12
                    }
                }
            }
        }
    }
});