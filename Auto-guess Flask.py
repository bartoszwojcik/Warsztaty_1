#! python3
from flask import Flask, request

app = Flask(__name__)


class RangeError(Exception):
    pass


@app.route("/", methods=["GET", "POST"])
def interface():
    """
    Simple website with forms for running a guessing game. User thinks of a number and gives hints to the computer.
    The solution is not safe though, as values are written into secret fields in HTML form.
    :return: html on GET, auto_guess function on POST
    """
    def auto_guess(min, max, attempt=1, hint=""):
        """
        Function for creating response to user input. Attempts to guess the correct number.
        :param min: integer, currently evaluated minimal possible number
        :param max: integer, currently evaluated maximal possible number
        :param attempt: integer, id of the current attempt
        :param hint: string, last hint provided by the user using an html form (button value)
        :return: string or f-string providing html with guessing form and updated secret values
        """
        if hint == "won":
            return "Wygrałem!"
        elif attempt == 11:
            return f"Nie oszukuj! {guess_html.format(min, max, attempt)}"
        elif hint == "more":
            min = int((max - min) / 2) + min
        elif hint == "less":
            max = int((max - min) / 2) + min

        guess = int((max - min) / 2) + min
        attempt += 1
        return f"Zgaduję: {guess} {guess_html.format(min, max, attempt)}"

    initial_html = """
    <html>
        <body>
            <h2>Zgadywanka</h2>
            <p>Pomyśl o liczbie z przedziału 1 do 1000. Komputer spróbuje odgadnąć Twoją liczbę w 10 próbach. Podpowiadaj mu naciskacjąc odpowiedni przycisk.</p>
            <p>Nie oszukuj ;-)</p>
            <form method="POST" action="/">
                <input type="hidden" value={} name="min" />
                <input type="hidden" value={} name="max" />
                <button type="submit" name="hint" value="start">Start</button>
            </form>
        </body>
    </html>
    """

    guess_html = """
    <html>
        <body>
            <form method="POST" action="/">
                <input type="hidden" value={} name="min" />
                <input type="hidden" value={} name="max" />
                <input type="hidden" value={} name="attempt" />
                <button type="submit" name="hint" value="more">więcej</button>
                <button type="submit" name="hint" value="less">mniej</button>
                <button type="submit" name="hint" value="won">trafiłeś</button>
            </form>
        </body>
    </html>
    """

    if request.method == "GET":
        return initial_html.format(0, 1000)
    elif request.method == "POST" and request.form['hint'] == "start":
        return auto_guess(int(request.form['min']), int(request.form['max']))
    elif request.method == "POST":
        return auto_guess(int(request.form['min']), int(request.form['max']),
                          int(request.form['attempt']), request.form['hint'])


if __name__ == "__main__":
    app.run()
