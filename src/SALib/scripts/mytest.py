

from SALib.sample import saltelli
from SALib.analyze import sobol
from SALib.test_functions import Ishigami
import numpy as np


    

def basic_sensitivities_test():
    # Define the model inputs
    problem = {
        'num_vars': 3,
        'names': ['x1', 'x2', 'x3'],
        'bounds': [[-3.14159265359, 3.14159265359],
                    [-3.14159265359, 3.14159265359],
                    [-3.14159265359, 3.14159265359]]
    }

    # Generate samples
    param_values = saltelli.sample(problem, 1024)

    # Run model (example)
    Y = Ishigami.evaluate(param_values)

    # Perform analysis
    Si = sobol.analyze(problem, Y, print_to_console=True)

    # Print the first-order sensitivity indices
    print(Si['S1'])
    
def advanced_sensitivities_test():
    problem = {
    'groups': ['Group_1', 'Group_2', 'Group_3'],
    'names': ['x1', 'x2', 'x3'],
    'num_vars': 3,
    'bounds': [[-3.14, 3.14], [-3.14, 3.14], [10, 20]]
}
    param_values = saltelli.sample(problem, 1024)
    # print(param_values, np.shape(param_values))
    
    Y = Ishigami.evaluate(param_values)
    
    # print(Y)
    
    Si = sobol.analyze(problem, Y, print_to_console=False)
    # print(type(Si))

    total_Si, first_Si, second_Si = Si.to_df()
    # print(Si.to_df())
    print(total_Si)
    print()
    print(first_Si)
    print()
    print(second_Si)
    print()
    # print(total_Si, first_Si, second_Si)
    exit()

def main():
    advanced_sensitivities_test()
    # basic_sensitivities_test()
    
if __name__ == '__main__':
    main()