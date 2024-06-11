from deepeval.models.base_model import DeepEvalBaseLLM
import requests
import json

class NowLLM(DeepEvalBaseLLM):
    def __init__(self,url,authtoken):
        self.url= url
        self.authtoken= authtoken

    def load_model(self):
        return self.url, self.authtoken

    def generate(self, prompt: str) -> str:
        final_prompt = "<|system|><|end|>\n\n<|user|>{}<|end|>\n\n<|assistant|>".format(prompt)
        llm_msg_body = {
            "inputs": final_prompt,
            "parameters": {
                "max_new_tokens": 500,
                "temperature": 0.01,
                "do_sample": True,
                "num_beams": 1,
                "no_repeat_ngram_size": 25
            }
        }
        header_json = {'Content-Type': 'application/json', 'formatter': 'dummy_formatter',
                   'chat_formatter': 'dummy_formatter', 'server': 'huggingface_server', 'Authorization': self.authtoken}
        resp = requests.post(self.url, json=llm_msg_body, headers=header_json)
        if resp.status_code == 200:
            resp = self.process_response(resp)
        else:
            print("error: response code from model API = ", str(resp.status_code))
        return resp

    def process_response(self, response):
        generated_text = json.loads(response.text)['generated_text']
        return generated_text.replace("<|end|>","").replace("</s>","").replace("</s","").replace("</","").strip()

    async def a_generate(self, prompt: str) -> str:
        return self.generate(prompt)

    def get_model_name(self):
        return "NowLLM"