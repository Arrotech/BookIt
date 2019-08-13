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

document.getElementById('addHotel').onclick = () => {
        event.preventDefault();

        token = window.localStorage.getItem('token');

        let name = document.getElementById('name').value;
        let location = document.getElementById('location').value;
        let lodges = document.getElementById('lodges').value;
        let conference_rooms = document.getElementById('conference_rooms').value;
        let img_url = document.getElementById('img_url').value;
        let category = document.getElementById('category').value;

        fetch('http://localhost:5000/api/v1/hotels', {
            method: 'POST',
            headers : {
            Accept: 'application/json',
                'Content-Type': 'application/json',
                'Authorization': 'Bearer ' + token,
            },
            body:JSON.stringify({name:name, location:location, lodges:lodges, conference_rooms:conference_rooms, img_url:img_url, category:category})
        }).then((res) => res.json())
        .then((data) =>  {
            console.log(data);
            let status = data['status'];
            let message = data['message'];
            if (status === '201'){
                onSuccess('Hotel added successfully');
            }else{
                raiseError(message);
            }

        })
        .catch((err)=>{
            raiseError("Please check your internet connection and try again!");
            console.log(err);
        })
    }
