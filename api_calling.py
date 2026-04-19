from google import genai
from dotenv import load_dotenv
import os
  

load_dotenv()

api_ke= os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=api_ke)




#issue generator
def issue_generator(image):

    prompt=""" You are a code debuger and you have to find out the error in the code.
    Do not provide the solution or hints.
    """
    response=client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=[prompt,image]
    )
    return response.text



#hints generator
def hints_generator(image):

    prompt=""" You are a code debuger and you have to debug the code given in the image 
    and find out the error in the code. give hints to the user to fix the error.
    """
    response=client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=[prompt,image]
    )
    return response.text


#solution generator
def solution_generator(image):

    prompt=""" You are a code debuger and you have to debug the code given in the image 
    and find out the error in the code. provide the solution to fix the error.
    """
    response=client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=[prompt,image]
    )
    return response.text

