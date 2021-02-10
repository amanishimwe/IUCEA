var endpoint = 'api/chart/data'
var defaultData = []
var labels = [];
$.ajax({
     method : "GET",
     url: endpoint,
     success: function(data){
         labels = data.thematic_areas
         defaultData = data.thematic_areas_count
         setPieChart()
    },
    error: function(error_data){
    console.log("error")
    console.log(error_data)
    }
})


 function setPieChart(){
var ctx = document.getElementById('myPieChart');
var myDoughnutChart = new Chart(ctx, {
    type: 'doughnut',
    data: {
        labels: labels,
        datasets: [{
            label: '# of Votes',
            data: defaultData ,
            backgroundColor: [
                'rgb(255,99,132)',
                'rgb(54,162,235)',
                'rgb(255,205,86)'
            ],
            borderColor: [
                'rgba(255, 99, 132, 1)',
                'rgba(54, 162, 235, 1)',
                'rgba(255, 206, 86, 1)',
                'rgba(75, 192, 192, 1)',
                'rgba(153, 102, 255, 1)',
                'rgba(255, 159, 64, 1)'
            ],
            borderWidth: 1
        }]
    },
});
}