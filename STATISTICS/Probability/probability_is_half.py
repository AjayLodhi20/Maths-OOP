import numpy as np
import sympy as sp


def run_simulation_method():
    print("---Method 1: Monte Carlo Simulation---")
    n_val = 5
    total_sum = 2*n_val
    max_product = n_val ** 2
    target_threshold= (3/4) * max_product # 75% of max product

    num_trials = 1_000_000

    x_vals = np.random.uniform(0, total_sum, num_trials)
    y_vals = total_sum - x_vals

    #calculate products
    products = x_vals * y_vals

    favourable_cases = np.sum(products >= target_threshold)
    simulated_probability = favourable_cases / num_trials

    print(f"Chosen n value: {n_val} (Total range length = {total_sum}")
    print(f"Target product threshold: {target_threshold}")
    print(f"Favorable trials: {favourable_cases:,} out of {num_trials:,}")
    print(f"simulated probability: {simulated_probability:.4f}\n")

def run_analytical_method():
    print("---Method 2: Symbolic Algebraic solution---")
    n = sp.symbols('n', positive= True)
    x = sp.symbols('x', positive= True)

    #total range of x is from 0 to 2n
    total_range = 2*n

    #set up the product inequality: x*y >= (3/4) * n^2
    y = 2*n  -x
    product = x*y
    max_product = n**2
    condition = product >= (3/4) * max_product

    #this automatically finds the boundaries the book derived: n/2 to 3n/2
    #solve the inequality for x
    favorable_interval = sp.solve_univariate_inequality(condition, x, relational=False)
    favorable_range = favorable_interval.end - favorable_interval.start

    exact_probability = favorable_range / total_range

    print(f"Inequality being solved: {product} >= {3/4 * max_product}")
    print(f"successful range computed for x: {favorable_interval}")
    print(f"Length of successful range: {favorable_range}")
    print(f"Exact calculated probability: {exact_probability}")

if __name__ == "__main__":
    run_simulation_method()
    run_analytical_method()