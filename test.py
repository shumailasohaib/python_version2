import pandas
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
tips=sns.load_dataset("tip")
sns.lineplot(x="day", y="total_bill", data = tips)