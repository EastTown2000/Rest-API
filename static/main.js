function get_text() {
fetch("http://127.0.0.1:5000/text")

  // Converting received data to JSON
  .then(response => response.json())
  .then(json => {

    li = "";
  
    json.forEach(text => {
      li += `<tr>
        <td>${text.text} </td>`;
  });

  document.getElementById("text").innerHTML = li;
  });
};

function post_text() {
// Post does not work gives 400 or 415 (wrong inside body)
  fetch("http://127.0.0.1:5000/text", {
    
    method: "POST",
    
    body: JSON.stringify({ text: document.getElementById("text").value, }),

    headers: {
      "Content-type": "application/json; charset=UTF-8"
    }
  })

  .then(response => response.json())
  .then(json => {

    li = "";

    json.forEach(text => {
      li += `<tr>
        <td>${text.text} </td>`;
  });

  document.getElementById("output").innerHTML = li;
  document.getElementById("text").value = "";
  });
}