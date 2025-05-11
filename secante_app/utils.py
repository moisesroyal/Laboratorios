import numpy as np
import matplotlib.pyplot as plt
import io
import base64

def metodo_secante(funcion_str, x0, x1, tolerancia, max_iter):
    pasos = [x1]
    try:
        safe_dict = {
            "sin": np.sin,
            "cos": np.cos,
            "tan": np.tan,
            "exp": np.exp,
            "log": np.log,
            "sqrt": np.sqrt,
            "abs": np.abs,
            "pi": np.pi,
            "e": np.e
        }

        f = lambda x: eval(funcion_str, {"__builtins__": {}}, {**safe_dict, "x": x})

        for i in range(max_iter):
            fx0 = f(x0)
            fx1 = f(x1)
            if fx1 - fx0 == 0:
                break
            x2 = x1 - fx1 * ((x1 - x0) / (fx1 - fx0))
            pasos.append(x2)
            if abs(x2 - x1) < tolerancia:
                return x2, i + 1, pasos
            x0, x1 = x1, x2
        return x2, max_iter, pasos
    except Exception:
        return None, 0, []

def generar_grafica_convergencia(pasos):
    plt.figure()
    x_vals = list(range(1, len(pasos) + 1))
    plt.plot(x_vals, pasos, marker='o', linestyle='-')

    for i, (x, y) in enumerate(zip(x_vals, pasos), start=1):
        plt.annotate(f"{i}", (x, y), textcoords="offset points", xytext=(0, 5), ha='center', fontsize=8)

    plt.title("Convergencia del Método de la Secante")
    plt.xlabel("Iteración")
    plt.ylabel("x")
    plt.grid(True)

    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    grafica_base64 = base64.b64encode(buf.read()).decode('utf-8')
    buf.close()
    plt.close()

    return grafica_base64
