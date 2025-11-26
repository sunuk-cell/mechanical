from pyngrok import ngrok
import subprocess
import time

# Streamlit 앱 코드 작성
app_code = """
import streamlit as st

st.title("⚙️ 역학 계산기 (속도 → 가속도 → 힘)")

st.markdown(\"\"\"이 웹 앱은 질량, 이동 거리, 시간, 초기/최종 속도를 입력하면
속도, 가속도, 힘을 자동으로 계산합니다.\"\"\")

mass = st.number_input("질량 m (kg)", min_value=0.0)
distance = st.number_input("이동 거리 d (m)", min_value=0.0)
time_input = st.number_input("시간 t (s)", min_value=0.0)
v_initial = st.number_input("초기 속도 v₀ (m/s)")
v_final = st.number_input("최종 속도 v (m/s)")

if st.button("계산"):
    if time_input == 0:
        st.error("시간은 0이 될 수 없습니다!")
    else:
        velocity = distance / time_input
        st.success(f"속도 v = {velocity:.4f} m/s")
        acceleration = (v_final - v_initial) / time_input
        st.success(f"가속도 a = {acceleration:.4f} m/s²")
        force = mass * acceleration
        st.success(f"힘 F = {force:.4f} N")
"""

# 파일로 저장
with open("mechanics_calc.py", "w") as f:
    f.write(app_code)

# Streamlit 실행
process = subprocess.Popen(["streamlit", "run", "mechanics_calc.py"])

# 잠시 대기 후 ngrok 링크 생성
time.sleep(5)
public_url = ngrok.connect(8501)
print("🌐 웹 앱 열기 →", public_url)


