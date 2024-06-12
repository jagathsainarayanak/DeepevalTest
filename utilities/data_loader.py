import pandas as pd

def load_data(file_path, system_prompt, user_prompt):
    df = pd.read_json(file_path)
    data = []
    for i in range(len(df)):
        case_prompt = f"""<|system|>\n{system_prompt}\n<|end|>\n<|user|>\n{df.iloc[i]['case_details']}\n{user_prompt}\n<|end|>\n<|assistant|>\n"""
        case_data = {}
        case_data["prompt"] = case_prompt
        case_data["case_detail"] = df.iloc[i]["case_details"]
        data.append(case_data)
    return data

    