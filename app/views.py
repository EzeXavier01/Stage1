import math
import requests
from django.http import JsonResponse
from django.views import View

class ClassifyNumberView(View):
    def get(self, request):
        number = request.GET.get("number")

        # Validate input
        if number is None or not number.lstrip("-").isdigit():
            return JsonResponse({"number": number, "error": True}, status=400)

        number = int(number)
        response_data = {
            "number": number,
            "is_prime": self.is_prime(number),
            "is_perfect": self.is_perfect(number),
            "properties": self.get_properties(number),
            "digit_sum": self.digit_sum(number),
            "fun_fact": self.get_fun_fact(number),
        }

        return JsonResponse(response_data, status=200)

    def is_prime(self, n):
        if n < 2:
            return False
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True

    def is_perfect(self, n):
        if n <= 0:
            return False
        return sum(i for i in range(1, n) if n % i == 0) == n

    def is_armstrong(self, n):
        num_str = str(abs(n))  # Convert to string and ignore sign
        num_digits = len(num_str)
        return sum(int(digit) ** num_digits for digit in num_str) == abs(n)

    def get_properties(self, n):
        properties = ["even" if n % 2 == 0 else "odd"]
        if self.is_armstrong(n):
            properties.insert(0, "armstrong")
        return properties

    def digit_sum(self, n):
        return sum(int(digit) for digit in str(abs(n)))  # Ignore sign

    def get_fun_fact(self, n):
        try:
            response = requests.get(f"http://numbersapi.com/{n}/math", timeout=5)
            if response.status_code == 200:
                return response.text
        except requests.exceptions.RequestException:
            pass
        return "No fun fact available."















# import requests
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status # type: ignore
# from .serializers import NumberSerializer

# def is_prime(n):
#     if n < 2:
#         return False
#     for i in range(2, int(n ** 0.5) + 1):
#         if n % i == 0:
#             return False
#     return True

# def is_perfect(n):
#     if n<=0:
#         return False
#     return sum(i for i in range(1, n) if n % i == 0) == n

# def is_armstrong(n):
#     digits = [int(d) for d in str(n)]
#     power = len(digits)
#     return sum(d ** power for d in digits) == n

# class ClassifyNumberView(APIView):
#     def get(self, request):
#         number = request.GET.get('number')

#         if not number or not number.isdigit():
#             return Response({"number": "alphabet", "error": True}, status=status.HTTP_400_BAD_REQUEST)

#         number = int(number)
#         properties = []
        
#         if is_armstrong(number):
#             properties.append("armstrong")
#         properties.append("odd" if number % 2 else "even")

#         fun_fact_url = f"http://numbersapi.com/{number}/math"
#         fun_fact = requests.get(fun_fact_url).text if requests.get(fun_fact_url).status_code == 200 else "No fun fact available."

#         response_data = {
#             "number": number,
#             "is_prime": is_prime(number),
#             "is_perfect": is_perfect(number),
#             "properties": properties,
#             "digit_sum": sum(int(d) for d in str(number)),
#             "fun_fact": fun_fact
#         }

#         serializer = NumberSerializer(response_data)
#         return Response(serializer.data, status=status.HTTP_200_OK)