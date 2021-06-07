
// function getCookie(name) {
//     let cookieValue = null;
//     if (document.cookie && document.cookie !== '') {
//         const cookies = document.cookie.split(';');
//         for (let i = 0; i < cookies.length; i++) {
//             const cookie = cookies[i].trim();
//             // Does this cookie string begin with the name we want?
//             if (cookie.substring(0, name.length + 1) === (name + '=')) {
//                 cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
//                 break;
//             }
//         }
//     }
//     return cookieValue;
// }

// function reservar(pk){
//     datajson = {'id':pk}
//     json_data = JSON.stringify(datajson)
//     fetch('/reservar',{
//         method: "POST",
//         body: json_data,
//         headers:{
//             "X-CSRFToken":  getCookie('csrftoken'),  
//             "X-Requested-With": "XMLHttpRequest"    
//         }
//     }).then(
//         function(response){
//             return response.json()
//         }
//     )
// }