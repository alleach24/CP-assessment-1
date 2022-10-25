from optimal_change import optimal_change


class TestOptimalChange:
    def test_one(self):
        assert optimal_change(62.13, 100) == "The optimal change for an item that costs $62.13 with an amount paid of $100 is 1 $20 bill, 1 $10 bill, 1 $5 bill, 2 $1 bills, 3 quarters, 1 dime, and 2 pennies."

    def test_two(self):
        assert optimal_change(31.51, 50) == "The optimal change for an item that costs $31.51 with an amount paid of $50 is 1 $10 bill, 1 $5 bill, 3 $1 bills, 1 quarter, 2 dimes, and 4 pennies."
    
    def test_three(self):
        assert optimal_change(99.99, 100) == "The optimal change for an item that costs $99.99 with an amount paid of $100 is 1 penny."

    def test_four(self):
        assert optimal_change(53.27, 250) == "The optimal change for an item that costs $53.27 with an amount paid of $250 is 1 $100 bill, 1 $50 bill, 2 $20 bills, 1 $5 bill, 1 $1 bill, 2 quarters, 2 dimes, and 3 pennies."
    
    def test_five(self):
        assert optimal_change(23.17, 97.99) == "The optimal change for an item that costs $23.17 with an amount paid of $97.99 is 1 $50 bill, 1 $20 bill, 4 $1 bills, 3 quarters, 1 nickel, and 2 pennies."
        
    def test_six(self):
        assert optimal_change(37.78, 40) == "The optimal change for an item that costs $37.78 with an amount paid of $40 is 2 $1 bills, 2 dimes, and 2 pennies."
    
    def test_seven(self):
        assert optimal_change(23.17, 97.99) == "The optimal change for an item that costs $23.17 with an amount paid of $97.99 is 1 $50 bill, 1 $20 bill, 4 $1 bills, 3 quarters, 1 nickel, and 2 pennies."
    
    def test_eight(self):
        assert optimal_change(5.07, 100) == "The optimal change for an item that costs $5.07 with an amount paid of $100 is 1 $50 bill, 2 $20 bills, 4 $1 bills, 3 quarters, 1 dime, 1 nickel, and 3 pennies."
    
    def test_nine(self):
        assert optimal_change(90, 100) == 'The optimal change for an item that costs $90 with an amount paid of $100 is 1 $10 bill.'
        

test = TestOptimalChange()

print(test.test_one())
print(test.test_two())
print(test.test_three())
print(test.test_four())
print(test.test_five())
print(test.test_six())
print(test.test_seven())
print(test.test_eight())
print(test.test_nine())