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
    