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

document.getElementById('getHotel').onclick = () => {
        event.preventDefault();

        token = window.localStorage.getItem('token');
        name = window.localStorage.getItem('name');

        fetch('http://localhost:5000/api/v1/hotels/' + name,{
            method: 'GET',
            path: name,
            headers : {
                Accept: 'application/json',
                'Content-Type': 'application/json',
                'Authorization': 'Bearer ' + token,
            },
        })
        .then((res) => res.json())
        .then((data) => {
            data.hotel.forEach(hotl => {
                let status = data['status'];
                let message = data['message'];
                const { name, location, lodges, conference_rooms, img_url, category } = hotl;
                output2 += `
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
                                <td>${hotl.name}</td>
                                <td>${hotl.location}</td>
                                <td>${hotl.lodges}</td>
                                <td>${hotl.conference_rooms}</td>
                                <td>${hotl.img_url}</td>
                                <td>${hotl.category}</td>
                            </tr>
                        </table>
                    </div>
                `;
                if (status === '200'){
                    document.getElementById('output2').innerHTML = output2;
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
