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

document.getElementById('getLodges').onclick = () => {
        event.preventDefault();

        token = window.localStorage.getItem('token');
        username = window.localStorage.getItem('username');

        fetch('http://localhost:5000/api/v1/lodges',{
            method: 'GET',
            headers : {
                Accept: 'application/json',
                'Content-Type': 'application/json',
                'Authorization': 'Bearer ' + token,
            },
        })
        .then((res) => res.json())
        .then((data) => {
            data.lodges.forEach(lodge => {
                let status = data['status'];
                let message = data['message'];
                const { booked_by, hotel_name, lodge_no} = lodge;
                output += `
                    <div>
                        <table>
                            <tr>
                                <th>Username</th>
                                <th>Hotel Name</th>
                                <th>Lodge No.</th>
                            </tr>
                            <tr>
                                <td>${lodge.booked_by}</td>
                                <td>${lodge.hotel_name}</td>
                                <td>${lodge.lodge_no}</td>
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
