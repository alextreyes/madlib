from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from stories import Story, story

this_story = story
app = Flask(__name__)


app.config['SECRET_KEY'] = 'secret_key'
app.debug = True

toolbar = DebugToolbarExtension(app)


@app.route("/")
def home():
    s = this_story.prompts
    return render_template("index.html", story_prompts=s)


# @app.route("/story")
# def story():
#     place = request.args
#     this = []
#     a = []
#     dict = {}
#     for prompt in request.args:
#         a.append(request.args[prompt])
#         this.append(prompt)
#         dict[prompt] = request.args[prompt]

#     return render_template("story.html", prompt=a, ans=this, dicta=dict)

@app.route("/story")
def show_story():
    """Show story result."""

    text = story.generate(request.args)

    return render_template("story.html", text=text)
