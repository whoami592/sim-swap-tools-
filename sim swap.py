import numpy as np
import pandas as pd
from itertools import product
import time

class SimSweepingTool:
    def __init__(self, sim_function, param_ranges):
        """
        Initialize the simulation sweeping tool.
        
        Args:
            sim_function: A function that takes parameters as input and returns a result.
            param_ranges: Dictionary of parameter names and their ranges (e.g., {'x': [0, 1, 2], 'y': [0, 1]}).
        """
        self.sim_function = sim_function
        self.param_ranges = param_ranges
        self.results = []

    def run_sweep(self):
        """
        Run the parameter sweep and store results.
        """
        print("Starting parameter sweep...")
        start_time = time.time()

        # Generate all combinations of parameters
        param_names = list(self.param_ranges.keys())
        param_values = [self.param_ranges[name] for name in param_names]
        all_combinations = list(product(*param_values))

        # Execute simulation for each combination
        for combo in all_combinations:
            params = dict(zip(param_names, combo))
            result = self.sim_function(**params)
            self.results.append({**params, 'result': result})

        end_time = time.time()
        print(f"Sweep completed in {end_time - start_time:.2f} seconds.")
        print(f"Total simulations run: {len(self.results)}")

    def get_results(self):
        """
        Return results as a pandas DataFrame.
        """
        return pd.DataFrame(self.results)

    def display_results(self):
        """
        Display the results in a readable format.
        """
        df = self.get_results()
        print("\nSimulation Results:")
        print(df)

# Example simulation function (customize this for your needs)
def example_sim(x, y):
    """
    Example simulation: computes x^2 + y^2.
    
    Args:
        x: First parameter.
        y: Second parameter.
    Returns:
        Result of the simulation.
    """
    return x**2 + y**2

# Usage example
if __name__ == "__main__":
    # Define parameter ranges
    param_ranges = {
        'x': np.linspace(0, 2, 5),  # 5 values from 0 to 2
        'y': np.linspace(0, 1, 3)   # 3 values from 0 to 1
    }

    # Create and run the sweeping tool
    sweeper = SimSweepingTool(sim_function=example_sim, param_ranges=param_ranges)
    sweeper.run_sweep()
    sweeper.display_results()
print("Sim Sweeping Tool - Created by Mr. Sabaz Ali Khan")
