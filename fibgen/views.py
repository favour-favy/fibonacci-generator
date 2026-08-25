from django.shortcuts import render

def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    sequence = [0, 1]
    while len(sequence) < n:
        sequence.append(sequence[-1] + sequence[-2])
    return sequence

def home(request):
    result = None
    error = None
    n_value = ""

    if request.method == "POST":
        n_value = request.POST.get("n", "")
        try:
            n = int(n_value)
            if n < 0:
                error = "Please enter a positive number."
            else:
                result = fibonacci(n)
        except ValueError:
            error = "Please enter a valid whole number."

    return render(request, "fibgen/home.html", {
        "result": result,
        "error": error,
        "n_value": n_value,
    })