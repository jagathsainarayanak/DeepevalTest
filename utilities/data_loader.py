import pandas as pd
import yaml
from yaml import Loader
from yaml.loader import SafeLoader

class PromptBuilder:
    def create_summary(self, dataset, case_details):
            instruction = self.get_instruction(dataset)
            tags = self.get_tags('nowllm')
            return tags.format(system_prompt = instruction['system'], user_prompt = instruction['user'], case_details= case_details)

    def create_search(self, dataset, context, query):
            instruction = self.get_instruction(dataset)
            if dataset == 'search_qa':
                tags = self.get_tags('nowllm_search')
            else:
                tags = self.get_tags('nowllm')
            return tags.format(system_prompt = instruction['system'], user_prompt = instruction['user'].format(CONTEXT=context, QUERY=query))

    def get_tags(self, model):
        with open('/Users/jagathsa.kakaraparty/Documents/GitHub/DeepevalTest/Tags_Prompts/tags.yaml','r') as file:
            tag = yaml.load(file, Loader)
        return tag[model]
        
    def get_instruction(self,dataset):
        with open("/Users/jagathsa.kakaraparty/Documents/GitHub/DeepevalTest/Tags_Prompts/prompts.yaml",'r') as file:
            values = yaml.load(file,Loader=SafeLoader)
        return values[dataset]

    def load_case_summarization_data(self):
        df = pd.read_json("/Users/jagathsa.kakaraparty/Documents/GitHub/DeepevalTest/data/servicenow_data/latest_case_data.json")
        data = []
        for i in range(len(df)):
            data.append({"prompt": self.create_summary('case_summarization', df.iloc[i]['case_details']), 'case_details': df.iloc[i]["case_details"]})
        return data

    def load_chat_summarization_data(self):
        df = pd.read_json("/Users/jagathsa.kakaraparty/Documents/GitHub/DeepevalTest/data/servicenow_data/latest_chat_data.json")
        data = []
        for i in range(len(df)):
            data.append({"prompt": self.create_summary('chat_summarization', df.iloc[i]["case_details"]), 'case_details': df.iloc[i]["case_details"]})
        return data

    def load_search_qa_data(self):
        df = pd.read_json('/Users/jagathsa.kakaraparty/Documents/GitHub/DeepevalTest/data/servicenow_data/search_qa.json')
        data_records = []
        for i in range(len(df)):
            data_records.append({'prompt':self.create_search('search_qa',df.iloc[i]['CONTEXT'], df.iloc[i]['QUERY']),'ground_truth':df.iloc[i]['GROUND_TRUTH'],'query':df.iloc[i]['QUERY'],'context':df.iloc[i]['CONTEXT'] })
        return data_records