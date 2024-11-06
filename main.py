from flask import Flask, jsonify, request
from functools import reduce
import time

app = Flask(__name__)


@app.route("/a1g", methods=["POST"])
def square_root_a1g():
    """
    A1G: Ich kann die Eigenschaften von Funktionen beschreiben
    (z.Bsp. pure function) und den Unterschied zu anderen
    Programmierstrukturen erläutern (z.Bsp. zu Prozedur).
    """
    data = dict(request.get_json())
    return jsonify({"square root": int(data["value"]) ** 0.5})


@app.route("/a1f", methods=["POST"])
def double_list_a1f():
    """
    A1F: Ich kann das Konzept von *immutable values* erläutern
    und dazu Beispiele anwenden. Somit kann ich dieses Konzept
    funktionaler Programmierung im Unterschied zu anderen
    Programmiersprachen erklären (z.Bsp. im Vergleich zu referenzierten Objekten)
    """
    lst = list(dict(request.get_json())["value"])
    new_lst = [x * 2 for x in lst]
    return jsonify({"doubled list": new_lst})


@app.route("/a1e/oop", methods=["POST"])
def square_list_oop_a1e():
    """
    A1E: Ich kann aufzeigen wie Probleme in den verschiedenen Konzepten
    (OO, prozedural und funktional) gelöst werden
    und diese miteinander vergleichen.
    """
    class NumberProcessor:
        def __init__(self, numbers):
            self.numbers = numbers

        def square_numbers(self):
            return [x ** 2 for x in self.numbers]

    processor = NumberProcessor(list(dict(request.get_json())["value"]))
    squared_numbers = processor.square_numbers()
    return jsonify({"squared list": squared_numbers})


@app.route("/a1e/procedural", methods=["POST"])
def square_list_procedural_a1e():
    """
    A1E: Ich kann aufzeigen wie Probleme in den verschiedenen Konzepten
    (OO, prozedural und funktional) gelöst werden
    und diese miteinander vergleichen.
    """
    numbers = list(dict(request.get_json())["value"])
    squared_numbers = []
    for number in numbers:
        squared_numbers.append(number ** 2)
    return jsonify({"squared list": squared_numbers})


@app.route("/a1e/functional", methods=["POST"])
def square_list_functional_a1e():
    """
    A1E: Ich kann aufzeigen wie Probleme in den verschiedenen Konzepten
    (OO, prozedural und funktional) gelöst werden
    und diese miteinander vergleichen.
    """
    numbers = list(dict(request.get_json())["value"])
    squared_numbers = list(map(lambda x: x ** 2, numbers))
    return jsonify({"squared list": squared_numbers})


@app.route("/b1g", methods=["POST"])
def filter_b1g():
    numbers = list(dict(request.get_json())["value"])
    filtered = [x for x in numbers if x % 2 == 0]
    return jsonify({"result": filtered})


@app.route("/b1f", methods=["POST"])
def filter_splitt_b1f():
    numbers = list(dict(request.get_json())["value"])

    def is_even(x):
        return x % 2 == 0

    filtered = [x for x in numbers if is_even(x)]
    return jsonify({"result": filtered})


@app.route("/b1e", methods=["POST"])
def filter_and_sum_b1e():
    numbers = list(dict(request.get_json())["value"])

    def filter_algorithm(lst):
        return [x for x in lst if x % 2 == 0]

    def add(a, b):
        return a + b

    def sum_algorithm(lst):
        return reduce(add, numbers)

    filtered = filter_algorithm(numbers)
    summed = sum_algorithm(filtered)
    return jsonify({"result": summed})


@app.route("/b2g", methods=["POST"])
def dynamic_operations_b2g():
    operation = dict(request.get_json())["operation"]
    values = list(dict(request.get_json())["values"])

    def add(a, b):
        return a + b

    def subtract(a, b):
        return a - b

    operations = {"add": add,
                  "sub": subtract}

    result = operations[operation](values[0], values[1])

    return jsonify({"result": result})


@app.route("/b2e", methods=["POST"])
def multiplier_b2e():
    value = dict(request.get_json())["value"]

    def create_multiplier(multiplier):
        def mult(x):
            return multiplier * x

        return mult

    multiply_by_three = create_multiplier(3)
    result = multiply_by_three(value)

    return jsonify({"result": result})


if __name__ == "__main__":
    app.run(debug=True)
