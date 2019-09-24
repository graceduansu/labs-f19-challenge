from flask import Flask, render_template, request
import requests

app = Flask(__name__)


@app.route('/', methods=['GET'])
def main():
    return render_template('index.html')


@app.route('/pokemon/<query>', methods=['GET'])
def show_pokemon_query_result(query):
    error = None
    response = requests.get('https://pokeapi.co/api/v2/pokemon/{}'.format(query))
    if response:
        json = response.json()
        is_name = False
        try:
            int(query)
        except ValueError:
            is_name = True

        if is_name:
            # if query is id, return name
            return render_template('pokemon.html', id=json.get('id'), payload=json.get('name'))
        else:
            # if query is name, return id
            return render_template('pokemon.html', name=json.get('name'), payload=json.get('id'))
    else:
        return render_template('pokemon.html', error=error)


if __name__ == '__main__':
    app.run()
