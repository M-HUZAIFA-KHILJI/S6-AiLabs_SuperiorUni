#MUHAMMAD HUZAIFA KHILJI
#f24-002
#LAB_4
def is_luhn_valid(number_str):
  
  # Remove spaces or non-digit characters 
  digits = [int(d) for d in number_str if d.isdigit()]

  # Process digits from right to left
  total_sum = 0
  # Use a flag or index to track every second digit from the right
  is_second_digit = False

  # Iterate through digits in reverse order
  for digit in reversed(digits):
    if is_second_digit:
      doubled_digit = digit * 2
      # If doubling results in a number > 9, subtract 9
      if doubled_digit > 9:
        doubled_digit -= 9
      total_sum += doubled_digit
    else:
      total_sum += digit

    # Flip the flag for the next digit
    is_second_digit = not is_second_digit

  # The number is valid if the total sum is a multiple of 10
  return total_sum % 10 == 0

# --- Example Usage ---
card_number1 = "49927398716" # Example valid number
card_number2 = "49927398717" # Example invalid number
invalid_format = "1234 5678 9012 3452" # Example with spaces (will be cleaned)

print(f"Is '{card_number1}' valid according to Luhn? {is_luhn_valid(card_number1)}")
print(f"Is '{card_number2}' valid according to Luhn? {is_luhn_valid(card_number2)}")
print(f"Is '{invalid_format}' valid according to Luhn? {is_luhn_valid(invalid_format)}")