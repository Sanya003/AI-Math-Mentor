def route_problem(parsed_problem):

    topic = parsed_problem.get("topic", "").lower()

    if "derivative" in topic:
        return "calculus"

    if "limit" in topic:
        return "limits"

    if "integral" in topic:
        return "integrals"

    if "matrix" in topic or "determinant" in topic:
        return "linear_algebra"

    return "general_math"