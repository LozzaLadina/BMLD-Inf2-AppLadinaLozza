import streamlit as st

st.title("Kalorienbedarf Rechner")

st.write("Ihr Rechner für den täglichen Kalorienbedarf.")

with st.form(key="calorie_form"):
    age = st.number_input("Alter (Jahre)", min_value=0, max_value=120, value=25)
    gender = st.selectbox("Geschlecht", ["Männlich", "Weiblich"])
    weight = st.number_input("Gewicht (kg)", min_value=0.0, format="%.1f")
    height = st.number_input("Grösse (cm)", min_value=0.0, format="%.1f")
    activity = st.selectbox(
        "Aktivitätslevel",
        [
            "Sitzend (wenig oder keine Bewegung)",
            "Leicht aktiv (leichte Bewegung/Sport 1-3 Tage/Woche)",
            "Mäßig aktiv (mäßige Bewegung/Sport 3-5 Tage/Woche)",
            "Sehr aktiv (harte Bewegung/Sport 6-7 Tage/Woche)",
            "Extrem aktiv (sehr harte tägliche Bewegung oder körperliche Arbeit)"
        ],
    )
    submit = st.form_submit_button("Berechnen")

# Berechnung
if submit:
    # Grundumsatz (BMR) nach Mifflin-St. Jeor
    if gender == "Männlich":
        bmr = 10 * weight + 6.25 * height - 5 * age + 5
    else:
        bmr = 10 * weight + 6.25 * height - 5 * age - 161

    # Aktivitätsfaktoren
    factors = {
        "Sitzend (wenig oder keine Bewegung)": 1.2,
        "Leicht aktiv (leichte Bewegung/Sport 1-3 Tage/Woche)": 1.375,
        "Mäßig aktiv (mäßige Bewegung/Sport 3-5 Tage/Woche)": 1.55,
        "Sehr aktiv (harte Bewegung/Sport 6-7 Tage/Woche)": 1.725,
        "Extrem aktiv (sehr harte tägliche Bewegung oder körperliche Arbeit)": 1.9,
    }
    maintenance_calories = bmr * factors.get(activity, 1.2)

    st.write(f"Ihr Grundumsatz (BMR) beträgt **{bmr:.0f} kcal/Tag**.")
    st.write(
        f"Um Ihr aktuelles Gewicht zu halten, benötigen Sie ungefähr **{maintenance_calories:.0f} kcal/Tag**."
    )