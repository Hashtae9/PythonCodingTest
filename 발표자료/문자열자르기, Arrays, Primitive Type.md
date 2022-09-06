
# 1. 문자열 자르기



### split()

split(String s); →구분자를 기준으로 배열 형식으로 문자열을 자름

split(String s, int i); →구분자를 기준으로 배열 형식으로 문자열을 i만큼 자름

split(",구분자@구분자-"); → 여러개의 구분자로 문자열을 자름

split("”); → 한글자씩 자름

### stringtokenizer

특정 문자에 따라 문자열을 자를 때 이용

String : 문자열을
Tokenizer : 토큰화하는 것

```java
import java.util.StringTokenizer;
public class Main {
	public static void main(String[] args)  {
		String str = "StringTokenizer 예제";
		StringTokenizer st = new StringTokenizer(str);//문자열
		
		System.out.println(st.nextToken());//output : StringTokenizer 
		System.out.println(st.nextToken());//output : 예제
	}
}
```

```java
import java.util.StringTokenizer;
public class Main {
	public static void main(String[] args)  {
	String str = "StringTokenizer 예제";
    			StringTokenizer st = new StringTokenizer(str,"i");//문자열,구분자
    			
    			System.out.println(st.nextToken());//output : Str
    			System.out.println(st.nextToken());//output : ngToken
    			System.out.println(st.nextToken());//output : zer 예제
	}
}
```

```java
import java.util.StringTokenizer;
public class Main {
	public static void main(String[] args)  {
String str = "StringTokenizer 예제";
    			StringTokenizer st = new StringTokenizer(str,"i",true);//문자열 구분자 true/false
    			
    			System.out.println(st.nextToken());//output : Str
    			System.out.println(st.nextToken());//output : i
    			System.out.println(st.nextToken());//output : ngToken
    			System.out.println(st.nextToken());//output : i
    			System.out.println(st.nextToken());//output : zer 예제
	}
}
```

**split과 StringTokenizer중 성능이 더 좋은 것은?**

> StringTokenizer
 is a legacy class that is retained for compatibility reasons although its use is discouraged in new code. It is recommended that anyone seeking this functionality use the split
 method of String
 or the java.util.regex package instead.
> 

[3]

StringTokenizer는 새 코드에서는 사용이 권장되지 않지만 호환성을 위해 유지되는 레거시 클래스입니다. 이 기능을 원하는 사람은 String 또는 java.util.regex 패키지의 split 메소드를 대신 사용하는 것이 좋습니다.

StringTokenizer가 성능이 나빠지는 경우

→ 구분자가 여러개인 경우

→ 구분자가 유니코드인 경우

→ hasMoreToke 혹은 nextToken 호출이 잦은경우

### +번외)

### toCharArray

문자열을 char배열로 변환하는데 사용

```java
String line=br.readLine();//안녕하세요
			for(char c:line.toCharArray()) {
   System.out.print(c+" ");//output : 안 녕 하 세 요
}
```

### charAt()

String으로 저장된 문자열 중에서 i번째 글자만 선택하여 char타입으로 변환해주는 method

```java
      char c = ' ';
    	str = "안녕하세요";
    	for(int i=0; i<str.length(); i++) {
    		c = str.charAt(i);
        	System.out.print(c+" ");//output :안 녕 하 세 요 
    	}
```

### ****substring****

String.substring(start) //start위치부터 끝까지 문자열 자르기
String.substring(start,end) //start위치 부터 end전까지 문자열 발췌

[11656번: 접미사 배열](https://www.acmicpc.net/problem/11656)


```java
//11656 활용 예시
//입력받은 문자열 중 첫글자를 제외하며 출력하는 case
for(int i=0; i<line.length(); i++)suffix[i]=line.substring(i);

//하나씩 자르고 싶은 경우
for(int i=0; i<line.length(); i++)suffix[i]=line.substring(i,i+1);
```

# 2. Arrays

[2]



배열을 다루기 위한 다양한 메소드를 **java.util.Arrays 클래스**를 통해 이용가능

- binarySearch() :

배열에서 **특정 객체의 위치**를 이진 검색 알고리즘을 사용해서 검색하고 반환(sorted array에서 동작)

해당 key를 찾지 못하면 -(key보다 greater한 최초의 index+1) return

- copyOf(arr, length) :

 전달받은 배열의 특정길이만큼 새 배열로 복사후 반환

새로운 배열의 길이가 원본 배열보다 길면, 나머지 요소는 배열 요소의 타입에 맞게 기본값으로 설정

- copyOfRange(arr, startIndex, end의 다음Index) :배열의 특정 범위에 해당하는 요소만 같은 타입의 새 배열로 복사후 반환
- fill(arr, 초기값) : 배열의 모든 요소 특정 값으로 초기화
- sort(arr) :배열의 요소 오름차순 정렬

- 코드보기
    
    ```jsx
    int[] arr = {1, 2, 3, 4, 5};
    
    Arrays.binarySearch(arr, 2);// 1
    Arrays.binarySearch(arr, 10);//-6 
    
    Arrays.copyOf(arr, 3);//1 2 3
    
    Arrays.copyOfRange(arr, 2, 4); //3 4
    
    Arrays.fill(arr, 7); //7 7 7 7 7
    
    Arrays.sort(arr);//오름차순 1 2 3 4 5
    Arrays.sort(arr,Collections.reverseOrder());//내림차순 5 4 3 2 1
    ```
    

# 3. primitive type 범위



타입(data type) : 해당 데이터가 메모리에 어떻게 저장되고, 프로그램에서 어떻게 처리되어야 하는지를 명시적으로 알려주는 역할

primitive type : 자바에서 미리 정의하여 제공하는 여러 형태의 type 

*기본형을 제외한 모든 타입은 참조형 타입(Reference type)으로 Array, Enumeration, Class, Interface등이 존재  (+ null존재)*

- 기본 값이 존재하여 null이 존재하지 않음
- 컴파일 시점에 data의 표현범위를 벗어나면 컴파일 에러가 발생

[10824번: 네 수](https://www.acmicpc.net/problem/10824)

 int형으로 처리하는 경우 

(백만자리+백만자리=1조자리) > int형의 최대 범위인 21억

→ 정수 오버플로우가 발생










*reference*

---

[1]  [https://gbsb.tistory.com/6](https://gbsb.tistory.com/6)

[2] [http://www.tcpschool.com/java/java_api_arrays](http://www.tcpschool.com/java/java_api_arrays)

[3][https://docs.oracle.com/javase/8/docs/api/java/util/StringTokenizer.html](https://docs.oracle.com/javase/8/docs/api/java/util/StringTokenizer.html)
