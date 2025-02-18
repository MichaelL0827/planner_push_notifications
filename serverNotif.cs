//this is meant for if we use our own server to send notifications.

using System.Net.Http;
using System.Text;
using System.Threading.Tasks;

public class PushNotificationService
{
    private readonly HttpClient _httpClient;

    public PushNotificationService(HttpClient httpClient)
    {
        _httpClient = httpClient;
    }

    public async Task SendNotificationAsync(string deviceToken, string title, string message)
    {
        var payload = new
        {
            to = deviceToken,
            notification = new
            {
                title = title,
                body = message
            }
        };

        var jsonPayload = JsonSerializer.Serialize(payload);
        var content = new StringContent(jsonPayload, Encoding.UTF8, "application/json");

        var response = await _httpClient.PostAsync("https://fcm.googleapis.com/fcm/send", content);
        response.EnsureSuccessStatusCode();
    }
}