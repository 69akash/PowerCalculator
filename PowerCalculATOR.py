class PowerCalculator:
    def Calculator(x,n):
        if n==0:
            return 1
        elif n<0:
            x=1/x
            n=-n
        result=1

        while n>0:
            if n%2==1:
                result*=x
            x*=x
            n//=1
        return result


x=float(input("Enter the base :"))
y=int(input("Enter  any exponent:"))

result2=PowerCalculator().Calculator(x,y)

print(f"{x} to the power{y}={result2}")