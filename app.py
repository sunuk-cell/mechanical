# ===============================================
#  코랩용 자동 Streamlit 실행 스크립트
# ===============================================

# 1️⃣ 필요한 패키지 설치
!pip install streamlit pyngrok -q

# 2️⃣ Streamlit 앱 파일 생성
with open("mechanics_calc.py", "w") as f:
    f.write("""
import streamlit as st

st.title("⚙️ 역학 계산기 (속도 → 가속도 → 힘)")

st.markdown(\"\"\"이 웹 앱은 질량, 이동 거리, 시간, 초기/최종 속도를 입력하면
속도, 가속도, 힘을 자동으로 계산합니다.\"\"\")

mass = st.number_input("질량 m (kg)", min_value=0.0)
distance = st.number_input("이동 거리 d (m)", min_value=0.0)
time = st.number_input("시간 t (s)", min_value=0.0)
v_initial = st.number_input("초기 속도 v₀ (m/s)")
v_final = st.number_input("최종 속도 v (m/s)")

if st.button("계산"):
    if time == 0:
        st.error("시간은 0이 될 수 없습니다!")
    else:
        velocity = distance / time
        st.success(f"속도 v = {velocity:.4f} m/s")
        acceleration = (v_final - v_initial) / time
        st.success(f"가속도 a = {acceleration:.4f} m/s²")
        force = mass * acceleration
        st.success(f"힘 F = {force:.4f} N")
""")

# 3️⃣ ngrok을 통해 웹에서 접속 가능하게 실행
from pyngrok import ngrok

# Streamlit 앱 실행
import subprocess
import time

# 8501 포트로 Streamlit 실행
cmd = ["streamlit", "run", "mechanics_calc.py"]
process = subprocess.Popen(cmd)

# 잠시 대기 후 ngrok으로 포트 연결
time.sleep(3)
public_url = ngrok.connect(8501)
print("웹 앱 열기 →", public_url)
