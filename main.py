from pandas import read_csv
from graphutils import Graph, get_dependents, get_dependencies

from flask import Flask, json, render_template,request

app = Flask(__name__,template_folder='front')

df = read_csv('grade_software.csv').values.tolist()

edges = []

for lista in df:
  lista[1] = eval(lista[1])
  for dependencie in lista[1]:
    edges.append((lista[0], dependencie))

grafo = Graph(edges = edges, directed = True)


@app.route('/', methods=["GET","POST"])
def index():
    if request.method == "GET":
        return render_template("index.html")
    else:
        print("entrou")
        target = str(request.form.get('target'))
        dependent = get_dependents(grafo, target)
        dependencie = get_dependencies(grafo, target)
        return render_template('list.html', target=target, dependent=dependent, dependencies=dependencie)
        # return f"<h1>{target}</h1>"


@app.route('/dependencies/<string:target>')
def dependencies(target):
    result = get_dependencies(grafo, target)

    data = { 'target': target, 'dependencies': result }
    response = app.response_class(
            response=json.dumps(data),
            status=200,
            mimetype='application/json'
        )
    return response

@app.route('/dependents/<string:target>')
def dependents(target):
    result2 = get_dependents(grafo, target)
    data = { 'target': target, 'direct': result2[0], 'indirect': result2[1] }
    response = app.response_class(
            response=json.dumps(data),
            status=200,
            mimetype='application/json'
        )
    return response

app.run(debug=True)
