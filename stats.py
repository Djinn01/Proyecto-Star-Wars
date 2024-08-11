from people import People
from planet import Planet
from film import Film
import csv
import os
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def homeworld_characters_comparison():
    csv_people = pd.read_csv("starwars (1)/csv/characters.csv")
    homeworld_people = csv_people["homeworld"].value_counts()

    plt.figure(figsize=(12, 8))
    homeworld_people.plot(kind='bar', color= "blue")
    plt.title('People Born on Each Planet')
    plt.xlabel('Planet')
    plt.ylabel('People')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()

def starships_characteristics():
    # Cargar los datos del csv
    starships_df = pd.read_csv('starwars (1)/csv/starships.csv')

    # Grafico Longitud
    plt.figure(figsize=(12, 8))
    starships_df.set_index('name')['length'].plot(kind='bar', color='blue')
    plt.title('Ship Lenght')
    plt.xlabel('Starship')
    plt.ylabel('Length')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()

    # Grafico cargo
    plt.figure(figsize=(12, 8))
    starships_df.set_index('name')['cargo_capacity'].plot(kind='bar', color='red')
    plt.title('Cargo Capacity Comparison')
    plt.xlabel('Starship')
    plt.ylabel('Cargo Capacity')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()

    # Grafico Hiperdrive
    plt.figure(figsize=(12, 8))
    starships_df.set_index('name')['hyperdrive_rating'].plot(kind='bar', color='salmon')
    plt.title('Hyperdrive Classification Comparison')
    plt.xlabel('Starship')
    plt.ylabel('Hyperdrive Rating')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()

    # Grafico MGLT
    plt.figure(figsize=(12, 8))
    starships_df.set_index('name')['MGLT'].plot(kind='bar', color='orange')
    plt.title('MGLT Comparison')
    plt.xlabel('Starship')
    plt.ylabel('MGLT')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()

