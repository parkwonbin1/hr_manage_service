# 인사관리 시스템 (HR Management System)

Django 기반의 간단한 인사관리 시스템입니다.

## 🚀 주요 기능

- **직원 추가**: 새로운 직원 정보를 입력하여 추가
- **직원 목록 조회**: 등록된 직원들을 목록으로 확인 (검색, 필터링, 페이지네이션 포함)
- **직원 상세 조회**: 개별 직원의 상세 정보 확인
- **직원 정보 수정**: 기존 직원 정보 편집
- **직원 삭제**: 직원 정보 삭제 (소프트 삭제)

## 🛠️ 기술 스택

- **Backend**: Django 4.2.7
- **Database**: SQLite
- **Frontend**: Bootstrap 5, HTML5, CSS3, JavaScript
- **Icons**: Font Awesome

## 📋 설치 및 실행

### 1. 프로젝트 클론
```bash
git clone <repository-url>
cd hr_management_system
```

### 2. 가상환경 생성 및 활성화
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
```

### 3. 의존성 설치
```bash
pip install -r requirements.txt
```

### 4. 데이터베이스 마이그레이션
```bash
python manage.py migrate
```

### 5. 슈퍼유저 생성
```bash
python manage.py createsuperuser
```

### 6. 서버 실행
```bash
python manage.py runserver
```

## 🌐 접속 정보

- **메인 페이지**: http://127.0.0.1:8000/
- **관리자 페이지**: http://127.0.0.1:8000/admin/

## 📊 데이터 모델

### Employee (직원)
- `name`: 이름 (CharField)
- `email`: 이메일 (EmailField, unique)
- `phone`: 전화번호 (CharField, optional)
- `department`: 부서 (ChoiceField)
- `position`: 직급 (ChoiceField)
- `hire_date`: 입사일 (DateField)
- `salary`: 급여 (DecimalField, optional)
- `is_active`: 재직 상태 (BooleanField)
- `created_at`: 생성일시 (DateTimeField)
- `updated_at`: 수정일시 (DateTimeField)

## 🎨 주요 특징

- **반응형 디자인**: 모바일 친화적 UI
- **한국어 지원**: 모든 텍스트가 한국어로 표시
- **검색 및 필터링**: 이름, 이메일, 전화번호 검색 및 부서별 필터링
- **페이지네이션**: 효율적인 데이터 표시
- **사용자 친화적**: 직관적인 네비게이션과 명확한 액션 버튼

## 📁 프로젝트 구조

```
hr_management_system/
├── hr_project/           # Django 프로젝트 설정
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── employees/            # 직원 관리 앱
│   ├── migrations/
│   ├── templates/
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
├── templates/            # 공통 템플릿
│   └── base.html
├── manage.py
├── requirements.txt
└── README.md
```

## 🔧 개발 환경

- Python 3.8+
- Django 4.2.7
- SQLite 3

## 📝 라이선스

이 프로젝트는 MIT 라이선스 하에 있습니다.
