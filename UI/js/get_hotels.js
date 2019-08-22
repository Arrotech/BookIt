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

document.getElementById('getHotels').onclick = () => {
        event.preventDefault();

        token = window.localStorage.getItem('token');
        username = window.localStorage.getItem('username');

        fetch('http://localhost:5000/api/v1/hotels',{
            method: 'GET',
            headers : {
                Accept: 'application/json',
                'Content-Type': 'application/json',
                'Authorization': 'Bearer ' + token,
            },
        })
        .then((res) => res.json())
        .then((data) => {
            data.hotels.forEach(hotel => {
                let status = data['status'];
                let message = data['message'];
                const { name, location, lodges, conference_rooms, img_url, category } = hotel;
                output += `
                    <div>
                        <table>
                            <tr>
                                <th>Hotel Name</th>
                                <th>Location</th>
                                <th>No of lodges</th>
                                <th>Conference rooms</th>
                                <th>Image</th>
                                <th>Category</th>
                            </tr>
                            <tr>
                                <td>${hotel.name}</td>
                                <td>${hotel.location}</td>
                                <td>${hotel.lodges}</td>
                                <td>${hotel.conference_rooms}</td>
                                <td>${hotel.img_url}</td>
                                <td>${hotel.category}</td>
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
