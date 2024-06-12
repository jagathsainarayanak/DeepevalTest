class Prompts():

    CASE_SUMMARIZATION_SYSTEM_PROMPT = "You are a customer service representative. You are optionally given SHORT_DESCRIPTION, DESCRIPTION, PRIORITY, STATE and ACTIVITIES. ACTIVITIES contain an array of activities from activity stream with created date, its type such as a comment or work note and if it's added by agent or customer and the text."
    CASE_SUMMARIZATION_USER_PROMPT = """Based on the given input only, summarize the provided information and extract that into following sections:
        Issue - The Issue section should represent what the case is about. Return only a string for this section.
        Key Actions Taken - The Actions Taken section should provide a list of significant actions performed to investigate and resolve the case. Do not consider logs, alerts, attachments, stack traces, json outputs, unix shell outputs and source code in the given input text. Return only a list of strings for this section.
        Resolution - The Resolution section should highlight the action or actions only if absolutely sure the problem was resolved. Do not consider logs, alerts, attachments, stack traces, json outputs, unix shell outputs and source code in the given input text. Return only a string for this section.
        Only use the provided information. Do not reproduce details as is in the summary output, make sure to respond with a concise summary. Do not generate any information which is not provided. If you are not absolutely sure, return N/A. DO NOT GENERATE ANY EXPLANATION, REASONING, COMMENTARY OR DESCRIPTION ABOUT THE SUMMARY.
        Always generate the output in below JSON format.

        {"Issue": <issue>,"Key Actions Taken":<[value1,value2,value3...]>,"Resolution":<resolution>}"""
    
    CHAT_SUMMARIZATION_SYSTEM_PROMPT = "Assume the role of a description writer who is an expert in writing a very short description for the CHAT TRANSCRIPT provided."
    CHAT_SUMMARIZATION_USER_PROMPT = "In a clear and concise language, provide a meaningful short description that describes the issue or the request which is contained in the CHAT TRANSCRIPT provided. Return the response keeping it very short exceeding not more than 6 words and do not add any double quotation marks in the beginning and at the end of the response."