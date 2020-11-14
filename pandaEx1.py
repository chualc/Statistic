import pandas as pd
import numpy as np

arrays = [np.array(['cat 1', 'cat 1', 'cat 2', 'cat 2', 'cat 3', 'cat 3', 'cat 4', 'cat 4']), np.array(['groupA', 'groupB', 'groupA', 'groupB', 'groupA', 'groupB', 'groupA', 'groupB'])]

data = pd.DataFrame(np.random.randn(8,3), index=arrays)

print(data)

