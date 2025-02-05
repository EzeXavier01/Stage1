import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status # type: ignore
from .serializers import NumberSerializer

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_perfect(n):
    if n<=0:
        return False
    return sum(i for i in range(1, n) if n % i == 0) == n

def is_armstrong(n):
    digits = [int(d) for d in str(n)]
    power = len(digits)
    return sum(d ** power for d in digits) == n

class ClassifyNumberView(APIView):
    def get(self, request):
        number = request.GET.get('number')

        if not number or not number.isdigit():
            return Response({"number": "alphabet", "error": True}, status=status.HTTP_400_BAD_REQUEST)

        number = int(number)
        properties = []
        
        if is_armstrong(number):
            properties.append("armstrong")
        properties.append("odd" if number % 2 else "even")

        fun_fact_url = f"http://numbersapi.com/{number}/math"
        fun_fact = requests.get(fun_fact_url).text if requests.get(fun_fact_url).status_code == 200 else "No fun fact available."

        response_data = {
            "number": number,
            "is_prime": is_prime(number),
            "is_perfect": is_perfect(number),
            "properties": properties,
            "digit_sum": sum(int(d) for d in str(number)),
            "fun_fact": fun_fact
        }

        serializer = NumberSerializer(response_data)
        return Response(serializer.data, status=status.HTTP_200_OK)