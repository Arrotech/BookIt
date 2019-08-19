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

document.getElementById('bookTrip').onclick = () => {
        event.preventDefault();

        token = window.localStorage.getItem('token');

        let booked_by = document.getElementById('booked_by').value;
        let pickup = document.getElementById('pickup').value;
        let destination = document.getElementById('destination').value;
        let means = document.getElementById('means').value;

        fetch('https://bookit-api-app.herokuapp.com/api/v1/trips', {
            method: 'POST',
            headers : {
            Accept: 'application/json',
                'Content-Type': 'application/json',
                'Authorization': 'Bearer ' + token,
            },
            body:JSON.stringify({booked_by:booked_by, pickup:pickup, destination:destination, means:means})
        }).then((res) => res.json())
        .then((data) =>  {
            console.log(data);
            let status = data['status'];
            let message = data['message'];
            if (status === '201'){
                window.location.replace('checkout.html');
                onSuccess('You have successfully booked the trip');
            }else{
                raiseError(message);
            }

        })
        .catch((err)=>{
            raiseError("Please check your internet connection and try again!");
            console.log(err);
        })
    }
