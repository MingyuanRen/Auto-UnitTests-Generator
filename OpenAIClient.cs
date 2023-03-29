using System;
using System.Net.Http;
using System.Text;
using System.Threading.Tasks;
using Newtonsoft.Json;

public class OpenAIClient
{
    private static readonly string apiKey = "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";
    private static readonly string apiUrl = "https://api.openai.com/v1/engines/davinci-codex/completions";

    public static async Task<string> GenerateUnitTest(string codeSnippet)
    {
        using (var client = new HttpClient())
        {
            client.DefaultRequestHeaders.Add("Authorization", $"Bearer {apiKey}");
            var prompt = $"Generate C# NUnit unit test for the following C# code snippet:\n{codeSnippet}\n";
            var requestBody = JsonConvert.SerializeObject(new { prompt = prompt, max_tokens = 300 });

            using (var response = await client.PostAsync(apiUrl, new StringContent(requestBody, Encoding.UTF8, "application/json")))
            {
                response.EnsureSuccessStatusCode();
                var responseBody = await response.Content.ReadAsStringAsync();
                var result = JsonConvert.DeserializeObject<OpenAIResponse>(responseBody);
                return result.choices?[0].text ?? string.Empty;
            }
        }
    }

    private class OpenAIResponse
    {
        public Choice[]? choices { get; set; }

        public class Choice
        {
            public string? text { get; set; }
        }
    }
}
