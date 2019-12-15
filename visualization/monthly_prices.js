// set the dimensions and margins of the graph
var margin = { top: 10, right: 30, bottom: 30, left: 60 },
  width = 960 - margin.left - margin.right,
  height = 400 - margin.top - margin.bottom;

// append the svg object to the body of the page
var svg = d3.select("#monthly_price")
  .append("svg")
  .attr("width", width + margin.left + margin.right)
  .attr("height", height + margin.top + margin.bottom)
  .append("g")
  .attr("transform",
    "translate(" + margin.left + "," + margin.top + ")");

//Read the data
d3.csv("../data/price_monthly.csv",

  // When reading the csv, I must format variables:
  function (d) {
    return { Month: d3.timeParse("%Y-%m")(d.Month), Price: d.Price }
  },

  // Now I can use this dataset:
  function (data) {

    // Add X axis --> it is a date format
    var x = d3.scaleTime()
      .domain(d3.extent(data, function (d) { return d.Month; }))
      .range([0, width]);
    svg.append("g")
      .attr("transform", "translate(0," + height + ")")
      .call(d3.axisBottom(x)
      );

    // text label for the x axis
    svg.append("text")
      .attr("transform",
        "translate(" + (width / 2) + " ," +
        (height + margin.top + 20) + ")")
      .style("text-anchor", "middle")
      .text("Date (Month)");

    // Add Y axis
    var y = d3.scaleLinear()
      .domain([0, d3.max(data, function (d) { return +d.Price; })])
      .range([height, 0]);
    svg.append("g")
      .call(d3.axisLeft(y));

    // text label for the y axis
    svg.append("text")
      .attr("transform", "rotate(-90)")
      .attr("y", 0 - margin.left)
      .attr("x", 0 - (height / 2))
      .attr("dy", "1em")
      .style("text-anchor", "middle")
      .text("Price (Dollars per Million Btu)");

    // Add the line
    svg.append("path")
      .datum(data)
      .attr("fill", "none")
      .attr("stroke", "steelblue")
      .attr("stroke-width", 1.5)
      .attr("d", d3.line()
        .x(function (d) { return x(d.Month) })
        .y(function (d) { return y(d.Price) })
      )
  });
  
