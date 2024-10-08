fetch("http://localhost:5000/text")

  // Converting received data to JSON
  .then(response => response.json())
  .then(json => {
  
    json.forEach(text => {
      li += `<tr>
        <td>${text.text} </td>`;
  });

  document.getElementById("text").innerHTML = li;
});