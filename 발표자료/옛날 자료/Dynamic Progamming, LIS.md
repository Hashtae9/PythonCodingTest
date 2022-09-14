# Dynamic Progamming

> **하나의 큰 문제를 여러 개의 작은 문제로 나누어서 그 결과를 저장하여 다시 큰 문제를 해결할 때 사용**



## DP가 적용되기 위해서는 2가지 조건

### 1. Overlapping Subproblems(겹치는 부분 문제)

>  **동일한 작은 문제들이 반복하여 나타나는 경우에 사용이 가능**

+ **부분 문제가 반복적으로 나타나지 않는다면 재사용이 불가능하니 부분 문제가 중복되지 않는 경우에는 사용할 수 없다.**
  + 이진 탐색 vs 피보나치 수열
    + 특정 데이터를 정렬된 배열 내에서 그 위치를 찾기 때문에 위치를 찾은 후 바로 반환(재사용 x)
    + f(n) = f(n-1) + f(n-2)의 경우 동일한 부분 문제가 중복되어 나타나는 케이스 존재

<img src="https://user-images.githubusercontent.com/101400894/184607050-2e6c5616-154a-4924-ab6a-ed972847fcd4.png" alt="image" style="zoom:80%;" />





### 2. Optimal Substructure(최적 부분 구조)

> **부분 문제의 최적 결과 값을 사용해 전체 문제의 최적 결과를 낼 수 있는 경우**

![image](https://user-images.githubusercontent.com/101400894/184607230-3b04eeb5-8552-4de3-aaaa-11cb6eb8400f.png)

+ 만약, A - B까지의 가장 짧은 경로를 찾고자 하는 경우를 예시로 할 때, 중간에 X가 있을 때, A - X / X - B가 많은 경로 중 가장 짧은 경로라면 전체 최적 경로도 A - X - B가 정답이 된다.



## DP 사용하기

> **특정한 경우에 사용하는** **알고리즘이 아니라 하나의 방법론이므로 다양한 문제해결에 쓰일 수 있다**



### 1.**DP로 풀 수 있는 문제인지 확인**

> 위에서 쓴 **조건들이 충족되는 문제인지를 한 번 체크**

+ 특정 데이터 내 최대화 / 최소화 계산을 하거나 특정 조건 내 데이터를 세야 한다거나 확률 등의 계산의 경우 DP로 풀 수 있는 경우가 많다.



### 2. **문제의 변수 파악**

> 문제 내 변수의 개수 파악(state를 결정할 필요)

+ 예를 들어, **피보나치 수열**에서는 n번째 숫자를 구하는 것이므로 n이 변수가 된다. 그 변수가 얼마이냐에 따라 결과값이 다르지만 그 결과를 재사용하고 있다.
+ 또한, **문자열 간의 차이**를 구할 때는 문자열의 길이, Edit 거리 등 2가지 변수를 사용한다.
+ 또, 유명한 **Knapsack 문제**에서는 index, 무게로 2가지의 변수를 사용한다.



### 3. **변수 간 관계식 만들기**

> 변수들에 의해 결과 값이 달라지지만 동일한 변수값인 경우 결과는 동일한 식을 세워야 함 = **점화식**

+ 짧은 코드 내에서 반복/재귀를 통해 문제가 자동으로 해결되도록 구축



### 4. 결과값 저장하기

> 관계식까지 정상적으로 생성되었다면 **변수의 값에 따른 결과를 저장**(Memoization)

+ 1~3차원 배열까지 다양한 방법으로 저장



### 5. **기저 상태 파악하기**

> **가장 작은 문제의 상태를 알아야 함** (초기값)

+ **피보나치 수열을 예시로 들면, f(0) = 0, f(1) = 1과 같은 방식**



### 6. 구현하기

#### 	6-1. **Bottom-Up 방식**

> **아래에서 부터 계산을 수행 하고 누적시켜서 전체 큰 문제를 해결하는 방식**

+ 메모를 위해서 dp라는 배열을 만들었고 이것이 1차원이라 가정했을 때, dp[0]가 기저 상태이고 dp[n]을 목표 상태라고 하자. Bottom-up은 dp[0]부터 시작하여 반복문을 통해 점화식으로 결과를 내서 dp[n]까지 그 값을 전이시켜 재활용하는 방식이다.
  + 이러한 방식을 `Tabulation`이라 함
  + 반복을 통해 dp[0]부터 하나 하나씩 채우는 과정을 **"table-filling"** 하며, 이 Table에 저장된 값에 직접 접근하여 재활용하므로 **Tabulation**이라는 명칭



#### 		6-2. **Top-Down 방식**

> dp[n]의 값을 찾기 위해 **위에서 부터 바로 호출을 시작**하여 dp[0]의 상태까지 내려간 다음 해당 결과 값을 재귀를 통해 전이시켜 재활용하는 방식

+ f(n) = f(n-2) + f(n-1)의 과정에서 함수 호출 트리의 과정에서 보이듯, n=5일 때, f(3), f(2)의 동일한 계산이 반복적으로 나오게 된다.
+ 이미 이전에 계산을 완료한 경우에는 단순히 메모리에 저장되어 있던 내역을 꺼내서 활용
+ 가장 최근의 상태 값을 메모해 두었다고 하여 **Memoization**



```java
packge com.test;

public class Fibonacci{
    // DP 를 사용 시 작은 문제의 결과값을 저장하는 배열
    // Top-down, Bottom-up 별개로 생성하였음(큰 의미는 없음)
    static int[] topDown_memo; 
    static int[] bottomup_table;
    public static void main(String[] args){
        int n = 30;
        topDown_memo = new int[n+1];
        bottomup_table = new int[n+1];
        
        long startTime = System.currentTimeMillis();
        System.out.println(naiveRecursion(n));
        long endTime = System.currentTimeMillis();
        System.out.println("일반 재귀 소요 시간 : " + (endTime - startTime));
        
        System.out.println();
        
        startTime = System.currentTimeMillis();
        System.out.println(topDown(n));
        endTime = System.currentTimeMillis();
        System.out.println("Top-Down DP 소요 시간 : " + (endTime - startTime));
        
        System.out.println();
        
        startTime = System.currentTimeMillis();
        System.out.println(bottomUp(n));
        endTime = System.currentTimeMillis();
        System.out.println("Bottom-Up DP 소요 시간 : " + (endTime - startTime));
    }
    
    // 단순 재귀를 통해 Fibonacci를 구하는 경우
    // 동일한 계산을 반복하여 비효율적으로 처리가 수행됨
    public static int naiveRecursion(int n){
        if(n <= 1){
            return n;
        }
        return naiveRecursion(n-1) + naiveRecursion(n-2);
    }
    
    // DP Top-Down을 사용해 Fibonacci를 구하는 경우
    public static int topDown(int n){
        // 기저 상태 도달 시, 0, 1로 초기화
        if(n < 2) return topDown_memo[n] = n;
        
        // 메모에 계산된 값이 있으면 바로 반환!
        if(topDown_memo[n] > 0) return topDown_memo[n];
        
        // 재귀를 사용하고 있음!
        topDown_memo[n] = topDown(n-1) + topDown(n-2);
        
        return topDown_memo[n];
    }
    
    // DP Bottom-Up을 사용해 Fibonacci를 구하는 경우
    public static int bottomUp(int n){
        // 기저 상태의 경우 사전에 미리 저장
        bottomup_table[0] = 0; bottomup_table[1] = 1;
        
        // 반복문을 사용하고 있음!
        for(int i=2; i<=n; i++){
            // Table을 채워나감!
            bottomup_table[i] = bottomup_table[i-1] + bottomup_table[i-2];
        }
        return bottomup_table[n];
    }
}

/*
결과
832040
일반 재귀 소요 시간 : 9

832040
Top-Down DP 소요 시간 : 0

832040
Bottom-Up DP 소요 시간 : 0
*/
```









## LIS(가장 긴 증가하는 부분수열)

> **Longest Increasing Sequence의 약자**
>
> 특정 값들이 저장되어 있는 배열 형태에서 **순차적으로 증가하는 부분 수열 중 가장 길이가 긴 것**을 의미

![image](https://user-images.githubusercontent.com/101400894/184645757-9e9c8e97-fbd9-433c-b0dc-68c229164d53.png)

+ 우선 각 숫자가 이전의 수보다 크다면, 그 순서가 가장 큰 경우를 구해보자. 그 배열을 sequence의 약자인 seq라 하자.

> i = 0 인 arr[0] = 10 일 때, 자기 자신 혼자 있더라도 수열을 만들 수 있으며 혼자서라도 LIS의 일부가 될 수 있으니 1로 시작할 수 있다.

```
arr[1] = 20, 20은 이전의 10보다 크니까 seq는 2이다.
arr[2] = 40, 40은 이전의 20보다 크니까 seq는 3이다.
arr[3] = 30, 30은 이전의 40보다는 작지만 그 이전의 20보다는 크다. 따라서 seq는 3이다.
arr[4] = 1, 1은 이전의 모든 숫자보다 작다. 따라서 seq는 1이다.
arr[5] = 3, 3은 이전의 1보다 크지만 그 이전의 숫자보다는 작다. 따라서 seq는 2이다.
arr[6] = 5, 5는 이전의 1, 3보다 크지만 그 이전의 숫자보다는 작다. seq는 3이다.
arr[7] = 2, 2는 이전의 3, 5보다 작고 1보다 크지만 그 이전보다는 작다. seq는 2이다.
arr[8] = 90, 90은 이전의 모든 숫자보다 크다. 따라서 이전의 숫자 중 seq가 가장 높은 숫자에 1을 더해야 한다. seq=3이 가장 큰데, 이에 해당하는 것은 arr[2]=40, arr[3]=30, arr[6]=5 인 경우이다. seq는 4이다.
```

![image](https://user-images.githubusercontent.com/101400894/184648188-bf286870-f423-4a40-a9e4-b45afc502911.png)

📌 **LIS는 부분적으로 여러 개가 존재할 수 있는것 아닌가?**

> 맞다. 하지만 최대 길이 그 자체는 하나의 숫자로 정해진다.



### 알고리즘 풀이

### 1. **완전탐색**

> 그 배열 내에서 각 위치의 데이터를 기준으로 **하나 하나 다 비교하며 길이가 얼마나 되는지 확인**

```java
package com.test;

public class LIS{
    public static void main(String[] args){
        int[] arr = new int[]{10, 20, 40, 30, 1, 3, 5, 2, 90};
        int result = 1; // 일단 최소한 1이 답이 될 수 있다.
        
        int[] lis = new int[arr.length]; // LIS 길이 값을 저장하는 배열
        int max_lis = 1;  // LIS의 길이 중 가장 긴 값을 저장
        
        for(int i=0; i < arr.length; i++){
            result = Math.max(result, exhSearch(arr, i)); // 각 부분에서 시작해 완전 탐색
            lis[i] = result; // 결과값 저장
            
            max_lis = Math.max(max_lis, result); // 현재 까지의 최장 길이 저장
            result = 1; // 다시 result는 1로 초기화(각 index의 실제 LIS를 알기 위함)
        }
        System.out.println("LIS 길이 : " + max_lis);
        // *********** 여기까지가 LIS 길이 구하는 부분. ***************
        // 아래 부분은 추가로 참조
        
        
        
        
        // LIS 길이 값 출력하기
        System.out.println("각 index의 LIS 값");
        for(int i=0; i < lis.length; i++){
            System.out.print(lis[i] + ", ");
        }
        System.out.println();
        
        // LIS에 따른 배열 출력해보기
        System.out.println("LIS 배열 출력하기");
        int start = 1; // max_lis 까지 순환
        
        for(int i=0; i < arr.length; i++){
            for(int j=start; j <= max_lis; j++){
                if(lis[i] == j){
                    System.out.print(arr[i] + ", ");
                    start++;
                    break;
                }
            }
        }
    }
    
    public static int exhSearch(int[] arr, int idx){
        if(idx == 0) return 1; // 맨 처음 1개일 때는 자기 자신만으로 LIS 구성. 1반환
        int ret = 1; // 1에서부터 시작
        
        for(int i=idx-1; i >= 0; i--){
            // 만약 현재 위치보다 이전의 값들이 자기 자신보다 작다면 LIS의 대상이 될 수 있으니
            // 해당 위치를 기준으로 재귀를 통해 지속 탐색 수행
            if(arr[i] < arr[idx]){
                ret = Math.max(ret, 1+exhSearch(arr, i));
            }
        }
        return ret;
    }
}

/*
결과
LIS 길이 : 4
각 index의 LIS 값
1, 2, 3, 3, 1, 2, 3, 2, 4,
LIS 배열 출력하기
10, 20, 40, 90,
*/
```

+ 이 방식은 각 Index에서 시작하여 제일 증가하는 부분 수열을 찾아 반복 + 재귀문을 사용하여 푸는 방식이다.
+ 각 index에서 시작하여 재귀를 통해 또 호출하고 있어서 복잡한데 **`전체 시간복잡도가 O(2^N)`**



### 2.  DP

📌우선 LIS가 조건에 부합하는 가?

> **Overlapping Subproblems**와 **Optimal Structure**가 모두 충족

![image](https://user-images.githubusercontent.com/101400894/184649156-f580abc2-4d9a-4c65-8a80-e902700e3288.png)

+ 시간복잡도가 O(2^N)으로 측정된다. 그런데, 해당 트리를 잘 보면 동일한 작은 문제가 반복되고 있으며 그 아래의 작은 문제가 최적결과가 있다면 그대로 사용할 수 있음을 알 수 있다.



#### 위의 문제 풀이 진행

##### 1. State(변수가 될 상태값) = 길이 N(배열의 길이)

+ 전체 배열은 길이가 정해져있지만, 우리가 작은 문제로 나누어서 생각한다면 배열의 길이가 1인 것부터 시작해서 그 최적값을 구해 전체 배열의 결과를 구할 수 있을 것이다. 따라서 **`길이 그 자체가 State`**



##### 2.**DP의 결과를 저장할 배열을 lis[]**



##### 5. 기저상태

**lis[0] = 1**



##### 3. 점화식

```
 lis[i] = lis[j] + 1 (단, j < i and arr[j] < arr[i]) //index는 i가 더 큰데 i값도 j인덱스가 가리키는 값보다 큰 경우
```

1) 현재 위치(i) 보다 이전 위치(j)와 비교한다.
2) 현재 위치(i)의 값(arr[i]) 보다 이전 위치(j)의 값(arr[j])이 더 작아야 한다.



**길이를 구했으면 실제 부분 수열 또한 구할 수 있어야 한다. 그 배열을 V[]라고 가정하고 아래의 배열을 예시로 보자.**



![image](https://user-images.githubusercontent.com/101400894/184650214-cd6a3194-4f58-4a7e-adee-d20507f76c81.png)

+ V배열을 이해해보자면, index 0의 위치한 arr[0]는 가장 처음에 무조건 와야 해서 이전에 더 작은 수가 없다. 따라서 **-1로 초기화한다**.

```
arr[1] 은 20. 이전의 작은 수 중 lis 길이가 가장 높은 수는 arr[0]. 따라서 V배열에 해당 index인 0을 저장.
arr[2] 는 40. 이전의 작은 수 중 lis 길이가 가장 높은 수는 arr[1]. 따라서 V배열에 해당 index인 1을 저장.
arr[3] 는 30. 이전의 작은 수 중 lis 길이가 가장 높은 수는 arr[1]. 따라서 V배열에 해당 index인 1을 저장.
arr[4] 는 1. 이전의 작은 수 중 lis 길이가 가장 높은 수는 없음. -1로 초기화.
arr[5] 는 3. 이전의 작은 수 중 lis 길이가 가장 높은 수는 arr[4]. 따라서 V배열에 해당 index인 4를 저장.
arr[6] 는 5. 이전의 작은 수 중 lis 길이가 가장 높은 수는 arr[5]. 따라서 V배열에 해당 index인 5를 저장.
arr[7] 는 2. 이전의 작은 수 중 lis 길이가 가장 높은 수는 arr[4]. 따라서 V배열에 해당 index인 4를 저장.
arr[8] 는 90. 이전의 작은 수 중 lis 길이가 가장 높은 수는 arr[6]. 따라서 V배열에 해당 index인 6를 저장.
   -> 참고로 arr[2], arr[3]도 그렇지만 코드 상 가장 가까운 것으로 저장됨.
```

+ 바로 이전의 값들 중 현재 값보다 작지만 가장 lis 길이가 긴 것의 index 값을 지정하는 것
+  lis 길이가 가장 긴 V[8]=6을 반환하면, arr[V[8]] = arr[6] = 5 가 된다. 
  + 즉, 이렇게 **거꾸로 돌아가면서 해당 index로 이동하며 전체 배열을 구할 수 있는 것**

![image](https://user-images.githubusercontent.com/101400894/184651034-edbf2375-3284-4a40-8b5f-6dd0ee74a610.png)

```java
package com.test;

import java.io.*;
public class LIS{
    static int[] arr; // 원 배열
    static int[] lis; // LIS 길이 저장
    static int[] V;   // 이전 인덱스 저장
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        
        arr = new int[]{10, 20, 40, 30, 1, 3, 5, 2, 90};
        lis = new int[arr.length];
        V = new int[arr.length];
        
        // 가장 긴 lis값을 갖는 index를 반환함
        int result = dp();
        bw.write("LIS 길이 : " + String.valueOf(lis[result]) + "\n");
        // *********** 여기까지가 LIS 길이 구하는 부분. ***************
        
        
        // LIS 길이 값 출력하기
        bw.write("각 index의 LIS 값 : ");
        for(int i=0; i < lis.length; i++){
            bw.write(lis[i] + ", ");
        }
        bw.write("\n");
        
        // LIS 배열 출력해보기
        // 출력 시 뒤에서부터 lis 길이를 기준으로 써내려가야 한다.
        // 앞에서부터 하면 제일 앞의 값이 가장 큰 값일 때, 그것을 걸러낼 수 없다.
        bw.write("LIS 배열 출력하기" + "\n");
        printLis(result, bw);
        
        br.close();
        bw.flush();
    }
    
    // Bottom-Up 방식으로 해결하는 DP
    public static int dp(){
        // 최대 lis 길이 값
        int max_lis = 0;
        
        // 최대 길이를 만족시키는 부분 수열의 마지막 인덱스, 초기는 0으로
        int last = 0;
        
        // lis[0]은 정해졌으니 그 이후부터 채워나감
        for(int i=0; i < lis.length; i++){
            lis[i] = 1; // 기본적으로 1로 초기화. 기저 상태도 초기화됨
            V[i] = -1; // 기본적으로 -1로 초기화. 기저 상태로 초기화됨
            
            // 자신보다 이전의 값들과 비교해야함. 그 중 가장 큰 값으로!
            for(int j=i-1; j >= 0; j--){
                // 이전 값이 더 작으면서 lis 길이 값은 같거나 큰 경우
                if(arr[j] < arr[i] && lis[j] >= lis[i]){
                    lis[i] = lis[j] + 1;
                    V[i] = j; // 이전의 index 저장
                }
                if(max_lis < lis[i]){
                    max_lis = lis[i];
                    last = i; // 최대 길이가 변경되어야 한다.
                }
            }
        }
        return last;
    }
    
    // 재귀를 통해 LIS 배열 출력
    private static void printLis(int idx, BufferedWriter bw) throws IOException{
        // 더 갈 수 없는 가장 이전 index 까지 간 경우
        if(V[idx] == -1) { 
            bw.write(arr[idx] + " "); 
            return;
        }
        printLis(V[idx], bw);
        bw.write(arr[idx] + " ");
    }
}

/*
결과
LIS 길이 : 4
각 index의 LIS 값
1, 2, 3, 3, 1, 2, 3, 2, 4,
LIS 배열 출력하기
1, 3, 5, 90,
*/


---------------------------------------------------------------------------
//Top-Down 방식
package com.test;

import java.io.*;
public class LIS{
    static int[] arr; // 원 배열
    static int[] lis; // LIS 길이 저장
    static int[] V;   // 이전 인덱스 저장
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        
        arr = new int[]{10, 20, 40, 30, 1, 3, 5, 2, 90};
        
        // 배열 정의 및 기저 상태 저장
        lis = new int[arr.length]; lis[0] = 1;
        V = new int[arr.length]; V[0] = -1;
        
        int result = 0;
        for(int i=0; i < lis.length; i++){
            int temp = dp(i);
            if(lis[result] < lis[temp]){
                result = temp;
            }
        }
        bw.write(String.valueOf("LIS의 길이 : " + lis[result]) + "\n");
        // *********** 여기까지가 LIS 길이 구하는 부분. ***************
        
        
        // LIS 길이 값 출력하기
        bw.write("각 index의 LIS 값 : ");
        for(int i=0; i < lis.length; i++){
            bw.write(lis[i] + ", ");
        }
        bw.write("\n");
        
        // LIS 배열 출력해보기
        // 출력 시 뒤에서부터 lis 길이를 기준으로 써내려가야 한다.
        // 앞에서부터 하면 제일 앞의 값이 가장 큰 값일 때, 그것을 걸러낼 수 없다.
        bw.write("LIS 배열 출력하기" + "\n");
        printLis(result, bw);
        
        br.close();
        bw.flush();
    }
    
    // Top-Down 방식으로 해결하는 DP
    public static int dp(int n){
        if(n == 0 || lis[n] > 0) return n; // 기저상태 또는 이미 이전의 값이 있는 경우 반환
        lis[n] = 1; // 우선 1로 초기화
        V[n] = -1; // 우선 -1로 초기화
        
        // 자신보다 이전의 값들과 비교해야함. 그 중 가장 큰 값으로!
        for(int i=n-1; i >= 0; i--){
            // 우선 -1로 초기화
            int temp = -1;
            
            // 이전의 값이 더 작으면
            if(arr[i] < arr[n]){
                temp = dp(i);
            }
            
            // 만약 -1보다 크게 바뀌었고, lis 길이도 더 긴 경우
            if(temp != -1 && lis[temp] >= lis[n]){
                lis[n] = lis[temp] + 1;
                V[n] = temp;
            }
        }
        return n;
    }
    
    // 재귀를 통해 LIS 배열 출력
    private static void printLis(int idx, BufferedWriter bw) throws IOException{
        // 더 갈 수 없는 가장 이전 index 까지 간 경우
        if(V[idx] == -1) { 
            bw.write(arr[idx] + " "); 
            return;
        }
        printLis(V[idx], bw);
        bw.write(arr[idx] + " ");
    }
}

/*
결과
LIS 길이 : 4
각 index의 LIS 값
1, 2, 3, 3, 1, 2, 3, 2, 4,
LIS 배열 출력하기
10, 20, 40, 90,
*/
```



### 3. **Nlogn으로 개선하기**

#### 아이디어

1) 추가 배열을 만들고 원 배열을 탐색하며 큰 수는 추가 배열에 이어 붙인다.
2) 추가 배열의 마지막에 추가된 값보다 작은 값은 **이분 탐색**을 통해 적절한 자리를 찾아 교환한다.

> 이 방법의 **장점**은 이분 탐색을 통해 빠르게 LIS의 길이를 구할 수 있다는 것이다.
> 이 방법의 **단점**은 LIS 배열 그 자체는 중간에 값이 교체되기 때문에 구할 수 없을 수도 있다는 것이다.

![image](https://user-images.githubusercontent.com/101400894/184653510-62b2ffec-7135-4336-983e-46815abccac5.png)

![image](https://user-images.githubusercontent.com/101400894/184653813-e278b2bc-8de2-47b1-bc3f-42a340bec9f2.png)

![image](https://user-images.githubusercontent.com/101400894/184653579-c087b9c5-c216-476f-99af-09c8954e1da4.png)



![image](https://user-images.githubusercontent.com/101400894/184653655-32bb3ab1-01cf-4562-b9ed-9bb6510f2d77.png)

+  **lis 배열의 마지막 값은 30이었다. arr[4]=1으로 이전 수보다 작은데, 순서 상 교체될 수 있는 위치는 lis[0]이므로 교체**

![image](https://user-images.githubusercontent.com/101400894/184654089-a9b3aafd-9e96-4c3e-b5a9-0f3da38f6e68.png)

+ 위와 같이 구한 결과 전체 LIS의 길이는 4라는 것을 알 수 있다. 하지만 상단에 단점에 대해 설명했듯이, 중간에 교체되어 lis배열이 실제 lis라고 볼 수는 없게 된다.

  실제로도 arr배열에서 1, 2, 5, 90이라는 LIS는 없다.

```java
package test;

import java.util.*;

public class Main {
    static int[] arr;
    static int[] lis;

    public static void main(String[] args) {
        arr = new int[]{10, 20, 40, 30, 1, 3, 5, 2, 90};
        lis = new int[arr.length];
        Arrays.fill(lis, Integer.MAX_VALUE);
        lis[0] = arr[0]; // 최초의 index 0의 값은 arr[0]이 된다.

        int idx = 0;
        for (int i = 1; i < arr.length; i++) {
            // 만약 원 배열이 탐색 중 더 큰 숫자라면 그대로 이어서 붙인다.
            if (lis[idx] < arr[i]) {
                lis[++idx] = arr[i];
                // 그렇지 않고 작다면 이진 탐색(Binary Search)를 통해 교체를 수행한다.
            } else {
                int target_index = binarySearch(lis, arr[i]);
                lis[target_index] = arr[i];
            }
            Arrays.stream(lis).forEach(s->System.out.print(s+" "));
            System.out.println();
        }

        // 현재 idx의 값에서 1을 더한 것이 바로 전체 LIS의 길이가 된다.
        System.out.println("LIS 길이 : " + (idx + 1));
        Arrays.stream(lis).forEach(s->System.out.print(s+" "));

    }

    // 반복문을 이용한 이진 탐색 방식
    public static int binarySearch(int[] arr, int x) {
        int start = 0;
        int end = arr.length - 1;

        // 현재 탐색한 위치가 찾고자 하는 값보다 크냐 작냐에 따라 중간 index 계산을 위한 start / end 값을 변경함
        while (start <= end) {
            int mid = (start + end) / 2;
            if (arr[mid] == x) {
                return mid;
            } else if (arr[mid] < x) {
                start = mid + 1;
            } else {
                end = mid - 1;
            }
        }
        // 일치값을 찾지 못했을 때, -1이 아니라 그 적절한 위치를 반환해야 함
        return start;
    }
}

/*
결과
LIS 길이 : 4
각 index의 LIS 값
1, 2, 3, 3, 1, 2, 3, 2, 4,
LIS 배열 출력하기
10, 20, 40, 90,
*/
```









-----------

*reference*

https://hongjw1938.tistory.com/47