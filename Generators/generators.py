def generate_numbers(limit):
    for num in range(1, limit + 1):
        yield num
sequence = generate_numbers(5)
for value in sequence:
    print(value)


    #def function(parameters):
    #yield statement

    def number_generator():
        numbers = [1, 2, 3]
        for num in numbers:
            yield num
            # Running the generator to display its output


    for item in number_generator():
        print(item)

        #Difference between Yield and Return
        def calculate_total():
            values = [1, 2, 3]
            result = sum(values)
            return result


        output = calculate_total()
        print(output)



        #generators expressions
        squares_generator = (num ** 2 for num in range(1, 6))
        for square in squares_generator:
            print(square)