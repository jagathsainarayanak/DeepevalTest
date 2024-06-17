import pandas as pd

def load_case_summarization_data(file_path, system_prompt, user_prompt):
    df = pd.read_json(file_path)
    data = []
    for i in range(len(df)):
        case_prompt = f"""<|system|>\n{system_prompt}\n<|end|>\n<|user|>\n{df.iloc[i]['case_details']}\n{user_prompt}\n<|end|>\n<|assistant|>\n"""
        case_data = {}
        case_data["prompt"] = case_prompt
        case_data["case_detail"] = df.iloc[i]["case_details"]
        data.append(case_data)
    return data

def load_chat_summarization_data(file_path, system_prompt, user_prompt):
    df = pd.read_json(file_path)
    data = []
    for i in range(len(df)):
        new_user_prompt = user_prompt[:]
        new_user_prompt = new_user_prompt.replace("\{case_details\}", df.iloc[i]['case_details'])
        case_prompt = f"""<|system|>\n{system_prompt}\n<|end|>\n<|user|>\n{user_prompt}\n<|end|>\n<|assistant|>\n"""
        case_data = {}
        case_data["prompt"] = case_prompt
        case_data["case_detail"] = df.iloc[i]["case_details"]
        data.append(case_data)
    return data

def load_search_qa_data(file_path, system_prompt, user_prompt):
    df = pd.read_json(file_path)
    data_records = []
    for i in range(len(df)):
        new_user_prompt = user_prompt[:]
        new_user_prompt = new_user_prompt.replace('\{CONTEXT\}', df.iloc[i]['CONTEXT'])
        new_user_prompt = new_user_prompt.replace('\{QUERY\}', df.iloc[i]['QUERY'])
        input_prompt = f"""<|system|>\n{system_prompt}\n<|end|>\n<|user|>\n{user_prompt}\n<|end|>\n<|assistant|>\n"""
        data_record = {}
        data_record['prompt'] = input_prompt
        data_record['ground_truth'] = df.iloc[i]['GROUND_TRUTH']
        data_record['query'] = df.iloc[i]['QUERY']
        data_record['context'] = df.iloc[i]['CONTEXT']
        data_records.append(data_record)
    return data_records
