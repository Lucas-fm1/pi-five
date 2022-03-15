# Pi-five
A surprising approximation for pi using 5's strings.

This string of fives can be thought as a palindrome with this only number, like 55, 555 or 555555.
To achieve the approximated pi result, it's needed to first take the reciprocal (inverse) of the 5-string, such as 1/5555 for example.
Then, when you evaluate the sine of the reciprocal, you'll get, in this case:

        sin(1/5555) = 3.141906844269051e-06
  
Indeed, it is not pi, it's "pi like" because of the scientific notation. However, the significant numbers in this example already gives a reasonably good result, since pi is 3.14159265359 (approximately), and it used just four digits. 

The reason for this curious fact is explainded in this amazing Numberphile video:
https://www.youtube.com/watch?v=IMY2_yzDm9I&t=827s 
