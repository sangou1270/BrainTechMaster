# 알고리즘 유형별 정리

이 문서는 코딩테스트에 자주 등장하는 알고리즘 유형별 개념과 구현 예시를 포함하고 있습니다.

## 1. 자료구조

자료구조는 데이터를 효율적으로 저장하고 접근하기 위한 방법을 제공합니다. 적절한 자료구조 선택은 알고리즘의 성능을 크게 좌우합니다.

### 스택 (Stack)

**개념**: 스택은 Last In First Out(LIFO) 원칙을 따르는 선형 자료구조입니다. 마지막에 삽입된 요소가 가장 먼저 제거됩니다.

**동작 원리**: 
- 삽입(push): 스택의 가장 위에 요소를 추가합니다.
- 제거(pop): 스택의 가장 위에 있는 요소를 제거하고 반환합니다.
- 확인(peek): 스택의 가장 위에 있는 요소를 제거하지 않고 반환합니다.

**시간 복잡도**: 
- 삽입/제거: O(1) - 스택의 맨 위에서만 작업이 이루어지기 때문입니다.
- 검색: O(n) - 최악의 경우 모든 요소를 순회해야 합니다.

**장점**: 
- 구현이 간단합니다.
- 함수 호출과 같은 재귀적 알고리즘에 적합합니다.
- 원소의 추가/제거가 빠릅니다.

**단점**: 
- 중간에 있는 데이터에 접근하기 어렵습니다.
- 크기가 고정되어 있을 수 있습니다(언어/구현에 따라 다름).

```python
# 스택 구현 예시
stack = []
stack.append(1)  # 삽입
stack.append(2)
stack.append(3)
print(stack.pop())  # 3 (마지막에 넣은 값이 먼저 출력)
```

**활용 사례**: 
- 괄호 짝 맞추기: 열린 괄호는 스택에 푸시하고, 닫힌 괄호를 만나면 스택에서 팝하여 짝이 맞는지 확인합니다.
- 함수 호출 관리: 프로그램 실행 중 함수 호출 스택을 관리합니다.
- DFS 알고리즘: 그래프의 깊이 우선 탐색에 사용됩니다.
- 실행 취소(undo) 기능: 이전 작업을 스택에 저장하여 되돌리기 기능을 구현합니다.

### 큐 (Queue)

**개념**: 큐는 First In First Out(FIFO) 원칙을 따르는 선형 자료구조입니다. 가장 먼저 삽입된 요소가 가장 먼저 제거됩니다.

**동작 원리**:
- 삽입(enqueue): 큐의 뒤쪽(rear)에 요소를 추가합니다.
- 제거(dequeue): 큐의 앞쪽(front)에서 요소를 제거하고 반환합니다.
- 확인(peek): 큐의 맨 앞 요소를 제거하지 않고 반환합니다.

**시간 복잡도**:
- 삽입/제거: O(1) - 큐의 양 끝에서만 작업이 이루어집니다.
- 검색: O(n) - 최악의 경우 모든 요소를 순회해야 합니다.

**장점**:
- 데이터의 순서를 보존합니다.
- 스케줄링, 버퍼링 등에 적합합니다.
- 너비 우선 탐색(BFS)에 필수적입니다.

**단점**:
- 중간에 있는 데이터에 접근하기 어렵습니다.
- 일반 배열로 구현할 경우 dequeue 연산이 O(n)이 될 수 있습니다.

```python
# 큐 구현 예시
from collections import deque
queue = deque()
queue.append(1)  # 삽입
queue.append(2)
queue.append(3)
print(queue.popleft())  # 1 (먼저 넣은 값이 먼저 출력)
```

**활용 사례**:
- 프린터 대기열: 인쇄 작업이 순서대로 처리됩니다.
- BFS 알고리즘: 그래프의 너비 우선 탐색에 사용됩니다.
- 작업 스케줄링: CPU 스케줄링, 디스크 스케줄링에 활용됩니다.
- 실시간 시스템: 이벤트 처리 순서를 관리합니다.
- 버퍼링: 데이터 스트림에서 일시적으로 데이터를 저장합니다.

### 해시 테이블 (Hash Table)

**개념**: 해시 테이블은 키-값 쌍을 저장하는 자료구조로, 해시 함수를 사용하여 키를 배열의 인덱스로 변환합니다.

**동작 원리**:
- 해시 함수: 키를 입력받아 배열의 인덱스로 변환합니다.
- 충돌 해결: 서로 다른 키가 같은 인덱스를 가리킬 때 이를 해결하는 방법(체이닝, 개방 주소법 등)을 사용합니다.
- 저장/검색/삭제: 해시 함수로 계산된 인덱스에 데이터를 저장하거나 가져오거나 삭제합니다.

**시간 복잡도**:
- 평균 케이스: 삽입/검색/삭제 모두 O(1)
- 최악의 케이스: O(n) (해시 충돌이 많을 경우)

**장점**:
- 빠른 검색, 삽입, 삭제 연산
- 키를 통한 직접 접근이 가능합니다.
- 중복 데이터 확인이 용이합니다.

**단점**:
- 충돌 처리가 필요합니다.
- 메모리 사용량이 상대적으로 큽니다.
- 순서가 보존되지 않습니다(일반적인 해시 테이블의 경우).

```python
# 해시 테이블(딕셔너리) 활용 예시
hash_table = {}
hash_table['apple'] = 5
hash_table['banana'] = 3

# 카운터로 활용
from collections import Counter
array = ['apple', 'banana', 'apple', 'orange']
counter = Counter(array)
print(counter)  # Counter({'apple': 2, 'banana': 1, 'orange': 1})
```

**활용 사례**:
- 중복 확인: 배열에서 중복된 요소를 찾을 때 O(n) 대신 O(1)으로 가능합니다.
- 데이터베이스 인덱싱: 빠른 데이터 검색을 위해 사용됩니다.
- 캐싱: 웹 서버에서 자주 요청되는 페이지를 저장합니다.
- 사전(Dictionary): 단어와 그 뜻을 매핑합니다.
- 집합(Set): 유일한 값들의 모음을 관리합니다.

**파이썬에서 유용한 해시테이블 종류**:
- `dict`: 기본 해시테이블 구현
- `Counter`: 요소의 개수를 세는 데 특화된 딕셔너리
- `defaultdict`: 기본값을 갖는 딕셔너리
- `OrderedDict`: 삽입 순서를 기억하는 딕셔너리

## 2. 정렬 알고리즘

정렬 알고리즘은 데이터를 특정 순서(오름차순, 내림차순 등)로 배열하는 알고리즘입니다. 정렬은 검색, 병합 등 다른 알고리즘의 기초가 되기 때문에 매우 중요합니다.

### 버블 정렬 (Bubble Sort)

**개념**: 버블 정렬은 인접한 두 요소를 비교하여 필요시 교환하며 정렬하는 간단한 알고리즘입니다.

**동작 원리**:
1. 배열의 첫 번째 요소부터 시작하여 인접한 요소와 비교합니다.
2. 현재 요소가 다음 요소보다 크면 두 요소를 교환합니다.
3. 배열의 끝까지 이 작업을 반복하면 가장 큰 요소가 배열의 끝으로 이동합니다.
4. 이 과정을 배열이 정렬될 때까지 반복합니다.

**시간 복잡도**:
- 최선/평균/최악의 경우: O(n²)
- 최적화된 버블 정렬(정렬 여부 확인)의 최선의 경우: O(n)

**공간 복잡도**: O(1) - 추가 메모리를 거의 사용하지 않는 제자리 정렬입니다.

**장점**:
- 구현이 매우 간단합니다.
- 작은 데이터셋에 대해 효율적일 수 있습니다.
- 안정적인 정렬(같은 값을 가진 요소들의 상대적 순서 유지)입니다.
- 정렬 과정을 시각적으로 이해하기 쉽습니다.

**단점**:
- 대규모 데이터셋에 매우 비효율적입니다.
- 다른 정렬 알고리즘에 비해 교환 연산이 많습니다.

```python
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

print(bubble_sort([64, 34, 25, 12, 22, 11, 90]))  # [11, 12, 22, 25, 34, 64, 90]
```

**최적화된 버블 정렬**:
```python
def optimized_bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:  # 교환이 없으면 이미 정렬된 상태
            break
    return arr
```

**활용 사례**:
- 교육용: 정렬 알고리즘의 기본 개념을 이해하는 데 사용됩니다.
- 거의 정렬된 작은 배열에서 효율적일 수 있습니다.
- 메모리 제약이 심한 환경에서 사용될 수 있습니다.

### 퀵 정렬 (Quick Sort)

**개념**: 퀵 정렬은 분할 정복(Divide and Conquer) 방식을 사용하는 효율적인 정렬 알고리즘입니다. 피벗(pivot)을 선택하고 피벗을 기준으로 배열을 분할하여 정렬합니다.

**동작 원리**:
1. 배열에서 피벗 요소를 선택합니다(일반적으로 첫 번째, 마지막, 또는 중간 요소).
2. 피벗보다 작은 요소는 왼쪽, 큰 요소는 오른쪽으로 재배치합니다.
3. 분할된 두 하위 배열에 대해 재귀적으로 퀵 정렬을 적용합니다.
4. 분할된 배열의 크기가 1 이하일 때 재귀가 종료됩니다.

**시간 복잡도**:
- 평균 케이스: O(n log n)
- 최악의 케이스: O(n²) (이미 정렬된 배열에서 끝 요소를 피벗으로 선택할 때)
- 최선의 케이스: O(n log n)

**공간 복잡도**:
- 평균적으로 O(log n)의 재귀 호출 스택 공간을 사용합니다.
- 최악의 경우 O(n)의 스택 공간을 사용할 수 있습니다.

**장점**:
- 평균적으로 다른 O(n log n) 정렬 알고리즘보다 빠릅니다.
- 추가 메모리 공간을 적게 사용합니다.
- 캐시 효율성이 좋습니다.
- 제자리 정렬이 가능합니다.

**단점**:
- 최악의 경우 성능이 O(n²)로 저하됩니다.
- 안정적인 정렬이 아닙니다(같은 값을 가진 요소들의 상대적 순서가 바뀔 수 있음).
- 이미 정렬된 데이터에서는 비효율적일 수 있습니다.

```python
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

print(quick_sort([64, 34, 25, 12, 22, 11, 90]))  # [11, 12, 22, 25, 34, 64, 90]
```

**개선된 퀵 정렬 (제자리 정렬)**:
```python
def in_place_quick_sort(arr, low, high):
    if low < high:
        pivot_index = partition(arr, low, high)
        in_place_quick_sort(arr, low, pivot_index - 1)
        in_place_quick_sort(arr, pivot_index + 1, high)
    return arr

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

# 사용 예:
# arr = [64, 34, 25, 12, 22, 11, 90]
# in_place_quick_sort(arr, 0, len(arr) - 1)
```

**활용 사례**:
- 대규모 데이터셋 정렬에 효율적입니다.
- 프로그래밍 언어의 내장 정렬 함수 구현(예: C++의 `std::sort`)에 사용됩니다.
- 데이터베이스 시스템의 정렬 연산에 활용됩니다.
- 다양한 응용 프로그램에서 가장 널리 사용되는 정렬 알고리즘 중 하나입니다.

### 기타 중요한 정렬 알고리즘

#### 병합 정렬 (Merge Sort)
- **시간 복잡도**: 항상 O(n log n)
- **공간 복잡도**: O(n)
- **특징**: 안정적인 정렬, 분할 정복 방식, 연결 리스트 정렬에 효율적

#### 힙 정렬 (Heap Sort)
- **시간 복잡도**: 항상 O(n log n)
- **공간 복잡도**: O(1)
- **특징**: 제자리 정렬, 불안정 정렬, 최대/최소 값을 빠르게 찾을 수 있음

#### 계수 정렬 (Counting Sort)
- **시간 복잡도**: O(n + k) (k는 최대값)
- **공간 복잡도**: O(k)
- **특징**: 비교 기반이 아님, 정수 또는 유한한 범위의 데이터에만 적용 가능

#### 기수 정렬 (Radix Sort)
- **시간 복잡도**: O(d * (n + k)) (d는 자릿수, k는 기수)
- **공간 복잡도**: O(n + k)
- **특징**: 비교 기반이 아님, 다중 키 정렬에 효율적

## 3. 탐색 알고리즘

탐색 알고리즘은 데이터 집합에서 특정 값이나 조건을 만족하는 항목을 찾는 알고리즘입니다. 효율적인 탐색은 대규모 데이터 처리의 핵심입니다.

### 이진 탐색 (Binary Search)

**개념**: 이진 탐색은 정렬된 배열에서 타겟 값을 찾는 효율적인 알고리즘입니다. 배열의 중간 요소와 타겟을 비교하고, 타겟이 중간 요소보다 작으면 왼쪽 절반을, 크면 오른쪽 절반을 탐색합니다.

**전제 조건**: 배열이 정렬되어 있어야 합니다.

**동작 원리**:
1. 배열의 중간 요소를 찾습니다.
2. 중간 요소가 찾고자 하는 타겟과 같으면 검색을 종료합니다.
3. 타겟이 중간 요소보다 작으면 왼쪽 절반에서 검색을 계속합니다.
4. 타겟이 중간 요소보다 크면 오른쪽 절반에서 검색을 계속합니다.
5. 배열이 더 이상 분할될 수 없을 때까지 이 과정을 반복합니다.

**시간 복잡도**:
- 평균 및 최악의 경우: O(log n)
- 최선의 경우: O(1) (중간 요소가 타겟인 경우)

**공간 복잡도**:
- 반복적 구현: O(1)
- 재귀적 구현: O(log n) (재귀 호출 스택)

**장점**:
- 매우 효율적인 검색 알고리즘입니다 (O(log n)).
- 대규모 데이터셋에서도 빠르게 동작합니다.
- 구현이 상대적으로 간단합니다.

**단점**:
- 배열이 정렬되어 있어야 합니다.
- 삽입/삭제가 빈번한 데이터에는 적합하지 않습니다.
- 연결 리스트와 같은 순차 접근 자료구조에는 비효율적입니다.

```python
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1  # 찾지 못한 경우

sorted_array = [11, 12, 22, 25, 34, 64, 90]
print(binary_search(sorted_array, 25))  # 3 (25의 인덱스)
```

**재귀적 구현**:
```python
def binary_search_recursive(arr, target, left, right):
    if left > right:
        return -1
    
    mid = (left + right) // 2
    
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, right)
    else:
        return binary_search_recursive(arr, target, left, mid - 1)
```

**활용 사례**:
- 사전에서 단어 찾기
- 데이터베이스 인덱싱 및 검색
- 컴퓨터 프로그램 컴파일러의 심볼 테이블 구현
- 숫자 게임(Up & Down)
- 특정 조건을 만족하는 값의 범위를 찾는 문제 (이진 탐색 변형)

**이진 탐색의 변형**:
- 가장 왼쪽/오른쪽에 있는 타겟 값 찾기
- 배열에 없는 경우 삽입 위치 찾기
- 근사값 찾기

### 너비 우선 탐색 (BFS)

**개념**: 너비 우선 탐색은 그래프나 트리 구조에서 루트 노드(혹은 다른 임의의 노드)에서 시작하여 인접한 노드를 먼저 탐색하는 알고리즘입니다.

**동작 원리**:
1. 시작 노드를 방문하고 큐에 추가합니다.
2. 큐에서 노드를 하나 꺼내 방문 처리합니다.
3. 해당 노드의 인접 노드 중 방문하지 않은 노드를 모두 큐에 추가합니다.
4. 큐가 빌 때까지 2-3 과정을 반복합니다.

**시간 복잡도**:
- O(V + E) - V는 정점(Vertex)의 수, E는 간선(Edge)의 수

**공간 복잡도**:
- O(V) - 최악의 경우 모든 정점이 큐에 들어갈 수 있습니다.

**장점**:
- 최단 경로를 찾는 데 적합합니다(가중치 없는 그래프의 경우).
- 두 노드 사이의 최단 경로나 최소 단계를 찾는 데 유용합니다.
- 레벨 단위로 그래프를 탐색합니다.

**단점**:
- DFS보다 더 많은 메모리를 사용할 수 있습니다.
- 경로의 특성을 고려하지 않습니다(예: 경로의 비용이나 가중치).

```python
from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)
    
    while queue:
        vertex = queue.popleft()
        print(vertex, end=' ')
        
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

# 그래프 예시 (인접 리스트)
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

bfs(graph, 'A')  # A B C D E F
```

**활용 사례**:
- 최단 경로 찾기 (단위 가중치 그래프)
- 웹 크롤링: 웹 페이지와 링크를 탐색합니다.
- 소셜 네트워크 분석: 친구 추천, 연결 네트워크 등
- 네트워크 브로드캐스트: 가장 가까운 노드부터 메시지 전달
- 퍼즐 게임 해결: 루빅스 큐브, 슬라이딩 퍼즐 등

### 깊이 우선 탐색 (DFS)

**개념**: 깊이 우선 탐색은 그래프나 트리 구조에서 가능한 한 깊이 들어가며 탐색한 후, 더 이상 진행할 수 없을 때 백트래킹하는 알고리즘입니다. 깊이 우선 탐색(DFS)에 가지치기(pruning)를 적용한 방식으로 볼 수 있습니다.

**동작 원리**:
1. 해를 찾기 위해 깊이 탐색을 진행합니다.
2. 현재 상태가 조건을 만족하는지 검사합니다.
3. 만족하지 않으면 이전 상태로 돌아가(백트래킹) 다른 경로를 탐색합니다.
4. 만족하면 다음 단계로 진행합니다.
5. 목표 상태에 도달하면 해를 반환합니다.

**장점**:
- 완전 탐색보다 효율적입니다(가지치기를 통해 불필요한 탐색을 줄임).
- 모든 가능한 해를 검색할 수 있습니다.
- 복잡한 제약 조건이 있는 문제에 적합합니다.

**단점**:
- 최악의 경우 지수 시간 복잡도를 가질 수 있습니다.
- 메모리 사용량이 많을 수 있습니다.
- 최적화 문제에 대해 최적해를 보장하지 않을 수 있습니다.

```python
def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    
    visited.add(start)
    print(start, end=' ')
    
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

# 그래프 예시 (인접 리스트)
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

dfs(graph, 'A')  # A B D E F C
```

**반복적(스택 사용) 구현**:
```python
def dfs_iterative(graph, start):
    visited = set()
    stack = [start]
    
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            print(vertex, end=' ')
            
            # 인접 노드를 스택에 역순으로 추가 (탐색 순서를 위해)
            for neighbor in reversed(graph[vertex]):
                if neighbor not in visited:
                    stack.append(neighbor)
```

**활용 사례**:
- 경로 찾기 문제
- 미로 탈출 같은 퍼즐 게임 해결
- 위상 정렬(Topological Sort)
- 강한 연결 요소(Strongly Connected Components) 찾기
- 사이클 감지
- 백트래킹 기반 알고리즘(예: N-Queen 문제, 스도쿠)

### BFS와 DFS의 비교

| 특성 | BFS | DFS |
|------|-----|-----|
| 기본 자료구조 | 큐(Queue) | 스택(Stack) |
| 탐색 방식 | 너비 우선(레벨 단위) | 깊이 우선 |
| 최단 경로 | 가중치 없는 그래프에서 최적 | 보장 안 됨 |
| 메모리 사용량 | 일반적으로 높음 | 일반적으로 낮음 |
| 무한 그래프 | 완전한 탐색 불가능 | 무한 루프 위험 |
| 적합한 문제 | 최단 경로, 네트워크 흐름 | 백트래킹, 사이클 감지 |

## 4. 동적 프로그래밍 (DP)

**개념**: 동적 프로그래밍은 복잡한 문제를 더 작고 단순한 하위 문제들로 나누어 해결하는 알고리즘 기법입니다. 각 하위 문제의 해결책을 저장(메모이제이션)하여 동일한 하위 문제가 다시 계산되는 것을 방지합니다.

**동적 프로그래밍의 두 가지 주요 접근법**:
1. **Top-down (하향식)**: 재귀와 메모이제이션을 사용합니다. 큰 문제에서 시작하여 작은 하위 문제들로 분할합니다.
2. **Bottom-up (상향식)**: 반복문을 사용하여 작은 하위 문제들부터 해결하고, 이를 바탕으로 더 큰 문제를 해결합니다.

**동적 프로그래밍이 적용되기 위한 조건**:
1. **겹치는 하위 문제(Overlapping Subproblems)**: 같은 하위 문제가 반복적으로 계산됩니다.
2. **최적 부분 구조(Optimal Substructure)**: 문제의 최적해가 하위 문제들의 최적해로부터 구성될 수 있습니다.

**장점**:
- 시간 복잡도를 크게 줄일 수 있습니다(지수 시간에서 다항 시간으로).
- 복잡한 문제를 체계적으로 해결할 수 있습니다.
- 최적화 문제에 특히 효과적입니다.

**단점**:
- 추가 메모리가 필요합니다(메모이제이션 테이블 저장).
- 모든 문제에 적용할 수 없습니다.
- 구현이 복잡할 수 있습니다.

### 피보나치 수열

피보나치 수열은 DP의 기본적인 예시입니다. 각 숫자는 앞의 두 숫자의 합입니다: 0, 1, 1, 2, 3, 5, 8, 13...

**재귀적 접근법 (비효율적)**:
```python
def fibonacci_recursive(n):
    if n <= 1:
        return n
    return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)
```
이 방법은 O(2^n)의 시간 복잡도를 가지며 매우 비효율적입니다.

**메모이제이션을 활용한 Top-down DP**:
```python
def fibonacci(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 2:
        return 1
    memo[n] = fibonacci(n-1, memo) + fibonacci(n-2, memo)
    return memo[n]

print(fibonacci(10))  # 55
```
이 방법은 O(n)의 시간 복잡도를 가집니다.

**반복문을 활용한 Bottom-up DP**:
```python
def fibonacci_iterative(n):
    if n <= 2:
        return 1
    dp = [0] * (n+1)
    dp[1] = dp[2] = 1
    for i in range(3, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]

print(fibonacci_iterative(10))  # 55
```
이 방법도 O(n)의 시간 복잡도를 가지지만, 재귀 호출 스택을 사용하지 않아 추가 메모리 사용이 적습니다.

**활용 사례**: 
- 수학적 시퀀스 계산
- 계단 오르기 문제
- 타일링 문제

### 배낭 문제 (Knapsack Problem)

배낭 문제는 동적 프로그래밍의 클래식한 예입니다. 무게 제한이 있는 배낭에 가장 가치 있는 물건들을 담는 문제입니다.

**문제 설명**:
- n개의 물건이 있고, 각 물건은 무게(weight)와 가치(value)를 가집니다.
- 배낭의 무게 제한(capacity)이 주어졌을 때, 배낭에 담을 수 있는 물건들의 최대 가치를 찾아야 합니다.

**0-1 배낭 문제** (각 물건은 하나만 선택 가능):

```python
def knapsack(weights, values, capacity):
    n = len(weights)
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i-1] <= w:
                dp[i][w] = max(values[i-1] + dp[i-1][w-weights[i-1]], dp[i-1][w])
            else:
                dp[i][w] = dp[i-1][w]
    
    return dp[n][capacity]

# 예: 물건의 무게, 가치, 배낭 용량
weights = [2, 3, 4, 5]
values = [3, 4, 5, 6]
capacity = 8

print(knapsack(weights, values, capacity))  # 10
```

**시간 복잡도**: O(n * capacity) - n은 물건의 수, capacity는 배낭의 용량
**공간 복잡도**: O(n * capacity)

**최적화된 공간 복잡도**:
```python
def knapsack_optimized(weights, values, capacity):
    n = len(weights)
    dp = [0 for _ in range(capacity + 1)]
    
    for i in range(n):
        for w in range(capacity, weights[i]-1, -1):
            dp[w] = max(dp[w], values[i] + dp[w-weights[i]])
    
    return dp[capacity]
```
이 방법은 O(capacity)의 공간 복잡도만 사용합니다.

**활용 사례**:
- 리소스 할당 문제
- 예산 계획
- 투자 전략 선택
- 시간 관리 및 스케줄링

### 최장 증가 부분 수열 (LIS)

**개념**: 배열에서 순서를 유지하면서 원소를 선택하여 만들 수 있는 가장 긴 증가하는 부분 수열을 찾는 문제입니다.

**예시**: 배열 [10, 22, 9, 33, 21, 50, 41, 60, 80]의 최장 증가 부분 수열은 [10, 22, 33, 50, 60, 80]이며 길이는 6입니다.

**DP 접근법**:
```python
def longest_increasing_subsequence(arr):
    n = len(arr)
    lis = [1] * n  # 각 위치에서 끝나는 LIS의 길이
    
    for i in range(1, n):
        for j in range(0, i):
            if arr[i] > arr[j] and lis[i] < lis[j] + 1:
                lis[i] = lis[j] + 1
    
    return max(lis)

# 예시
arr = [10, 22, 9, 33, 21, 50, 41, 60, 80]
print(longest_increasing_subsequence(arr))  # 6
```

**시간 복잡도**: O(n²)
**공간 복잡도**: O(n)

**이진 탐색을 활용한 최적화**:
```python
def lis_optimized(arr):
    if not arr:
        return 0
        
    tails = [0] * len(arr)
    size = 0
    
    for x in arr:
        i, j = 0, size
        while i != j:
            m = (i + j) // 2
            if tails[m] < x:
                i = m + 1
            else:
                j = m
        
        tails[i] = x
        size = max(i + 1, size)
    
    return size
```

**시간 복잡도**: O(n log n)
**공간 복잡도**: O(n)

**활용 사례**:
- 시퀀스 분석(생물 정보학)
- 패턴 인식
- 최적 전략 게임

### 최소 편집 거리 (Edit Distance)

**개념**: 두 문자열 간의 최소 편집 거리를 계산하는 문제입니다. 편집 연산에는 삽입, 삭제, 대체가 포함됩니다.

**예시**: "kitten"을 "sitting"으로 변환하기 위한 최소 편집 거리는 3입니다:
1. kitten → sitten (k를 s로 대체)
2. sitten → sittin (e를 i로 대체)
3. sittin → sitting (끝에 g 삽입)

**DP 접근법**:
```python
def edit_distance(word1, word2):
    m, n = len(word1), len(word2)
    dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
    
    # 초기화
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j
    
    # DP 테이블 채우기
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if word1[i-1] == word2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(dp[i-1][j],      # 삭제
                                   dp[i][j-1],      # 삽입
                                   dp[i-1][j-1])    # 대체
    
    return dp[m][n]

# 예시
print(edit_distance("kitten", "sitting"))  # 3
```

**시간 복잡도**: O(m * n) - m, n은 각 문자열의 길이
**공간 복잡도**: O(m * n)

**활용 사례**:
- 자연어 처리
- DNA 시퀀스 비교
- 맞춤법 검사 및 자동 수정
- 표절 감지

### 동적 프로그래밍을 활용한 기타 문제들

1. **계단 오르기**: 한번에 1칸 또는 2칸씩 오를 수 있을 때, n개의 계단을 오르는 방법의 수
2. **최대 부분합**: 배열에서 연속된 부분 배열의 최대 합
3. **행렬 경로 문제**: 격자에서 왼쪽 위에서 오른쪽 아래로 이동하는 최소 비용 경로
4. **동전 교환 문제**: 주어진 금액을 만드는데 필요한 최소 동전 개수
5. **구간 합**: 배열의 특정 범위 내 원소들의 합

## 5. 그리디 알고리즘

**개념**: 그리디 알고리즘(탐욕 알고리즘)은 각 단계에서 지역적으로 최적인 선택을 하는 방식으로 전체 문제의 최적해를 구하는 알고리즘입니다. 각 선택은 현재 상태에서 가장 좋아 보이는 옵션을 선택하는 "욕심쟁이" 방식으로 이루어집니다.

**그리디 알고리즘의 작동 원리**:
1. 현재 상태에서 최적의 선택을 합니다.
2. 이 선택이 문제의 나머지 부분에 어떤 영향을 미칠지 고려하지 않습니다.
3. 다음 하위 문제로 넘어가 동일한 과정을 반복합니다.

**그리디 알고리즘이 최적해를 보장하는 조건**:
1. **탐욕 선택 속성(Greedy Choice Property)**: 지역적으로 최적인 선택이 전역적으로도 최적인 해결책의 일부가 되는 속성
2. **최적 부분 구조(Optimal Substructure)**: 문제의 최적해가 하위 문제들의 최적해를 포함하는 속성

**장점**:
- 구현이 일반적으로 간단합니다.
- 실행 속도가 빠른 경우가 많습니다.
- 복잡한 상태를 유지할 필요가 없습니다.

**단점**:
- 모든 문제에 적용할 수 없습니다.
- 최적해를 항상 보장하지 않습니다.
- 적용 가능성을 증명하기 어려울 수 있습니다.

### 거스름돈 문제

**문제 설명**: 특정 금액을 만들기 위해 필요한 최소 동전 개수를 구하는 문제입니다.

**그리디 접근법**: 가장 큰 단위의 동전부터 사용하여 남은 금액을 최소한의 동전으로 만듭니다.

```python
def min_coins(coins, amount):
    coins.sort(reverse=True)  # 큰 동전부터 사용
    count = 0
    for coin in coins:
        while amount >= coin:
            amount -= coin
            count += 1
    return count if amount == 0 else -1

print(min_coins([500, 100, 50, 10], 1260))  # 6개 (500원 2개, 100원 2개, 50원 1개, 10원 1개)
```

**시간 복잡도**: O(n + k) - n은 동전 종류의 수, k는 교환 과정의 반복 횟수(최악의 경우 amount)
**공간 복잡도**: O(1)

**그리디가 최적해를 보장하는 이유**: 이 문제에서는 모든 동전이 서로의 배수 관계이면 그리디 접근이 최적해를 보장합니다.

**그리디가 최적해를 보장하지 않는 예**: 동전 [1, 3, 4]로 6을 만들 때, 그리디 접근은 4+1+1=6으로 3개를 사용하지만, 최적해는 3+3=6으로 2개입니다.

### 활동 선택 문제 (Activity Selection)

**문제 설명**: 한 사람이 여러 활동 중에서 겹치지 않게 최대한 많은 활동을 선택하는 문제입니다.

**그리디 접근법**: 활동을 종료 시간 기준으로 정렬한 후, 가능한 빨리 끝나는 활동부터 선택합니다.

```python
def activity_selection(start, finish):
    n = len(start)
    # 종료 시간으로 정렬된 활동 인덱스 생성
    activities = sorted(range(n), key=lambda i: finish[i])
    
    selected = [activities[0]]  # 첫 번째 활동 선택
    last_finish = finish[activities[0]]
    
    for i in range(1, n):
        idx = activities[i]
        if start[idx] >= last_finish:  # 이전 활동 종료 후 시작하는 활동만 선택
            selected.append(idx)
            last_finish = finish[idx]
    
    return selected

# 예: 활동의 시작 시간과 종료 시간
start = [1, 3, 0, 5, 8, 5]
finish = [2, 4, 6, 7, 9, 9]

print(activity_selection(start, finish))  # [0, 1, 3, 4] 또는 [0, 1, 3, 5]
```

**시간 복잡도**: O(n log n) - 정렬이 가장 비용이 많이 드는 부분
**공간 복잡도**: O(n)

**그리디가 최적해를 보장하는 이유**: 가장 빨리 끝나는 활동을 선택하면 남은 시간이 최대화되어 더 많은 활동을 선택할 가능성이 높아집니다.

### 허프만 코딩 (Huffman Coding)

**문제 설명**: 문자의 빈도수에 따라 가변 길이 코드를 할당하여 데이터를 압축하는 문제입니다.

**그리디 접근법**: 빈도가 낮은 문자에 긴 코드를, 빈도가 높은 문자에 짧은 코드를 할당합니다.

```python
import heapq
from collections import Counter

def huffman_encoding(data):
    if not data:
        return None, None
    
    # 문자 빈도수 계산
    frequency = Counter(data)
    
    # 우선순위 큐 생성
    heap = [[weight, [char, ""]] for char, weight in frequency.items()]
    heapq.heapify(heap)
    
    # 허프만 트리 구축
    while len(heap) > 1:
        lo = heapq.heappop(heap)
        hi = heapq.heappop(heap)
        
        for pair in lo[1:]:
            pair[1] = '0' + pair[1]
        for pair in hi[1:]:
            pair[1] = '1' + pair[1]
        
        heapq.heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])
    
    # 허프만 코드 추출
    huff = sorted(heapq.heappop(heap)[1:], key=lambda p: (len(p[1]), p[0]))
    
    # 코드 딕셔너리 생성
    huffman_code = {char: code for char, code in huff}
    
    # 인코딩된 데이터 생성
    encoded_data = ''.join([huffman_code[char] for char in data])
    
    return encoded_data, huffman_code

# 예시
data = "AABBBCDDDEEEEEFFFFFFF"
encoded_data, huffman_code = huffman_encoding(data)

print("허프만 코드:", huffman_code)
print("인코딩된 데이터:", encoded_data)
```

**시간 복잡도**: O(n log n) - n은 고유 문자의 수
**공간 복잡도**: O(n)

**활용 사례**: 
- 텍스트 압축
- JPEG, MP3와 같은 미디어 파일 압축
- 통신 프로토콜

### 최소 신장 트리 (MST) 알고리즘

#### Kruskal 알고리즘

**문제 설명**: 그래프의 모든 정점을 연결하는 최소 가중치의 트리를 찾는 문제입니다.

**그리디 접근법**: 간선을 가중치 기준으로 정렬하고, 사이클을 형성하지 않는 한 가장 가중치가 작은 간선부터 선택합니다.

```python
# 유니온-파인드 구현
def find(parent, i):
    if parent[i] != i:
        parent[i] = find(parent, parent[i])
    return parent[i]

def union(parent, rank, x, y):
    root_x = find(parent, x)
    root_y = find(parent, y)
    
    if root_x == root_y:
        return
    
    if rank[root_x] < rank[root_y]:
        parent[root_x] = root_y
    elif rank[root_x] > rank[root_y]:
        parent[root_y] = root_x
    else:
        parent[root_y] = root_x
        rank[root_x] += 1

def kruskal_mst(graph, vertices):
    result = []
    i, e = 0, 0
    
    # 간선을 가중치 기준으로 정렬
    graph = sorted(graph, key=lambda item: item[2])
    
    parent = [i for i in range(vertices)]
    rank = [0] * vertices
    
    while e < vertices - 1:
        u, v, w = graph[i]
        i += 1
        x = find(parent, u)
        y = find(parent, v)
        
        if x != y:
            e += 1
            result.append([u, v, w])
            union(parent, rank, x, y)
    
    return result

# 예시
graph = [
    [0, 1, 10],
    [0, 2, 6],
    [0, 3, 5],
    [1, 3, 15],
    [2, 3, 4]
]
vertices = 4

mst = kruskal_mst(graph, vertices)
print("Kruskal MST:", mst)
```

**시간 복잡도**: O(E log E) 또는 O(E log V) - E는 간선 수, V는 정점 수
**공간 복잡도**: O(E + V)

**활용 사례**:
- 네트워크 설계
- 회로 설계
- 클러스터링
- 이미지 분석

## 6. 백트래킹 알고리즘

**개념**: 백트래킹은 해를 찾는 도중에 해가 아니라고 판단되면 즉시 이전 단계로 돌아가서 다른 경로를 탐색하는 알고리즘입니다. 깊이 우선 탐색(DFS)에 가지치기(pruning)를 적용한 방식으로 볼 수 있습니다.

**백트래킹의 작동 원리**:
1. 해를 찾기 위해 깊이 탐색을 진행합니다.
2. 현재 상태가 조건을 만족하는지 검사합니다.
3. 만족하지 않으면 이전 상태로 돌아가(백트래킹) 다른 경로를 탐색합니다.
4. 만족하면 다음 단계로 진행합니다.
5. 목표 상태에 도달하면 해를 반환합니다.

**장점**:
- 완전 탐색보다 효율적입니다(가지치기를 통해 불필요한 탐색을 줄임).
- 모든 가능한 해를 검색할 수 있습니다.
- 복잡한 제약 조건이 있는 문제에 적합합니다.

**단점**:
- 최악의 경우 지수 시간 복잡도를 가질 수 있습니다.
- 메모리 사용량이 많을 수 있습니다.
- 최적화 문제에 대해 최적해를 보장하지 않을 수 있습니다.

### N-Queen 문제

**문제 설명**: NxN 체스판에 N개의 퀸을 서로 공격할 수 없도록 배치하는 문제입니다.

**백트래킹 접근법**: 각 행에 하나의 퀸을 배치하고, 이전에 배치한 퀸들과 충돌하지 않는지 확인합니다. 충돌이 있으면 다른 위치를 시도합니다.

```python
def is_safe(board, row, col, n):
    # 같은 열에 퀸이 있는지 확인
    for i in range(row):
        if board[i][col] == 1:
            return False
    
    # 왼쪽 위 대각선 확인
    for i, j in zip(range(row-1, -1, -1), range(col-1, -1, -1)):
        if board[i][j] == 1:
            return False
    
    # 오른쪽 위 대각선 확인
    for i, j in zip(range(row-1, -1, -1), range(col+1, n)):
        if board[i][j] == 1:
            return False
    
    return True

def solve_n_queens(n):
    board = [[0 for _ in range(n)] for _ in range(n)]
    solutions = []
    
    def backtrack(row):
        if row == n:
            solution = [''.join('Q' if cell == 1 else '.' for cell in row) for row in board]
            solutions.append(solution)
            return
        
        for col in range(n):
            if is_safe(board, row, col, n):
                board[row][col] = 1
                backtrack(row + 1)
                board[row][col] = 0  # 백트래킹
    
    backtrack(0)
    return solutions

print(len(solve_n_queens(4)))  # 4x4 체스판에서는 2개의 해결책이 있음
```

**시간 복잡도**: O(N!) - 최악의 경우
**공간 복잡도**: O(N²)

**개선된 접근법**:
```python
def solve_n_queens_optimized(n):
    solutions = []
    
    def backtrack(row, cols, diag1, diag2):
        if row == n:
            board = []
            for i in range(n):
                row_str = '.' * cols[i] + 'Q' + '.' * (n - cols[i] - 1)
                board.append(row_str)
            solutions.append(board)
            return
        
        for col in range(n):
            if col not in cols and row+col not in diag1 and row-col not in diag2:
                cols.append(col)
                diag1.append(row+col)
                diag2.append(row-col)
                
                backtrack(row+1, cols, diag1, diag2)
                
                cols.pop()
                diag1.pop()
                diag2.pop()
    
    backtrack(0, [], [], [])
    return solutions
```

**활용 사례**:
- 퍼즐 게임 해결
- 라우팅 및 스케줄링 문제
- 리소스 할당 문제

### 부분집합 문제 (Subset Sum)

**문제 설명**: 주어진 집합의 요소들 중 일부를 선택하여 특정 합을 만들 수 있는지 확인하는 문제입니다.

**백트래킹 접근법**: 각 요소를 포함하거나 포함하지 않는 두 가지 선택을 재귀적으로 탐색합니다.

```python
def subset_sum(nums, target):
    result = []
    
    def backtrack(start, subset, current_sum):
        if current_sum == target:
            result.append(subset[:])
            return
        
        if current_sum > target or start >= len(nums):
            return
        
        # 현재 요소 포함
        subset.append(nums[start])
        backtrack(start + 1, subset, current_sum + nums[start])
        
        # 현재 요소 제외 (백트래킹)
        subset.pop()
        backtrack(start + 1, subset, current_sum)
    
    backtrack(0, [], 0)
    return result

# 예시
nums = [2, 3, 6, 7]
target = 7
print(subset_sum(nums, target))  # [[7]]
```

**시간 복잡도**: O(2^N) - 최악의 경우
**공간 복잡도**: O(N)

**가지치기 최적화**:
- 배열을 정렬하여 현재 합이 목표를 초과하면 즉시 가지치기
- 현재까지의 합과 남은 요소들의 합이 목표보다 작으면 가지치기

### 스도쿠 해결

**문제 설명**: 9x9 그리드에 1-9까지의 숫자를 각 행, 열, 3x3 서브그리드에 겹치지 않게 채우는 문제입니다.

**백트래킹 접근법**: 빈 칸을 하나씩 채우면서 유효한 숫자를 시도합니다. 충돌이 발생하면 이전 상태로 돌아가 다른 숫자를 시도합니다.

```python
def solve_sudoku(board):
    # 빈 칸 찾기
    def find_empty():
        for i in range(9):
            for j in range(9):
                if board[i][j] == 0:
                    return i, j
        return None
    
    # 유효성 검사
    def is_valid(num, pos):
        row, col = pos
        
        # 행 검사
        for j in range(9):
            if board[row][j] == num and j != col:
                return False
        
        # 열 검사
        for i in range(9):
            if board[i][col] == num and i != row:
                return False
        
        # 3x3 서브그리드 검사
        box_row, box_col = row // 3 * 3, col // 3 * 3
        for i in range(box_row, box_row + 3):
            for j in range(box_col, box_col + 3):
                if board[i][j] == num and (i, j) != pos:
                    return False
        
        return True
    
    # 백트래킹
    def backtrack():
        empty = find_empty()
        if not empty:
            return True
        
        row, col = empty
        for num in range(1, 10):
            if is_valid(num, (row, col)):
                board[row][col] = num
                
                if backtrack():
                    return True
                
                board[row][col] = 0  # 백트래킹
        
        return False
    
    backtrack()
    return board
```

**시간 복잡도**: O(9^(N*N)) - 최악의 경우, N은 그리드 크기(9x9에서는 9)
**공간 복잡도**: O(N*N)

**활용 사례**:
- 퍼즐 게임 해결
- 라우팅 및 스케줄링 문제
- 리소스 할당 문제

## 7. 그래프 알고리즘

그래프는 정점(Vertex)과 간선(Edge)으로 구성된 자료구조로, 많은 실생활 문제를 모델링하는 데 사용됩니다. 그래프 알고리즘은 이러한 그래프 구조에서 최단 경로, 연결성, 순환 등 다양한 특성을 분석하고 활용합니다.

### 다익스트라 알고리즘 (최단 경로)

**개념**: 다익스트라 알고리즘은 가중치가 있는 그래프에서 한 정점에서 다른 모든 정점까지의 최단 경로를 찾는 알고리즘입니다.

**전제 조건**: 모든 간선의 가중치는 음수가 아니어야 합니다.

**동작 원리**:
1. 시작 정점의 거리를 0으로, 나머지 정점의 거리를 무한대로 초기화합니다.
2. 방문하지 않은 정점 중 가장 거리가 짧은 정점을 선택합니다.
3. 선택한 정점에서 인접한 정점들의 거리를 갱신합니다.
4. 모든 정점을 방문할 때까지 2-3 과정을 반복합니다.

**구현**:
```python
import heapq

def dijkstra(graph, start):
    # 시작 정점에서 각 정점까지의 거리를 저장
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    priority_queue = [(0, start)]
    
    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)
        
        # 이미 처리된 노드라면 무시
        if current_distance > distances[current_vertex]:
            continue
            
        # 인접한 노드들 확인
        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight
            
            # 현재 알고 있는 경로보다 더 짧은 경로를 발견한 경우
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
    
    return distances

# 그래프 예시 (인접 딕셔너리)
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

print(dijkstra(graph, 'A'))  # {'A': 0, 'B': 1, 'C': 3, 'D': 4}
```

**시간 복잡도**: 
- 인접 행렬: O(V²)
- 우선순위 큐(힙): O((V + E) log V) - V는 정점 수, E는 간선 수

**공간 복잡도**: O(V)

**최적화 기법**:
- 이진 힙 대신 피보나치 힙 사용: O(E + V log V)
- 양방향 탐색(Bidirectional search)
- A* 알고리즘: 휴리스틱을 사용한 다익스트라 확장

**활용 사례**:
- 네트워크 라우팅 프로토콜(OSPF)
- 지도 앱에서 최단 경로 찾기
- 로봇 경로 계획
- 사회 네트워크 분석: 친구 추천, 연결 네트워크 등
- 네트워크 브로드캐스트: 가장 가까운 노드부터 메시지 전달
- 퍼즐 게임 해결: 루빅스 큐브, 슬라이딩 퍼즐 등

### 벨만-포드 알고리즘 (음수 가중치 최단 경로)

**개념**: 벨만-포드 알고리즘은 음수 가중치가 있는 그래프에서도 최단 경로를 찾을 수 있는 알고리즘입니다.

**전제 조건**: 음수 사이클이 없어야 최단 경로가 정의됩니다.

**동작 원리**:
1. 시작 정점의 거리를 0으로, 나머지 정점의 거리를 무한대로 초기화합니다.
2. 모든 간선에 대해 완화(relaxation) 작업을 수행합니다.
3. 정점 수 - 1번 반복합니다.
4. 음수 사이클 확인을 위해 한 번 더 모든 간선을 확인합니다.

**구현**:
```python
def bellman_ford(graph, start):
    # 정점과 간선 정보 추출
    vertices = list(graph.keys())
    edges = []
    for u in graph:
        for v, w in graph[u].items():
            edges.append((u, v, w))
    
    # 초기화
    distances = {vertex: float('infinity') for vertex in vertices}
    distances[start] = 0
    
    # |V| - 1번 반복
    for _ in range(len(vertices) - 1):
        for u, v, w in edges:
            if distances[u] != float('infinity') and distances[u] + w < distances[v]:
                distances[v] = distances[u] + w
    
    # 음수 사이클 확인
    for u, v, w in edges:
        if distances[u] != float('infinity') and distances[u] + w < distances[v]:
            raise ValueError("Graph contains a negative-weight cycle")
    
    return distances
```

**시간 복잡도**: O(V * E) - V는 정점 수, E는 간선 수
**공간 복잡도**: O(V)

**활용 사례**:
- 네트워크 라우팅 알고리즘(거리 벡터 라우팅)
- 차익 거래(Arbitrage) 탐지
- 시스템 최적화

### 플로이드-워셜 알고리즘 (모든 쌍 최단 경로)

**개념**: 플로이드-워셜 알고리즘은 그래프의 모든 정점 쌍 사이의 최단 경로를 찾는 알고리즘입니다.

**동작 원리**:
1. 인접 행렬로 그래프를 표현합니다.
2. 모든 중간 정점 k에 대해, i에서 j로 가는 경로가 k를 거쳐 가는 것이 더 짧은지 확인합니다.
3. 더 짧은 경로가 있으면 거리를 갱신합니다.

**구현**:
```python
def floyd_warshall(graph):
    # 정점 목록 추출
    vertices = list(graph.keys())
    n = len(vertices)
    
    # 인접 행렬 초기화
    dist = [[float('infinity') for _ in range(n)] for _ in range(n)]
    
    # 자기 자신으로의 거리는 0, 직접 연결된 간선의 가중치 설정
    for i in range(n):
        dist[i][i] = 0
        for j, weight in graph[vertices[i]].items():
            if j in vertices:
                j_idx = vertices.index(j)
                dist[i][j_idx] = weight
    
    # 플로이드-워셜 알고리즘
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    
    # 결과를 원래 정점 이름으로 변환
    result = {}
    for i in range(n):
        result[vertices[i]] = {}
        for j in range(n):
            result[vertices[i]][vertices[j]] = dist[i][j]
    
    return result
```

**시간 복잡도**: O(V³) - V는 정점 수
**공간 복잡도**: O(V²)

**활용 사례**:
- 네트워크 라우팅
- 전이적 폐쇄(Transitive closure) 계산
- 복잡한 관계 분석
- 로봇 경로 계획

### 프림 알고리즘 (최소 신장 트리)

**개념**: 프림 알고리즘은 가중치가 있는 무방향 그래프에서 모든 정점을 포함하는 최소 비용의 트리(최소 신장 트리)를 찾는 알고리즘입니다.

**동작 원리**:
1. 임의의 정점에서 시작합니다.
2. 현재 트리에 연결된 간선 중 가장 가중치가 작은 간선을 선택하여 트리를 확장합니다.
3. 모든 정점이 트리에 포함될 때까지 반복합니다.

**구현**:
```python
import heapq

def prim_mst(graph):
    # 시작 정점 (첫번째 정점으로 선택)
    start_vertex = list(graph.keys())[0]
    
    # MST와 가중치 합 초기화
    mst = []
    total_weight = 0
    
    # 방문한 정점 추적
    visited = {vertex: False for vertex in graph}
    
    # 우선순위 큐 초기화
    priority_queue = [(0, start_vertex, None)]  # (가중치, 정점, 부모 정점)
    
    while priority_queue:
        weight, vertex, parent = heapq.heappop(priority_queue)
        
        if visited[vertex]:
            continue
        
        visited[vertex] = True
        
        if parent is not None:
            mst.append((parent, vertex, weight))
            total_weight += weight
        
        for neighbor, edge_weight in graph[vertex].items():
            if neighbor not in visited:
                heapq.heappush(priority_queue, (edge_weight, neighbor, vertex))
    
    return mst, total_weight
```

**시간 복잡도**: O(E log V) - E는 간선 수, V는 정점 수
**공간 복잡도**: O(V + E)

**활용 사례**:
- 네트워크 설계
- 클러스터링
- 전기 회로 설계
- 파이프라인 설계

### 위상 정렬 (Topological Sort)

**개념**: 위상 정렬은 방향 비순환 그래프(DAG)에서 정점들을 선형으로 정렬하여, 모든 간선 (u, v)에 대해 정렬 결과에서 u가 v보다 앞에 오도록 하는 알고리즘입니다.

**동작 원리**:
1. 진입 차수(in-degree)가 0인 정점을 큐에 추가합니다.
2. 큐에서 정점을 꺼내 결과 리스트에 추가합니다.
3. 해당 정점에서 나가는 모든 간선을 제거하고, 이로 인해 진입 차수가 0이 된 정점을 큐에 추가합니다.
4. 큐가 빌 때까지 2-3 과정을 반복합니다.

**구현**:
```python
from collections import deque

def topological_sort(graph):
    # 진입 차수 계산
    in_degree = {vertex: 0 for vertex in graph}
    for vertex in graph:
        for neighbor in graph[vertex]:
            in_degree[neighbor] += 1
    
    # 진입 차수가 0인 정점으로 큐 초기화
    queue = deque([vertex for vertex in in_degree if in_degree[vertex] == 0])
    
    # 결과 리스트 초기화
    result = []
    
    while queue:
        vertex = queue.popleft()
        result.append(vertex)
        
        for neighbor in graph[vertex]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    
    # 모든 정점을 방문하지 못했다면 사이클이 존재
    if len(result) != len(graph):
        raise ValueError("Graph contains a cycle")
    
    return result
```

**시간 복잡도**: O(V + E) - V는 정점 수, E는 간선 수
**공간 복잡도**: O(V)

**활용 사례**:
- 작업 스케줄링
- 코스 일정 계획
- 프로그램 빌드 시스템(의존성 해결)
- 데이터 직렬화

### 강한 연결 요소 (Strongly Connected Components)

**개념**: 강한 연결 요소(SCC)는 방향 그래프에서 모든 정점 쌍 (u, v)에 대해 u에서 v로, v에서 u로 가는 경로가 모두 존재하는 최대 부분 그래프입니다.

**타잔 알고리즘**:
```python
def tarjan_scc(graph):
    index_counter = [0]
    index = {}  # 정점 방문 순서
    lowlink = {}  # 정점이 도달할 수 있는 가장 작은 인덱스
    onstack = set()  # 현재 스택에 있는 정점들
    stack = []
    result = []
    
    def strongconnect(vertex):
        # 정점 초기화
        index[vertex] = index_counter[0]
        lowlink[vertex] = index_counter[0]
        index_counter[0] += 1
        stack.append(vertex)
        onstack.add(vertex)
        
        # 인접 정점 탐색
        for neighbor in graph.get(vertex, []):
            if neighbor not in index:
                # 아직 방문하지 않은 정점
                strongconnect(neighbor)
                lowlink[vertex] = min(lowlink[vertex], lowlink[neighbor])
            elif neighbor in onstack:
                # 이미 스택에 있는 정점 (백엣지)
                lowlink[vertex] = min(lowlink[vertex], index[neighbor])
        
        # SCC 확인
        if lowlink[vertex] == index[vertex]:
            # 새로운 SCC 찾음
            scc = []
            while True:
                w = stack.pop()
                onstack.remove(w)
                scc.append(w)
                if w == vertex:
                    break
            result.append(scc)
    
    # 모든 정점에 대해 실행
    for vertex in graph:
        if vertex not in index:
            strongconnect(vertex)
    
    return result
```

**시간 복잡도**: O(V + E) - V는 정점 수, E는 간선 수
**공간 복잡도**: O(V)

**활용 사례**:
- 회로 분석
- 컴파일러 최적화
- 고정점 계산
- 데이터베이스 의존성 분석

### 그래프 알고리즘의 비교

| 알고리즘 | 문제 유형 | 시간 복잡도 | 가중치 | 음수 가중치 |
|---------|---------|---------|------|-----------|
| 다익스트라 | 단일 출발 최단 경로 | O((V+E)log V) | 필요 | 불가능 |
| 벨만-포드 | 단일 출발 최단 경로 | O(V*E) | 필요 | 가능 |
| 플로이드-워셜 | 모든 쌍 최단 경로 | O(V³) | 필요 | 가능 |
| 크루스칼 | 최소 신장 트리 | O(E log E) | 필요 | 가능 |
| 프림 | 최소 신장 트리 | O(E log V) | 필요 | 가능 |
| BFS | 최단 경로(단위 가중치) | O(V+E) | 단위 가중치 | 해당 없음 |
| DFS | 그래프 탐색 | O(V+E) | 불필요 | 해당 없음 |
| 위상 정렬 | 정점 순서 | O(V+E) | 불필요 | 해당 없음 |
| 타잔 | 강한 연결 요소 | O(V+E) | 불필요 | 해당 없음 |

---

## 태그
#알고리즘 #자료구조 #코딩테스트 #DP #그리디 #백트래킹 #BFS #DFS #정렬 #그래프