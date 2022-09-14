
# Dynamic Programming

## 동적 프로그래밍의 적용 상황

- 최적 부분구조optimal substructure / principle of optimality
→ 큰 문제의 최적 솔루션에 작은 문제의 최적 솔루션이 포함됨
- 재귀호출시 중복 overlapping recursive calls
→ 재귀적 해법으로 풀면 같은 문제에 대한 재귀호출이 심하게 중복됨
 <br/><br/>


## DC VS DP

- 공통점
 <br/>큰 문제를 작은 문제로 나누는 방식

- 차이점
<br/>
DP : 작은 문제부터 풀고 작은 문제의 솔루션 메모, 이후 큰 문제에서 가져다 사용<br/>
D-and-C : 전에 이미 풀었던 문제이더라도 다시 푸는 방식
<br/><br/>
DP : 일반적으로 Bottom-up방식(Top-down도 가능)<br/>
D-and-C : 일반적으로 Top-down



<br/><br/>
<br/><br/>
<br/><br/>

# 시간복잡도

## 점근적 표기법 (Asymtotic notation)
: n이 커질때 수행시간이 대략적으로 어떤 함수에 비례하는지 측정하는 용도로 (빅오), Ω(오메가), Θ(세타) 존재

<br/><br/>
<br/><br/>

## 빅-오 표기법(Big-Oh notation) : O

 ![O.png](https://pastoral-topaz-a50.notion.site/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2F1cc03f0b-0fd3-4fab-a0e7-4707aa8ea155%2FUntitled.png?table=block&id=02ba6aed-1c8f-4087-924b-630e169d0734&spaceId=5ed0efe9-74ef-4cae-80fe-be7b08543073&width=1920&userId=&cache=v2)

### 정의

$$
O(g(n)) = { f(n) | ∃c > 0, n0 ≥ 0 s.t.∀n ≥ n0, cg(n) ≥ f(n) }
$$

- 최악의 경우를 측정할 수 있는 표기법 (넉넉하게 표기)
- f(n) = O(g(n)) → f는 기껏해야 g(n)의 비율로 증가하는 함수로 g보다 좋음
- f(n) ∈ O(g(n)을 관행적으로 f(n) = O(g(n))

### 특징

- 점근적 상한선 = n이 가장 나쁜 상황에서도 비교함수와 같거나 좋다
- 알 수 있는 한 tight하게 표기
- 상수 비율의 차이는 무시

### 예제

- 3n^2 + 2n = O(n2)
- 7n^2 – 100n = O(n^2)
- nlogn + 5n = O(nlogn)

<br/><br/>
<br/><br/>

## 오메가 표기법 : Ω

![Ω.png](https://pastoral-topaz-a50.notion.site/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2F4d2e1340-8dc7-4e9a-99f8-5807c66df6ae%2FUntitled.png?table=block&id=a29e2530-1434-4205-8295-fd35b3cadf4b&spaceId=5ed0efe9-74ef-4cae-80fe-be7b08543073&width=1920&userId=&cache=v2)

### 정의

$$
Ω(g(n)) = { f(n) | ∃c > 0, n0 ≥ 0 s.t.∀n ≥ n0, cg(n)≤f(n) }
$$

- f(n) = Ω(g(n)) → f는 적어도 g(n)의 비율로 증가하는 함수로 g보다 안좋음
- f(n) = Ω(g(n)) → f는 g보다 느리게 증가하지 않는다

### 특징

- 점근적 하한선 = n이 가장 좋은 상황에서도 비교함수와 같거나 안좋다
- O(g(n))과 대칭적

<br/><br/>
<br/><br/>

## 세타 표기법 : Θ

![Θ.png](https://pastoral-topaz-a50.notion.site/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2Fcab6d2d9-2a07-4737-b0f6-81fc7a484daa%2FUntitled.png?table=block&id=5a365a58-a042-40eb-8528-b82c4b191f77&spaceId=5ed0efe9-74ef-4cae-80fe-be7b08543073&width=1920&userId=&cache=v2)

### 정의

$$
Θ( g(n) ) = O( g(n) ) ∩ Ω( g(n) )
$$

- f(n) = Θ(g(n)) ⇒ f는 g와 같은 정도로 증가한다

### 특징

- g(n)의 비율로 증가하는 함수
- 비교적 정확하다는 특징