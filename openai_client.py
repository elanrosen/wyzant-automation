# openai_client.py

from decouple import config
from openai import OpenAI

def create_openai_client():
    OPENAI_API_KEY = config('OPENAI_API_KEY')
    return OpenAI(api_key=OPENAI_API_KEY)

def generate_openai_message(client, poster_name, job_subject, job_description):
    """
    Generates an OpenAI message using the GPT-3.5 Turbo model.

    Args:
        client (OpenAI.ChatCompletion): The OpenAI ChatCompletion client.
        poster_name (str): The name of the job poster.
        job_subject (str): The subject of the job posting.
        job_description (str): The description of the job posting.

    Returns:
        str: The generated message.

    """
    system_message = """"
            You are to help me draft intro messages to potential tutoring clients. I will provide you with a job posting description and client name, and you should generate a message greeting them, and mention the fact I have plenty of experience.

            Here's a template to use:

            1) 'Hi ___! I saw that you're looking for help with ___. I have plenty of experience with ____, and would love to help. Hope to hear from you!'

            (keep it short and sweet). If they use an acronym keep it in acronym form (don't restate the full word). 
            Also, if they are a college student looking for help on a project, mention you are confident 
            you'll be able to help them finish their project as soon as possible (mention you have experience 
            with CS projects as a recent student). Don't mention projects otherwise.

            Sometimes the job posting will be for a parent looking for help for their child. In this case, recognize that in your response.
            Sometimes the job posting will mention an introductory meeting. In this case, mention you're available for an introductory meeting.
            Sometimes the job posting will have additional information in the description. In this case, make sure to mention you're familiarity with any additional technologies mentioned.
            
            """

    prompt = f"Job Posting: \n Name: {poster_name}\n Subject: {job_subject}\n Description: {job_description}"

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": system_message},
            {"role": "user", "content": prompt},
        ]
    )

    return response.choices[0].message.content.strip("'")
