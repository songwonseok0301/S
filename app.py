import streamlit as st
from PIL import Image
import requests
from io import BytesIO

# 이미지 로드 함수
def load_image(url):
    try:
        response = requests.get(url)
        return Image.open(BytesIO(response.content))
    except:
        return None

if "자기소개" == "자기소개":  # 테스트용 조건문
    st.set_page_config(page_title="자기소개서", layout="wide")

    # 전체 페이지 스타일 추가
    st.markdown("""
        <style>
            body {
                background-color: #2b2b2b;
            }
            .custom-container {
                background-color: #3a3a3a;
                padding: 40px;
                border-radius: 15px;
                box-shadow: 0 4px 10px rgba(0, 0, 0, 0.4);
                color: white;
            }
            .title {
                text-align: center;
                font-size: 48px;
                color: #ffcc00;
                font-weight: bold;
                margin-bottom: 10px;
            }
            .subtitle {
                text-align: center;
                font-size: 36px;
                color: white;
                margin-bottom: 20px;
            }
            .highlight {
                color: #f5af19;
                font-size: 20px;
                text-align: center;
            }
            .icon-bar {
                text-align: center;
                margin-top: 20px;
            }
            .icon-bar i {
                font-size: 26px;
                margin: 0 15px;
                color: #ffcc00;
            }
        </style>
        <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" rel="stylesheet">
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 3, 1])
    
    with col2:
        st.markdown('<div class="custom-container">', unsafe_allow_html=True)

        # 상단 아이콘 및 텍스트
        st.markdown('<h2 style="text-align:center;color:#ffcc00;font-size:40px;font-weight:bold;">송원석</h2>', unsafe_allow_html=True)

        # 이미지 출력
        firefighter_img = load_image("https://www.fpn119.co.kr/imgdata/fpn119_co_kr/202404/2024042536138624.jpg")
        if firefighter_img:
            st.image(firefighter_img, use_column_width=True)

        # 학과와 문구
        st.markdown("""
            <h3 style="text-align:center;margin-top:30px;">건양대학교 재난안전소방학과</h3>
            <p class="highlight">미래의 소방관을 향한 여정</p>
        """, unsafe_allow_html=True)

        # 하단 아이콘
        st.markdown("""
            <div class="icon-bar">
                <i class="fas fa-helmet-safety"></i>
                <i class="fas fa-truck"></i>
                <i class="fas fa-fire-extinguisher"></i>
            </div>
        </div>
        """, unsafe_allow_html=True)

# 메뉴바 생성
menu = ["자기소개", "개인 및 학과 소개", "진로 목표: 소방관", "현장 안전관리자 경험", "미래 계획"]
choice = st.sidebar.radio("목차", menu)

# 페이지 1: 자기소개
if choice == "자기소개":
    # 배경을 위한 컨테이너
    with st.container():
        col1, col2, col3 = st.columns([1, 3, 1])
        
        with col2:
            st.markdown('<div class="fire-gradient">', unsafe_allow_html=True)
            
            # 아이콘과 제목
            st.markdown('<div style="text-align:center;"><i class="fas fa-fire" style="font-size:50px;color:#f5af19;"></i></div>', unsafe_allow_html=True)
            st.markdown('<h1 style="text-align:center;color:white;font-size:48px;margin-top:20px;font-weight:bold;">자기소개서</h1>', unsafe_allow_html=True)
            st.markdown('<div class="center-divider"></div>', unsafe_allow_html=True)
            st.markdown('<h2 style="text-align:center;color:white;font-size:40px;font-weight:bold;">송원석</h2>', unsafe_allow_html=True)

            # 이미지 삽입 (생성된 이미지 사용)
            st.image("song.png.png", use_column_width=True, caption="나의 모습")
            
            # 하단 텍스트
            st.markdown('<h3 style="text-align:center;color:white;font-size:28px;margin-top:20px;">건양대학교 재난안전소방학과</h3>', unsafe_allow_html=True)
            st.markdown('<p style="text-align:center;color:#f5af19;font-size:18px;">미래의 소방관을 향한 여정</p>', unsafe_allow_html=True)
            
            # 하단 아이콘들
            st.markdown('''
            <div style="text-align:center;margin-top:20px;">
                <i class="fas fa-helmet-safety" style="font-size:24px;color:#f5af19;margin:0 15px;"></i>
                <i class="fas fa-truck-fire" style="font-size:24px;color:#f5af19;margin:0 15px;"></i>
                <i class="fas fa-house-fire" style="font-size:24px;color:#f5af19;margin:0 15px;"></i>
            </div>
            ''', unsafe_allow_html=True)
            
            st.markdown('</div>', unsafe_allow_html=True)

# 페이지 2: 개인 및 학과 소개
elif choice == "개인 및 학과 소개":
    # 배경을 위한 컨테이너
    with st.container():
        st.markdown('<div class="fire-gradient"><div class="dark-overlay">', unsafe_allow_html=True)
        
        # 제목
        st.markdown('<h1 class="white-text" style="font-size:40px;font-weight:bold;">개인 소개 및 학과 소개</h1>', unsafe_allow_html=True)
        st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
        
        # 두 컬럼으로 나누기
        col1, col2 = st.columns(2)
        
        with col1:
            # 개인 소개 섹션
            st.markdown('<div class="card">', unsafe_allow_html=True)
            st.markdown('<h2 style="font-size:24px;font-weight:bold;"><span class="icon">👤</span>개인 소개</h2>', unsafe_allow_html=True)
            
            profile_col1, profile_col2 = st.columns([1, 2])
            
            with profile_col1:
                profile_img = load_image("https://png.pngtree.com/png-vector/20210912/ourlarge/pngtree-professional-firefighter-png-image_3908279.jpg")
                if profile_img:
                    st.image(profile_img, use_column_width=True)
            
            with profile_col2:
                st.markdown('''
                <ul style="list-style-type:none;padding-left:0;">
                    <li style="margin-bottom:8px;"><span style="color:#f12711;font-weight:bold;display:inline-block;width:80px;">이름:</span> 송원석</li>
                    <li style="margin-bottom:8px;"><span style="color:#f12711;font-weight:bold;display:inline-block;width:80px;">소속:</span> 건양대학교</li>
                    <li style="margin-bottom:8px;"><span style="color:#f12711;font-weight:bold;display:inline-block;width:80px;">학과:</span> 재난안전소방학과</li>
                    <li style="margin-bottom:8px;"><span style="color:#f12711;font-weight:bold;display:inline-block;width:80px;">비전:</span> 전문 소방관</li>
                    <li style="margin-bottom:8px;"><span style="color:#f12711;font-weight:bold;display:inline-block;width:80px;">경험:</span> 현장 안전관리자 업무</li>
                </ul>
                ''', unsafe_allow_html=True)
            
            st.markdown('</div>', unsafe_allow_html=True)
            
            # 인용구 섹션
            st.markdown('''
            <div class="card" style="background-color:#f8f9fa;">
                <div style="display:flex;align-items:center;font-size:18px;">
                    <span style="color:#f12711;margin-right:5px;">❝</span>
                    <p style="font-style:italic;">"안전을 책임지는 전문 소방관이 되는 것이 저의 꿈입니다."</p>
                    <span style="color:#f12711;margin-left:5px;">❞</span>
                </div>
            </div>
            ''', unsafe_allow_html=True)
        
        with col2:
            # 학과 소개 섹션
            st.markdown('<div class="card">', unsafe_allow_html=True)
            st.markdown('<h2 style="font-size:24px;font-weight:bold;"><span class="icon">🎓</span>학과 소개</h2>', unsafe_allow_html=True)
            
            st.markdown('''
            <div style="display:flex;align-items:flex-start;margin-top:15px;">
                <span style="color:#f12711;margin-right:10px;font-size:18px;">🧯</span>
                <div>
                    <h3 style="font-weight:bold;font-size:18px;color:#991b1b;">재난안전소방학과란?</h3>
                    <p>화재, 재난, 재해 등의 상황에서 국민의 생명과 재산을 보호하고 안전을 책임질 전문 인재를 양성하는 학과입니다.</p>
                </div>
            </div>
            
            <div style="display:flex;align-items:flex-start;margin-top:15px;">
                <span style="color:#f12711;margin-right:10px;font-size:18px;">📚</span>
                <div>
                    <h3 style="font-weight:bold;font-size:18px;color:#991b1b;">핵심 교육 분야</h3>
                    <ul style="padding-left:20px;">
                        <li>화재 진압 및 예방 기술</li>
                        <li>응급 구조 및 구급 활동</li>
                        <li>재난 안전 관리 시스템</li>
                        <li>위기 상황 대응 전략</li>
                    </ul>
                </div>
            </div>
            
            <div style="display:flex;align-items:flex-start;margin-top:15px;">
                <span style="color:#f12711;margin-right:10px;font-size:18px;">💼</span>
                <div>
                    <h3 style="font-weight:bold;font-size:18px;color:#991b1b;">졸업 후 진로</h3>
                    <ul style="padding-left:20px;">
                        <li>소방공무원</li>
                        <li>소방안전 관리자</li>
                        <li>재난안전 전문가</li>
                        <li>소방시설 관리 전문가</li>
                    </ul>
                </div>
            </div>
            ''', unsafe_allow_html=True)
            
            st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown('</div></div>', unsafe_allow_html=True)

# 페이지 3: 진로 목표: 소방관
elif choice == "진로 목표: 소방관":
    # 배경을 위한 컨테이너
    with st.container():
        st.markdown('<div class="fire-gradient"><div class="dark-overlay">', unsafe_allow_html=True)
        
        # 제목
        st.markdown('<h1 class="white-text" style="font-size:40px;font-weight:bold;">진로 목표: 소방관</h1>', unsafe_allow_html=True)
        st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
        
        # 두 컬럼으로 나누기
        col1, col2 = st.columns([2, 3])
        
        with col1:
            # 이미지
            st.markdown('<div style="background-color:white;padding:8px;border-radius:10px;">', unsafe_allow_html=True)
            firefighter_img = load_image("https://www.fpn119.co.kr/imgdata/fpn119_co_kr/202404/2024042536138624.jpg")
            if firefighter_img:
                st.image(firefighter_img, use_column_width=True)
            st.markdown('</div>', unsafe_allow_html=True)
            
            # 소방관이 된 미래의 모습
            st.markdown('<div class="card" style="margin-top:20px;">', unsafe_allow_html=True)
            st.markdown('<h2 style="font-size:22px;font-weight:bold;"><span class="icon">🔥</span>소방관이 된 미래의 모습</h2>', unsafe_allow_html=True)
            
            st.markdown('''
            <div style="margin-top:15px;">
                <div style="display:flex;align-items:center;margin-bottom:10px;">
                    <span style="color:#e53e3e;margin-right:10px;">🛡️</span>
                    <p>국민의 생명과 안전을 수호하는 전문가</p>
                </div>
                <div style="display:flex;align-items:center;margin-bottom:10px;">
                    <span style="color:#e53e3e;margin-right:10px;">👥</span>
                    <p>팀워크를 통한 위기 대응 능력 발휘</p>
                </div>
                <div style="display:flex;align-items:center;margin-bottom:10px;">
                    <span style="color:#e53e3e;margin-right:10px;">🎓</span>
                    <p>지속적인 학습과 전문성 향상</p>
                </div>
                <div style="display:flex;align-items:center;margin-bottom:10px;">
                    <span style="color:#e53e3e;margin-right:10px;">🏅</span>
                    <p>재난 대응 분야의 리더로 성장</p>
                </div>
            </div>
            ''', unsafe_allow_html=True)
            
            st.markdown('</div>', unsafe_allow_html=True)
        
        with col2:
            # 소방관을 꿈꾸게 된 계기
            st.markdown('<div class="card">', unsafe_allow_html=True)
            st.markdown('<h2 style="font-size:22px;font-weight:bold;"><span class="icon">❤️</span>소방관을 꿈꾸게 된 계기</h2>', unsafe_allow_html=True)
            
            st.markdown('''
            <div style="margin-top:15px;">
                <p style="margin-bottom:10px;"><span style="color:#f12711;font-weight:bold;">현장 안전관리자 경험:</span> 현장에서 안전관리자로 일하며 느낀 책임감과 보람이 소방관이라는 꿈을 확고히 했습니다.</p>
                <p style="margin-bottom:10px;"><span style="color:#f12711;font-weight:bold;">사명감:</span> 위기 상황에서 국민의 생명과 재산을 보호하는 소방관의 사명에 깊은 감명을 받았습니다.</p>
                <p style="margin-bottom:10px;"><span style="color:#f12711;font-weight:bold;">전문성:</span> 재난안전소방학과에서 배운 이론적 지식을 실제 현장에서 적용하고 싶은 열망이 있습니다.</p>
            </div>
            ''', unsafe_allow_html=True)
            
            st.markdown('</div>', unsafe_allow_html=True)
            
            # 소방관에 필요한 역량과 준비 과정
            st.markdown('<div class="card" style="margin-top:20px;">', unsafe_allow_html=True)
            st.markdown('<h2 style="font-size:22px;font-weight:bold;"><span class="icon">📋</span>소방관에 필요한 역량과 준비 과정</h2>', unsafe_allow_html=True)
            
            # 역량과 준비과정을 2개 컬럼으로 나누기
            skills_col1, skills_col2 = st.columns(2)
            
            with skills_col1:
                st.markdown('<h3 style="font-size:18px;font-weight:bold;color:#b91c1c;margin-top:15px;">핵심 역량</h3>', unsafe_allow_html=True)
                
                # 체력
                st.markdown('<div style="display:flex;justify-content:space-between;margin-top:10px;"><span>체력</span><span>85%</span></div>', unsafe_allow_html=True)
                st.markdown('<div class="progress-container"><div class="progress-bar" style="width:85%;"></div></div>', unsafe_allow_html=True)
                
                # 전문 지식
                st.markdown('<div style="display:flex;justify-content:space-between;margin-top:10px;"><span>전문 지식</span><span>90%</span></div>', unsafe_allow_html=True)
                st.markdown('<div class="progress-container"><div class="progress-bar" style="width:90%;"></div></div>', unsafe_allow_html=True)
                
                # 위기 대응력
                st.markdown('<div style="display:flex;justify-content:space-between;margin-top:10px;"><span>위기 대응력</span><span>80%</span></div>', unsafe_allow_html=True)
                st.markdown('<div class="progress-container"><div class="progress-bar" style="width:80%;"></div></div>', unsafe_allow_html=True)
                
                # 팀워크
                st.markdown('<div style="display:flex;justify-content:space-between;margin-top:10px;"><span>팀워크</span><span>95%</span></div>', unsafe_allow_html=True)
                st.markdown('<div class="progress-container"><div class="progress-bar" style="width:95%;"></div></div>', unsafe_allow_html=True)
            
            with skills_col2:
                st.markdown('<h3 style="font-size:18px;font-weight:bold;color:#b91c1c;margin-top:15px;">준비 과정</h3>', unsafe_allow_html=True)
                
                st.markdown('''
                <ul style="list-style-type:none;padding-left:0;margin-top:10px;">
                    <li style="display:flex;align-items:flex-start;margin-bottom:8px;">
                        <span style="color:#15803d;margin-right:8px;">✅</span>
                        <span>소방공무원 시험 대비 체력 훈련</span>
                    </li>
                    <li style="display:flex;align-items:flex-start;margin-bottom:8px;">
                        <span style="color:#15803d;margin-right:8px;">✅</span>
                        <span>소방 관련 자격증 취득 준비</span>
                    </li>
                    <li style="display:flex;align-items:flex-start;margin-bottom:8px;">
                        <span style="color:#15803d;margin-right:8px;">✅</span>
                        <span>재난안전 관련 실습 및 현장 경험</span>
                    </li>
                    <li style="display:flex;align-items:flex-start;margin-bottom:8px;">
                        <span style="color:#15803d;margin-right:8px;">✅</span>
                        <span>응급구조 관련 지식 학습</span>
                    </li>
                    <li style="display:flex;align-items:flex-start;margin-bottom:8px;">
                        <span style="color:#2563eb;margin-right:8px;">🔄</span>
                        <span>소방학개론 심화 학습</span>
                    </li>
                </ul>
                ''', unsafe_allow_html=True)
            
            st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown('</div></div>', unsafe_allow_html=True)

# 페이지 4: 현장 안전관리자 경험
elif choice == "현장 안전관리자 경험":
    # 배경을 위한 컨테이너
    with st.container():
        st.markdown('<div class="fire-gradient"><div class="dark-overlay">', unsafe_allow_html=True)
        
        # 제목
        st.markdown('<h1 class="white-text" style="font-size:40px;font-weight:bold;">현장 안전관리자 경험</h1>', unsafe_allow_html=True)
        st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
        
        # 두 컬럼으로 나누기
        col1, col2 = st.columns(2)
        
        with col1:
            # 안전관리자 업무 경험
            st.markdown('<div class="card">', unsafe_allow_html=True)
            st.markdown('<h2 style="font-size:22px;font-weight:bold;"><span class="icon">⛑️</span>안전관리자 업무 경험</h2>', unsafe_allow_html=True)
            
            st.markdown('''
            <div style="margin-top:15px;">
                <div style="display:flex;align-items:flex-start;margin-bottom:10px;">
                    <span style="color:#e53e3e;margin-right:10px;font-size:16px;">📅</span>
                    <p><span style="font-weight:bold;">활동 기간:</span> 현장 안전관리자로서 실무 경험 축적</p>
                </div>
                <div style="display:flex;align-items:flex-start;margin-bottom:10px;">
                    <span style="color:#e53e3e;margin-right:10px;font-size:16px;">📋</span>
                    <p><span style="font-weight:bold;">주요 업무:</span> 현장 안전 점검, 위험 요소 식별, 안전 교육 실시, 비상 상황 대응 계획 수립</p>
                </div>
                <div style="display:flex;align-items:flex-start;margin-bottom:10px;">
                    <span style="color:#e53e3e;margin-right:10px;font-size:16px;">🏢</span>
                    <p><span style="font-weight:bold;">근무 환경:</span> 다양한 위험요소가 존재하는 현장에서 안전 관리 업무 수행</p>
                </div>
            </div>
            ''', unsafe_allow_html=True)
            
            st.markdown('</div>', unsafe_allow_html=True)
            
            # 배운 점과 깨달음
            st.markdown('<div class="card" style="margin-top:20px;">', unsafe_allow_html=True)
            st.markdown('<h2 style="font-size:22px;font-weight:bold;"><span class="icon">💡</span>배운 점과 깨달음</h2>', unsafe_allow_html=True)
            
            st.markdown('''
            <div style="margin-top:15px;">
                <div style="display:flex;align-items:flex-start;margin-bottom:10px;">
                    <span style="color:#15803d;margin-right:10px;">✅</span>
                    <p>"안전은 타협할 수 없는 최우선 가치임을 체득했습니다."</p>
                </div>
                <div style="display:flex;align-items:flex-start;margin-bottom:10px;">
                    <span style="color:#15803d;margin-right:10px;">✅</span>
                    <p>"위험 상황을 사전에 예측하고 대비하는 능력이 향상되었습니다."</p>
                </div>
                <div style="display:flex;align-items:flex-start;margin-bottom:10px;">
                    <span style="color:#15803d;margin-right:10px;">✅</span>
                    <p>"다양한 안전 규정과 절차에 대한 실무 지식을 습득했습니다."</p>
                </div>
                <div style="display:flex;align-items:flex-start;margin-bottom:10px;">
                    <span style="color:#15803d;margin-right:10px;">✅</span>
                    <p>"팀원들과의 효과적인 의사소통이 안전 관리의 핵심임을 알게 되었습니다."</p>
                </div>
            </div>
            
            <div style="margin-top:20px;padding:15px;background-color:#fefce8;border:1px solid #fef08a;border-radius:10px;">
                <p style="font-size:18px;font-weight:600;color:#b91c1c;display:flex;align-items:center;">
                    <span style="margin-right:8px;">⭐</span>핵심 깨달음
                </p>
                <p style="font-style:italic;color:#4b5563;margin-top:8px;">"현장에서 안전관리자로 일하며 느낀 책임감과 보람이 소방관이라는 꿈을 더욱 확고하게 만들었습니다."</p>
            </div>
            ''', unsafe_allow_html=True)
            
            st.markdown('</div>', unsafe_allow_html=True)
        
        with col2:
            # 현장 사진과 성장한 역량
            st.markdown('<div class="card">', unsafe_allow_html=True)
            
            # 현장 사진
            safety_img = load_image("https://get.pxhere.com/photo/person-equipment-fire-profession-exercise-yellow-emergency-service-brand-use-held-respiratory-protection-fire-fighter-volunteer-firefighter-dresden-emergency-firefighter-firefighters-delete-heroes-forces-meissen-radebeul-delete-exercise-professional-fire-brigade-kameraden-respirators-carrier-breathing-air-compressed-air-respirator-scba-overprint-normal-pressure-1040589.jpg")
            if safety_img:
                st.image(safety_img, use_column_width=True)
            
            st.markdown('<h2 style="font-size:22px;font-weight:bold;margin-top:15px;"><span class="icon">📈</span>현장 경험을 통해 성장한 역량</h2>', unsafe_allow_html=True)
            

# 타이틀 영역


# 본문 내용
left_col, right_col = st.columns(2)

# 왼쪽: 진로 로드맵
with left_col:
    st.header("🚒 소방관 진로 로드맵")

    st.subheader("1단계: 학부 졸업 및 자격증 취득")
    st.write("- 재난안전소방학과 학업 과정 완료")
    st.markdown("**자격증:**")
    st.markdown("- 소방안전관리자\n- 응급처치사\n- 위험물안전관리자")

    st.subheader("2단계: 소방공무원 시험 준비")
    st.write("- 필기시험 집중 학습 및 체력 훈련")
    st.write("- 체력 항목: 1,500m 달리기, 팔굽혀펴기, 윗몸일으키기")

    st.subheader("3단계: 소방공무원 합격 및 임용")
    st.write("- 공채 시험 합격 후 소방학교 입교 및 기본 교육 이수")

    st.subheader("4단계: 전문 소방관으로 성장")
    st.write("- 구조, 구급, 화재진압 등 분야별 전문성 강화")
    st.write("- 특수구조단, 소방항공대 등 전문 부서 진출 목표")

# 오른쪽: 역량 및 비전
with right_col:
    st.header("🛠 개발할 역량 및 준비사항")

    st.markdown("### 📘 전문지식")
    st.write("- 소방학개론 심화 학습")
    st.write("- 화재 안전 관리 전문 지식")

    st.markdown("### 💪 체력 단련")
    st.write("- 근력 및 지구력 강화")
    st.write("- 체력시험 대비 훈련")

    st.markdown("### 🧾 자격증 취득")
    st.write("- 응급구조사 자격증")
    st.write("- 인명구조사 취득")

    st.markdown("### 💬 의사소통 능력")
    st.write("- 위기상황 커뮤니케이션")
    st.write("- 팀워크 및 리더십 역량")

    st.header("🎯 비전 및 목표")
    st.image("https://img.freepik.com/premium-vector/fire-fighter-firemen-professional-occupation-career-swearing-helmet-firefighting-extinguisher_1162612-2494.jpg", width=250)

    st.success('"국민의 안전을 책임지는 전문 소방관으로 성장하겠습니다"')
    st.write("재난안전소방학과에서 쌓은 지식과 경험을 바탕으로 국민의 생명과 재산을 보호하는 믿음직한 소방관이 되겠습니다.")

    if st.button("🔥 더 나은 미래를 향해"):
        st.balloons()