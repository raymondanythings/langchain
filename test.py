
from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate,ChatPromptTemplate
from langchain.prompts.few_shot import FewShotPromptTemplate
from langchain.callbacks import StreamingStdOutCallbackHandler

chat = ChatOpenAI(temperature=0.1,
                model="gpt-4-turbo-preview",streaming=True,callbacks=[StreamingStdOutCallbackHandler()])

