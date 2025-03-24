# AI 참조 설정 및 가이드

**마지막 업데이트**: 2024년 3월 24일

## 개요

이 문서는 AI 비서가 TechMaster 프로젝트에서 사용자 지원 시 참조해야 할 설정, 리소스 및 지침을 포함합니다. 세션 간 연속성을 유지하고 최적의 지원을 제공하기 위한 참조 문서입니다.

## 참조 자료

### 주요 도서 및 학습 자료

1. **Fluent Python (2022)** - Luciano Ramalho
   - 경로: `/Users/sangou/TechMaster/Resources/Books/Python/luciano-ramalho-fluent-python_-clear-concise-and-effective-programming-oreilly-media-2022.pdf`
   - 용도: 파이썬 고급 프로그래밍 개념, 파이썬 언어의 특징 및 관용적인 코드 작성 방법에 대한 참조
   - 주요 주제: 데이터 구조, 함수, 객체지향 프로그래밍, 컨트롤 흐름, 메타프로그래밍

2. **Jump to Python** - 박응용
   - 경로: `/Users/sangou/TechMaster/Resources/Books/Python/jump2python.pdf`
   - 용도: 파이썬 기초 학습 및 실습, 초보자를 위한 파이썬 입문서
   - 주요 주제: 파이썬 기본 문법, 자료형, 제어문, 함수, 클래스, 모듈, 예외 처리, 정규 표현식
   - 진행 상황: 2장까지 완료, 예제 및 솔루션 코드 구현 (/Users/sangou/TechMaster/Python/Basics/JumpToPython/)
   - 주요 실습 내용:
     - 1장: 파이썬 소개 및 설치
     - 2장: 숫자형, 문자열, 리스트, 튜플, 딕셔너리, 집합, 불, 변수 등 자료형
     - 다음 예정: 3장 제어문 (if, while, for)

3. **추가 자료**:
   - 향후 추가될 도서, 문서, 강의 자료 등을 여기에 기록

## 세션 관리

### 세션 시작 시 참조할 문서

1. `/Users/sangou/TechMaster/session_tracker.md` 
   - 프로젝트 진행 상황, 완료된 작업, 계획된 작업 등을 포함
   - 매 세션 시작 시 반드시 최신 상태 확인

2. `/Users/sangou/TechMaster/ai_reference_settings.md` (현재 문서)
   - 참조 자료 및 설정 정보

3. `/Users/sangou/TechMaster/docs/jump_to_python_progress.md`
   - Jump to Python 학습 진행 상황 및 예제 파일 관리
   - 각 장마다 완료된 예제와 솔루션 파일 목록

### 세션 종료 시 업데이트할 문서

1. `/Users/sangou/TechMaster/session_tracker.md`
   - 새로 완료된 작업 추가
   - 다음 계획 업데이트
   - 문제점 및 해결책 기록

2. `/Users/sangou/TechMaster/docs/jump_to_python_progress.md`
   - Jump to Python 관련 학습 진행 시 내용 업데이트

## 코딩 지원 가이드라인

### 파이썬 코딩 지원 시

1. **Jump to Python 참조**:
   - 기초 파이썬 학습 중일 때는 Jump to Python 책 내용을 기반으로 설명
   - 진행 중인 장과 예제에 맞는 코드 작성 지원
   - 예제와 솔루션 코드로 나누어 기본 개념과 응용 방법 모두 제공

2. **Fluent Python 참조**:
   - 사용자가 파이썬 코딩에 관련된 고급 질문을 할 때, Fluent Python 도서의 내용을 참조하여 현대적이고 관용적인 파이썬 코딩 방법 제안
   - 특히 파이썬의 고유한 특성(리스트 컴프리헨션, 제너레이터, 데코레이터, 특수 메서드 등)을 활용한 코드 작성 권장

3. **코드 품질**:
   - PEP 8 스타일 가이드를 준수하는 코드 작성
   - 명확하고 간결한 코드 우선
   - 적절한 주석과 문서화 포함

4. **학습 진행 방향**:
   - TechMaster/Python/Basics/JumpToPython/에서 시작하여 점진적으로 Advanced로 진행
   - 사용자의 현재 지식 수준에 맞는 설명 제공
   - 실제 예제와 실습 코드 제공

### 프로젝트 구조 관리

1. **디렉토리 구조**:
   - 관련 코드는 적절한 디렉토리에 저장
   - 새 프로젝트 시작 시 기존 구조 활용
   - Jump to Python 학습 코드는 /Python/Basics/JumpToPython/ 내에 챕터별로 구성

2. **파일 명명 규칙**:
   - 소문자와 언더스코어 사용 (snake_case)
   - 의미 있는 파일 이름 사용
   - 관련 파일들은 같은 디렉토리에 그룹화
   - 각 예제와 솔루션 파일은 [주제].py, [주제]_solution.py 형식으로 저장

## 참고 자료 관리

1. **새로운 참고 자료 추가 시**:
   - Resources/ 디렉토리의 적절한 하위 폴더에 저장
   - 이 문서에 참조 정보 추가
   - session_tracker.md에 자료 추가 내용 기록

2. **자료 참조 방법**:
   - 특정 주제에 관한 질문에 대응할 때 관련 자료 참조
   - 필요시 자료의 특정 부분 인용 (페이지 번호 또는 섹션 명시)

## 버전 관리 및 백업

1. **Git을 통한 버전 관리**:
   - 모든 코드 변경사항은 Git을 통해 관리
   - 로컬 저장소: `/Users/sangou/TechMaster/`
   - GitHub 저장소: https://github.com/sangou/TechMaster
   - 주요 커밋 및 푸시 시점: 
     - 각 장의 예제 및 솔루션 파일 완성 시
     - 중요한 학습 문서 업데이트 시

2. **GitHub 저장소 관리**:
   - 지침 문서: `/Users/sangou/TechMaster/github_instructions.md`

## 사용자 기본 정보

- **주 프로그래밍 언어**: Python
- **학습 목표**: 파이썬 프로그래밍 기술 향상, 코딩 테스트 준비, 데이터 사이언스 및 AI 학습
- **프로젝트 환경**: macOS Ventura, 터미널, VS Code, Jupyter Notebook

## 추가 지침

1. **사용자 선호도**:
   - 실용적이고 구체적인 예제 선호
   - 단계별 설명 선호
   - 코드에 대한 간결한 설명 선호

2. **세션 연속성**:
   - 매번 새로운 세션을 시작할 때 이전 대화 내용 참조
   - 진행 중인 프로젝트가 있다면 해당 컨텍스트 유지

---

*이 설정 문서는 AI와의 협업을 더 효과적으로 만들기 위해 작성되었으며, 필요에 따라 업데이트됩니다.*