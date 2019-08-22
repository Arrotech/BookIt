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

document.getElementById('bookLodge').onclick = () => {
        event.preventDefault();

        token = window.localStorage.getItem('token');

        let booked_by = document.getElementById('booked_by').value;
        let hotel_name = document.getElementById('hotel_name').value;
        let lodge_no = document.getElementById('lodge_no').value;

        fetch('http://localhost:5000/api/v1/lodges', {
            method: 'POST',
            headers : {
            Accept: 'application/json',
                'Content-Type': 'application/json',
                'Authorization': 'Bearer ' + token,
            },
            body:JSON.stringify({booked_by:booked_by, hotel_name:hotel_name, lodge_no:lodge_no})
        }).then((res) => res.json())
        .then((data) =>  {
            console.log(data);
            let status = data['status'];
            let message = data['message'];
            if (status === '201'){
                window.location.replace('checkout.html');
                onSuccess('You have successfully booked the lodge');
            }else{
                raiseError(message);
            }

        })
        .catch((err)=>{
            raiseError("Please check your internet connection and try again!");
            console.log(err);
        })
    }
