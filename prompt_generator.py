from langchain_core.prompts import PromptTemplate

template = PromptTemplate(
    template = '''Please summarize the research paper titled {paper_input} 
    with the following specifications: explanation style {style_input}
    (simple, maths, or code) and explanation length {length_input}, 
    including relevant mathematical equations if present 
    and explaining them using simple, intuitive code snippets where applicable, 
    while also using relatable analogies to simplify complex ideas;
    if certain information is not available in the paper,
    respond with “Insufficient information available” instead of guessing,
    and ensure the summary is clear, accurate, and aligned with the provided style and length.''',
    input_variables=['paper_input','style_input','length_input'],
    validate_template=True
)  

template.save('template.json')
