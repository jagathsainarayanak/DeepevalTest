import pandas as pd 

def case_summarization_report(results):
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
    
def chat_summarization_report(results):
    chat_results = []
    overall_results = {}
    total_faithfulness = 0
    total_relavance = 0
    total_coherance = 0
    for result in results:
        chat_result = {}
        chat_result["faithfulness score"] = result.metrics[0].score
        chat_result["relavance score"] = result.metrics[1].score
        chat_result["coherance score"] = result.metrics[2].score
        chat_result["faithfulness reason"] = result.metrics[0].reason
        chat_result["relavance reason"] = result.metrics[1].reason
        chat_result["coherance reason"] = result.metrics[2].reason
        chat_result["status"] = result.success
        total_faithfulness += chat_result['faithfulness score']
        total_relavance += chat_result['relavance score']
        total_coherance += chat_result['coherance score']
        chat_results.append(chat_result)
    df = pd.DataFrame(chat_results)
    df.to_excel("output/chat_record_level_results.xlsx")
    overall_results['faithfulness score'] = (total_faithfulness / len(chat_results)) * 100
    overall_results['relavance score'] = (total_relavance / len(chat_results)) * 100
    overall_results['coherance score'] = (total_coherance / len(chat_results)) * 100
    df = pd.DataFrame(list(overall_results.items()), columns=['Metric', 'Score'])
    df.to_excel("output/chat_overall_results.xlsx")

def search_qa_report(results):
    outputs = []
    for result in results:
        output = {}
        output['input'] = result.input
        output['expected output'] = result.expected_output
        output['actual output'] = result.actual_output
        output['status'] = result.success
        output['score'] = result.metrics[0].score
        output['reason'] = result.metrics[0].reason
        outputs.append(output)
    df = pd.DataFrame(outputs)
    df.to_excel("/Users/jagathsa.kakaraparty/Documents/GitHub/DeepevalTest/output/search_qa_record_level_metrics.xlsx")