function addMessage(message, type) {
    // Create a new message element
    var messageElement = $("<div class='message " + type + "'></div>");
    messageElement.text(message);

    // Append message in chat history
    $("#chat-history").append(messageElement);
    // Scroll to lastest
    $("#chat-history").scrollTop($("#chat-history")[0].scrollHeight);
}

//addMessage("Hello Welcome to this chat")

// deprecated way to add old messages to history