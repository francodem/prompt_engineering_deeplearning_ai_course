import openai
from dotenv import load_dotenv
from os import getenv

# Getting environment variables
load_dotenv()

# Setting openai api key
openai.api_key = getenv('OPENAI_API_KEY')


def get_completion(prompt, model='gpt-3.5-turbo'):
    messages = [{'role': 'user', 'content': prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0
    )
    
    return response.choices[0].message['content']


text = f"""
You should express what you want a model to do by \
providing instructions that are as clear and \
specific as you can possibly make them. \
This will guide the model towards the desired output, \
and reduce the chances of receiving irrelevant \
or incorrect responses. Don't confuse writing a \
clear prompt with writing a short prompt. \
In many cases, longer prompts provide more clarity \
and context for the model, which can lead to \
more detailed and relevant outputs.
"""

# in the prompt are delimited the input to prevent
# possible prompt injections using triple backticks (```)
prompt = f"""
Summarize the text delimited by triple backticks \
into a single sentence.
```
{text}
```
"""

# response = get_completion(prompt)
# print(response)

prompt = f"""
Generate a list of three made-up book titles along \
with their authors and genres.
Provide them in JSON format with the following keys:
book_id, title, author, genre.
"""
# response = get_completion(prompt)
# print(response)

text = """
Create a landing page to then run a script over it, after that \
build a code to operate the cloud infrastructure. You will finish \
when the response results in a 200 code.
"""

prompt = f"""
You will be provided with text delimited by triple quotes.
If it containes a sequence of instructions, \
re-write those instructions in the following format:

Step 1 - . . .
Step 2 - . . .
...
Step N - . . .

If the text does not contain a sequence of instructions, \
then simply write \"No steps provided.\"

\"\"\"{text}\"\"\"
"""

# response = get_completion(prompt)
# print(response)

text = """
Francisco goes to the UNIR to learn more about
Artificial Intelligence where he will found more
details about the new technology of the future.
"""

prompt = f"""
Your task is to perform the following actions:
1 - Summarize the following text delimited by
  <> with 1 sentence.
2 - Translate the summary into French.
3 - List each name in the French summary.
4 - Output a json object that contains the
  following keys: french_summary, num_names.

Use the following format:
Text: <text to summarize>
Summary: <summary>
Translation: <summary translation>
Names: <list of names in Italian summary>
Output JSON: <json with summary and num_names>

Text: <{text}>
"""

# response = get_completion(prompt)
# print(response)
text = f"""
Let x be the size of the installation in square feet.
Costs:
1. Land cost: 100x
2. Solar panel cost: 250x
3. Maintenance cost: 100,000 + 100x
Total cost: 100x + 250x + 100,000 + 10x = 350x + 100,000
"""

prompt = f"""
Your task is to determine if the student's solution \
is correct or not.
To solve the problem do the following:
- First, work out your own solution to the problem.
- Then compare your solution to the student's solution \
and evaluate if the student's solution is correct or not.
Don't decide if the student's solution is correct until
you have done the problem yourself.

Use the following format:
Question:
```
question here
```
Student's solution:
```
student's solution here
```
Actual solution:
```
steps to work out the solution and your solution here
```
Is the student's solution the same as actual solution \
just calculated:
```
yes or no
```
Student grade:
```
correct or incorrect
```
Question:
```
I'm building a solar power installation and I need help \
working out the financials.
- Land costs $100 / square feet
- I can buy solar panels for $250 / square feet
- I negotiated a contract for maintenance that will cost \
me a flat $100k per year, and an additional $10 / square \
feet
What is the total cost for the first year of operations \
as a function of the number of the square feet.
```
Student's solution:
```
{text}
```
Actual solution:
"""

# the model isn't good with maths
# response = get_completion(prompt)
# print(response)

fact_sheet_chair = """
OVERVIEW
- Part of a beautiful family of mid-century inspired office furniture, 
including filing cabinets, desks, bookcases, meeting tables, and more.
- Several options of shell color and base finishes.
- Available with plastic back and front upholstery (SWC-100) 
or full upholstery (SWC-110) in 10 fabric and 6 leather options.
- Base finish options are: stainless steel, matte black, 
gloss white, or chrome.
- Chair is available with or without armrests.
- Suitable for home or business settings.
- Qualified for contract use.

CONSTRUCTION
- 5-wheel plastic coated aluminum base.
- Pneumatic chair adjust for easy raise/lower action.

DIMENSIONS
- WIDTH 53 CM | 20.87”
- DEPTH 51 CM | 20.08”
- HEIGHT 80 CM | 31.50”
- SEAT HEIGHT 44 CM | 17.32”
- SEAT DEPTH 41 CM | 16.14”

OPTIONS
- Soft or hard-floor caster options.
- Two choices of seat foam densities: 
 medium (1.8 lb/ft3) or high (2.8 lb/ft3)
- Armless or 8 position PU armrests 

MATERIALS
SHELL BASE GLIDER
- Cast Aluminum with modified nylon PA6/PA66 coating.
- Shell thickness: 10 mm.
SEAT
- HD36 foam

COUNTRY OF ORIGIN
- Italy
"""

prompt = f"""
Your task is to help a marketing team create a 
description for a retail website of a product based 
on a technical fact sheet.

Write a product description based on the information 
provided in the technical specifications delimited by 
triple backticks.

Technical specifications: ```{fact_sheet_chair}```
"""
# response = get_completion(prompt)
# print(response)

context = []
while True:
    user_input = str(input())

    prompt = f"""
    BACKGROUND
    Tu seras un agente de ventas de servicios de Internet, ofreceras los servicios \
    de la siguiente manera siguiendo paso a paso de la seccion de PASOS que se te dara \
    a continuacion teniendo en cuenta el paso en el que te encuentras, leeras el contexto \
    , y con ello basaras tu conversacion. Ten en cuenta el nombre de la compañia que ofrece \
    los servicios: Totalplay. Tambien ten en cuenta los PAQUETES disponibles. Ten en cuenta el \
    estado de la conversacion actual en CONTEXTO brindado entre comillas triples (```). No olvides \
    tener en cuenta la entrada del usuario como USER INPUT como el estado de la conversacion más actual \
    brindado entre puntos triples (...).

    PAQUETES
    A. Paquete Sonico de 50 MB de Internet. Precio lista $400 MXN por mes, precio promocion \
    $350 MXN por mes.
    B. Paquete Sonico 2 de 100 MB de Internet. Precio lista $600 MXN por mes, precio promocion \
    $500 MXN por mes.

    VENTAJAS
    A. Mejor compañia de servicios en México.
    B. Mejor internet en el país.
    C. Mejor precio del mercado.

    PASOS
    1 - Saludar: Saludar al usuario y darle la bienvenida a la compañia de servicios.
    2 - Ver su necesidad: Lee lo que el usuario te responda y aborda su necesidad. En caso \
    de que no te escriba su necesidad y solo un saludo, ofrece tu a cambio los paquetes que \
    se tienen disponibles. Consulta los paquetes para ello y brindacelos.
    3 - Mencionar ventajas: Una vez hayas anunciado los paquetes, lee que cual es el paquete \
    que al usuario le parece mejor. En caso de que el usuario dude sobre el servicio, mencionale \
    las ventajas que ofrece la compañia de servicios. Para ello ten en cuenta las VENTAJAS. 
    4 - Cierre de venta: Una vez te diga que quiere cierto paquete, invita al usuario a que te \
    brinde su nombre completo, fecha de nacimiento, ciudad de residencia y domicilio.

    IMPORTANTE
    No hables de nada que no tenga que ver con este BACKGROUND que te fue encomendado. Para el caso \
    de que no te hable el usuario sobre esto relacionado, mencionale que no puedes brindar informacion \
    que no sea relacionada al servicio que ofrece la compañia. No brindes la misma informacion contenida \
    en CONTEXTO y INPUT DEL USUARIO. Siempre brinda nueva informacion.

    CONTEXTO
    ```{context}```

    INPUT DEL USUARIO
    ...{user_input}...
    """

    response = get_completion(prompt)

    print(response + '\n')

    context.append(f"AGENTE:{response}")
    context.append(f"USUARIO:{user_input}")
    