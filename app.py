import requests
import streamlit as st

# Function to fetch weather data
def get_weather_data(place, api_key):
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {"q": place, "appid": api_key, "units": "metric"}
    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        data = response.json()
        return {
            "Weather": data["weather"][0]["main"],
            "Description": data["weather"][0]["description"].capitalize(),
            "Temperature": f"{data['main']['temp']}°C",
            "Feels Like": f"{data['main']['feels_like']}°C",
            "Humidity": f"{data['main']['humidity']}%",
            "Wind Speed": f"{data['wind']['speed']} m/s",
            "Icon": f"http://openweathermap.org/img/wn/{data['weather'][0]['icon']}@2x.png"
        }
    except:
        return {"Error": "Could not retrieve weather data. Check the place name or try again."}

# Streamlit app
def main():
    st.set_page_config(page_title="Weather App", page_icon="🌤️", layout="centered")

    # Custom CSS for advanced UI/UX
    st.markdown(
        """
        <style>
        [data-testid="stAppViewContainer"] {
            background: linear-gradient(to bottom right, #6dd5fa, #2980b9);
            background-size: cover;
            font-family: 'Arial', sans-serif;
            color: #fff;
            height: 100vh;
        }
        [data-testid="stHeader"] {
            background: rgba(0, 0, 0, 0);
        }
        [data-testid="stToolbar"] {
            visibility: hidden;
        }
        [data-baseweb="input"] {
            background-color: rgba(255, 255, 255, 0.9) !important;
            border-radius: 12px !important;
            padding: 12px !important;
            box-shadow: 0 2px 6px rgba(0, 0, 0, 0.1) !important;
            border: none !important;
            color: black !important;
            font-size: 1rem !important;
        }
        [data-baseweb="input"]::placeholder {
            color: grey !important;
            font-style: italic !important;
        }
        .center-button {
            display: flex;
            justify-content: center;
            margin-top: 20px;
        }
        .stButton > button {
            background: linear-gradient(to right, #4facfe, #00f2fe);
            color: white;
            font-weight: bold;
            font-size: 1rem;
            padding: 10px 30px;
            border-radius: 12px;
            border: none;
            cursor: pointer;
            transition: all 0.3s ease-in-out;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.2);
        }
        .stButton > button:hover {
            background: linear-gradient(to right, #1d976c, #93f9b9);
            transform: translateY(-2px);
            box-shadow: 0 6px 12px rgba(0, 0, 0, 0.3);
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    # Title and subtitle with styling
    st.markdown(
        """
        <div style="text-align: center; color: white;">
            <h1 style="font-size: 3rem; margin-bottom: 0;">🌤️ Weather Application</h1>
            <p style="font-size: 1.2rem; margin-top: 0;">Get real-time weather updates in your fingertips!</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Input field
    st.markdown("<h3 style='color: white;'>Enter a location:</h3>", unsafe_allow_html=True)
    place = st.text_input("", placeholder="e.g., Kolkata, Tokyo, Paris")

    # Centered button below the input
    button_container = st.markdown('<div class="center-button">', unsafe_allow_html=True)
    button_clicked = st.button("Get Weather")
    st.markdown('</div>', unsafe_allow_html=True)

    # Handle button click
    if button_clicked:
        if place:
            api_key = "f9b4fb0b3cc41917d8c304761544072c"  # Replace with your API key
            with st.spinner('Fetching weather data...'):
                result = get_weather_data(place, api_key)

            # Display results
            if "Error" in result:
                st.error(result["Error"])
            else:
                st.markdown(f"<hr style='border: 1px solid white;'>", unsafe_allow_html=True)
                st.markdown(f"<h2 style='color: white;'>Weather in {place.capitalize()}</h2>", unsafe_allow_html=True)
                
                # Weather Info with Black Text
                st.markdown(
                    f"""
                    <div style="background: rgba(255, 255, 255, 0.9); padding: 20px; border-radius: 12px; text-align: center; margin-top: 20px; color: black;">
                        <img src="{result['Icon']}" alt="Weather Icon" style="width: 80px; height: 80px;">
                        <h3 style="color: black;">{result['Weather']} - {result['Description']}</h3>
                        <p><strong>Temperature:</strong> {result['Temperature']}</p>
                        <p><strong>Feels Like:</strong> {result['Feels Like']}</p>
                        <p><strong>Humidity:</strong> {result['Humidity']}</p>
                        <p><strong>Wind Speed:</strong> {result['Wind Speed']}</p>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )
        else:
            st.warning("Please enter a valid place name.")

if __name__ == "__main__":
    main()
