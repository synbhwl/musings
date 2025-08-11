from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from jinja2 import Template
import markdown

app = FastAPI()

@app.get('/')
def show_posts():
    try:
        with open('docs/musings.md', 'r') as f:
            musings_raw = f.read()
        musings_html = markdown.markdown(musings_raw)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"err: can't read main file: {str(e)}")

    try:
        with open('templates/index.html', 'r') as fh:
            html_template = Template(fh.read())
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"err: can't read template file: {str(e)}")


    final_html = html_template.render(
        content=musings_html
    )    

    return HTMLResponse(content=final_html)