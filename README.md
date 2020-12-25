# Extract-Blogs-api
Flask code to deploy an API that translates Text Accurately to any of the 103 languages

Translations between the following languages are supported:

This is a source code of an API that you can find here (free plan available): https://rapidapi.com/karthikhosur15/api/language-translator1




![](extract_image.png)


## Quick Start
1. Clone the repository to your local folder 


2. Create a Python virtual environment (3.6+)

`python -m venv env`

3. Activate the environment

`source env/bin/activate`

4. Run `pip install -r requirements.txt`
5. Run `python app.py` in your terminal 

If everything is OK then you should be able to check your API on `http://127.0.0.1:5000/translate`

Example of request: `http://127.0.0.1:5000/translate`
``
Request Body: 
{
"text": "The world is a beautiful place to live in. I love to eat a lot of food.",
"output_language": "fr"
}
``
## Example of Response Body
``` 
{
"input_language":"en"
"output_language":"fr"
"text":"Le monde est un endroit magnifique où vivre. J&#39;adore manger beaucoup."
}
```


## Built with
[Flask](https://github.com/pallets/flask) Copyright 2010 Pallets

