# ===============================================
#        역학 계산기 - 속도/가속도
# ===============================================

def velocity_calc():
    print("\n[속도 계산 v = d / t]")
    d = float(input("이동 거리 d (m) 입력: "))
    t = float(input("시간 t (s) 입력: "))
    
    if t == 0:
        print("⚠️ 시간은 0이 될 수 없습니다!")
        return
    
    v = d / t
    print("계산 결과: 속도 v = {:.4f} m/s".format(v))


def acceleration_calc():
    print("\n[가속도 계산 a = Δv / t]")
    v_initial = float(input("초기 속도 v₀ (m/s) 입력: "))
    v_final = float(input("최종 속도 v (m/s) 입력: "))
    t = float(input("시간 t (s) 입력: "))
    
    if t == 0:
        print("⚠️ 시간은 0이 될 수 없습니다!")
        return
    
    a = (v_final - v_initial) / t
    print("계산 결과: 가속도 a = {:.4f} m/s²".format(a))


# ================== 메인 메뉴 ==================
while True:
    print("\n=====================================")
    print("         역학 계산기 (속도/가속도)")
    print("=====================================")
    print("1. 속도 계산 (v = d / t)")
    print("2. 가속도 계산 (a = Δv / t)")
    print("3. 종료")

    choice = input("메뉴 선택: ")

    if choice == "1":
        velocity_calc()
    elif choice == "2":
        acceleration_calc()
    elif choice == "3":
        print("프로그램을 종료합니다!")
        break
    else:
        print("잘못된 입력입니다.")
