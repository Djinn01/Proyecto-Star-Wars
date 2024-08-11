from people import People
from planet import Planet
from film import Film
import csv
import os
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

csv_people = pd.read_csv("starwars (1)/csv/characters.csv")
homeworld_people = csv_people["homeworld"].value_counts()

plt.figure(figsize=(12, 8))
homeworld_people.plot(kind='bar', color= "red")
plt.title('People Born on Each Planet')
plt.xlabel('Planet')
plt.ylabel('People')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()