// CalculatorTests.cs
using Xunit;
using MyCalculator;

namespace MyCalculator.Tests
{
    public class CalculatorTests
    {
        private readonly Calculator _calculator;

        public CalculatorTests()
        {
            _calculator = new Calculator();
        }

        [Fact]
        public void Add_TwoNumbers_ReturnsCorrectSum()
        {
            // Arrange
            int a = 5;
            int b = 7;

            // Act
            int result = _calculator.Add(a, b);

            // Assert
            Assert.Equal(12, result);
        }

        [Fact]
        public void Subtract_TwoNumbers_ReturnsCorrectDifference()
        {
            // Arrange
            int a = 10;
            int b = 6;

            // Act
            int result = _calculator.Subtract(a, b);

            // Assert
            Assert.Equal(4, result);
        }

        [Fact]
        public void Multiply_TwoNumbers_ReturnsCorrectProduct()
        {
            // Arrange
            int a = 3;
            int b = 4;

            // Act
            int result = _calculator.Multiply(a, b);

            // Assert
            Assert.Equal(12, result);
        }

        [Fact]
        public void Divide_TwoNumbers_ReturnsCorrectQuotient()
        {
            // Arrange
            int a = 20;
            int b = 5;

            // Act
            double result = _calculator.Divide(a, b);

            // Assert
            Assert.Equal(4, result);
        }

        [Fact]
        public void Divide_DivideByZero_ThrowsDivideByZeroException()
        {
            // Arrange
            int a = 10;
            int b = 0;

            // Act & Assert
            Assert.Throws<System.DivideByZeroException>(() => _calculator.Divide(a, b));
        }
    }
}
