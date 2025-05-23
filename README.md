# Description of an app like Calendly
The aim of the project is to create a modern, lightweight and easy-to-use Calendly-type web application, intended mainly for business clients. The application is to enable effective planning of meetings during the day, with an additional function of notifying the user by phone about an upcoming meeting, which increases its practicality and usability in environments with a high pace of work.

## Backend
<p>
  The application logic is based on the Python language, using Flask – a lightweight and fast web framework that is great for building microservices and REST APIs. Flask enables efficient management of user requests, integration with the database and implementation of notifications.
</p>
<p>
  The non-relational MongoDB database is used to store data about users and scheduled meetings. Its flexible document structure (JSON/BSON format) is perfect for storing dynamic and diverse data, such as meeting times, user contact details, or notification history.
</p>
<p>
  To reduce infrastructure maintenance costs, the application backend will be run on the AWS Lambda platform – a serverless solution that allows for automatic scaling of the application in response to demand, while not requiring server management. Thanks to this, the application's operating costs are charged only for the actual use of computing resources.
</p>

## Frontend
The frontend layer of the application will be a simple, intuitive website built using HTML5 and the modern CSS framework Tailwind CSS. Tailwind allows for the quick creation of responsive user interfaces with an aesthetic, minimalist design. The site is to be light, clear and accessible on both computers and mobile devices.

## Key functionalities of the application:

<ul>
  <li>User registration and login</li>
  <li>Creating and editing available time slots</li>
  <li>Booking of meetings by end customers</li>
  <li>Automatic telephone notifications about upcoming meetings</li>
</ul>
