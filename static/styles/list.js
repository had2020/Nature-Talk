// Get the elements by their ids and store them in variables
let addToDoButton = document.getElementById('addToDo');
let toDoContainer = document.getElementById('toDoContainer');
let inputField = document.getElementById('inputField');

// Add an event listener to the button that triggers a function when clicked
addToDoButton.addEventListener('click', function(){
    // Create a paragraph element and store it in a variable
    var paragraph = document.createElement('p');
    // Add the class paragraph-styling to the paragraph element
    paragraph.classList.add('paragraph-styling');
    // Set the inner text of the paragraph element to the value of the input field
    paragraph.innerText = inputField.value;
    // Append the paragraph element to the to-do container element
    toDoContainer.appendChild(paragraph);
    // Clear the value of the input field
    inputField.value = "";
    // Add an event listener to the paragraph element that triggers a function when clicked
    paragraph.addEventListener('click', function(){
        // Add a line-through style to the paragraph element
        paragraph.style.textDecoration = "line-through";
    })
    // Add an event listener to the paragraph element that triggers a function when double-clicked
    paragraph.addEventListener('dblclick', function(){
        // Remove the paragraph element from the to-do container element
        toDoContainer.removeChild(paragraph);
    })
})
