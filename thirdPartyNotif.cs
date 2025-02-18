
// This is a skeleton for sending notifications, and is not finale. 
//This will need to be updated to work properly and will need to be adjusted depending on if we use our own server or a 3rd party service.

using Android.App;
using Android.Content;
using AndroidX.Core.App;

public class NotificationManagerService : INotificationManagerService
{
    const string channelId = "default";
    const string channelName = "Default";
    const string channelDescription = "The default channel for notifications.";
    bool channelInitialized = false;

    public event EventHandler NotificationReceived;

    public void SendNotification(string title, string message, DateTime? notifyTime = null)
    {
        if (!channelInitialized)
        {
            CreateNotificationChannel();
        }

        var intent = new Intent(Application.Context, typeof(MainActivity));
        intent.PutExtra("title", title);
        intent.PutExtra("message", message);

        var pendingIntent = PendingIntent.GetActivity(Application.Context, 0, intent, PendingIntentFlags.UpdateCurrent);
        var builder = new NotificationCompat.Builder(Application.Context, channelId)
            .SetContentTitle(title)
            .SetContentText(message)
            .SetSmallIcon(Resource.Drawable.icon)
            .SetContentIntent(pendingIntent)
            .SetAutoCancel(true);

        var notificationManager = NotificationManagerCompat.From(Application.Context);
        notificationManager.Notify(0, builder.Build());
    }

    void CreateNotificationChannel()
    {
        var channel = new NotificationChannel(channelId, channelName, NotificationImportance.Default)
        {
            Description = channelDescription
        };
        var notificationManager = (NotificationManager)Application.Context.GetSystemService(Context.NotificationService);
        notificationManager.CreateNotificationChannel(channel);
        channelInitialized = true;
    }

    public void ReceiveNotification(string title, string message)
    {
        NotificationReceived?.Invoke(null, new NotificationEventArgs { Title = title, Message = message });
    }
}