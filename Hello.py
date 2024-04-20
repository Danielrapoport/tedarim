import streamlit as st
import numpy as np

st.title("Tedarim Meditation")

def genWave(left:float, right:float, seconds=600):
    sample_rate = 44100  # 44100 samples per second
    # Generate array with seconds*sample_rate steps, ranging between 0 and seconds
    t = np.linspace(0, seconds, seconds * sample_rate, False)
    l,r = (left, right)
    note_l = np.sin(l * t * 2 * np.pi)
    note_r = np.sin(r * t * 2 * np.pi)
    st.audio(np.array([note_l, note_r]), sample_rate=sample_rate)
    

st.markdown("## Relax")
st.markdown("### 0.5hz - Strong")
genWave(55,55.5)
st.divider()
st.markdown("### 1hz - Strong")
genWave(55,56)
st.divider()
st.markdown("### 4hz")
genWave(55,59)
st.divider()
st.markdown("### 6hz")
genWave(55,61)
st.markdown("## Energy")
st.markdown("### 60hz")
genWave(216,276)
st.divider()
st.markdown("### 40hz - Best")
genWave(216,256)
st.divider()
st.markdown("### 32hz")
genWave(216,248)

with st.form("teder"):
    st.markdown("## Advanced Editor")
    left = st.number_input('Left Wave', min_value=0, max_value=1000, value=55)
    right = st.number_input('Right Wave', min_value=0, max_value=1000, value=56)
    seconds = st.number_input('Duration (seconds)', min_value=0, max_value=86440, value=600)
    if st.form_submit_button("Generate"):
        st.markdown("### {}hz".format(right - left))
        genWave(left, right, seconds)
