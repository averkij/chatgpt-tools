#%%

# pip install revChatGPT
# https://github.com/acheong08/ChatGPT

from revChatGPT import Official
import json
import time
import random

FILE_OUT = "res.txt"

# get API KEY here: https://platform.openai.com/account/api-keys

chatbot = Official.Chatbot(api_key="<API_KEY>")

#%%
adv = ["brave", "smart", "dumb"]
animals = ["monkey", "cat", "dog", "elephant", "fox", "bear", "hare"]

TEMPERATURE = 0.5

for _ in range(5):
    query = f"write a hokku about {random.choice(adv)} {random.choice(animals)}"

    print("A:", query, "\n")

    res = chatbot.ask(query, temperature=TEMPERATURE)
    res_json = {"query": query, "temperature": TEMPERATURE, "answer_raw": dict(res)}

    with open(FILE_OUT, mode="a", encoding="utf-8") as fout:
        fout.write(json.dumps(res_json) + "\n")

    print(
        "Q:",
        res_json["answer_raw"]["choices"][0]["text"].strip(),
        "\n\n-----------------------\n",
    )

    time.sleep(1 + random.randint(2, 5) / 10)

# %%
