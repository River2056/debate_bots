from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate


class Message:
    def __init__(self, id, msg):
        self.id = id
        self.msg = msg

    def __str__(self):
        return f"Message[id: {self.id}, msg: {self.msg}]"


class ChatBot:
    def __init__(
        self, model, id, total_rounds=0, topic="", setting_prompt="", setting_partial=""
    ):
        self.id = id
        self.total_rounds = total_rounds
        self.topic = topic
        self.setting_prompt = setting_prompt
        self.setting_partial = setting_partial
        self.msg = []
        model = OllamaLLM(model=model)
        prompt = ChatPromptTemplate.from_template(setting_prompt)
        self.chain = prompt | model

    def debate(self, current, all_msgs):
        filtered_msgs = list(filter(lambda x: x.id != self.id, all_msgs))
        # print(f"messages by {self.id}: {self.msg}")
        # for fil_msg in filtered_msgs:
        #     print(f"messages by others: {fil_msg.id}::{fil_msg.msg}")

        result = self.chain.invoke(
            {
                "setting": self.setting_partial,
                "topic": self.topic,
                "total": self.total_rounds,
                "current": current,
                "selfMsgs": self.msg,
                "allMsg": filtered_msgs,
            }
        )
        msg = Message(self.id, result)
        self.msg.append(msg)
        print(msg)
        return msg
