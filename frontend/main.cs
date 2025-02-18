using System.Runtime.Serialization;

public class mainPage : contentPag
{
    public mainPage()
    {
        var createEvent = new Button("Create Event");
    createEvent.Clicked += OnCreateEventClicked;


    }

}
