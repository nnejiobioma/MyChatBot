const chatDisplay = document.querySelector('.chatDisplay ul')
const userInput = document.getElementById("user-input")
const sendButton = document.getElementById("send")

const handleInput = () => {
    const message = userInput.value.trim();
    generateResponse(message);
    
    if (message !== ''){
        const MessageItem = document.createElement('li');
        MessageItem.className = "outgoing";
        MessageItem.innerHTML = `
            <p class="userMessage"></p>
            <span class="userIcon material-symbols-rounded">Face</span>
        `;

        MessageItem.querySelector('p').textContent = message;
        chatDisplay.appendChild(MessageItem);

        userInput.value = "";
    }
}

const generateResponse = (userMessageItem) => {
    const API_URL = "https://api.openai.com/v1/chat/completions"

    const requestOptions = {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            "Authorization": `Bearer ${API_KEY}`
        },
        body: JSON.stringify({
            model: "gpt-3.5-turbo",
            messages: [{role: "user", content: userMessageItem}]
        })
    }

    fetch(API_URL, requestOptions)
    .then(res => res.json())
    .then(data => {
        const botMessageCont = data.choices[0].message.content;
            console.log(botMessageCont)
        const botMessageItem = document.createElement('li')
        botMessageItem.className ="incoming";
        botMessageItem.innerHTML = `
        <span class="botIcon material-symbols-rounded">smart_toy</span>
        <p class="botMessageCont"></p>
        `;

        botMessageItem.querySelector('p').textContent = botMessageCont;
        chatDisplay.appendChild(botMessageItem)
    })
    .catch(error => {
        console.log(error)
    })
}

sendButton.addEventListener("click", handleInput)
userInput.addEventListener("keydown", (e) => {
    if (e.key === "Enter" && !e.shiftKey && window.innerWidth > 800){
        e.preventDefault();
        handleChat();
    }
})

