function callToast() {

    var x = document.getElementById("snackbar");
    x.className = "show";
    setTimeout(function(){ x.className = x.className.replace("show", ""); }, 3000);
}

function onSuccess(msg){

    document.getElementById('snackbar').innerText = msg
    callToast();
}

function raiseError(msg){

    document.getElementById('snackbar').innerText = msg
    callToast();
}

document.getElementById('getTrips').onclick = () => {
        event.preventDefault();

        token = window.localStorage.getItem('token');
        username = window.localStorage.getItem('username');

        fetch('http://localhost:5000/api/v1/trips',{
            method: 'GET',
            headers : {
                Accept: 'application/json',
                'Content-Type': 'application/json',
                'Authorization': 'Bearer ' + token,
            },
        })
        .then((res) => res.json())
        .then((data) => {
            data.trips.forEach(trip => {
                let status = data['status'];
                let message = data['message'];
                const { booked_by, pickup, destination, means } = trip;
                output += `
                    <div>
                        <table>
                            <tr>
                                <th>Username</th>
                                <th>Pickup</th>
                                <th>Destination</th>
                                <th>Means</th>
                            </tr>
                            <tr>
                                <td>${trip.booked_by}</td>
                                <td>${trip.pickup}</td>
                                <td>${trip.destination}</td>
                                <td>${trip.means}</td>
                            </tr>
                        </table>
                    </div>
                `;
                if (status === '200'){
                    document.getElementById('output').innerHTML = output;
                }else{
                    raiseError(message);
                }
                });
                })
        .catch((err)=>{
            raiseError("Please check your internet connection and try again!");
            console.log(err);
        })
}
