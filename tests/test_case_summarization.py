from deepeval.metrics import GEval, AnswerRelevancyMetric
from deepeval.test_case import LLMTestCaseParams, LLMTestCase
from deepeval import evaluate
import pandas as pd 

from utilities.Read_config import Config_read
from utilities.data_loader import load_data
from utilities.prompts import Prompts
from models.Nowllm import NowLLM


def test_case_summarization():
    system_prompt = Prompts.CASE_SUMMARIZATION_SYSTEM_PROMPT
    user_prompt = Prompts.CASE_SUMMARIZATION_USER_PROMPT
    data = load_data(file_path="data/servicenow_data/latest_case_data.json",
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
    faithfulness_metric = GEval(
        threshold=0.7,
        name="Faithfulness",
        criteria="Determine whether the actual output is factually correct based on the input.",
        evaluation_params=[LLMTestCaseParams.INPUT, LLMTestCaseParams.ACTUAL_OUTPUT],
    )
    relavance_metric = AnswerRelevancyMetric(
        threshold=0.7,
        model="gpt-4",
        include_reason=True
    )
    coherance_metric = GEval(
        threshold=0.7,
        name="Coherance",
        criteria="Does the actual output organize the information into a well-structured summary?",
        evaluation_params=[LLMTestCaseParams.INPUT, LLMTestCaseParams.ACTUAL_OUTPUT]
    )
    results = evaluate(
        test_cases=test_cases,
        metrics=[faithfulness_metric, relavance_metric, coherance_metric]
    )
    case_results = []
    for result in results:
        case_result = {}
        case_result["faithfulness score"] = result.metrics[0].score
        case_result["relavance score"] = result.metrics[1].score
        case_result["coherance score"] = result.metrics[2].score
        case_result["faithfulness reason"] = result.metrics[0].reason
        case_result["relavance reason"] = result.metrics[1].reason
        case_result["coherance reason"] = result.metrics[2].reason
        case_result["status"] = result.success
        case_results.append(case_result)
    df = pd.DataFrame(case_results)
    df.to_excel("output/case_results.xlsx")
