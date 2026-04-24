import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate, SystemMessagePromptTemplate, HumanMessagePromptTemplate

load_dotenv()

class AIGenerator:

    def __init__(self):
        api_key = os.getenv("gemini_key")
        if not api_key:
            raise ValueError("API key not found")

        os.environ["GOOGLE_API_KEY"] = api_key

        self.model = ChatGoogleGenerativeAI(
            model="gemini-2.5-flash"
        )

    def generate_website(self, description, content):
        system_template = """You are a Senior Frontend Web Developer with 10+ years experience in HTML5, CSS3, and modern JavaScript (ES6+).

                            Generate COMPLETE frontend code.

                            FORMAT:

                            ---html---
                            [html]
                            ---html---

                            ---css---
                            [css]
                            ---css---

                            ---js---
                            [js]
                            ---js---
                            """

        human_template = "Build a {description} using: {content}"

        system_message = SystemMessagePromptTemplate.from_template(system_template)
        human_message = HumanMessagePromptTemplate.from_template(human_template)

        chat_prompt = ChatPromptTemplate.from_messages([system_message, human_message])

        prompt = chat_prompt.invoke({
            "description": description,
            "content": content
        })

        response = self.model.invoke(prompt)

        return response.content