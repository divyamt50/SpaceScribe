# SpaceScribe
<img src="static/images/logo.svg" alt="Alt Text" width="300" />

[Visit the Project](http://13.55.119.184/)

SpaceScribe is a dynamic and interactive web application that allows users to create and manage virtual "spaces" for collaborative discussions and interactions. Inspired by the concept of online chat rooms, SpaceScribe takes it a step further by providing a visually appealing and user-friendly environment for users to engage in meaningful conversations within their chosen topics.

## Features
- **Create and Manage Rooms:** Users can easily create their own rooms and customize the name, description, and topic of the room. Each room becomes a unique space for discussions.
- **Real-time Messaging:** Within each room, users can exchange messages in real-time, enabling fluid conversations and instant communication.
- **Browse Topics:** Users can explore different topics of interest, helping them find rooms that align with their preferences and engage in relevant discussions.
- **User Profiles:** Users have their own profiles where they can view and manage the rooms they've created, their participation in other rooms, and their message history.
- **Responsive Design:** The app is designed to be responsive, ensuring an optimal experience across various devices, from desktops to smartphones.
- **RESTful API:** SpaceScribe also provides a RESTful API that allows developers to interact with the app programmatically. Users can call the API using the endpoint domain/api/ to access various functionalities.

## Getting Started
To run SpaceScribe locally on your machine, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/SpaceScribe.git
   ```
2. Navigate to the project directory:

```bash
cd SpaceScribe
```
3. Install the required dependencies:

```bash
pip install -r requirements.txt
```
4. Set up databse

```bash
python manage.py migrate
```

5. Create a superuser account for administration:

```bash
python manage.py createsuperuser
```

6. Start the development server:

```bash
python manage.py runserver
```

7. Open your web browser and visit http://localhost:8000 to access the app.

## Using the API
SpaceScribe's API provides various endpoints for interacting with the app programmatically. You can access the API using the endpoint `http://localhost:8000/api/`.

For example:

- To retrieve a list of rooms: `http://localhost:8000/api/rooms/`
- To create a new room: `http://localhost:8000/api/rooms/` (HTTP POST request)
- To retrieve details of a specific room: `http://localhost:8000/api/rooms/<room_id>/`
Refer to the API documentation for more details on available endpoints and their functionalities.

## Technologies Used
- Django: Backend web framework
- Django Channels: Real-time communication
- Django Rest Framework: API development
- HTML, CSS, JavaScript: Frontend development
- PostgreSQL: Database storage
- Redis: Backend caching
- Bootstrap: Responsive UI components

## Contributing
Contributions are welcome! If you'd like to contribute to SpaceScribe, feel free to submit pull requests or open issues on the GitHub repository.

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

Feel free to further tailor and expand upon this README based on your project's specific features, API endpoints, and any additional information you want to provide to users and contributors.
