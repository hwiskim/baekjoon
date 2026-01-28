import heapq
import sys

def solve():
    # 빠른 입력을 위해 sys.stdin.readline 사용
    input = sys.stdin.readline
    
    # 1. 도시의 개수(N)와 버스의 개수(M) 입력
    n = int(input())
    m = int(input())
    
    # 2. 인접 리스트로 그래프 구현
    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        u, v, w = map(int, input().split())
        graph[u].append((v, w))
    
    # 3. 출발점과 도착점 입력
    start_node, end_node = map(int, input().split())
    
    # 4. 최단 거리 테이블 초기화 (무한대로 설정)
    distance = [float('inf')] * (n + 1)
    
    # 다익스트라 알고리즘 함수
    def dijkstra(start):
        pq = []
        # (비용, 현재 노드) 형태로 우선순위 큐에 삽입
        heapq.heappush(pq, (0, start))
        distance[start] = 0
        
        while pq:
            # 가장 비용이 적은 노드 꺼내기
            dist, now = heapq.heappop(pq)
            
            # 이미 처리된 노드라면 무시
            if distance[now] < dist:
                continue
                
            # 인접 노드 확인
            for next_node, weight in graph[now]:
                cost = dist + weight
                # 현재 노드를 거쳐서 가는 게 더 빠를 경우 업데이트
                if cost < distance[next_node]:
                    distance[next_node] = cost
                    heapq.heappush(pq, (cost, next_node))

    # 다익스트라 실행 및 결과 출력
    dijkstra(start_node)
    print(distance[end_node])

solve()