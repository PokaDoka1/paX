import os
from flask import Flask, request
import cohere
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

co = cohere.ClientV2(
    os.environ["COHERE_API_KEY"]
)

@app.route("/chat", methods=["POST"])
def chat():
    messages = request.json["messages"]

    response = co.chat(
        model="command-a-03-2025",
        messages=messages,
    )

    return {"response": response.message.content[0].text}

if __name__ == "__main__":
    print("starting")
    app.run(port=8000, debug=True)
