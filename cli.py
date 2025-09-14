import requests
import json

system_prompt = """
You are part of an RPG game. This RPG game is designed to prepare soldiers for when they are deployed to foreign countries.

China as an adversary country has stepped in to help a 3rd world country

The united states must step back in to regain its soft power and influence in the region.

In this particular scenario, you are a Cambodian local who is mistrusting of the US.
Please brainstorm a detailed background, personality, and motivations for your character.
Please respond in concise, natural sentences. This is a natural conversation, so avoid overly formal, robotic, or lengthy language.
"""

def main():
    print("Welcome to paX CLI chat!")
    print("Type your message and press Enter. Type 'exit' to quit.")
    messages = [
        {"role": "system", "content": system_prompt}
    ]
    while True:
        user_input = input("You: ")
        if user_input.strip().lower() == "exit":
            print("Goodbye!")
            break
        messages.append({"role": "user", "content": user_input})
        payload = {"messages": messages}
        try:
            assistant_reply = ""
            print(f"Agent: ", end="", flush=True)
            with requests.post(
                "http://localhost:8000/chat",
                headers={"Content-Type": "application/json"},
                data=json.dumps(payload),
                stream=True,
            ) as r:
                for line in r.iter_content(chunk_size=None, decode_unicode=True):
                    if line:
                        assistant_reply += line
                        print(line, end="", flush=True)
            print()
            messages.append({"role": "assistant", "content": assistant_reply})
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
