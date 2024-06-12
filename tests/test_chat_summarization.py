from deepeval.test_case import LLMTestCase
from deepeval import evaluate

from utilities.Read_config import Config_read
from utilities.data_loader import load_chat_summarization_data
from utilities.prompts import Prompts
from utilities.metrics import faithfulness_metric, relavance_metric, coherance_metric
from utilities.cleanup import cleanup_pycache
from utilities.report import chat_summarization_report
from models.Nowllm import NowLLM


def test_chat_summarization():
    system_prompt = Prompts.CHAT_SUMMARIZATION_SYSTEM_PROMPT
    user_prompt = Prompts.CHAT_SUMMARIZATION_USER_PROMPT
    data = load_chat_summarization_data(file_path="data/servicenow_data/latest_chat_data.json",
                     system_prompt=system_prompt,
                     user_prompt=user_prompt)
    url = Config_read.read_conf()["Nowllm"]["url"]
    authtoken = Config_read.read_conf()["Nowllm"]["authtoken"]
    model = NowLLM(url, authtoken)
    model_responses = []
    test_cases = []
    for i in range(len(data)):
        model_response = model.generate(data[i]["prompt"])
        test_case = LLMTestCase(
            input=data[i]["case_detail"],
            actual_output=model_response
        )
        model_responses.append(model_response)
        test_cases.append(test_case)
        results = evaluate(
            test_cases=test_cases,
            metrics=[faithfulness_metric, relavance_metric, coherance_metric]
        )
    chat_summarization_report(results)
    cleanup_pycache()
