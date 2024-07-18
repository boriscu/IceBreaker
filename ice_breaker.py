from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser

from third_parties.linkedin import scrape_linkedin_profile

if __name__ == "__main__":

    summary_template = """
        given the information {information} about a company from I want you to create a:
        1. a short summary in 3 sentences
        2. 2 sentences regarding their workplace/company
        3. two interesting facts about them
    """

    summary_prompt_template = PromptTemplate(
        input_variables=["information"], template=summary_template
    )

    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")

    chain = summary_prompt_template | llm | StrOutputParser()

    linkedin_data = scrape_linkedin_profile(mock=True)

    res = chain.invoke(input={"information": linkedin_data})

    print(res)
