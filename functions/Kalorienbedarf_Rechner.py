from datetime import datetime
import pytz
import pandas as pd
import streamlit as st

def calculate_calorie_needs(gender, age, weight, height, activity):
    # Grundumsatz (BMR) nach Mifflin-St. Jeor
    if gender == "Männlich":
        bmr = 10 * weight + 6.25 * height - 5 * age + 5  
    else:
        bmr = 10 * weight + 6.25 * height - 5 * age - 161      

    return {
        "timestamp": datetime.now(pytz.timezone('Europe/Zurich')),  # Current swiss time
        "age": age,
        "gender": gender,
        "weight": weight,
        "height": height,
        "activity": activity,
    } 