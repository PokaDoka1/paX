import os
from flask import Flask, Response, request
from flask_cors import CORS, cross_origin
import cohere
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
cors = CORS(app)

co = cohere.ClientV2(
    os.environ["COHERE_API_KEY"]
)

@app.route("/chat", methods=["POST"])
@cross_origin()
def chat():
    messages = request.json["messages"]

    def generate():
        response = co.chat_stream(
            model="command-a-03-2025",
            messages=messages,
        )

        for chunk in response:
            if chunk and chunk.type == "content-delta":
                yield chunk.delta.message.content.text

    return Response(generate(), mimetype="text/plain")

if __name__ == "__main__":
    print("starting")
    app.run(port=8000, debug=True)
