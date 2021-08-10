from pandas import read_csv
from graphutils import Graph, get_dependents, get_dependencies

from flask import Flask, json, render_template,request

app = Flask(__name__,template_folder='front')

df = read_csv('grade_software.csv').values.tolist()

edges = []

# print(df)
for lista in df:
  lista[1] = eval(lista[1])
  if len(lista[1]) == 0:
    edges.append((lista[0], ''))
  for dependencie in lista[1]:
    # print(f"{lista[0]} -> {dependencie}")
    edges.append((lista[0], dependencie))
# print(edges)

grafo = Graph(edges = edges, directed = True)



@app.route('/', methods=["GET","POST"])
def index():
    if request.method == "GET":
        vertices = grafo.get_vertices()
        vertices.remove('')
        return render_template("index.html",vertices=vertices)
    else:
        target = str(request.form.get('target')).replace("_"," ")
        dependent = get_dependents(grafo, target)
        # dependent[0] = [i for i in dependent[0] if i != '']
        if '' in dependent[0]:
            dependent[0] = ['Nenhuma matéria' for i in dependent[0] if i == '']
        if '' in dependent[1]:
            dependent[1] = ['Nenhuma matéria' for i in dependent[1] if i == '']
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
