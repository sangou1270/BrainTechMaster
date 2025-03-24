# Cursor와 MCP 설치 가이드

## Cursor 설치 가이드

### Cursor란?
Cursor는 AI 기능이 내장된 코드 에디터로, OpenAI의 GPT 모델을 활용하여 코드 작성, 버그 수정, 코드 이해 등을 도와주는 개발자용 도구입니다.

### 설치 방법

1. **공식 웹사이트 방문**
   - [Cursor 공식 웹사이트](https://cursor.sh/)에 접속합니다.

2. **다운로드**
   - 웹사이트에서 "Download" 버튼을 클릭하여 Mac용 설치 파일을 다운로드합니다.

3. **설치 파일 실행**
   - 다운로드된 `.dmg` 파일을 실행하고 Cursor 앱을 Applications 폴더로 드래그합니다.

4. **Cursor 실행**
   - Applications 폴더에서 Cursor를 실행합니다.

5. **로그인 및 설정**
   - 처음 실행 시 OpenAI API 키를 입력하거나 Cursor 계정으로 로그인합니다.
   - 기본 설정을 완료합니다.

### 주요 기능

- **AI 코드 완성**: 코드 작성 시 자동으로 다음 줄을 예측하고 완성해줍니다.
- **코드 설명**: 코드 블록을 선택하고 AI에게 설명을 요청할 수 있습니다.
- **버그 수정**: 코드의 오류를 AI가 감지하고 수정 방법을 제안합니다.
- **AI 챗**: 코드 관련 질문에 대한 답변을 AI에게 직접 물어볼 수 있습니다.

## MCP(Multi-Agent Collaboration Platform) 설치 가이드

### MCP란?
MCP는 AI 에이전트 간의 협업을 가능하게 하는 플랫폼으로, 지식 그래프를 통해 데이터를 조직화하고 AI 에이전트가 이를 활용할 수 있게 합니다.

### 설치 요구사항
- Node.js (v18 이상)
- npm 또는 yarn

### 설치 방법

1. **저장소 클론하기**
   ```bash
   git clone https://github.com/mcpai-quanta/mcp.git
   cd mcp
   ```

2. **의존성 설치**
   ```bash
   npm install
   # 또는
   yarn install
   ```

3. **환경 설정**
   - 프로젝트 루트에 `.env` 파일을 생성하고 다음과 같이 설정합니다:
   ```
   PORT=8080
   KNOWLEDGE_GRAPH_PATH=/Users/sangou/Library/Mobile Documents/com~apple~CloudDocs/obsidian/Brain
   ```

4. **서버 실행**
   ```bash
   node simple-server.js
   # 또는
   npm start
   ```

5. **브라우저에서 접속 확인**
   - 브라우저에서 `http://localhost:8080`에 접속하여 Knowledge Graph 시각화를 확인합니다.

### MCP와 Obsidian 연동하기

1. **Obsidian 볼트 설정**
   - Obsidian 볼트의 경로를 `.env` 파일의 `KNOWLEDGE_GRAPH_PATH`에 설정합니다.
   - 볼트 경로: `/Users/sangou/Library/Mobile Documents/com~apple~CloudDocs/obsidian/Brain`

2. **노드 생성**
   - Knowledge Graph API를 통해 Obsidian 노트에 해당하는 노드를 생성할 수 있습니다.
   ```bash
   curl -X POST http://localhost:8080/api/nodes -H "Content-Type: application/json" -d '{
     "name": "노드 이름",
     "type": "노드 타입",
     "content": "노드 내용"
   }'
   ```

3. **노드 간 관계 설정**
   - Knowledge Graph API를 통해 노드 간 관계를 설정할 수 있습니다.
   ```bash
   curl -X POST http://localhost:8080/api/edges -H "Content-Type: application/json" -d '{
     "from": "출발 노드 ID",
     "to": "도착 노드 ID",
     "relationship": "관계 유형"
   }'
   ```

4. **그래프 시각화**
   - 브라우저에서 `http://localhost:8080`에 접속하여 Knowledge Graph 시각화를 확인합니다.

## 활용 팁

### Cursor와 MCP 함께 사용하기
- Cursor로 MCP 코드를 개발/수정할 때 AI의 도움을 받아 더 효율적으로 작업할 수 있습니다.
- Cursor의 AI 기능을 활용해 MCP의 지식 그래프 쿼리를 작성하거나 분석할 수 있습니다.
- MCP의 지식 그래프에서 얻은 인사이트를 Cursor에서 코드로 구현할 때 활용할 수 있습니다.

### 유용한 명령어
- MCP 서버 상태 확인: `curl http://localhost:8080/api/health`
- 지식 그래프 데이터 조회: `curl http://localhost:8080/api/knowledge-graph`
- 포트 충돌 시 프로세스 확인: `lsof -i :8080`
- 프로세스 종료: `kill -9 [PID]`

## 문제 해결

### 포트 충돌 발생 시
```bash
# 포트를 사용 중인 프로세스 확인
lsof -i :8080

# 해당 프로세스 종료
kill -9 [PID]

# 다른 포트로 서버 실행
# .env 파일에서 PORT=8081로 변경 후 재시작
```

### MCP 서버 연결 문제
- 서버가 실행 중인지 확인
- 올바른 URL로 접속 중인지 확인 (http://localhost:8080)
- 환경 설정 파일(.env)이 올바르게 설정되었는지 확인

### Cursor AI 기능 작동 문제
- OpenAI API 키가 올바르게 설정되었는지 확인
- 인터넷 연결 상태 확인
- Cursor 앱 재시작 시도