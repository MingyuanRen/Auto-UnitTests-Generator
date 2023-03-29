
    string codeSnippet = @"
public class Calculator
{
    public int Add(int a, int b)
    {
        return a + b;
    }
}";
    string generatedUnitTest = await OpenAIClient.GenerateUnitTest(codeSnippet);
    Console.WriteLine(generatedUnitTest);
